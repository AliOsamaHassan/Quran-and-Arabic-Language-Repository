#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  litebase.py
#  Used to manage Sqlite database with easiest way
#  
#  Copyright 2015 Abdelkrime Aries <kariminfo0@gmail.com>
#  Copyright 2014 DzCoding group <dzcoding@googlegroups.com>
#  
#  ---- AUTHORS ----
#  2014-2015    Abdelkrime Aries <kariminfo0@gmail.com>
#  
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#  

import os, os.path
import sqlite3 as db
import sys
import re
import string

class liteBase(object):
	
	def __init__(self, filePath=u''):
		self.__database = None
		self.__cursor = None
		self.__tables = {}
		if len(filePath)>0:
			self.setPath(filePath)
		
	def __del__(self):
		if self.__database:
			self.__database.close()
			
	def setPath(self, filePath):
		if self.__database:
			print 'Database already exists'
			return 	
			
		if os.path.exists(filePath):
			if hasattr(sys,'frozen'): # only when running in py2exe this exists
				base = sys.prefix
			else: # otherwise this is a regular python script
				base = os.path.dirname(os.path.realpath(__file__))
			filePath=os.path.join(base, filePath)

		# print "database: " + filePath
		self.__database = db.connect(filePath)
		self.__cursor = self.__database.cursor()
		try:
			sql = u"SELECT sql FROM sqlite_master WHERE type='table';"
			self.__cursor.execute(sql)
			for row in self.__cursor:
				tableSql = row[0]
				# print tableSql
				self.__addTable(tableSql)
		except:
			print "database information not found"

	def __addTable(self, sqlQuery):

		sqlQuery = u'' + sqlQuery	
		theLiteTable = liteTable()
		tableName = u''
		matches = re.findall('CREATE TABLE "?([^"\s]+)"?.*\n',sqlQuery)
		for m in matches:
			tableName = "%s" % m
		theLiteTable.beginTable(tableName)
		matches = re.findall(ur'^[\s\t]*"?([^"\(\s\n]+)"?\s+([^\n\s,]+)([^\n,]*).*$',sqlQuery, re.M)
		for m in matches:
			if "CREATE" in m:
				continue
			if "KEY" in m:
				continue
			columnName = m[0]
			columnDef  = makeLiteType(m[1])
			defaultVal = m[2]
			theLiteTable.addColumn(columnName, columnDef, defaultVal, False)

		theLiteTable.endTable()
		self.__tables[tableName] = theLiteTable
		theLiteTable.setLiteBase(self)	
		
			
	def addTable(self, theLiteTable):
		if not self.__cursor:
			return 
		if not isinstance(theLiteTable, liteTable):
			return 
		tableName = theLiteTable.getTableName().strip()
		if self.__tables.has_key(tableName):
			print 'This table exists in the database'
			return 
			
		if theLiteTable.addable():
			theLiteTable.endTable()
			
		try:
			sql = theLiteTable.getSqlQuery()
			self.__cursor.execute(sql)
			self.__tables[tableName] = theLiteTable
			theLiteTable.setLiteBase(self)
		except:
			print 'the table "%s" couldn\'t be created' % (tableName)
	
	def getTable(self, tableName):
		if not self.__tables.has_key(tableName):
			print 'table named "%s" doesn\'t exist' % (tableName)
			return None
		return self.__tables[tableName]
	
	
	def executeMyQuery(self, theLiteTable):
		if not isinstance(theLiteTable, liteTable):
			print "you have to input a liteTable object"
			return
		tableName = theLiteTable.getTableName().strip()
		if not self.__tables.has_key(tableName):
			print 'This table doesn\'t exist in the database'
			return 
		if self.__tables[tableName] != theLiteTable:
			print 'The table name exists, but this is not the right table '
			return
		try:	
			self.__cursor.execute(theLiteTable.getTmpQuery())
		except:
			print "couldn't execute the query"
			
		return self.__cursor
		
	def commit(self):
		self.__database.commit()	
		
	def containTable(self, tableName):
		return self.__tables.has_key(tableName)
		
