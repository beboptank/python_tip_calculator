print("Welcome to Tipsy, a free tip calculation tool.")

total_bill = float(input("What was the total bill? $"))
percentage_tip = int(input("What percentage tip would you like to leave? 15, 18, or 20? "))
number_of_people = int(input("How many people are splitting the bill? "))

total_plus_tip = total_bill + (total_bill * (percentage_tip / 100))
amount_owed_per_person = round(total_plus_tip / number_of_people, 2)

print(f"Each person should pay: ${amount_owed_per_person}")

