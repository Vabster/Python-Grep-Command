# Python-Grep-Command
Simple Python Grep command

A python module that implements the grep command, including the -v and -x flags.

How to run examples:

python grep.py hello *
  This command would print the file name where the keyword "hello" is found" and the text on the line
  
python grep.py -x hello *  
  This command would only print lines with exactly match the keyword "hello"
  
python grep.py -v hello *  
  This command would only print lines with that do not contain the keyword "hello"
  
