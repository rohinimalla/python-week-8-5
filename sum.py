student = { "John": 85, "Alice": 90,"Bob": 75}
value_to_find = 90
for key, value in student.items():
   if value == value_to_find:
       print("Key for value", value_to_find, "is:", key)
       break
else:
   print("Value not found")

