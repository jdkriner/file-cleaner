import os
import time
from params import directory, suffix


#collect files to be deleted
for dir in directory:
    temp = []
    for file in os.listdir(dir):
        if file.endswith('_SCH'):
            delfile = os.path.join(dir, file)
            os.remove(delfile)


