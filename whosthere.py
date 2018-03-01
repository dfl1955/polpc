#!/usr/bin/python

# Author : Dave Levy  Date : 2 November 2015  Version 1.1
#
# This program tests a post code against a file list of postcodes. It is
# designed to see if an postcode is within a Parliamentary Constituency. It 
# will take the post code from the command line or as a file. I obtained the
# reference data from http://www.doogal.co.uk/ElectoralConstituencies.php

#	helpmsg = ' inthisclp.py -q <inputfile> -c <reference file>'
#
# this needs to return the count as a response parameter and needs to be part
# of a suit, the next version needs to output a list of addresses for each 
# match and maybe there should be a prompt for the reference files.

import sys, getopt, os.path

def parseargs(argv):
	query = '' 
	referencefile = 'LewDeptPostCodes_List.txt'
	helpmsg = ' inthisclp.py -q <inputfile> -c <reference file>'
	try:
		opts, args = getopt.getopt(argv, "hq:c:",["query=", "allclp"])
	except getopt.GetoptError:
		print helpmsg
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print helpmsg
			sys.exit()
		elif opt in ("-q", "--query"):
			query = arg
		elif opt in ("-c", "--allclp"):
			referencefile = arg
	response = [ query, referencefile ]
	return response


a = parseargs(sys.argv[1:])

print "%s ... starts" % ( sys.argv[0] ) 
print "    using %s as the object reference file" % ( a[1] )

# a holds the query file string and reference file

# if its a string we need to Upper Case it, but lets tests if its a file first
if os.path.isfile(a[0]):
	print "    the query parameter is %s" % ( a[0] )
	with open(a[0]) as g:
		queries = g.read().splitlines()
else:
	queries = [a[0].upper()]
	print "    the query parameter is %s" % ( a[0] )

with open(a[1]) as f:
	allcodes = f.read().splitlines()

print " "
i = 0
for query in queries:
	if query in allcodes:
		print "the code %s is in the reference file " % ( query )
		i = i + 1

h='has' ; s='match'
if i > 1:
	s = 'matches'
	h = 'have'

print "there %s been %i %s" % ( h, i, s )

exit

