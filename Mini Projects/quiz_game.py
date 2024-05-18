print("Welcome to my computer quiz!")

playing  = input("Do you want to play? (y/n): ")

if playing.lower() != "y":
    quit()
   

print("Okay, let's play!")

score = 0  # doing this to provide score how many correct answer

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1 
else:
    print("Incorrect!")
        

answer = input("What ML stand for? ")
if answer.lower() == "machine learning":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")        


answer = input("What does DL stand for? ")
if answer.lower() == "deep learning":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")    
    
answer = input("What does AI stand for? ")
if answer.lower() == "artificial intelligence":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")    
    
    
print("You got " + str(score) + " questions corrects!")    

print("you got " + str((score/4) * 100) + " %.")    