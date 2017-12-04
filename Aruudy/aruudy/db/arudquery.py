#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  arudquery.py
#  Used to build a query for words search, using the pattern, the word's
#  ending, etc.
#  
#  Copyright 2015 Abdelkrime Aries <kariminfo0@gmail.com>
#  Copyright 2014 DzCoding group <dzcoding@googlegroups.com>
#  
#  ---- AUTHORS ----
#  2014-2015	Abdelkrime Aries <kariminfo0@gmail.com>
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

import pattern

WORD = u'word'
PATTERN = u'pattern'

class ArQuery(object):
	def __init__(self):
		self.initiate()

	def initiate(self):
		self.__end = u''
		self.__pattern = None
	
	def setPattern(self, thepattern):
		if not isinstance(thepattern, pattern.Pattern):
			return
		self.__pattern = thepattern
	
	def setEnd(self, ending):
		self.__end = ending
	
	def getResult(self):
		result = []
		
		if self.__pattern:
			patterncode = self.__pattern.getPatternCode()
			tmp = u"pattern='%s'" % patterncode
			'''pos = self.__pattern.getPos3in()
			patterncode = patterncode[0:pos] + u'0' + patterncode[pos+1:]
			tmp += u" OR pattern='%s')" % patterncode'''
			result.append(tmp)
			'''start = self.__pattern.getStart()
			beginlen = len(start)
			
			if beginlen > 0 :
				tmp = u"substr(%s,1,%s)='%s'" % (WORD, str(beginlen), start)
				result.append(tmp)
			'''
		if len(self.__end) > 0 :
			endlen = len(self.__end)
			tmp = u"substr(%s,length(%s) - %s,%s)='%s'" % (WORD, WORD, str(endlen-1), str(endlen), self.__end)
			result.append(tmp)
		return result


if __name__ == '__main__':
	import arudquery
	q = ArQuery()
	q.setPattern(pattern.Pattern(u'مٌسْتَفْعَل'))
	t = q.getResult()
	print t
	
