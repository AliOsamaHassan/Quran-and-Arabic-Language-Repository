#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Copyright 2017 Abdelkrime Aries <kariminfo0@gmail.com>
#
#  ---- AUTHORS ----
#  2017	Abdelkrime Aries <kariminfo0@gmail.com>
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
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from aruudy.poetry import armetre


def test_arfilter():
    orig = u"تطويـــــــــــــــــــــل"
    dest = u"تطويل"
    assert armetre.arfilter(orig) == dest

def test_fix_al():
    orig = u"الأول الشمس القمر"
    dest = u"اَلأول شمس لقمر"
    assert armetre.fix_al(orig) == dest

def test_fix_awy():
    orig = u"ساح يسيح يسوح"
    dest = u"سَاح يسِيح يسُوح"
    assert armetre.fix_awy(orig) == dest


def test_get_cv ():
    orig = u"أَسِرْبَ القَطا هَلْ مَنْ يُعِيْرُ جَناحَهُ"
    dest = "VVCVCVVCVCVCVVCVVVCVVC"
    orig = armetre.fix_al(orig)
    orig = armetre.fix_awy(orig)
    assert armetre.get_cv(orig) == dest

def test_get_metre ():
    orig = "VVCVCVVCVCVCVVCVVVCVVC"
    dest = "u--u---u-uu-u-"
    assert armetre.get_metre(orig) == dest

def test_get_metre_name():
    orig = "u--u---u-uu-u-"
    dest = "tawiil"
    assert armetre.get_metre_name(orig) == dest
