# Module 07: Communication — Input/Output, Files, and Networks

## Learning Objectives

1. Use **print**, **input**, **file I/O**, and **APIs** to let your program communicate with the outside world.
2. Understand that communication in code means **transferring information across a boundary** — the program's Markov blanket.
3. Build a simple program that sends and receives messages.

## Introduction

A program that does not communicate is useless. It needs to talk to users (print, input), to files (read, write), to the Internet (API requests), and to other programs (sockets, protocols). Communication is how your code agent shares its model of the world with other agents. This module teaches the mechanics of digital communication.

## Key Concepts

### 1. Standard I/O: Talking to Humans

```python
name = input("What is your name? ")  # Perception (reading from human)
print(f"Hello, {name}!")              # Action (writing to human)
```

`input()` is the program's **ear** — it perceives information from the user. `print()` is the program's **mouth** — it communicates information back. Together, they form the program's communication boundary.

### 2. File I/O: Long-Term Communication

Writing to a file is like leaving a note for the future:

```python
# Write (send a message to the future)
with open("high_scores.txt", "w") as f:
    f.write(f"{player_name},{score}\n")

# Read (receive a message from the past)
with open("high_scores.txt", "r") as f:
    scores = f.readlines()
```

Files are a form of **asynchronous communication** — the sender and receiver do not need to be active at the same time.

### 3. APIs: Talking to Other Programs

An **API** (Application Programming Interface) lets your program talk to another program over the Internet:

```python
import requests
response = requests.get("https://api.weather.gov/points/39.7,-104.9")
weather = response.json()
print(f"Forecast: {weather['properties']['forecast']}")
```

Your program sends a request (an action), the server processes it, and sends back a response (new sensory data). The API is the Markov blanket: it defines *exactly* what information can cross the boundary.

## Activities

### 💬 Activity 1: Chatbot

Build a simple chatbot that:

1. Asks the user their name
2. Asks what they want to know about (weather, jokes, math)
3. Responds based on their choice
4. Saves the conversation to a file

### 🌐 Activity 2: API Explorer

Using a free public API (like the Pokémon API: <https://pokeapi.co/>), write a program that asks the user for a Pokémon name and displays its type, abilities, and stats. The API is the boundary between your program and the Pokémon database!

## Summary

Communication in code happens through I/O (talking to humans), files (talking across time), and APIs (talking to other programs). Each communication channel is a boundary that defines what information passes in and out — the code version of a Markov blanket.

## References

* Sweigart, A. (2015). *Automate the Boring Stuff with Python*. Chapters 9, 12.
