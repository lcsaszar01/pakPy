#!/bin/bash

#shell script to update the pip libraries\

##### CONSTANTS #########
welcome_title="Welcome!"
right_now="$(date +"%x %r %Z")"
time_stamp="Accessed on $right_now by $USER"
program_name=PakPy
####### FUNCTIONS #######



###### MAIN ########
echo Hello $HOSTNAME 
echo Accesssing $program_name
echo $welcome_title
echo $time_stamp
chmod 777 main.py
./main.py
