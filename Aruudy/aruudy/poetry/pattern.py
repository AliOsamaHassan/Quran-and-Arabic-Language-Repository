#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pattern.py
#  Used to detect patterns from a fully vocalized word
#  Kasra = 1
#  Dhamma = 2
#  Fatha = 3
#  Sukuun = 4
#  Unvocalized = 0
#
#  Copyright 2015-2017 Abdelkrime Aries <kariminfo0@gmail.com>
#  Copyright 2014 DzCoding group <dzcoding@googlegroups.com>
#  
#  ---- AUTHORS ----
#  2014-2017    Abdelkrime Aries <kariminfo0@gmail.com>
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

import re
from Levenshtein import distance

TASHKIIL	= [u'ِ', u'ُ', u'َ', u'ْ']
TANWIIN		= [u'ٍ', u'ٌ', u'ً']

wazns = [
"fulal",
"faEAlil",
"mafAEil",
">afoyAl",
"faEAlilap",
"fawAEiyl",
"fulal",
"fuwal",
"faEAlil",
">afAEiy~",
"faEAliyl",
"faEAliyl",
"fawAEiyl",
"faE~Alap",
"faEAliyl",
"falAEil",
">afiE~A'",
"fAEa",
"faE~uwlap",
">ufoEiy~ap",
"faEolaliy~",
"fuwlap",
"ful~ap",
"mifoEal~ap",
"fulaEolAp",
"fuEAlap",
"faEoluwlap",
"fuwEolAliy~",
"fuE~Alap",
"fiyEAlap",
"fiEoliy~ap",
"fuEoliy",
">afal",
"ma>oEal",
"fAEiy",
"faEoyap",
"faEA}il",
"faEAliyl",
"fiyal",
"mafAEil",
"mafAEiyl",
"faEAEil",
"fuEolaliy~ap",
"fuEolAliy~ap",
"fuwEolAliy~ap",
"faEAlilap",
"faEAliyl",
"faEAliyl",
">afAEilap",
"fuEaE",
"faEA}il",
"faEAliyl",
"faEAyil",
"faEA}il",
"fawAE~",
"fawAE~",
"faEAliy~",
"faEAlilap",
"faEAliyl",
"faEAliyl",
"faEAliy",
">afoEAE",
"mafAEil",
"fiEaE",
"faEAliy",
"fiEaEap",
"mafA}il",
"faEAlil",
"|fAl",
"ma|Eil",
"fuEAap",
">afAEiyl",
">afAEil",
"faEAyA",
"faEAlil",
">afoEAl",
"fuEal",
">afAEil",
"faEA}il",
"faEAlil",
">afAEiyl",
"faEAlilap",
"faEAliyl",
"fuE~Al",
"fuE~Al",
"faEolAl",
"mafAlap",
"mafoEulap",
"fAEiy",
"mafoEaY",
"faEAyil",
">afoEAl",
">afoEAE",
"faEAlil",
"mafAEil",
"|fA'",
"fa>oy",
"fawAEil",
"mafAEil",
"tafAEiyl",
"mafAEiy",
"tafAEil",
"faEAlilap",
"faEAliyl",
">afoEilap",
"faEAliyl",
"ma|Eil",
"|EAl",
"fuEuwl",
"filAl",
"faEAliyl",
"faEAliyl",
"faEAlilap",
"ma|lil",
">afAEil",
"fuEolAn",
"faEAliy",
"fiyEAn",
"fiEal",
"fiEal",
"ma|Eil",
"mafAEil",
">afoEiyap",
">afiE~ap",
"fawAEiyl",
"ma|Eil",
"faEA}il",
">af~Al",
"|Eilap",
"fiEolAn",
"fawAEil",
"faEol",
">afoEAl",
">afoEul",
"fuEolAn",
"fuEuwl",
"fiEAl",
">afoEiyap",
"fAl",
">afoEAl",
"fiylAn",
"fuEAl",
">afoEilap",
"fiEolAn",
"fawAEil",
"faEuwl",
">afoEilap",
"fuEul",
"faEA}il",
"fiEolAn",
">afoEilap",
"faEA}il",
"fuEul",
"fuEolAn",
">afoEilA'",
">afoEul",
"faEiyl",
"fiEAl",
"fuEalA'",
">afil~A'",
">afil~ap",
"faEolaY",
"faEAlaY",
"fiEAl",
">afil~ap",
">afoEilap",
"|Eiyap",
">afoEul",
"fuEolAn",
"faEA}il",
"fuEul",
"faEiyl",
"faEAl",
">afoEilap",
"fiEolAn",
"fuEalA'",
"fal~",
">afoEAl",
"fuEuwl",
"faEal",
"fiEAl",
">afoEAl",
"fiEolap",
"fiEAlap",
"fuEuwl",
"fuEolAn",
"fiEolAn",
"faEil",
">afoEAl",
"faEul",
">afoEAl",
"fuEul",
">afoEAl",
"|fAl",
"fuEol",
">afoEAl",
"fiEAl",
"fiEolAn",
"fiylAn",
"fuEuwl",
"fuwl",
"waEol",
">afoEAl",
"mawAEiyl",
"fiylAn",
"fiEal",
">afoEAl",
"fiEil",
"|EAl",
"fiEol",
"fiE~",
">afoEAl",
"fiEalap",
"fiEAl",
"fuEuwl",
">afoEilap",
">afoEul",
"fuEal",
">afoEAl",
"faEiy~",
"fiEolap",
"faEAlA",
">afoEilA'",
"fuEol",
"faEolaY",
"fiEol",
"faEiylap",
"fuEul",
"faEA}il",
"fuEalA'",
"faEAlil",
"faEAlil",
"mawAEiyl",
"mafAE~",
"mafAEiy",
"mafAEap",
"miyEAl",
"tafaAEiy",
"fuEayol",
"mafoEAp",
"fuE~Al",
"fAEiyl",
"faEuwlal",
"fiE~",
"mafoEAp",
"mafaE~",
"fulaEolAp",
"fiE~",
"fiyEAl",
"faEolAlal",
">ufoEuwlap",
"tafAEulap",
"fiyluEolAliy~",
"fiyl",
"fiyEAliyap",
"fuEolul",
"mafoEuwliy~ap",
"faE",
"faEuwliy~",
"fuE~iy~ap",
"mifal~ap",
"fiyluEolAliy~ap",
"fAEiliy~ap",
"mafaE~ap",
"fiylap",
"fAE~ap",
"mafAEil",
"fuEal",
"fuEal",
"mufoEilap",
"mufiE~ap",
"fuEalA'",
"fiEoluwl",
"faEoliyliy~",
"fuEolAl",
"faEaliy~",
"fuEoliy~",
">afoEaliy~ap",
">afaE~iy~ap",
"fuwEap",
"fuEolAliy~",
"faE~ap",
"mafoEuwlap",
"faEilap",
"filaEoliyliy~",
"faEaliy~ap",
"fiEap",
"mufaE~alap",
"fuEoluwliy~ap",
"faEoliy~ap",
"faEiy~ap",
"fuE~ap",
"fuE~ap",
"fiEA'",
"faEow",
"fiEA'",
"fiE~ap",
"faEap",
"fuEolap",
"fuEal",
"fuEolaY",
"fuEal",
"fiEAl",
"faEolap",
"fuEaY",
"fiEAl",
"fAlap",
"fawAEil",
"fiEolap",
"fiEolaY",
"fiEal",
"fiEolAn",
"fiEaY",
"fAE",
"fuEAp",
"fAEil",
"fAE~",
"|Eil",
"faEalap",
"fuE~al",
"faEolaY",
"fuE~Al",
"fawAEil",
"fuEolAn",
"fuEalA'",
"fuE~",
"fiEalap",
"faE~il",
"faEolaY",
"faEalap",
"fiEAl",
"faEolAn",
"fiEAl",
"faElaY",
"fuEolAn",
"faEAlA",
"faE~",
"fuEuwl",
">afoEaY",
"fuEolAn",
"fawoEal",
"fawAEil",
"fawoEalap",
"fawAEil",
"fAEal",
"fawAEil",
"fAEilap",
"fawAEil",
"faEA}il",
"fAEuwlap",
"fawAEiyl",
"faEAlap",
"faEA}il",
"fuEul",
"fiEAlap",
"faEA}il",
"faEalA'",
"faEAliy",
"faEolaY",
"faEAlaY",
"faEolA'",
"faEAlaY",
"faEAlaY",
"fuEolulap",
"faEAlil",
"fiEolilap",
"faEAlil",
"faEoliyl",
"faEAliyl",
"fiEoliyl",
"faEAliyl",
"faEAlilap",
"faEolaluwl",
"faEAlil",
"mafoEil",
"mafAEil",
"mafAEiyl",
"mifoEal",
"mafAEil",
"mafoEal",
"mafAEil",
"mufoEal",
"mafAEil",
"faEolal",
"fawAEil",
"fayoEal",
"fayAEil",
"fawAEil",
">afoEal",
">af~al",
">afAEil",
">ufoEul",
">afAEil",
"<ifoEal",
">afAEil",
">ufoEuwl",
">afAEiyl",
"yafoEuwl",
"yafAEiyl",
"fiEolAl",
"faEAliyl",
"fuEoluwl",
"faEAliyl",
"mifoEAl",
"mafAEiyl",
"mafoEuwl",
"mafAEiyl",
"mafoEiyl",
"mafAEiyl",
"tafoEAl",
"tifoEAl",
"tafAEiyl",
"tafoEiyl",
"tafAEiyl",
"mafoEilap",
"mafAEil",
"mafoEalap",
"mafoEAp",
"fiEAlap",
"faEalAn",
"fuEAl",
"faEiyl",
"fuEolap",
"<ifoEAl",
"<iyEAl",
"tafoEiyl",
"mufAEalap",
"faEolalap",
"AisotifoEAl",
"AisotiyfAl",
"tafaE~ul",
"tafaE~iy",
"tafaE~",
"mafoEal",
"mafoEil",
"AinofiEAl",
"faEol",
"fuEol",
"fiEol",
"AifotiEAl",
"Aif~iEAl",
"fiEAl",
"fuEuwl",
"fuEuwlap",
"tafAEul",
"tafAEiy",
"tafAE",
"AisotifAlap",
"faEal",
"faEAlap",
"tafoEilap",
"tafaEolul",
"AifoEilAl",
"Ait~iEAl",
"<ifoEA'",
"mufAEAp",
"AinofiEA'",
"faEolap",
"AinofiEAlap",
"faEoy",
">ifAlap",
"AifotiEAlap",
"tafoEiylap",
"mifoEal",
"mifal~",
"mifoEAl",
"mifoEalap",
"mafoEalap",
"faE~Alap",
"fAEilap",
"fAEuwl",
"fAEil",
"mufaE~il",
"mufAEil",
"mufAE~",
"mufoEil",
"mufil~",
"muwfil",
"mufiyl",
"mutafaE~il",
"mutafAEil",
"mutafAl~",
"munofaEil",
"munofal~",
"mufotaEil",
"mufotal~",
"mut~aEil",
"mufoEal~",
"musotafoEil",
"musotafiyl",
"musotafil~",
"mufaEolil",
"mutafaEolil",
"mufoEalil~",
"musotafoEiy",
"mutafaE~iy",
"mafoEuwl",
"mufoEAl",
"mafuwl",
"mafiyl",
"mafoEiy",
"mufaE~al",
"mufAEal",
"mufoEal",
"muf~aEaY",
"muwfal",
"mufal~",
"mufAl",
"mutafaE~al",
"mutafAEal",
"munofaEal",
"mufotaEal",
"mufoTaEal",
"mut~aEal",
"musotafoEal",
"musotafAl",
"musotafal~",
"mufaEolal",
"faE~Al",
"faE~Alap",
"mifoEAl",
"faEuwl",
"faEiyl",
"faEil",
"mifoEiyl",
"fiE~iyl",
"fAEilap",
"mufaE~il",
"fAEuwl",
">afoEal",
"faEolAn",
"faEolA'",
"faEal",
"fuEAl",
"faEAl",
"faEol",
"fiEol",
"fuEol",
"fuE~",
"fuEul",
"faEil",
"faEiyl",
"fAEil",
"faEuwl",
"fay~il",
"mufotaEil",
"mufoTaEil",
"muf~aEil",
"mafoEuwl",
"musotafiyl",
">afoEal",
">afaE~",
"fuEolaY",
"mafoEal",
"mafoEil",
"musotafoEal",
"mafoEalAn",
"mafuwlap",
"mafiylap",
"mafiyl",
"faEolAlal",
"fiyEAl",
"fiyl",
"fiyl",
"fiEalap",
"fuEoluwAn",
"fuEolul",
"mafaE~",
"mafaE~",
"mafaE~",
"faEaluwt",
"fuEayol",
"fuEoliyl",
"fuEoliyl",
"faEoluwl",
"faEoluwl",
"fuEay~il",
"tafAE~",
"faEuwlal",
">ufoEulAn",
"fuEAlaY",
"fuE~al",
"fuE~al",
"faEolalAn",
"faEolalAn",
"AifoEiloEAn",
"fuEolulAn",
"fuwlAn",
"fiEal~",
"faE~uwl",
"fuEul~ul",
"faEal",
"|l",
"faEil",
"faEul",
"fAl",
"|l",
"faEiyl",
"faEaY",
"faE~",
"faEA",
"faEolal",
"faE~al",
"faE~aY",
"faE~aA",
"fAEal",
"fAEaY",
">afoEal",
">afaE~",
"|Eal",
">afAl",
">afoEaY",
"tafaE~al",
"tafaE~aY",
"tafAEal",
"tafAEaY",
"AinofaEal",
"AinofAl",
"AinofaEaY",
"Ainofal~",
"AifotaEal",
"AifoTaEal",
"AifoEAl",
"Aif~Eal",
"AifotAl",
"Aifotal~",
"AifotaEaY",
"Ait~aEal",
"AifoEal~",
"AisotafoEal",
"AisotafoEaY",
"AisotafAl",
"Aisotafal~",
"AifoEawoEal",
"tafaEolal",
"AifoEalal~",
"AifotiEAliy~", #Added by Karim
"AifotiEAliy~ap", #Added by Karim
"AifotiEAlAt", #Added by Karim
"AisotifoEAliy~", #Added by Karim
]

