print(" === Smart School Day Planner === ")
print("Answer 3 quick questions and I will plan your day.")

day = input(" What day is it? (Monday to Sunday): ").strip().capitalize()
weather = input(" What is the weather like? (sunny rainy/cloudy,): ").strip().lower()
homework = input("Is your homework done ? (yes/no): ").strip().lower()

print()
print(f"=== Your Plan for {day} ===")
print("-"*35)

if day in ("Saturday", "Sunday"):
    print("Day type   : Weekend - Enjoy your day off!")
elif day == "Monday":
    print("Day type   : First day of the week. Pack your weekly planner.")
elif day in  "Friday":
    print("Day type   : Last School day. Return Library books today.")
elif day in ("Tuesday", "Wednesday", "Thursday"):
    print("Day type   : Regular School day. Stay focused!")
else:
    print("Day type   :  Day not recognized. Please check your spelling.")
    