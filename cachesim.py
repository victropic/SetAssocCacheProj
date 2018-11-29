#!/usr/bin/python

import sys;
import set_assoc_cache as CacheLib;

argc = len(sys.argv);

if argc < 2:
	print("ERROR: incorrect number of arguments.");
	print("usage: cachesim [input_file]");
	exit();
	
file = open(sys.argv[1]);

cache = CacheLib.Cache(32, 2);

print(cache.ways);
print(cache.sets);
print(cache[0]);
	
