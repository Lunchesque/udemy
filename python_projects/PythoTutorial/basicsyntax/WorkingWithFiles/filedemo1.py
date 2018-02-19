"""
File I/O
'w' -> Write-Only Mode
'r' -> Read-only Mode
'r+' -> Read And Write Mode
'a' -> Append Mode
"""

my_list = ["first line", "second line1", "third line"]

my_file = open("firstfile.txt", "w")

for item in my_list:
    my_file.write(str(item) + "'\n")

my_file.close()