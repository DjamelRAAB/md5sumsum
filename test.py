#! /usr/bin/env python3
import os, sys, timeit
import progressbar

# Get command-line arguments
(F, N), T = map(int, sys.argv[1:3]), float(sys.argv[3])

# Generate a random file hierarchy
print(f'1. Generate {F} random files for testing:')
for f in progressbar.progressbar(range(0, F)):
    os.system(f'mkdir -p test; dd if=/dev/urandom of=test/{f} bs=1 count=1024 > /dev/null 2>&1')

# Mesure 10 execution of a call to md5sumsum on our test dataset
print(f'2. Mesure {N} executions of our script:')
x = timeit.timeit("""
import os
os.system('./md5sumsum test')
""", number=N)

# Return an error exit code to Travis CI if our script is too slow
print(f'Our execution time is {x}s, our test goal was {T}s')
sys.exit(1 if x > T else 0)