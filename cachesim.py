#!/usr/bin/python

import sys;

argc = len(sys.argv);

if argc < 2:
	print("ERROR: incorrect number of arguments.");
	print("usage: cachesim [input_file]");
	exit();
	
file = open(sys.argv[1]);

for line in file:
	print(line);
	
