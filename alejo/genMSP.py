import os
import re
def getCertNames():
  certs = os.listdir(".")

def getOrgName(filename):
  if "orderer" in filename:
    org = "ordererOrganizations"
    orgName = "dlt.ericsson.com"
    nodeName = re.search(r"orderer[0-5]", filename)[0]
  else:
    org = "peerOrganizations"
    orgName = re.search(r"peer[0-5].(.*).cer",cert)[1]
    nodeName = re.search(r"peer[0-5]", filename)[0]
  return org, orgName , nodeName


cert = "orderer2.dlt.ericsson.com.cer"
org, orgName, nodeName = getOrgName(cert)
print ("Org:{} , OrgName={} , NodeName={}".format(org, orgName, nodeName))