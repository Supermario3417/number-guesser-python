import random
import time

score = 0
streak = 0
strikes = 0

def generateRandomNumber():
    return random.randint(1, 2 + streak)

while True:
    randomNumber = generateRandomNumber()
    response = input("Guess the number between 1 to " + str(streak + 2) + ": ")
    time.sleep(0.05)
    print("")
    time.sleep(0.1)
    randomMessage = random.randint(0, 2)
    
    if int(response) < 1 and int(response) > 2:
        while not response >= 1 and response <= 2:
            input("This is an invalid number. Try again.")
    if int(response) == randomNumber:
        if streak >= 20:
            print("*Screaming in the background*")
        elif streak >= 15:
            if randomMessage == 0:
                print("W- W- WHAT!?!?")
            elif randomMessage == 1:
                print("HOW ARE YOU DOING THIS!?!?")
            elif randomMessage == 2:
                print("GUYS!!! LOOK!!! THEY'RE DOING IT!!!")
        elif streak >= 10:
            if randomMessage == 0:
                print("Amazing!!!")
            elif randomMessage == 1:
                print("Beutiful!!!")
            elif randomMessage == 2:
                print("Numerical!!!")
        elif streak >= 5:
            if randomMessage == 0:
                print("Great!!")
            elif randomMessage == 1:
                print("Wow!!")
            elif randomMessage == 2:
                print("Keep it up!!")
        else:
            if randomMessage == 0:
                print("Ok!")
            elif randomMessage == 1:
                print("Nice!")
            elif randomMessage == 2:
                print("Good!")
        
        time.sleep(0.1)
        print("+" + str(100 + (50 * streak)))

        score += 100 + (50 * streak)
        streak += 1
    else:
        strikes += 1

        if strikes >= 3:
            if randomMessage == 0:
                print("Game over for you!")
            elif randomMessage == 1:
                print("You're done...")
            elif randomMessage == 2:
                print("You're out!")
            
            time.sleep(0.1)
            print("Final score: " + str(score))
            time.sleep(5)
            break
        else:
            if streak >= 15:
                if randomMessage == 0:
                    print("Ouch... After all that work...")
                elif randomMessage == 1:
                    print("Is it over...?")
                elif randomMessage == 2:
                    print("Wow... it finally dropped...")
            elif streak >= 10:
                if randomMessage == 0:
                    print("Ouch... After all that work?")
                elif randomMessage == 1:
                    print("And the streak is finally gone!")
                elif randomMessage == 2:
                    print("Back to zero... that was a long run.")
            elif streak >= 5:
                if randomMessage == 0:
                    print("Oof. Sorry, but no.")
                elif randomMessage == 1:
                    print("Well, it wasn't such a big streak... right?")
                elif randomMessage == 2:
                    print("Son- I- Alright...")
            else:
                if randomMessage == 0:
                    print("Nope!")
                elif randomMessage == 1:
                    print("Try again...")
                elif randomMessage == 2:
                    print("Incorrect.")
            time.sleep(0.2)
            print("Strike recived")
            streak = 0
    
    time.sleep(0.1)
    print("")
    time.sleep(0.1)
    print("Score: " + str(score))
    time.sleep(0.1)
    print("Streak: " + str(streak))
    time.sleep(0.1)
    print("Strikes: " + str(strikes))
    time.sleep(0.05)
    print("")
    time.sleep(0.5)
    print("")
    time.sleep(0.1)