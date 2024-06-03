# a-z
# 0-9
# . _ time 1 before @
# @ time 1
# . 2nd or 3rd position from last after @ 

import re
email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email = input("Please enter your email address :  ")

if re.search(email_condition, user_email):
    print("Your email address {user_email} is valid")
    
else:
    print("Your email address {user_email} is not valid")