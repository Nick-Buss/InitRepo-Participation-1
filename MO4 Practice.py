
print("Ticket Price calculator")

age = int(input("What is your age: "))

child_ticket = 8
teen_ticket = 12
adult_ticket = 15
senior_ticket = 10


if age <= 12:
    ticket_price = child_ticket
elif age <= 17:
    ticket_price = teen_ticket
elif age <= 64:
    ticket_price = adult_ticket
else:
    ticket_price = senior_ticket

print("Your ticket costs: $", str(ticket_price))

# calculate 7% tax and print it
tax = ticket_price * 0.07
print("Tax (7%): $", f"{tax:.2f}")

# new total ticket price and print
new_total = ticket_price + tax
print("Total price: $", f"{new_total:.2f}")