class Pattern(object):
	def __init__(self, definition):
		self.__label = definition
		self.__unvocal = unvocalize(definition)
		self.__code = getPattern(definition)


	def getPatternCode(self):
		return self.__code

	def getPatternLabel(self):
		return self.__label

	def getUnvocalized(self):
		return self.__unvocal


def getPattern(word):

	tmpPattern = u''

	for char in word:

		if char in TASHKIIL:
			tmpPattern += u'' + str(TASHKIIL.index(char)+1)

		elif char in TANWIIN:
			tmpPattern += u'0'

		elif char == u'ّ':
			tmpPattern += u'x'

		elif char == u'آ':
			if len(tmpPattern)>0 and tmpPattern[-1]== u'C':
				tmpPattern += u'3'
			tmpPattern += u'30'

		elif char == u'ا' or char == u'ى':
			if len(tmpPattern)>0 and tmpPattern[-1]== u'C':
				tmpPattern += u'3'
			tmpPattern += u'0'

		elif char == u'ﻻ':
			tmpPattern += u'30'

		else:
			tmpPattern += u'C'

	#~ tmp = u''
	#~ finalPattern = u''
	#~ for char in tmpPattern:
		#~ if char == u'C' and len(tmp)>0:
			#~ if tmp[0] == u'C':
				#~ if len(tmp)==1:
					#~ finalPattern += u'0'
				#~ else:
					#~ finalPattern += tmp[1:]
			#~ else:
				#~ finalPattern += tmp
			#~ tmp = u''
		#~ tmp += char
		#~
	#~ if tmp[0] == u'C':
		#~ if len(tmp)==1:
			#~ finalPattern += u'0'
		#~ else:
			#~ finalPattern += tmp[1:]
	#~ else:
		#~ finalPattern += tmp
	finalPattern = tmpPattern

	finalPattern = finalPattern.replace('CC', '0C')
	if finalPattern[-1]==u'C':
		finalPattern += u'0'
	finalPattern = finalPattern.replace('C', '')
	if finalPattern[-1]==u'x':
		finalPattern += u'0'
	finalPattern = finalPattern.replace('x', '4')

	return finalPattern


