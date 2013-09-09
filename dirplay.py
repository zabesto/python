import os
from os.path import join, getsize

print os.getcwd()


directory = r'c:\foo\goo'

head, tail = os.path.split(directory)

print "head: " + head
print "tail: " + tail

#if not os.path.exists(directory):
#    os.makedirs(directory)

if os.path.exists(directory):
    print "path found"
    os.removedirs(directory)
else:
    print "path NOT found"

tempdir = os.path.expandvars('%temp%')
for (dirpath, dirnames, filenames) in os.walk(tempdir):
    print dirpath
    print dirnames
    print filenames

# os.rename
# os.renames
# os.remove
# os.removedirs
# os.open
# os.getcwd
# os.path.splitunc
# os.listdir
# os.walk

