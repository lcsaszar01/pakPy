#!/bin/bash

#shell script to update the pip libraries\

##### CONSTANTS #########
welcome_title="Welcome!"
right_now="$(date +"%x %r %Z")"
time_stamp="Accessed on $right_now by $USER"
program_name=pakPy
####### FUNCTIONS #######



###### MAIN ########
echo Hello $HOSTNAME 
echo $welcome_title
echo $pwd $time_stamp
chmod 754 main.py
./main.py
