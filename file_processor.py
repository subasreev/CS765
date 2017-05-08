# very simple example of reading a gradebook JSON
# - reads in the JSON file and writes an output file
# that contains score, lateness, number of posts,
# average length of posts, fixed category for each student
#
#  - can be run from the command line
#       python file_processor.py RealisticData/100x15.json
#
# sample code for CS765 Design Challenge 3
#
# this doesn't do a visualization (although, arguably it is a visualization)
# but it does show how to read in a data file and produce an output
# (in this case, text, not a picture)
# Reference: Prof. Michael Gleicher 
# Author:    Subasree Venkatsubhramaniyen, May 2017

import json
import sys

def gradebookSimple(filename):
    with open(filename,"rb") as fp:
        gb = json.load(fp)          # loads the json file
	outputfile = "scatterplot_file.csv"
	f = open(outputfile, 'w')
	f.write("score,lateness,num_posts,avg_post_length,category\n")
	#numassigns = len(gb["assignments"])

        # iterate over the students...
	for student in gb["students"]:
		for gradelist in student["grades"]:
			post_lengths = [g["length"] for g in gradelist["posts"]]
			sum = 0.0
			#print("printing ", post_lengths)
			for post_len in post_lengths:
				#print(post_len)
				sum = sum + post_len
			num_posts = len(gradelist["posts"])
			if num_posts == 0:
				avg = 0.0
			else:
				avg = sum/num_posts
			gradeline = "" + str(gradelist["score"]) + "," + str(gradelist["late"]) + "," + str(num_posts) + ","+ str(avg) + ",type1\n"
			f.write(gradeline)

            # for the scores, drop the lowest 2
	    #scores.sort()
	    #scores = scores[2:]

            # for the late, don't consider anything that's less than 4 hours late late

            # just print out the info - but to make nice columns, limit the width to 30 characters
	f.close()
# if this is run from the command line - call the program appropriately
# yes, I know this is a over-simplified way to do this, but it's meant to be quick and dirty
if __name__ == "__main__":
    gradebookSimple(sys.argv[1])
