import json
import sys
import os


def check_exists(file_path):
    if os.path.exists(file_path):
       print("the file exists")
    else:
        print('The file does not exist')


def recieveJson(file_path):
    check_exists(file_path)
    with open(file_path)as file:
        try:
            json.load(file)
            print("Valid JSON")
        except ValueError as err:
            print("The file has JSON-structured errors in its syntax:")
            print(err)



file = sys.argv[1]
recieveJson(file)