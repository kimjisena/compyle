#! /usr/bin/python

import os, sys

# compyle src:dest
def watch():
    fileStat = {}
    inFile, outFile = sys.argv[1].split(':')
    fileStat['lastMod'] = os.stat(inFile).st_mtime

    print('Watching {} for changes...'.format(inFile))
    print('<Ctrl + C> to exit...')
    while True:
        try:    
            if os.stat(inFile).st_mtime != fileStat['lastMod']:
                print('{} changed...'.format(inFile))
                fileStat['lastMod'] = os.stat(inFile).st_mtime
            else:
                continue
        except KeyboardInterrupt:
            print('\n')
            break

if __name__ == '__main__': watch()