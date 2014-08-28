#!/usr/bin/env python 
""" 
Convert JSON data to human-readable form. 
(Reads from stdin and writes to stdout) 
""" 
import sys 
import json as json



for x in range(0, 52):
	f=open("/input/input.txt","r")
	obj = (json.dumps(json.loads(f.read()) [x]) )
	f1=open("/input/output"+str(x)+".txt" ,"w")
	f1.write(obj)
	f1.close()
	f.close()
	




 
