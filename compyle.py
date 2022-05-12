#! /usr/bin/python

import os, sys, subprocess as sub

# compyle src:dest
def compile(infile, outfile):
    gccargs = ['gcc {} -o {}'.format(infile, outfile)]
    gcc = sub.Popen(gccargs, shell=True, stdout=sub.PIPE)
    return gcc.communicate()[1]

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
                status = compile(inFile, outFile)
                if status == None:
                    pass
                else:
                    print(status)
            else:
                continue
        except KeyboardInterrupt:
            print('\n')
            break

if __name__ == '__main__': watch()