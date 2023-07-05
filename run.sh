#!/bin/bash

#shell script to update the pip libraries\

##### CONSTANTS #########
welcome_title="Welcome!"
right_now="$(date +"%x %r %Z")"
time_stamp="Accessed on $right_now by $USER"
program_name=PakPy

####### FUNCTIONS #######



###### MAIN ########
echo $welcome_title
echo Accesssing $program_name
echo $time_stamp
chmod 777 ./src/main.py
echo  
./src/main.py > output_file.txt 2>&1
echo DONE
