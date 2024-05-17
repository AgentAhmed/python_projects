import random 

def guess(x):
    
    random_number = random.randint(1,x)
    
    guess = 0
    while guess != random_number:
        guess = int(input("guess a number between 1 and {x}:  "))
        if guess < random_number:
            print("Sorry, guess again, to low")
        elif guess > random_number:
            print("Sorry, guess again, to high")
    print("yay , congrats , you have guess the number {random_number} correct ")            
        
guess(10)        
        