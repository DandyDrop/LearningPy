# day 1 - 5
import time
import random

error_message = "I don`t understand u, try again please"

def generator():
    while True:
        print("\n\nWelcome to the generator of the crap ;)")
        shape_of_dick = input("Enter the shape of ur dick > \n")
        length_of_dick = input("Enter the length of ur dick > \n")
        time.sleep(1.5)
        print("generating the dick...")
        time.sleep(2)
        print("Ur dick has a(n) " + shape_of_dick + " shape and a length of ur dick is " + length_of_dick + " meters")
        print("So u have a " + length_of_dick + " " + shape_of_dick + " dick")

def calc():
    while True:
        print("\n\nWelcome to the Bill calculator")
        bill = float(input("What was the total bill? > "))
        percentage = float(input("What percentage tip would u like to dive? > "))
        print(f"Ur percentage is: {percentage}%")
        result_percentage = (bill / 100) * percentage
        amount_of_people = int(input("How many people to split the bill? > "))
        final_bill = (bill + result_percentage) / amount_of_people
        print(f"Each person should pay: ${round(final_bill)}")

def calc2():
    while True:
        print("\n\nWelcome to the Bill calculator")
        bill = float(input("What was the total bill? > "))
        percentage = float(input("What percentage tip would u like to dive?\n 10, 12 or 15? > "))
        if percentage == 10:
            result_percentage = (bill / 100) * 10
        elif percentage == 12:
            result_percentage = (bill / 100) * 12
        elif percentage == 15:
            result_percentage = (bill / 100) * 10
        else:
            print("I don`t understand u, try again please")

        amount_of_people = int(input("How many people to split the bill? > "))
        final_bill = (bill + result_percentage) / amount_of_people
        print(f"Each person should pay: ${round(final_bill)}")

def isEven(number):
    if number % 2 == 0:
        return True
    elif number > 0:
        return False

def BMIcalc():
    while True:
        height = float(input("Enter ur height in m > "))
        weight = float(input("Enter ur weight in kg> "))
        BMI = round(weight / (height**2), 2)
        if BMI <= 18.5:
            print(f"Ur BMI equals {BMI} and u are underweighted")
        elif 18 < BMI <= 25:
            print(f"Ur BMI equals {BMI} and u have a normal weight")
        elif 25 < BMI <= 30:
            print(f"Ur BMI equals {BMI} and u are overweighted")
        elif 30 < BMI <= 35:
            print(f"Ur BMI equals {BMI} and u are obese")
        else:
            print(f"Ur BMI equals {BMI} and u are clinically obese")

def leapYear():
    while True:
        year = int(input("Enter the year > "))
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    print("LEA-A-A-A-A-AP!")
                else:
                    print("NO LEA-A-A-A-A-AP! ;(")
            else:
                print("LEA-A-A-A-A-AP!")
        else:
            print("This is not a leap year")

def pizzaOrder():

    while True:
        print("\n\nWelcome to Deep Pizza Deliveries ;) ")
        size = input("What size pizza do u want? S, M or L? > ")
        if size == "S":
            price = 15
        elif size == "M":
            price = 20
        elif size == "L":
            price = 25
        else:
            print(error_message)
            pizzaOrder()

        add_pepperoni = input("Do u want pepperoni? Y or N? > ")
        if add_pepperoni == "Y" and size == "S":
            price += 2
        elif add_pepperoni == "Y" and size == "M" or "L":
            price += 3
        else:
            if add_pepperoni != "N":
                print(error_message)
                pizzaOrder()

        extra_cheese = input("Do u want an extra cheese? Y or N? > ")
        if extra_cheese == "Y":
            price += 1
        else:
            if extra_cheese != "N":
                print(error_message)
                pizzaOrder()

        print(f"Ur final price is: ${price}")

