from time import sleep
from random import randint    

def sad():
    print()
    print('Oh no.. What happend?')
    sleep(1.8)
    print('You can share with me!')
    sleep(1.9)
    print("I'll keep it as secret!")
    a = input("Share here :(    ")
    sleep(1.9)
    print('Very Sad, Hope your problem will solve soon :)')
    sleep(1.5)
    print("Let me try to boostup your mood.. ")
    sleep(1.8)
    print("I'll be back.. Stay tuned!!")
    sleep(2)
    print("I'm Back")
    sleep(2)
    dec()

def dec():
    print()
    print("Let's play a game now")
    sleep(1.5)
    print("Which game you want to play?")
    sleep(1.5)
    print("""1. Number Guessing.
2. Memory based. """)
   # time.sleep(1)
    c = input("Enter 1 or 2: ")
    try:
        c = int(c)
        if (c <= 2):
            if (c == 1):
                onegame()
            else:
                twogame()
        else:
            print("Enter correct choice :(")
    except:
        print("Sad!! Enter an integer, run the program again :(")

def twogame():
    print()
    print("---------------------Memory Game---------------------")
    print()
    sleep(2)
    print("This game is based on your memory")
    sleep(2)
    print("Ok, I'll eplain the rules")
    sleep(2)
    print("I'll give you 5 random words..")
    sleep(2)
    print("Remember all the words")
    sleep(2)
    print("You will have 5 seconds to remember")
    sleep(2)
    r = input("""Are you ready
1. Yes, I'm Ready to play
2. No, Swtich to Number guessing game
3. Quit
Enter(1 or 2 or 3): """)
    try:
        r = int(r)
        if(r <= 3):
            if(r == 1):
                memory()
            elif(r == 2):
                sleep(1.5)
                print("Switching to Number Guessing game, Stay tuned.. :)")
                sleep(1.5)
                onegame()
            else:
                sleep(1.5)
                print(" :( Sorry for disappointing you")
                sleep(1.5)
                print("Thankyou for testing Me! See you later, Bye")
        else:
            sleep(1.5)
            print("Please enter correct choice :(")
       
    except:
        print("Don't play with me..")
        sleep(1.5)
        print("Run the program again and enter integer :( ")

def onegame():
    print()
    print("---------------------Number guessing---------------------")
    sleep(2)
    print()
    print("This game is based on your luck.")
    sleep(2)
    print("Ok, I'll explain the rules")
    sleep(2)
    print("Simple, just guess a number b/w 1 to 30")
    sleep(2)
    print("I'll also guess my number, if both numbers are same, you'll get a point!")
    sleep(2)
    print("""Is it ok??
1. Good, let's try it
2. Not okay! Swtich to another game
3. Quit""")
  #  time.sleep(1)
    p = input("Enter your choice: ")
    try:
        p = int(p)
        if(p <= 3):
            if( p == 1):
                print("Let's see.. You can't catch me easily")
                game(0)
            elif(p == 2):
                print("Swtiching to Memory game.. Stay tuned!!")
                sleep(1.5)
                twogame()
            else:
                print(":( Sorry for disappointing you")
                sleep(1.5)
                print("Thankyou for testing me!  See you later, Bye :)")
        else:
            print("Enter an integer <= 3")       
    except:
        print("Sad, Run again and enter an integer :(")
            
# clearing screen

def cls():
    print("\n\n\n"*10)
    print("  ")
    print("\n\n\n"*10)
    print("\n\n\n"*10)
    print("  ")
    print("  ")
    print("\n\n\n"*10)
    print("  ")
    print("\n\n\n"*10)
    print("\n\n\n"*10)

# Calling memory game

