#! /usr/bin/env python3

import sys
import re

def updateUserDict (per_user, username, entry):
    if username not in per_user:
        counter = {}
        counter["INFO"]=1
        per_user[username]= counter
    else:
        per_user[username].counter["INFO"] += 1

def updateErrorDict (error, error_message):
    if error_message not in error:
        error[error_message] = 1
    else:
        error[error_message] += 1


def createDicts(logfile):
    import operator
    per_user = {}
    error = {}
    with open (logfile,"r") as file:
        for line in file:
            username = re.search(r".* \((\w*)\)?",line)
            if "ticky: INFO" in line:
                updateUserDict(per_user, username, "INFO")
            if "ticky: ERROR:" in line:
                updateUserDict(per_user, username, "ERROR")
                error_message=re.search(r"ERROR: ([\w ]*)",line)
                updateErrorDict(error, error_message)
    error_sorted = sorted(error.items(), key = operator.itemgetter(1), reverse=True)
    per_user_sorted = sorted(per_user.items())
    return (error_sorted, per_user_sorted)

def writeCSV (dict , keys, file_name):
    import csv
    with open(file_name, "w") as file:
        writer = csv.DictWriter(file,fieldnames=keys)
        writer.writeheader()
        writer.writerows(dict)

logfile = sys.argv[1]
error , per_user = createDicts(logfile)
error_keys=["Error", "Count"]
writeCSV(error, error_keys, "error_message.csv")
user_keys=["Username", "INFO", "ERROR"]
writeCSV(per_user, user_keys, "user_statistics.csv")
