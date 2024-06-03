from time import *
import random as r # using this here to use multiple strings, but as list only

def mistake(paratest,usertest):
    error = 0
    for i in range(len(paratest)):
        try:
            if paratest[i]!=usertest[i]:
                error+=1
        except:
            error+=1     
            
    return error        
    
def speed_time(time_s, time_e, userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay,2)
    speed = len(userinput)/ time_R
    return round(speed)

if __name__ == '__main__':

    while True:  
        
        ck = input("  ready to test :  yes / no  :")  
        if ck == "yes":
            

            test = ["Hello india", "My name is ahmed", "What is your name"]

            test1 = r.choice(test)
            print("   ***** Typing speed *****")
            print(test1)
            print()
            print()
            time_1 = time()
            testinput = input(" Enter :  ")
            time_2 = time()

            print("Speed: ", speed_time(time_1, time_2, testinput)," w/sec")
            print("Error : ", mistake(test1, testinput))

        elif ck == "no":
            print(" Thank you")
            break

        else:
            print("Wrong input")
