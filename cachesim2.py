#! /usr/bin/python


import sys
import re
import set_assoc_cache as CacheLib

if len(sys.argv) < 2:
    print("ERROR: incorrect number of arguments")
    print("usage: cachesim filename [cacheSize | cacheLineSize | ways]")
    sys.exit(1)

file= open(sys.argv[1], "r")
#file= open("1KB_64B")
#**Error check later**

#Initialize variables with the arguments (Later)

if len(sys.argv) == 5:
  cacheLnSz = int(sys.argv[3])
  cacheSz = int(sys.argv[2])
  ways = int(sys.argv[4])
  cache = CacheLib.Cache(cacheSz, ways, cacheLnSz)


while True:
  inputLine = file.readline()
  #Exit condition on empty line
  if inputLine == "":
      break
  #
  whiteSpaceMatch = re.match(r'^\s*$',inputLine)
  if whiteSpaceMatch != None:
      continue
  inputLine = inputLine.rstrip('\n')
  #Split current line into 3 tokens: PC, R/W, and memory address
  tokenM = inputLine.split()
  #Converting the string into an int, then a hexa. There may be
  #a more graceful method, but this works
  virtAddr = int(tokenM[2], 16)
  
  RW = tokenM[1]
  #PC isn't important, this is just here for consistency
  PC = tokenM[0]
  cache[virtAddr]
    
    
if cache.accesses != 0 :
  print("miss rate: " + str( (cache.misses/cache.accesses)*100 )+"%")
