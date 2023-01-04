name = "Sam"
country = "US"
age = 26
satisfied = False
Hourly_Wage = 0
Daily_Wage = 0 * 8

print(f"I live in the {country}, I'm {age} and I make ${Daily_Wage}; Am I satisfied with my job? {satisfied}" )


Grocery_List = ["Milk", "Bread", "Eggs", "Peanut Butter", "Jelly"]
print(Grocery_List)
Grocery_List[3] = "Almond Butter"
Grocery_List.remove("Jelly")
print(Grocery_List)
Grocery_List.append("Coffee")
print(Grocery_List)

Pet_Info = {"Name": "Ringo", "Age": 7, "Hobbies": ["Barking", "Sleeping", "Snacking"], "Wakes": "Monday Morning", "Tuesday Night", "Etc"}       
print(f"My pet {Pet_Info[name]} is {Pet_Info[age]} and likes {Pet_Info[Hobbies]} he woken me up {Pet_Info[Wakes]} ")