class liteTable(object):
	
	def __init__(self):
		self.__columnNames = []
		self.__columnTypes = []
		self.__indexed = []
		self.__tableName = u''
		self.__sqlQuery = u''
		self.__canAddColumns = True
		self.__defStarted = False #if the user use many beginTable(tableName), the query won't be affected
		self.__liteDB = None
		self.__tmpQuery = u''
		
	def beginTable(self, tableName):
		if self.__defStarted:
			return 

		self.__defStarted = True	
		self.__tableName = tableName
		self.__sqlQuery = u'CREATE TABLE %s (\n' % (tableName)
		
	def endTable(self):
		if not self.__canAddColumns:
			return 
		
		self.__sqlQuery += u'\n);'
		self.__canAddColumns = False
		
			
	def addColumn(self, columnName, columnDef, columnInf, index):
		if not self.__canAddColumns:
			return 
		if len(self.__tableName) < 1:
			return
		if len(columnName)< 1:
			print "There is no name for the column"
			return 
		if not isinstance(columnDef, liteType):
			print "The definition must be a liteType class"
			return
			 
		if len(self.__columnNames) > 0:
			self.__sqlQuery += u',\n'

		self.__columnNames.append(columnName)
		self.__columnTypes.append(columnDef)
		self.__indexed.append(index)
		self.__sqlQuery += u'%s %s' % (columnName, columnDef.getDefinition())
		if len(columnInf)>0:
			self.__sqlQuery += u' ' + columnInf
	
	
	def insertData (self, values, columns=u''):
		if not self.__liteDB:
			return 
		self.__tmpQuery = u'INSERT INTO %s ' % self.__tableName
		if len(columns)>0:
			self.__tmpQuery += u'(%s) ' % columns
		self.__tmpQuery += u'VALUES (%s);' % values
		self.__liteDB.executeMyQuery(self)
	
	def getData (self, conditions=[]):
		if not self.__liteDB:
			return 
		self.__tmpQuery = u'SELECT * FROM %s' % self.__tableName
		if len(conditions)>0:
			self.__tmpQuery += u'\n WHERE %s ' % conditions[0]
			i = 1
			while i < len(conditions):
				self.__tmpQuery += u'\n AND %s' % conditions[i]
				i+=1
		#~ print self.__tmpQuery
		return self.__liteDB.executeMyQuery(self)
			
		
	def setLiteBase(self, theLiteBase):
		if self.__liteDB:
			return 
		if not isinstance(theLiteBase, liteBase):
			print "You have to input an instance of liteBase class"
			return 
			
		self.__liteDB = theLiteBase
		
		
	def getSqlQuery(self):
		return self.__sqlQuery
	
	
	def getTableName(self):
		return self.__tableName
		
		
	def addable(self):
		return self.__canAddColumns
	
	
	def getTmpQuery(self):
		tmp = self.__tmpQuery
		self.__tmpQuery = u''
		return tmp
		
	def getColumnName(self, index):
		if number >= len(self.__columnNames):
			print "out of boundary index"
			return None
		return self.__columnNames[index]
	
	def getColumnIndex(self, columnName):
		if not columnName in self.__columnNames:
			print "column not exists"
			return None
		return self.__columnNames.index(columnName)


	def clone(self, tableName):

		sqlQuery = self.__sqlQuery
			
		theLiteTable = liteTable()

		theLiteTable.beginTable(tableName)
		matches = re.findall(ur'^[\s\t]*([^\(\s\n]+)\s+([^\n\s,]+)([^\n,]*).*$',sqlQuery, re.M)
		for m in matches:
			if "CREATE" in m:
				continue
			if "KEY" in m:
				continue
			columnName = m[0]
			columnDef  = makeLiteType(m[1])
			defaultVal = m[2]
			theLiteTable.addColumn(columnName, columnDef, defaultVal, False)

		theLiteTable.endTable()	
		return theLiteTable

class liteType(object):
	def __init__(self, definition):
		self.__typeDef = definition
		
	def getDefinition(self):
		return self.__typeDef
		
		
class liteINT(liteType):
	def __init__(self, number):
		if number < 1:
			definition = u'INT'
		else:
			definition = u'INT(%s)' % number
		liteType.__init__(self, definition)

class liteCHAR(liteType):
	def __init__(self, number):
		if number < 1:
			number = 1
		definition = u'CHAR(%s)' % number
		liteType.__init__(self, definition)

class liteVARCHAR(liteType):
	def __init__(self, number):
		if number < 1:
			number = 1
		definition = u'VARCHAR(%s)' % number
		liteType.__init__(self, definition)

class liteTEXT(liteType):
	def __init__(self):
		definition = u'TEXT'
		liteType.__init__(self, definition)

class liteINTEGER(liteType):
	def __init__(self):
		definition = u'INTEGER'
		liteType.__init__(self, definition)
	
class liteREAL(liteType):
	def __init__(self):
		definition = u'REAL'
		liteType.__init__(self, definition)

class litePK_INT_INC(liteType):
	def __init__(self):
		definition = u'INTEGER PRIMARY KEY AUTOINCREMENT'
		liteType.__init__(self, definition)
		
class litePK_INT(liteType):
	def __init__(self):
		definition = u'INTEGER PRIMARY KEY'
		liteType.__init__(self, definition)


def makeLiteType(stringType):
	stringType = string.upper(stringType)
	if re.match('INT[^\(]', stringType):
		return liteINT(0)
	if re.match('TEXT', stringType):
		return liteTEXT()
	if re.match('INTEGER', stringType):
		return liteINTEGER()
	if re.match('REAL', stringType):
		return liteREAL()
		
	matcher = re.findall('INT\(([^\)]+)\)', stringType)
	for m in matcher:
		num = m
		return liteINT(num)
	matcher = re.findall('VARCHAR\(([^\)]+)\)', stringType)
	for m in matcher:
		num = m
		return liteVARCHAR(num)
	matcher = re.findall('CHAR\(([^\)]+)\)', stringType)
	for m in matcher:
		num = m
		return liteCHAR(num)
	
	return liteType(stringType)
			
if __name__ == '__main__':
	c = makeLiteType("int")
	print c.getDefinition()
	
