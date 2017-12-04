#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Improve repr predifined function to best display of objects containing unicode
Unicode represention texts
@author: Taha Zerrouki
@contact: taha dot zerrouki at gmail dot com
@copyright: Taha Zerrouki
@license: GPL
@date:2014/03/01
@version: 0.1
"""
import repr as reprlib
class ArabicRepr(reprlib.Repr):
    """ A redifinition of repr fucntion,
    you can use it like this
    
    Example:
        >>> import pyarabic.arabrepr as arabrepr
        >>> arepr = arabrepr.ArabicRepr()
        >>> repr = arepr.repr
        >>> word = u"السلام عليكم ورحمة الله"
        >>> wordlist = word.split(" ")
        >>> print wordlist
        [u'\u0627\u0644\u0633\u0644\u0627\u0645', u'\u0639\u0644\u064a\u0643\u0645', u'\u0648\u0631\u062d\u0645\u0629', u'\u0627\u0644\u0644\u0647']
        >>> print repr(wordlist)
        [u'السلام', u'عليكم', u'ورحمة', u'الله']
    """
    def repr_unicode(self, obj, level):
        "Modify unicode display "
        return u"u'%s'" % obj
