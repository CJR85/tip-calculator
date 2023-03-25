# If the bill was $150.00, split between 5 people, with 12% tip
# Each person should pay (150.00 / 5) * 1.12 = 33.6
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? £"))
tip = int(input("How much tip would you like to give? 10, 12 or 15?"))
people = int(input("How many to split the bill?"))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
# Round the result to 2 decimal places = 33.60
final_amount = "{:.2f}".format(bill_per_person)
final_amount = round(bill_per_person, 2)
print(f"Each person should pay £{final_amount}")