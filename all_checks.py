#! /usr/bin/env python3
import os

def check_reboot():
  """returns TRUE if a reboot is pending """
  return os.path.exists("/run/reboot-required")

def main():
  pass

main()
print ("reboot needed?: {}\n".format(check_reboot()))