def unvocalize(word):
	diac = u'ّ'.join(TASHKIIL).join(TANWIIN)
	return re.sub(ur'[%s]' % diac, "", word)

def deleteDiacritics(word):
	#return word.translate(None, 'auiFNK~_o')
	return re.sub('[auiFNK~_o]', '', word)

def deleteRoot(word):
	return re.sub('[fEl]', '.', word)


def getTemplateNoDiac(word):
	"""This function take an Arabic word as parameter;
	it deletes its diacritics if exist; then returns the possible Templates;
	If there are many possible templates, they will be separated with + """

	template = u""
	minDistance = 1000
	word_u = deleteDiacritics(word)
	word_u = unicode(word_u)
	for wazn in wazns:
		wazn_u = deleteDiacritics(wazn)
		wazn_u = deleteRoot(wazn_u)
		wazn_u = unicode(wazn_u)
		if len(wazn_u) != len(word_u):
			continue

		#print "distance(" + word_u + "," + wazn_u + ")"
		distanceI = distance(word_u, wazn_u)
		if distanceI < minDistance:
			if re.match(wazn_u, word_u):
				minDistance = distanceI
				template = wazn
			continue
		if distanceI == minDistance:
			if re.match(wazn_u, word_u):
				template = template + '+' + wazn
	return template

def getTemplateFromList(word, template):
	"""This function take an Arabic  word (diacretized)
	and some possible templates separated by a +;
	If the program succeed to choose just one, it will add a (;)
	at the end
	"""
	minDistance = 1000

	#Here, we have a lot of templates, so we will test the diacritics
	templates = template.split('+')
	minDistance = 1000
	word_u = unicode(word)
	for wazn in templates:
		wazn_u = unicode(wazn)
		distanceI = distance(word_u, wazn_u)
		if distanceI < minDistance:
			minDistance = distanceI
			template = wazn
			continue
		if distanceI == minDistance:
			template = template + '+' + wazn
	if not '+' in template:
		template = template + ";"
	return template

def getTemplate(word):
	template = getTemplateNoDiac(word)
	if not '+' in template:
		return template
	return getTemplateFromList(word, template)

if __name__ == '__main__':
        from pattern import Pattern
        import sys
        from sys import argv
        script, word = argv
        word = unicode(word, 'utf-8')
        wordpat = Pattern(word)
        print wordpat.getPatternCode()
        print wordpat.getUnvocalized()
