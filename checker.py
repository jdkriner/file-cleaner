import time
import os
from params import directory, suffix

x=0
if x == 0:
    for dir in directory:

    #get number of files every x seconds
        numFiles = len(os.listdir(dir))
        time.sleep(600)
        newNumFiles = len(os.listdir(dir))

    #when a file is downloaded, this will execute
        if numFiles != newNumFiles:
            newFiles = newNumFiles - numFiles

            #get the files in dir, sorted by recency
            files = filter(lambda x: os.path.isfile(os.path.join(dir, x)), os.listdir(dir))

            files = sorted(files, key=lambda x: os.path.getmtime(os.path.join(dir, x)))

            filelist = []
            for file in files:
                fname = os.path.join(dir, file)
                #ftime = time.strftime('%m/%d/%Y :: %H:%M:%S', time.gmtime(os.path.getmtime(fname)))

                filelist.append(fname)

            #pick out the x most recent files, however many were downloaded
            rename = []
            for i in range(newFiles):
                rename.append(filelist.pop(-1 -i))



            for file in rename:
                os.rename(f'{file}', f'{file}{suffix}')
            print(rename)




'''
directory = '/home/jack/Downloads'

files = filter(lambda x: os.path.isfile(os.path.join(directory, x)), os.listdir(directory))

files = sorted(files, key = lambda x: os.path.getmtime(os.path.join(directory, x)))

filelist = []
for file in files:
    fname = os.path.join(directory, file)
    ftime = time.strftime('%m/%d/%Y :: %H:%M:%S', time.gmtime(os.path.getmtime(fname)))

    filelist.append(fname)

print(filelist)'''