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

def treasureMap():
    while True:
        print("\n\n  a    b     c")
        row1 = ["N", "N", "N"]               # a1 - map[0][0]
        row2 = ["N", "N", "N"]               # c2 - map[1][2]
        row3 = ["N", "N", "N"]
        map = [row1, row2, row3]
        print(f"{row1}\n{row2}\n{row3}\n")
        choice1 = input("Gamer1, choose the tile that u want to place the X on. E.g. - a2 or b1 or c3.\nIf u want to place "
                       "multiple - type it separated by a comma >\n")
        print(choice1[1])

        place(map, choice1, "X")

        print(f"\n\n{row1}\n{row2}\n{row3}\n")

        choice2 = input("Gamer2, choose the tile that u want to place the 0 on. E.g. - a2 or b1 or c3.\nIf u want to place "
                        "multiple - type it separated by a comma >\n")

        place(map, choice2, "0")

        print(f"\n\n{row1}\n{row2}\n{row3}\n")
        time.sleep(10)

def place(map, choice, symbol):
    choice_final = choice.split(", ")
    for i in range(len(choice_final)):
        if choice_final[i].count("a") != 0:
            peek_column = 0
        elif choice_final[i].count("b") != 0:
            peek_column = 1
        elif choice_final[i].count("c") != 0:
            peek_column = 2
        else:
            print(error_message)
            treasureMap()

        if choice_final[i].count("1") != 0:
            peek_row = 0
        elif choice_final[i].count("2") != 0:
            peek_row = 1
        elif choice_final[i].count("3") != 0:
            peek_row = 2
        else:
            print(error_message)
            treasureMap()

        map[peek_row][peek_column] = symbol

def RPS():
    while True:
        print("\n\nWELCOME TO THE RPS GAME! STAAAAAAAAAAAAARTING!")
        pc_choice = random.randint(0, 2)
        user_choice = int(input("Choose 0 for rock, 1 for paper and 2 for scissors "))

        rock = """
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """

        paper = """
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """

        scissors = """
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """

        all_choices = [rock, paper, scissors]

        if (user_choice != 0) and (user_choice != 1) and (user_choice != 2):
            print(error_message)
            RPS()

        if pc_choice == user_choice:
            print(f"U chose > \n{all_choices[user_choice]}")
            print(f"Computer chose:\n{all_choices[pc_choice]}\n\nDraw")
        elif pc_choice == 0 and user_choice == 1 or (pc_choice == 1 and user_choice == 2) or (
                pc_choice == 2 and user_choice == 0):
            print(f"U chose > \n{all_choices[user_choice]}")
            print(f"Computer chose:\n{all_choices[pc_choice]}\n\nU won")
        else:
            print(f"U chose > \n{all_choices[user_choice]}")
            print(f"Computer chose:\n{all_choices[pc_choice]}\n\nU lost")

        # or


        if user_choice == 0:
            print(f"U chose > \n{rock}")
            if pc_choice == 0:
                print(f"Computer chose:\n{rock}\n\nDRAW, ROCK WITH ROCK GOT TO THE STOCK ;( ")
            elif pc_choice == 1:
                print(f"Computer chose:\n{paper}\n\nU LOSE ;( Paper worked as a craper")
            else:
                print(f"Computer chose:\n{scissors}\n\nU WON! YEEEEEEEEEEEEEEEEEEEE")

        elif user_choice == 1:
            print(f"U chose > \n{paper}")
            if pc_choice == 0:
                print(f"Computer chose:\n{rock}\n\nU WON! YEEEEEEEEEEEEEEEEEEEE")
            elif pc_choice == 1:
                print(f"Computer chose:\n{paper}\n\nTHERE IS THE DRAW! THERE IS THE PAPER GETTING TO THE ANAL!")
            else:
                print(f"Computer chose:\n{scissors}\n\nU LOSE ;( Scissors look good as a winners")

        elif user_choice == 2:
            print(f"U chose > \n{scissors}")
            if pc_choice == 0:
                print(f"Computer chose:\n{rock}\n\nU LOSE ;(")
            elif pc_choice == 1:
                print(f"Computer chose:\n{paper}\n\nU won")
            else:
                print(f"Computer chose:\n{scissors}\n\nDraw")
        else:
            print(error_message)
            RPS()

