#!/usr/bin/env python
import os
import sys
from optparse import OptionParser
def cronOptionParser():
	name=sys.argv[1]
	
	parser = OptionParser()
	parser.add_option("","--stop",dest="stopname",action="store_false",help="stop a job")
	parser.add_option("","--start",dest="startname",action="store_false",help="start a job")
	parser.add_option("-l","--list",dest="listname",action="store_false",help="list a job")
	(options,args) = parser.parse_args()
	stopname = options.stopname
	startname = options.startname
	listname = options.listname
	if stopname!=None:
		
		os.system('crontab -e')
	if startname!=None:
		
		os.system('crontab -e')
	if listname!=None:
	
		os.system('crontab -l | grep name')


if __name__=="__main__":
	cronOptionParser()