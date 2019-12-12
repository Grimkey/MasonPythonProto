f=open("file.csv", "r")
contents = f.readlines()
i = 0

for line in contents:
   print("Line " + str(i) + " is " + line)
   i += 1