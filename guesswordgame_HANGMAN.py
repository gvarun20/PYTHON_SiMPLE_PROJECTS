# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 14:53:15 2024

@author: varung
"""

import random

def choose_word():
    return random.choice(["tiger", "superman", "thor", "doraemon", "avenger", "water", "stream", "boy", "girl"])

def display_word(word, guessed_letters):
    return ' '.join(letter if letter in guessed_letters else '_' for letter in word)

def hangman():
    word = choose_word()
    valid_letters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessed_letters = set()

    print("Welcome to Hangman!")
    name = input("Enter your name: ")
    print(f"Welcome, {name}!")
    print("=====================")

    while turns > 0:
        guess = input(f"Guess the word: {display_word(word, guessed_letters)}\n").casefold()

        if guess in valid_letters:
            guessed_letters.add(guess)
        else:
            print("Enter a valid character")
            continue

        if guess not in word:
            turns -= 1

        print(f"{turns} turns left")
        draw_hangman(turns)

        if set(word) <= guessed_letters:
            print(f"Congratulations, {name}! You win!")
            break

    else:
        print("You lose")
        print(f"Sorry, {name}. The word was '{word}'.")

def draw_hangman(turns):
    hangman_parts = [
        ["  ---------  "],
        ["      O      "],
        ["   \  |  /   "],
        ["    \ | /    "],
        ["      |      "],
        ["     / \     "],
        ["-------------"]
    ]

    for part in hangman_parts[:10 - turns]:
        print(part[0])

hangman()
