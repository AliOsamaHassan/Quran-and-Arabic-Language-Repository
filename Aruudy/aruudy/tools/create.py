#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  create.py
#  Used to create the database from arramouz database (http://arramooz.sourceforge.net/)
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

import sys
sys.path.insert(0,'../')

import db.litebase

if __name__ == '__main__':

	#you can create the dictionary using arramouz database (http://arramooz.sourceforge.net/)
	# ory ou can find it by downloading 
	#"http://sourceforge.net/projects/mishkal/files/mishkal2013-05-18.tar.bz2/download"
	# in ./lib/qalsadi/data/arabicdictionary.sqlite
	srcdb = litebase.liteBase('arabicdictionary.sqlite')
		
	dstdb = litebase.liteBase('words.sqlite')
	
	tab = litebase.liteTable()
	tab.beginTable("nouns")
	tab.addColumn('id', litebase.litePK_INT_INC(), u'', False)
	tab.addColumn('word', litebase.liteVARCHAR(20), u'DEFAULT NULL', True)
	tab.addColumn('pattern', litebase.liteVARCHAR(20), u'DEFAULT NULL', True)
	tab.endTable()
	print tab.getSqlQuery()
	
	dstdb.addTable(tab)
	src = srcdb.getTable('nouns')
	
	rows = src.getData()
	
	first = True
	for row in rows:
		if first:
			first = False
			continue
		vocalized = src.getColumnIndex('vocalized')
		unvocalized = src.getColumnIndex('unvocalized')
		pattern = getPattern(row[vocalized])
		data = u"'%s', '%s'" % (row[unvocalized],pattern)
		#~ print data
		tab.insertData(data, u'word, pattern')
	
	dstdb.commit() 
