#! /usr/bin/env python3
import os
import sys

def check_reboot():
  """returns TRUE if a reboot is pending """
  return os.path.exists("/run/reboot-required")

def main():
  print("...starting script")
  if check_reboot():
    print ("Pending reboot \n")
    sys.exit(1)
  print ("Everything is ok")
  system.exit(0)

main()

