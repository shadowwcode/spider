#!/usr/bin/env Python
# Filename: backup_ver1.py

import os
import time


# 1. The file and directories to be backed up are specified in the list
sources = ['/root/prac', '/root/trash']

# 2. The backup must be stored in a main backup directory
target_dir = '/tmp/backup/'

# 3. The files are backed up into a tar.gz file
# 4. The current day is the name of the subdirectory in the main directory
today = target_dir + time.strftime('%Y%m%d')
# The current name is the name of file
now = time.strftime('%H%M%S')

# Create the subdirectory if it isn't already there
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created the directory.' + today)

# The name of the file
target = today + os.sep + now + '.tar.gz'

# 5. We use the zip command(in Linux/Unix) to the put the files in a zip archive
tar_command = "tar -zcvf %s %s" % (target, ' '.join(sources))

# Run
if os.system(tar_command) == 0:
    print('Successful to backup to %s' % target_dir)
else:
    print('Backup failed!')






