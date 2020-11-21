import csv
import sys
import re
import operator

def updateUserDict (per_user, username, entry):
    if username not in per_user:
        counter = {}
        per_user.update({username:counter})
        per_user[username].update({entry:1})
    else:
        counter = per_user.get(username)
        if counter.get(entry) == 0:
            counter[entry] = 1
        else:
            counter[entry] = counter.get(entry,0) + 1
        per_user[username].update(counter)


def updateErrorDict (error, error_message):
    if error_message not in error:
        error[error_message] = 1
    else:
        error[error_message] = error.get(error_message,0) + 1


def createDicts(logfile):

    per_user = {}
    error = {}
    with open (logfile,"r") as file:
        for line in file:
            result = re.search(r".* \((\w*)\)?",line)
            username = result.group(1)
            if "ticky: INFO" in line:
                updateUserDict(per_user, username, "INFO")
            if "ticky: ERROR:" in line:
                updateUserDict(per_user, username, "ERROR")
                results2=re.search(r"ERROR: ([\w ]*)",line)
                error_message=results2.group(1)
                updateErrorDict(error, error_message)
    return error, per_user

def createDictsLists(logfile):

    userList = []
    errorList = []
    with open (logfile,"r") as file:
        for line in file:
            result = re.search(r".* \((\w*)\)?",line)
            username = result.group(1)
            if "ticky: INFO" in line:
                updateUserDict(per_user, username, "INFO")
            if "ticky: ERROR:" in line:
                updateUserDict(per_user, username, "ERROR")
                results2=re.search(r"ERROR: ([\w ]*)",line)
                error_message=results2.group(1)
                updateErrorDict(error, error_message)
    return error, per_user


def writeCSV (dict , keys, file_name):
    with open(file_name, "w") as file:
        writer = csv.DictWriter(file,fieldnames=keys)
#        writer = csv.writer(file,fieldnames=keys)
        writer.writeheader()
        print("Dict: {} \n Keys: {}".format(dict, keys))
        writer.writerows(dict)

def writeList2CSV (list , keys, file_name):
    with open(file_name, "w") as file:
        writer = csv.writer(file)
        writer.writerow(keys)
        writer.writerows(list)


def printDicts (dict):
    items = dict.items()
    for key, value in items:
        print("Key: {} Value: {}".format(key,value))


#logfile = sys.argv[1]
logfile = "./syslog"
error_sortedList=[]
user_sortedList=[]
error , per_user = createDicts(logfile)
print("error Dict \n Type:{} \n contents:{} \n".format(type(error),error))
print("User Dict \n Type:{} \n contents:{} \n".format(type(per_user),per_user))
error_sortedList = sorted(error.items(), key = operator.itemgetter(1), reverse=True)
user_sortedList = sorted(per_user.items(), key = operator.itemgetter(0))
print("error sorted \n Type:{} \n contents:{} \n".format(type(error_sortedList),error_sortedList))
print("User sorted \n Type:{} \n contents:{} \n".format(type(user_sortedList),user_sortedList))
error_keys=["Error", "Count"]
#writeCSV(error, error_keys, "error_message.csv")
writeList2CSV(error_sortedList, error_keys, "error_message.csv")
user_keys=["Username", "INFO", "ERROR"]
writeList2CSV(user_sortedList, user_keys, "user_statistics.csv")
#writeCSV(per_user, user_keys, "user_statistics.csv")
