
import random

from color import *
from colorama import Fore
class TodaysWin():

    def todaywin(self):
        print("\33[1m\33[35mToday's powerball winning Numbers\33[0m:")
        win_number = []
        for i in range(1, 20):
            win_number.append(i)
        get_index = random.sample(win_number, k=5)  # the sample uses not repeat the numbers and the K is chosen numbers
        get_index.sort()
        powerball = random.randint(1, 10)
        get_index.append(powerball)
        print(Fore.BLUE, *get_index)  # to print out today's winning_numbers by different colors.
        return get_index


class LuckyNom(TodaysWin):

    def luckyfun(self):
        print("\33[1m\33[35m your lucky Number\33[0m")
        lucky_number = []
        for lucy in range(1, 20):
            lucky_number.append(lucy)
        lucky_index = random.sample(lucky_number, k=5)
        lucky_index.sort()
        powerbol = random.randint(1, 10)
        lucky_index.append(powerbol)
        print(Fore.BLUE, *lucky_index)  # to print out today's lucky_numbers by different colors.
        return lucky_index


class Resualt():

    def childfun(self):
        countd = 0    # to count down powerball
        win = TodaysWin().todaywin()  # to call the  first class
        lucky = LuckyNom().luckyfun() # to call the  second class
        for i in win:
            if i in lucky:
                countd = countd + 1
        print("the amount of pbol", countd)
        print("***************************************************************************")
        if win[5] == lucky[5] and countd == 5:
            print("jack point $324,000,000")
        elif win[5] != lucky[5] and countd == 5:
            print("jack point $1,000,000")
        elif win[5] == lucky[5] and countd == 4:
            print("jack point $10,000")
        elif win[5] != lucky[5] and countd == 4:
            print("jack point $100")
        elif win[5] == lucky[5] and countd == 3:
            print("jack point $100")
        elif win[5] != lucky[5] and countd == 3:
            print("jack point $7")
        elif win[5] == lucky[5] and countd == 2:
            print("jack point $7")
        elif win[5] != lucky[5] and countd == 2:
            print("\33[1m\33[31mTry Again! ")
        elif win[5] == lucky[5] and countd == 1:
            print("jack point $4")
        elif win[5] != lucky[5] and countd == 1:
            print("\33[1m\33[31mTry again! ")
        elif win[5] == lucky[5] and countd == 0:
            print("jack point $4")
        elif win[5] != lucky[5] and countd == 0:
            print("\33[1m\33[31mTry again!")