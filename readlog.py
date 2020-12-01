#!/usr/bin/env python3
import re
import sys

def createDicts(logfile):
  per_user={}
  error={}
  with open (logfile,"r") as file:
    for line in file:
      username = re.search(r".* \((\w*)\)?",line)
      if "INFO" in line:
        if username in per_userwq


