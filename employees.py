#

first_name = input("\nFirst name: ")
last_name = input("Last name: ")
hourly_wage = float(input("Hourly wage: "))
round (hourly_wage, 2)
hours_worked = float(input("Hours worked this week: "))
round (hours_worked, 2)

print ("\nFirst:\t", "Last:\t", "Hourly Pay:\t", "Hours Worked:")
print ("----------------------------------------------")
print (first_name,"\t", last_name,"\t", hourly_wage,"\t\t", hours_worked,"\n")

pay = hourly_wage * hours_worked

format_pay = "{:.2f}".format(pay)
print (f"${format_pay} will be owed to", first_name, "for this week.\n")

#