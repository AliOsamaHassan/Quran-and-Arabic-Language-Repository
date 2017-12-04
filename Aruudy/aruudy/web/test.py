#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test.py
#  test the aruud on the web
#  
#  Copyright 2016 Abdelkrime Aries <kariminfo0@gmail.com>
#  
#  ---- AUTHORS ----
#  2016    Abdelkrime Aries <kariminfo0@gmail.com>
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

# enable debugging
import cgi
import cgitb
import json
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

import urlparse, urllib

import ar_metre

cgitb.enable()

args = cgi.FieldStorage()

res = {}

r = u""

r = args.getvalue("text")

r = unicode(r)

r = ar_metre.ar_filter(r)
res["filtred"] = r.encode('utf-8')

r = ar_metre.fix_al(r)
res["fix-al"] = r.encode('utf-8')

r = ar_metre.fix_awy(r)
res["fix-awy"] = r.encode('utf-8')
    
r = ar_metre.get_cv(r)
res["cv"] = r.encode('utf-8')
    
r = ar_metre.get_metre(r)
res["metre"] = r.encode('utf-8')
    
r = ar_metre.get_metre_name(r)
res["metre-name"] = r
    
print "Content-type: application/json;charset=utf-8"
print
print (json.dumps(res))
