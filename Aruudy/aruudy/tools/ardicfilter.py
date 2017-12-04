#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ardicfilter.py
#  Used to create the database from another which contains only the words vocalised and not vocalized
#  
#  Copyright 2015 Abdelkrime Aries <kariminfo0@gmail.com>
#  
#  ---- AUTHORS ----
#  2015    Abdelkrime Aries <kariminfo0@gmail.com>
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
import os
sys.path.insert(0,'../')

import re
from db import litebase
from trans.buckwalter import Buckwalter
import pattern

	
if __name__ == '__main__':

	# 
	'''theword = "AbotAE"
	theword_u = "AbtAE"
	print distance(theword, "AfotaAEa")
	print getTemplate(theword, theword_u)
	exit()'''
	srcdb = litebase.liteBase(os.path.realpath('../test/ardic.sqlite'))
		
	dstdb = litebase.liteBase(os.path.realpath('../test/words.sqlite'))
	
	tab = litebase.liteTable()
	tab.beginTable("words")
	tab.addColumn('id', litebase.litePK_INT_INC(), u'', False)
	tab.addColumn('word', litebase.liteVARCHAR(20), u'DEFAULT NULL', True)
	tab.addColumn('pattern', litebase.liteVARCHAR(20), u'DEFAULT NULL', True)
	tab.addColumn('vocalized', litebase.liteVARCHAR(20), u'DEFAULT NULL', True)
	tab.endTable()
	# print tab.getSqlQuery()
	
	dstdb.addTable(tab)
	
	src = srcdb.getTable('ardict')
	
	print src.getSqlQuery()
	
	rows = src.getData()
	
	vocalized = src.getColumnIndex('vocal')
	unvocalized = src.getColumnIndex('unvocal')
	i=0
	for row in rows:
		i = i + 1
		print "processing " + row[unvocalized]
		wtranslate = Buckwalter.translaterate(row[vocalized])
		#print deleteDiacritics(deleteRoot(wtranslate))
		wpattern = getTemplate(wtranslate)
		#wpattern_u = Buckwalter.untranslaterate(wpattern)
		#print deleteDiacritics(deleteRoot(wpattern))
		#pattern.getPattern(row[vocalized], row[unvocalized])
		data = u"'%s', '%s', '%s'" % (row[unvocalized], wpattern, row[vocalized])
		print data
		tab.insertData(data, u'word, pattern, vocalized')
		if i == 5000:
			dstdb.commit() 
			i=0
	
	dstdb.commit() 