def memory(pnt = 0):
    print()
    print("I'm going to give you 5 words.. Get ready")
    LIST = ['sun', 'moon', 'five', 'river', 'number', 'desktop', 'profile', 'commit', 'bash', 'phone', 'coffee', 'tea', 'music', 'movie', 'change', 'request', 'morning', 'browser']
    NEW = []
    print()
    sleep(1.5)
    v1 = LIST[randint(0,len(LIST)-1)]
    print(v1)
    NEW.append(v1)
    sleep(1.5)
    v2 = LIST[randint(0,len(LIST)-1)]
    print()
    print(v2)
    NEW.append(v2)
    sleep(1.5)
    v3 = LIST[randint(0,len(LIST)-1)]
    print()
    print(v3)
    NEW.append(v3)
    sleep(1.5)
    v4 = LIST[randint(0,len(LIST)-1)]
    print()
    print(v4)
    NEW.append(v4)
    sleep(1.5)
    v5 = LIST[randint(0,len(LIST)-1)]
    print()
    print(v5)
    NEW.append(v5)
    #sleep(1.5)
    #print(NEW)
    sleep(2)
    print("Time up!!, I'm going to clear the screen, remember all words")
    sleep(2)
    cls()

    print("Done!! Screen Cleared..")
    sleep(2)
    print("It's your turn now!")
    sleep(1.5)
    print("Get ready..!!")
    sleep(1.5)
    ran = randint(1,len(NEW))
    print("Now, enter word - {0}".format(ran))
   # print(NEW[ran-1])
    sleep(0.8)
    ran1 = input("Enter here(case sensitive): ")
    ran1 = ran1.strip()
    if(ran1 == NEW[ran-1]):
        pnt = pnt + 1
        print("You are correct, you just scored a point")
        sleep(1.5)
        print("""Do you want to try again or stop here?
1. Yes, Continue my progress.
2. No, Swtich to Number Guessing game.
3. Quit""")
        n = input("Enter 1 or 2 or 3:  ")
        try:
            n = int(n)
            if(n <= 3):
                if(n == 1):
                    memory(pnt)
                elif(n == 2):
                    print("Wow, You scored {0} points!! Congrats".format(pnt))
                    sleep(1.5)
                    print("Swtiching to Number Guessing game.. Stay tuned :)")
                    onegame()
                else:
                    print("Wow, You scored {0} points!! Congrats".format(pnt))
                    sleep(1.5)
                    print("Thankyou for testing me, See you later Bye:)")
            else:
                print("Enter an integer <= 3 :(")
        except:
                print(":( Waiting for correct reply.. Sad!!")
    else:
        print("OOPS!! correct word is {0}, but you entered {1}".format(NEW[ran-1], ran1))
        sleep(1.5)
        print("""Do you want to try again or stop here?
1. Yes, Try again.
2. No, Switch to Number Guessing game.
3. Quit""")
        n = input("Enter 1 or 2 or 3: ")
        try:
            n = int(n)
            if(n <= 3):
                if(n == 1):
                    game(pt)
                elif(n == 2):
                    print("Wow, You scored {0} points!! Congrats".format(pnt))
                    sleep(1.5)
                    print("Hope, You liked it! Switching to Number Guessing game.. Stay tuned :)")
                    sleep(2)
                    onegame()
                else:
                    print("Wow, You scored {0} points!! Congrats".format(pnt))
                    sleep(1.5)
                    print("Thankyou for testing me!  See you later, Bye :)")
            else:
                print("Enter an integer <= 3  :(")
        except:
            print("Ok, I'm tired.. Good night")

# Calling Number guessing

def game(pt=0):
    print()
    q = randint(1,30)
   # print(q)
    sleep(1.5)
    t = input("Enter your guess: ")
    try:
        # if entered input is an integer
        t = int(t)
        if(t <= 30):  # for ineteger less than 30
            if(t == q):
                pt = pt + 1
                sleep(1.5)
                print("Wow!! You just scored a point.. You are lucky!!")
                sleep(1.5)
                print("""Do you want to try again or stop here?
1. Yes, Continue my progress.
2. No, Swtich to Memory game
3. Quit""")
                n = input("Enter 1 or 2 or 3: ")
                try:
                    n = int(n)
                    if(n <= 3):
                        if(n == 1):
                            game(pt)
                        elif(n == 2):
                            if(pt == 0):
                                print("Oops!! You scored 0 points, Better luck next time.. :(")
                                sleep(1.5)
                                print("Swtiching to another game.. Stay tuned!")
                                twogame()
                            else:
                                print("Wow, You scored {0} points!! Congrats".format(pt))
                                sleep(1.5)
                                print("Swtiching to another game.. Stay tuned!")
                                twogame()
                        else:
                            print("Wow, You scored {0} points!! Congrats".format(pt))
                            sleep(1.5)
                            print("Thankyou for testing me!  See you later, Bye :)")
                    else:
                        print("Enter an integer <= 3  :(")
                except:
                        print(":( Waiting for correct reply.. Sad!!")
            else:
                pt = pt
                print("OOPS!! My number is {0} and your guess is {1}".format(q,t))
                sleep(1.5)
                print("Better luck next time")
                sleep(1.5)
                print("""Do you want to try again or stop here?
1. Yes, Try again.
2. No, Swtich to Memory game
3. Quit""")
                n = input("Enter 1 or 2 or 3: ")
                try:
                    n = int(n)
                    if(n <=3 ):
                        if(n == 1):
                            game(pt)
                        elif(n == 2):
                            # if points are zero, if case will execute
                            if(pt == 0):
                                print("Oops!! You scored 0 points, Better luck next time.. :(")
                                sleep(1.5)
                                print("Swtiching to another game.. Stay tuned!")
                                twogame()
                            else:
                                print("Wow, You scored {0} points!! Congrats".format(pt))
                                sleep(1.5)
                                print("Swtiching to another game.. Stay tuned!")
                                twogame() 
                        else:
                            # Quitting from program
                            print("Wow, You scored {0} points!! Congrats".format(pt))
                            sleep(1.5)
                            print("Thankyou for testing me!  See you later, Bye :)")
                    else:
                        print("Enter an integer less than 3")
                except:
                    print(":( Waiting for correct reply.. Sad!!")
    except:
        # if entered input is not an integer
        print("Enter a number b/w 1 to 30")

# Execution starts from here

print("-----------------------WELCOME-----------------------")
print()
# Intro
sleep(1)
print("I'm a .py Robot :) Born on 29th July 19:07 IST")
sleep(1.3)
print()
print("""How are you??
1. Fine
2. Not fine""")

k = input("Enter 1 or 2: ")
try:
    k = int(k)
    if(k <= 2):
        if(k == 2):
            sad()
        else:
            print("Woah! Super")
            sleep(1.5)
            dec()
    else:
        sleep(1.5)
        print("Please enter correct choice :(")
except:
    print("Oh no!! Run the program again and enter integer :( ")
