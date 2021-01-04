pointspossible = 37
score = 74
percent = score/pointspossible
grade = ""
print("Percentage is {}".format(percent))
studentName= "Luis"
if(1>=percent>=0.9):
    grade ="A"
elif (0.89>=percent>=0.8):
    grade ="B"
elif(0.79>=percent>=0.7):
    grade ="C"
elif (0.69>=percent>=0.6):
    grade="D"
elif (0.59>=percent>=0):
    grade="F"
else:
    grade="No exist"
print("Student name = {} and the grade is {}".format(studentName,grade))    
