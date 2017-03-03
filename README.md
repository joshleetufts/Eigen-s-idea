# Kupper's illustration of Eigen's idea from Professor Dennett's book, Darwin's Dangerous Idea

## Program Description

This program simulates natural selection and was motivated by a selection from Professor Dennett's book, Darwin's Dangerous Idea page 160~161. Simply put, it has one reproducing and placing its color to another cell randomly until all colors are the same. Below is the passage that describes the theoretical significance of this simulation.


*Kuppers borrows an example from Eigen (1976) to illustrate the underlying idea: a game of "non-Darwinian selection" you can play on a checkerboard with differently colored marbles. Start by randomly placing the marbles on all the squares, creating the initial confetti effect. Now, throw two (eight-sided!) dice to determine a square (column 5, row 7, for instance) on which to act. Remove the marble on that square. Throw the dice again: go to the square they name and check the color of the marble on this square and put a marble of that color on the just-vacated square ("reproduction" of that marble). Repeat the process, over and over. Eventually, it has the effect of unrandomizing the initial distribution of colors, so that one color ends up "winning" but for no reason at all—just historical luck. He calls this "non-Darwinian selection" because it is selection in the absence of a biasing cause; selection without adaptation would be the more familiar term. It is non-Darwinian only in the sense that Darwin didn't see the importance of allowing for it, not in the sense that Darwin ( or Darwinism ) cannot accommodate it. Manifestly it can.*

**Note**: The count seems to lag at times (numbers overlapping), but that is because I draw the checkerboard only if the cells in the two cells are not of the same color. Then the program does not redraw the whole board, but only redraws the count. Because this highly reduced the processing cost (graphically drawing the board each time is quite expensive, slowing down our program), the count actually gets faster, making the previous count look as if it is overlapping with the next count. 

## Program Requirements

You must download pygames to get the visualization to work. Here is the link to the guidelines on how to install pygame according to the OS that you have:

[Pygames install guide](webprojects.eecs.qmul.ac.uk/fa303/pgs/install.html)

## Credits

I would like to thank Tom Frikker for showing me how to use Pygame to visualize my data and Professor Dennett for giving us this idea to create a simulation of Eigen's idea.
