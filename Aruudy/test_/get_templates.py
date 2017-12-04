#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test.py
#  after creating database, you can try this to test the program
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
import os
import sys
import pattern
from trans.buckwalter import Buckwalter

if __name__ == '__main__':
	
	reload(sys)  
	sys.setdefaultencoding('utf8')
	
	print "To exit enter an empty word"
	
	while (True):
		sys.stdout.write("Please enter an Arabic word: ")
		word = raw_input()
		if len(word)< 2:
			print "Thank you for using me"
			break
			
		wtrans = Buckwalter.translaterate(unicode(word))
		#print wtrans # Translateration
		templates = pattern.getTemplateNoDiac(wtrans)
		print Buckwalter.untranslaterate(templates)
		
