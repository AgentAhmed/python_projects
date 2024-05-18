print("Welcome to my computer quiz!")

playing  = input("Do you want to play? (y/n): ")

if playing != "y":
    quit()
   

print("Okay, let's play!")

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
else:
    print("Incorrect!")
        

answer = input("What does GPU stand for? ")
if answer.lower() == "Graphics processing unit":
    print("Correct!")
else:
    print("Incorrect!")        


answer = input("What does RAM stand for? ")
if answer.lower() == "Random Access Memory":
    print("Correct!")
else:
    print("Incorrect!")    
    
answer = input("What does PSU stand for? ")
if answer.lower() == "Power Supply":
    print("Correct!")
else:
    print("Incorrect!")        