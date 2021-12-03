import sys
file = open("students.txt", "r")
file_lines = file.readlines()
students = dict()
for line in file_lines:
    line = line.strip("\n")
    line = line.split(":")
    students[line[0]] = line[1]

for command in sys.argv[2].split(","):
    try:
        print("Name: {}, University: {}".format(command, students[command]))
    except KeyError:
        print("No record of ‘{}’ was found!".format(command))

