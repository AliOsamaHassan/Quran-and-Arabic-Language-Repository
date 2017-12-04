Aruudy
======

| |Project|
| |License|
| |PyPI|
| |Travis|
| |Codecov|

It is a set of python libraries which aims for Arabic prosody (Arud) or
"Science of Poetry".

Features
--------

-  Detecting Arabic poetry metre
-  Detection of word pattern
-  Search words with pattern, beginning and ending

Use
---

Install
~~~~~~~

::


    ### Command line

aruudy -bahr

::

    pip install aruudy

Command line
~~~~~~~~~~~~

::

    aruudy -b 'أَسِرْبَ القَطا هَلْ مَنْ يُعِيْرُ جَناحَهُ'

Python
~~~~~~

Arabic poetry meter detection

.. code:: python

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    from poetry import ar_metre

    r = u'أَسِرْبَ القَطا هَلْ مَنْ يُعِيْرُ جَناحَهُ'
    print("original: " + r)

    r = ar_metre.ar_filter(r)
    r = ar_metre.fix_al(r)
    print("filtered: " + r)

    r = ar_metre.fix_awy(r)
    print("awy fixed: " + r)

    r = ar_metre.get_cv(r)
    print("metre desc: " + r)

    r = ar_metre.get_metre(r)
    print("metre: " + r)

    r = ar_metre.get_metre_name(r)
    print("metre name: " + r)

@TODO more examples

License
-------

Copyright (C) 2014-2017 Abdelkrime Aries

| Licensed under the Apache License, Version 2.0 (the "License");
| you may not use this file except in compliance with the License.
| You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

| Unless required by applicable law or agreed to in writing, software
| distributed under the License is distributed on an "AS IS" BASIS,
| WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
  implied.
| See the License for the specific language governing permissions and
| limitations under the License.

.. |Project| image:: https://img.shields.io/badge/Project-Aruudy-0BDA51.svg?style=plastic
   :target: http://ararud.sourceforge.net
.. |License| image:: https://img.shields.io/badge/License-Apache_2-0BDA51.svg?style=plastic
   :target: http://www.apache.org/licenses/LICENSE-2.0
.. |PyPI| image:: https://img.shields.io/pypi/v/aruudy.svg?style=plastic
   :target: https://pypi.python.org/pypi/aruudy
.. |Travis| image:: https://img.shields.io/travis/kariminf/aruudy.svg?style=plastic
   :target: https://travis-ci.org/kariminf/pytransliteration
.. |Codecov| image:: https://img.shields.io/codecov/c/github/kariminf/aruudy.svg?style=plastic
   :target: https://codecov.io/gh/kariminf/aruudy
