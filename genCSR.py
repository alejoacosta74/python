
#! /usr/bin/env python3
import os
import sys
import pexpect
import subprocess

def genCSR(command):
 child = pexpect.spawn(command)
 child.logfile = sys.stdout.buffer
 child.expect ('Enter PEM pass phrase')
 child.sendline ('ericsson')
 child.expect ('Verifying - Enter PEM pass phrase')
 child.sendline ('ericsson')
 child.expect ('Country Name')
 child.sendline ('SE')
 child.expect ('State or Province Name ')
 child.sendline ('Stockholm')
 child.expect ('Locality Name ')
 child.sendline ('Stockholm')
 child.expect ('Organization Name')
 child.sendline ('Ericsson')
 child.expect ('Organizational Unit Name')
 child.sendline ('IT')
 child.expect ('Common Name')
 child.sendline ('peer0.seller.dlt.ericsson.com')
 child.expect ('Email Address')
 child.sendline ('')
 child.expect ('challenge password')
 child.sendline ('')
 child.expect ('optional company name')
 child.sendline ('')

my_env = os.environ.copy()
openSSLgenKey = 'openssl genpkey -genparam -algorithm ec -pkeyopt ec_paramgen_curve:P-256 -out ECPARAM.pem'
#keyResult = subprocess.run(openSSLgenKey, env = my_env)
child1 = pexpect.run(openSSLgenKey)
openSSLreq = 'openssl req -newkey ec:ECPARAM.pem -keyout PRIVATEKEY.key -out MYCSR.csr'
genCSR(openSSLreq)




#main()

