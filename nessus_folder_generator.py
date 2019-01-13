"""
1.Read xslx file
2.

"""

import os
import re
import openpyxl
import sys

pathname = os.path.abspath(sys.argv[0])
if len(sys.argv) > 1 :
	pathname = os.path.abspath(sys.argv[1])
print(pathname)

