import os
import re
import string

import pyprocar as _; p=str(_.__path__)

c=re.sub(r'[\'\]\[]',r'',p)
os.system('cp scriptBandsplot.py %s' % (c))
os.system('cp -r procarplot %s' % (c))
print("--> installed path <--")
