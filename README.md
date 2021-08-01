![](https://github.com/clauskovacs/chaiss/workflows/unit-test%20(boardcontrol)/badge.svg)

# chaiss
A chess engine with various different agents to play with or against, including a terminal renderer.

## Requirements
Python3 as well as a computer with **at least** two cores is necessary to run this program.

## Folder Structure

This project has the following folder structure
```
.
├── logs
├── src
└── test
```

1. The folder **logs** contains all logfiles regarding games (moves, boardstates, agent informations, etc.).

2. In the folder **src** all python files are stored. These are:
    - *agents.py* (contains the all the different computer player logic controls)
    - *boardcontrol.py* (setting up the board and pieces move management)
    - *chaiss.py* (the main program)
    - *stdoutwrapper.py* (a wrapper for curses used to put text to the terminal post running)
    - *windowhandler.yp* (curses Windowhandler for terminal rendering)

3. The last folder **test** contains all the unit tests regarding this program.

## Additional Information

To be able to provide the user with a level of interactivity, curses is used to render the boardstate as well as all additional information to the screen. Using this, any key on the keyboard may be used additionally. To separate the game logic and the code which renders the screen, two threads are used. In one thread runs the game logic (responsible for playing the game) and the other thread is used to draw the board as well as registering keyboard inputs by the user. Data transfer between these two threads is realised using *Queue* objects.

## Dependencies
Python3 as well as the following modules are required: `Queue, collections, curses, multiprocessing, numpy, os, random, sys, threading, time`.

## Executing the Program
Use the provided makefile or the terminal via `python3 src/chaiss.py` to run the program.