def RPSMASHA():
    while True:
        print("\n\nWELCOME TO THE RPS GAME! STAAAAAAAAAAAAARTING!")
        user_choice = int(input("Choose 0 for rock, 1 for paper and 2 for scissors "))
        if user_choice == 0:
            pc_choise = 1
        elif user_choice == 1:
            pc_choise = 2
        elif user_choice == 2:
            pc_choise = 0
        else:
            print(error_message)
            RPS()




        rock = """
                    _______
                ---'   ____)
                      (_____)
                      (_____)
                      (____)
                ---.__(___)
                """

        paper = """
                     _______
                ---'    ____)____
                           ______)
                          _______)
                         _______)
                ---.__________)
                """

        scissors = """
                    _______
                ---'   ____)____
                          ______)
                       __________)
                      (____)
                ---.__(___)
                """

        all_choices = [rock, paper, scissors]

        print(f"U chose > \n{all_choices[user_choice]}\n, but computer chose: \n{all_choices[pc_choise]}\n\nSo u lose. "
              f"But don`t worry, then u will win in a bedroom fight!")


def averageHeight():
    while True:
        all_heights = []
        length = int(input("Welcome to the average height calculator! Enter the length "
                           "of random list of heights (>0) > "))
        for i in range(length):
            all_heights.append(random.randint(150, 200))

        # the rule was that I can`t use the sum() or len() functions
        sum_height = 0
        len_counter = 0

        print(all_heights)

        for i in all_heights:
            sum_height += i
            len_counter += 1

        average_height = sum_height / len_counter
        print(f"The average height ~ {round(average_height)}")

        # the solution with sum() and len()
        average_height = sum(all_heights) / len(all_heights)
        print(f"The average height ~ {round(average_height)}")
        # or even
        print(f"The average height ~ {round(sum(all_heights) / len(all_heights))}")

def maxScore():
    while True:
        all_scores = []
        length = int(input("Welcome to the average max score searcher! Enter the length "
                           "of random list of heights (>0) > "))
        for i in range(length):
            all_scores.append(random.randint(1, 100))

        max = 0

        for score in all_scores:
            if max < score:
                max = score

        print(all_scores)
        print(f"The max score is - {max}")

# recursion method:
def maxScore1(Array):
    print(ezer(Array, 0, 0))
def ezer(Array, max, index):
    if index == len(Array):
        return max
    if Array[index] > max:
        max = Array[index]
    return ezer(Array, max, index + 1)


def sumEv(min, max):
    sum = 0
    for num in range(min, max+1):
        if num % 2 == 0:
           sum += num
    return sum

    # or if we know that min is odd (e.g. 1 - 100):

    # for num in range (2, 101, 2):
    #     sum += num
    #
    # return 1 + sum

# Fizz Buzz game 1 - 100
def fizzBuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 5 == 0:
            print("Buzz")
        elif num % 3 == 0:
            print("Fizz")
        else:
            print(num)

def passGenerator():
    while True:
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                   's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                   'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "~", "`"]
        final_pass = []
        final_print = ""
        print("\n\nWelcome to the pass generator!")
        nr_letters = int(input("How many letters would u like in ur pass? (Type - 1 if u want to see completely random "
                               "pass) > "))
        if nr_letters == -1:
            final_char = letters + numbers + symbols + numbers
            for char in range(random.randint(5, 25)):
                final_pass.append(str(final_char[random.randint(0, len(final_char) - 1)]))
        else:

            nr_symbols = int(input("How mane symbols would u like in ur pass? > "))
            nr_nums = int(input("How mane nums would u like in ur pass? > "))


            # with choice() and shuffle()
            for i in range(nr_letters):
                final_pass.append(random.choice(letters))
            for i in range(nr_symbols):
                final_pass.append(random.choice(symbols))
            for i in range(nr_nums):
                final_pass.append(str(random.choice(numbers)))

            random.shuffle(final_pass)


            # with choice()
            # for i in range(nr_letters):
            #     final_pass.insert(random.randint(0, len(final_pass) - 1), random.choice(letters))
            # for i in range(nr_symbols):
            #     final_pass.insert(random.randint(0, len(final_pass) - 1), random.choice(symbols))
            # for i in range(nr_nums):
            #     final_pass.insert(random.randint(0, len(final_pass) - 1), random.choice(numbers))

            # without choice() and shuffle()
            # for i in range(nr_letters):
            #     final_pass.append(letters[random.randint(0, len(letters) - 1)])
            # for i in range(nr_symbols):
            #     final_pass.insert(random.randint(0, len(final_pass) - 1), symbols[random.randint(0, len(symbols) - 1)])
            # for i in range(nr_nums):
            #     final_pass.insert(random.randint(0, len(final_pass) - 1), str(numbers[random.randint(0, len(numbers) - 1)]))

        for char in final_pass:
            final_print += char
        print(final_print)

def reorderList():
    mylist = ["a", "b", "c", "d"]
    order = [3, 2, 0, 1]
    mylist1 = [mylist[index] for index in order]
    print(mylist)
    print(mylist1)
