import time
from random import *

def begin(name):
    print("Hello, " + name + ". I'm ChatBot.")

def color(pick):
    if pick == "blue" or "pink":
        print("Nice! That's my favorite color too!")
    else:
        print("Nice! My favorite color is blue!")

def joke(choice):
    if choice == "yes":
        print("How was Rome split in two?")
        time.sleep(2)
        print("With a pair Ceasars! Haha!")
    elif choice == "no":
        print("Ok...")

def rps(user_choice, computer_choice):

    if computer_choice == 1:
    	computer_word = "rock"
    elif computer_choice == 2:
    	computer_word = "paper"
    elif computer_choice == 3:
        computer_word = "scissors"

    if user_choice == "rock" and computer_word == "paper":
        print("computer wins")
    elif user_choice == "rock" and computer_word == "rock":
        print("tie")
    elif user_choice == "rock" and computer_word == "scissors":
        print("user wins")

    if user_choice == "paper" and computer_word == "paper":
        print("tie")
    elif user_choice == "paper" and computer_word == "rock":
        print("user wins")
    elif user_choice == "paper" and computer_word == "scissors":
        print("computer wins")

    if user_choice == "scissors" and computer_word == "paper":
        print("user wins")
    elif user_choice == "scissors" and computer_word == "rock":
        print("computer wins")
    elif user_choice == "scissors" and computer_word == "scissors":
        print("tie")

def main():
    name = input("What is your name?")
    begin(name)

    time.sleep(1)

    pick = input("What is your favorite color?")
    color(pick)

    time.sleep(1)

    choice = input("Would you like to hear a joke?")
    joke(choice)

    time.sleep(1)

    user_choice = input("Let's play a game! Rock, paper, or scissors?")
    computer_choice = randint(1, 3)
    computer_word = ""
    rps(user_choice, computer_choice)

if __name__ == "__main__":
    chatbot = input("Would you like to speak to ChatBot 1 or 2?")
    if chatbot == "1" or "2":
        main()
        exit()
    else:
        exit()