def loveCalc():
    while True:
        print("\n\nWelcome to the Love Calc")
        name1 = input("What is ur name? > ")
        name2 = input("What is there name? > ")
        names = name1 + name2
        names.lower()
        counter1 = 0
        counter2 = 0
        # чекает, сколько раз буквы слов "true" и "love" появляются в именах наших партнеров
        for i in "t", "r", "u", "e":
            counter1 += names.count(i)
        for i in "l", "o", "v", "e":
            counter2 += names.count(i)
        counter = int(str(counter1) + str(counter2))
        percent = round((counter / len(names) * 100), 2)
        if 0 <= percent <= 100:
            print(f"The score is {percent}%, so u do not want to suck!")
        elif 100 < percent <= 500:
            print(f"Ur score is {percent}%, so u love each other ;) ")
        else:
            print(f"Ur score is {percent}%! SO U ARE CRAZY!")

def loveCalcPro(name1, name2):
    print("\n\nWelcome to the Love Calc")
    names = name1 + name2
    names.lower()
    # чекает, сколько раз буквы слов "true" и "love" появляются в именах наших партнеров

    t = names.count("t")
    r = names.count("r")
    u = names.count("u")
    e = names.count("e")
    true = t + r + u + e

    l = names.count("l")
    o = names.count("o")
    v = names.count("v")
    love = l + o + v + e

    counter = int(str(true) + str(love))
    percent = round((counter / len(names) * 100), 2)

    if 0 <= percent <= 100:
        print(f"The score is {percent}%, so u do not want to suck!")
    elif 100 < counter <= 500:
        print(f"Ur score is {percent}%, so u love each other ;) ")
    else:
        print(f"Ur score is {percent}%! SO U ARE CRAZY!")

def treasureIsland():
    while True:
        print("\n\nWelcome to the Treasure Island. Ur mission is to find the treasure ;)")
        where = input("There is the lake on the left side and the forest on the right side. L or R? > ")
        if where == "R":
            print("There was a strange frankenstein dinosaur in this forest... U are done ;(")
        else:
            what_to_do = input("Do u want to swim or wait for the boat? S or W? > ")
            if what_to_do == "S":
                print("There was an enormous dragon living in the lake`s bottom ... U are done ;(")
            else:
                final_choise = input("Now u have a dick in anus. What to do?\n 1 - try to take it out. 2 - stick "
                                     "another dick in anus to enlarge it. 3 - wait and cum if dick lets u")
                if final_choise == 1:
                    print("No, the dick was too big and u collapsed. GAME OVER, MAGGOT!")
                elif final_choise == 2:
                    print("ATA CMO ZONA, GAME FUCKING OVER!")
                else:
                    print("U have penetrated urself so nice. The dick gave u the treasure and u took "
                          "everything with urself leaving this strange island. U won!")

def coinToss():
    while True:
        print("\n\nWelcome to the coin Toss")
        random.seed(int(input("Enter the seed number > ")))
        num1 = int(input("1-st num > "))
        num2 = int(input("2-d num > "))
        if num1 % 2 == 0:
            num11 = num1 / 2
        else:
            num11 = (num1 - 1) / 2
        if num2 % 2 == 0:
            num21 = num2 / 2
        else:
            num21 = (num2 - 1) / 2
        first_random = round((random.random() * num1 / 70) * (random.randint(int(num21), num2)))
        second_random = round((random.random() * num2 / 70) * (random.randint(int(num11), num1)))
        if first_random < second_random:
            final_random = round(random.randint(first_random, second_random) * (random.random() ** 3), 5)
        elif first_random > second_random:
            final_random = round(random.randint(second_random, first_random) * (random.random() ** 3), 5)
        else:
            print("Try another seed number please")
            coinToss()
        print(final_random)
        if final_random % 5 > 2 or final_random % 2 >= 0:
            print("Tails!")
        else:
            print("Heads!")

def whosACapitalistSlave():
    while True:
        random.seed(float(input("Give me the dick > ")))
        names = input("Give me everybody`s names, separated by a comma > ").split(", ")
        print(f"Today {names[random.randint(0, len(names) - 1)]} is paying! The fucking capitalist!")
        # or we can use the "choice" function that will pick a random object of a list or something else
        print(f"Today {random.choice(names)} is paying! The fucking capitalist!")

whosACapitalistSlave()
