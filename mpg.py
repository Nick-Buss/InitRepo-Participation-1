#!/usr/bin/env python3
print("Nicholas Buss's MGP App") #Title

# display a welcome message
print("The Miles Per Gallon program") #Title
print() #Blank line


# get input from the user
miles_driven= float(input("Enter miles driven:\t\t")) #Input for miles driven
gallons_used = float(input("Enter gallons of gas used:\t")) #input for gallons used
gas_price = float(input("Enter cost per gallon:\t")) #input for gas price

# calculate miles per gallon
mpg = miles_driven / gallons_used #Miles per gallon calculation
mpg_round = round(mpg, 1) #create value for rounded mpg value
cost_per_mile= gallons_used/gas_price #Cost per mile calculation


            
# format and display the result
print() #blank line
print("Miles Per Gallon:\t\t" + str(mpg_round)) #Convert rounded mpg to string and display
print() #blank line
print("Cost per Mile:\t\t" + str(round(cost_per_mile, 2))) #Convert cost per mile to rounded number and display as string
print("Done") #Done message


