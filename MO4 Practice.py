
print("Ticket Price calculator")

age = int(input("What is your age: "))

child_ticket = 8
teen_ticket = 12
adult_ticket = 15
senior_ticket = 10

if age <= 12:
    print("Your ticket costs: $",str(child_ticket))
elif age <= 17:
    print("Your ticket costs: $",str(teen_ticket))
elif age <= 64:
    print("Your ticket costs: $",str(adult_ticket))
else:
    print("Your ticket costs: $",str(senior_ticket))


