#!/usr/bin/env python

# I love Tabasco... the hot, legendary pepper sauce


from distutils.core import setup
from DistUtilsExtra.command import *

setup(name="unity-scope-trimet",
      version="0.1",
      author="Benjamin Kerensa",
      author_email="bkerensa@ubuntu.com",
      url="http://launchpad.net/~bkerensa",
      license="GNU General Public License (GPL)",
      data_files=[
    ('lib/unity-scope-trimet', ['src/unity-scope-trimet']),
    ('share/dbus-1/services', ['unity-scope-trimet.service']),
    ('share/unity/lenses/utilities', ['trimet.scope']),
    ('share/unity/lenses/utilities', ['icons/trimet-48.png']),
    ], cmdclass={"build":  build_extra.build_extra, })
