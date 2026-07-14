'''1. Write a Dictionary to a JSON File (Most Common)'''

# import json

# student = {
#     "name": "Amit",
#     "age": 22,
#     "course": "Math",
#     "marks": 95
# }

# with open("student.json", "w") as file:
#     json.dump(student, file, indent=4)

# print("JSON file created Successfully")

import json

with open("student.json", "r") as file:
    data = json.load(file)

print(data)
print(data["name"])
print(data["age"])
