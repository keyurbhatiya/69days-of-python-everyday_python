# day 23 of 69 days of python
# regex

# regular expressions (regex) in python

import re

# validate email address

# email = input("Enter your email :")

# email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

# if re.match(email_pattern,email):
#     print("Valid email addess..")
# else:
#     print("Invalid email...")


# validate phone number

# phone = input("Enter your phone number :")
# phone_pattern = r'^[6-9]\d{9}$'

# if re.match(phone_pattern, phone):
#     print("Valid Phone Number")
# else:
#     print("Invalid Phone Number")

# find all numbers from a string

text ="My order numbers are 456, and 789456"

numbers = re.findall(r'\d+',text)
print("Numbers found in the text : ",numbers)

# replace digits with '*'

marked_text = re.sub(r'\d','*',text)
print("Marked text : ",marked_text)

print("End of day22 of 69 days of python")