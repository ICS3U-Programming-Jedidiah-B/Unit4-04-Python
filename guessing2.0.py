# !/usr/bin/env python3
# Created by: Jedidiah
# Created on: April 26 2022

import random
random.Random


def main():

    # this function uses a try statement
    try:

        loop_counter = 0

        while loop_counter != -1:
            loop_counter = loop_counter + 1
            number = random.randint(0, 5)
            guess = int(input("Guess a number from 0 to 9! "))
            print(" {} time through loop".format(loop_counter))
            if guess != number:
                print(
                    "You guessed incorrectly, {} was correct!".format(number))

            if guess == number:
                print("You guessed correctly")
                break
    except ValueError:
        print("")
        print("that is not an number")
    else:
        print("")
    finally:
        if loop_counter == 1:
            print("perfection")
        print("")
        print("done")


if __name__ == "__main__":
    main()
