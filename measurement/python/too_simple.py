# The Computer Language Benchmarks Game
# https://salsa.debian.org/benchmarksgame-team/benchmarksgame/
# python too_simple.py 100000000


import sys 
def main():
    n = int(sys.argv[1])
    sum = 0.0
    flip = -1.0
    for i in range(1,n):    
        flip *= -1.0        
        sum += flip / (2*i - 1)                                      
    print("%.9f" % (sum*4.0))
main() 