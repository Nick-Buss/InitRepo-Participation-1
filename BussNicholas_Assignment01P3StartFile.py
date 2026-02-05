firstName = 'Nicholas' #Name variable
print('Hello, my name is ' + firstName) #Name display msg

var_school = 'Utah Valley University' #school variable
print('I go to ' + var_school) #display school name

credits = 3  #credits value
classes = 6 #classes value
totalcredits = credits * classes #equation for total credits

print('If I take 6 classes this semester and all are three credits each I will be taking ' + str(totalcredits) + ' credits') #Display msg for total credits

print('I would like to save money by taking this many credits.') #display msg

maxCredits = 12 #max credit variable
costPerClass = 350 #cost per class
classFee = 20 #individual class fee

totalCostPerSemester = (totalcredits - maxCredits) / credits * costPerClass + (classFee * (totalcredits - maxCredits)/3) #equation to remove the free credits, then calculate total cost including class fees


print('If classes are free after the ' + str(maxCredits) + ' credits and each class cost $' + str(costPerClass) + ' (plus an additional $' + str(classFee) + ' per class fee), I will be saving $' + str(totalCostPerSemester) + ' a semester.') #equation for cost savings and display msg

totalCostPerYear = totalCostPerSemester * 3 #costPerYear equation

print('That is a wopping $' + str(totalCostPerYear) + ' a year!') #totalCostPerYear display msg

print('This was a very informative and worth while Python assignment!') #closing msg
