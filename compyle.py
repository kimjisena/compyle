#! /usr/bin/python

import os, sys, subprocess as sub
# compyle src:dest
def compile(infile, outfile):
    gccargs = ['gcc {} -o {}'.format(infile, outfile)]
    gcc = sub.Popen(gccargs, shell=True, stdout=sub.PIPE)
    return gcc.communicate()[1]

# compyle src:dest -r [args]
def run(outfile, args):
    command = './' + outfile
    for arg in args:
        command += ' ' + arg 
    #print(command)
    print(str(sub.Popen(command, shell=True, stdout=sub.PIPE).communicate()[0], 'utf-8'))

def watch():
    fileStat = {}
    inFile, outFile = sys.argv[1].split(':')
    fileStat['lastMod'] = os.stat(inFile).st_mtime

    print('Watching {} for changes...'.format(inFile))
    print('<Ctrl + C> to exit...')
    while True:
        try:    
            if os.stat(inFile).st_mtime != fileStat['lastMod']:
                sub.Popen(['clear'], shell=True)
                print('{} changed...'.format(inFile))
                fileStat['lastMod'] = os.stat(inFile).st_mtime
                status = compile(inFile, outFile)
                if len(sys.argv) > 2:
                    cliargs = sys.argv[3:]
                    run(outFile, cliargs)
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