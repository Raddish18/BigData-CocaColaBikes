#!/usr/bin/python

# --------------------------------------------------------
#           PYTHON PROGRAM
# Here is where we are going to define our set of...
# - Imports
# - Global Variables
# - Functions
# ...to achieve the functionality required.
# When executing > python 'this_file'.py in a terminal,
# the Python interpreter will load our program,
# but it will execute nothing yet.
# --------------------------------------------------------

import sys
import codecs
import itertools
import more_itertools
import calendar
import datetime as dt
from datetime import timedelta
#---------------------------------------
#  FUNCTION get_key_value
#---------------------------------------
def get_key_value(line):
    # 1. We create the output variable
    res = ()

    # 2. We remove the end of line char
    line = line.replace('\n', '')

    # 3. We get the key and value
    words = line.split('\t')
    day = words[0]
    hour = words[1]

    # 4. We process the value
    hour = hour.rstrip(')')
    hour = hour.strip('(')

    # 4. We assign res
    res = (day, hour)

    # 5. We return res
    return res

# ------------------------------------------
# FUNCTION my_reduce
# ------------------------------------------
def my_reduce(my_input_stream, my_output_stream, my_reducer_input_parameters):
    
	#Check date and then iterate through the times and check them against another iterating list. 
	
	#if the date is the same and the time is within 5 mins of the last then add 1 to counter

	#Add first time and counter to list
	
	num_ran_outs = 0
	current_time = ""
	current_date = ""
	last_time = ""
	df = []

    	for line in my_input_stream:
		info = get_key_value(line)
		
		if(current_date == "" and current_time == ""):
			current_date = info[0]
			current_time = info[1]
			last_time = info[1]
		elif(current_date == info[0] and dt.datetime.strptime(info[1], '%H:%M:%S') - dt.datetime.strptime(current_time, '%H:%M:%S') <= timedelta(minutes=5) ):
				num_ran_outs = num_ran_outs +1
				current_time = info[1]
				#print(1)
		else:
			mystr = (current_date + "\t(" + last_time + ", " + str(num_ran_outs)+")\n")
			my_output_stream.write(mystr)
			current_date = info[0]
			current_time = info[1]
			last_time = info[1]
			num_ran_outs = 1
			
			
			
		
	
 
def my_main(local_False_Cloudera_True,
            my_reducer_input_parameters,
            input_file_example,
            output_file_example
           ):

    # 1. We select the input and output streams based on our working mode
    my_input_stream = None
    my_output_stream = None

    # 1.1: Local Mode --> We use the debug files
    if (local_False_Cloudera_True == False):
        my_input_stream = codecs.open(input_file_example, "r", encoding='utf-8')
        my_output_stream = codecs.open(output_file_example, "w", encoding='utf-8')

    # 1.2: Cloudera --> We use the stdin and stdout streams
    else:
        my_input_stream = sys.stdin
        my_output_stream = sys.stdout

    # 2. We trigger my_reducer
    my_reduce(my_input_stream, my_output_stream, my_reducer_input_parameters)

# ---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
# ---------------------------------------------------------------
if __name__ == '__main__':
    # 1. Local Mode or Cloudera
    local_False_Cloudera_True = False

    # 2. Debug Names
    input_file_example = "../../my_result/A01 - Hint3/2. my_sort_simulation/sort_1.txt"
    output_file_example = "../my_result/A01 - Hint3/3. my_reduce_simulation/reduce_sort_1.txt"

    # 3. my_reducer.py input parameters
    # We list the parameters here
    measurement_time = 5

    # We create a list with them all
    my_reducer_input_parameters = [measurement_time]

    # 4. We call to my_main
    my_main(local_False_Cloudera_True,
            my_reducer_input_parameters,
            input_file_example,
            output_file_example
           )
