#! /usr/bin/env python3
import os

def check_reboot():
  """returns TRUE if a reboot is pending """
  return os.path.exists("/run/reboot-required")

def main():
  print("...starting script")
  print ("reboot needed?: {}".format(check_reboot()))
  pass

main()

