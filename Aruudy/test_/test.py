#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test.py
#  after creating database, you can try this to test the program
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
import os
from db.litebase import liteBase
import pattern
import arudquery
#~ import wazn

if __name__ == '__main__':
	
	dbpath = os.path.realpath('test/arabicdict.sqlite')
	print dbpath
	srcdb = liteBase(dbpath)
	tab = srcdb.getTable('nouns')
	
	queryengine = arudquery.ArQuery()
	arpattern = pattern.Pattern(u'مَفْعَل')
	
	queryengine.setPattern(arpattern)#wazn.V3I4R3B
	queryengine.setEnd(u'ب')
	
	conditions = queryengine.getResult()
	print conditions
	
	rows = tab.getData(conditions)
	for row in rows:
		word = tab.getColumnIndex('word')
		patt = tab.getColumnIndex('pattern')
		print row[word] + "   " + row[patt]
