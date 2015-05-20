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
files_list_copy = []

for root, dirs, files in os.walk(source_folder):
  for f in files:
    files_list.append(f)
    files_list_copy.append(f)


for idf,f in enumerate(files_list):
  position_dot = f.rfind('.')
  target_file = f[:position_dot] +'.'+ destination_ext
  found = False
  for destination_root, destination_dirs, destination_files in os.walk(destination_folder,topdown=True, onerror=None, followlinks=True):
    for destination_file in destination_files:
      if destination_file == target_file:
        shutil.copy(destination_root + "/" + target_file, source_folder)
        files_list_copy.remove(f)
        found = True
  print f
  if found == False:
    print "found"
  else:
    print "not found"

if len(files_list_copy) > 0:
  print "\n"
  print "files not found:"
  for f in files_list_copy:
    print f
else:
  print "all files have been copied"
