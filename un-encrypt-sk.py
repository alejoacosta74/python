#! /usr/bin/env python3
import os
import sys
import pexpect
import subprocess
import re

def getKeyFiles(path):
    keyfiles = []
    tree = os.walk(path)
    for root, directories, files in tree:
        for file in files:
          if "sk" in file:
            keyfiles.append(os.path.join(root,file))  
            #print (os.path.join(root,file))
    return keyfiles

def unEncriptFiles(keyfiles):
    for f in keyfiles:
        command = "openssl ec -in {} -out {} ".format(f,f)
        child = pexpect.spawn(command)
        child.logfile = sys.stdout.buffer
        child.expect (["Enter PEM pass phrase", pexpect.EOF])
        child.sendline ("ericsson")

def checkIsUnencrypted (keyfiles):
    for f in keyfiles:
        with open (f, mode="r") as key:
          if "BEGIN EC PRIVATE KEY" in key.read():
             filename = re.search(r"keystore\/(.*sk$)", f)[1]
             print ("{} succesufully un-encrypted".format(filename))
          else:
             print ("{} ENCRYPTED".format(f))


path = sys.argv[1]
keyfiles = getKeyFiles(path)
unEncriptFiles(keyfiles)
keyfiles = getKeyFiles(path)
checkIsUnencrypted(keyfiles)
