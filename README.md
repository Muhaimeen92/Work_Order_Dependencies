# WORK ORDERS

This program is a utility that takes a pair of plain text files as the input (orders and dependencies) and outputs a structured JSON file that shows all work orders and their dependencies. 

The orders.txt file contains information about the orders. The file has the following columns:
● id - the id of the order (any integer between 0 and 10000)
● name - the name of the order (any string of length 1 to 100)

The dependencies.txt file contains all dependency relationships. Each row represents one dependency (i.e. in the example below, order 2 depends on order 1 being completed). The file has the following columns:
● id - the id of an order
● child_id - the id of an order that depends on the order in column 1

The output of the program is a JSON file that shows all the work orders and their dependencies.

The test.py file is designed to test result and output files. 
The files must already exist and the correct corresponding file paths provided for the unittest to 
run accurately.# Work_Order_Dependencies
