# ==========================================================================
# A simple command line tool that takes 2 values and adds them together using
# the funcs.py library's 'add2' function.
# ==========================================================================


import sys
import funcs

argnumbers = len(sys.argv) - 1

if argnumbers == 2 :
    print("")
    a = str(sys.argv[1])
    b = str(sys.argv[2])
    print(f"{a} + {b} = {str(funcs.add2(a, b))}")
    print("")
    sys.exit(0)

if argnumbers != 2 :
    print("")
    print("You entered " + str(argnumbers) + " value/s.")
    print("")
    print("Usage: 'addValues X Y' where X and Y are individual values.")
    print("       If addValues is not in your path, usage is './add2vals X Y'.")
    print("       If unbundled, usage is 'python addValues.py X Y'.")
    print("")
    sys.exit(1)