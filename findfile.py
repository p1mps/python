#!sr//bin/python

import shutil
import sys
import os


if len(sys.argv) < 4:
  print "Usage: sourceFolder destinationFolder destinationExtension"
  sys.exit(0)
  
source_folder = sys.argv[1]
destination_folder = sys.argv[2]
destination_ext = sys.argv[3]

files_list = []

for root, dirs, files in os.walk(source_folder):
  for f in files:
    files_list.append(f)

for root, dirs, files in os.walk(source_folder):
  for f in files:
    position_dot = f.rfind('.')
    target_file = f[:position_dot] +'.'+ destination_ext
    found = False
    for destination_root, destination_dirs, destination_files in os.walk(destination_folder,topdown=True, onerror=None, followlinks=True):
      for destination_file in destination_files:
        if destination_file == target_file:
          shutil.copy(destination_root + "/" + target_file, source_folder)
          files_list.remove(f)
          found = True
          break
        
    print f
    if found == False:
      print "not found"
    else:
      print "found"

if len(files_list) > 0:
  print "\n"
  print "files not found:"
  for f in files_list:
    print f
else:
  print "all files have been copied"
