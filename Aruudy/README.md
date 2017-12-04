# Aruudy

[![Project](https://img.shields.io/badge/Project-Aruudy-0BDA51.svg?style=plastic)](http://ararud.sourceforge.net)
[![License](https://img.shields.io/badge/License-Apache_2-0BDA51.svg?style=plastic)](http://www.apache.org/licenses/LICENSE-2.0)
[![PyPI](https://img.shields.io/pypi/v/aruudy.svg?style=plastic)](https://pypi.python.org/pypi/aruudy)
[![Travis](https://img.shields.io/travis/kariminf/aruudy.svg?style=plastic)](https://travis-ci.org/kariminf/pytransliteration)
[![Codecov](https://img.shields.io/codecov/c/github/kariminf/aruudy.svg?style=plastic)](https://codecov.io/gh/kariminf/aruudy)

It is a set of python libraries which aims for Arabic prosody (Arud) or "Science of Poetry".

[Test here](http://ararud.sourceforge.net)

## Features
* Detecting Arabic poetry metre
* Detection of word pattern [not this version]
* Search words with pattern, beginning and ending [not this version]


## Use

### Install

```
pip install aruudy
```

### Command line

```
aruudy -b 'أَسِرْبَ القَطا هَلْ مَنْ يُعِيْرُ جَناحَهُ'
```

### Programming

Arabic poetry meter detection

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from poetry import armetre

r = u'أَسِرْبَ القَطا هَلْ مَنْ يُعِيْرُ جَناحَهُ'
print("original: " + r)

#Filters characters like tatwiil
r = armetre.ar_filter(r)
print("filtered: " + r)

# Al has diacretics according to shamsi-qamari characters
r = armetre.fix_al(r)
print("al fixed: " + r)

# When there is madd (a, o, i), folks don't put diacritics for the character
r = armetre.fix_awy(r)
print("awy fixed: " + r)

# Farahidi metre for poetry
r = armetre.get_cv(r)
print("scansion: " + r)

# Western-like metre
r = armetre.get_metre(r)
print("western scansion: " + r)

# Metre name
r = armetre.get_metre_name(r)
print("metre name: " + r)
```

## Recommendations

To detect the metre, the poem's part must be fully vocalized (has diacritics).
To this end, It is recommended to use [Mishkal](https://github.com/linuxscout/mishkal)

@TODO more examples

## License
Copyright (C) 2014-2017 Abdelkrime Aries

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

[http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
