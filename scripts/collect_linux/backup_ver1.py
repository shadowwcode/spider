#!/usr/bin/env Python
# Filename: backup_ver1.py

import os
import time


# 1. The file and directories to be backed up are specified in the list
sources = ['/root/prac/', '/root/trash/']

# 2. The backup must be stored in a main backup directory
target_dir = '/tmp/backup'

# 3. The files are backed up into a tar.gz file
# 4. The name of the zip archive is the current date and time
target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.tar.gz'

# 5. We use the zip command(in Linux/Unix) to the put the files in a zip archive
tar_command = "tar -zcvf %s %s" % (target, ' '.join(sources))

# Run
if os.system(tar_command) == 0:
    print('Successful to backup to ', target_dir )
else:
    print('Backup failed!')






