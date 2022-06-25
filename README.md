# Compyle

`compyle.py` is a simple python script that watches a C file for changes and 
automatically compiles it (and runs the resulting program).

## Usage

`$ ./compyle.py src:des` - watches `src` for changes and compiles it, saving output to `des`

`$ ./compyle.py src:des -r [...args]` - watches `src` for changes, compiles and runs it, 
passing `[...args]` as arguments.

`compyle.py` outputs to `stdout`, the result of compiling or running the C program.