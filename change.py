from importlib.resources import path
import os
from pathlib import Path
myfile=os.listdir()
for i in myfile:
    if(i!='change.py'):
        p =Path(i)
        p.rename(p.with_suffix('.jpg'))