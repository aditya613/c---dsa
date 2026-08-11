dictStudent = {"Daksh":2520, }


dictStudent["Aditya"]=2510
dictStudent["Arpit"]=2511

for student in dictStudent:
    print((student) + "-" + str(dictStudent[student]))

dictStudent.clear()

dictStudent["Kapoor"]=1110

print(dictStudent)