## Instructions for running the code

Download the file

Open terminal

CD to the directory your console_memory file is located

Make sure you are on the right directory by typing 'ls' on the console and finding the file console_memory.py on the listed files

Type on terminal 'python console_memory' and your game starts!

PS: In case you do not have python already installed, type in your terminal 'brew install python'
if this does not work, you can also download it through their website https://www.python.org/

## Rules

This is a memory game between 2 players
Each player pass the coordinate of the 2 cards they want to reveal in their turn,
the row and column starts with 0 and go until the number of row or column you choose - 1.
So if your table has size of 4 rows and 5 columns, the last card will have coordinate of
3rd row and 4th column.
If it is a match that player makes a point
Whether you find or not matching cards the next turn will always be your opponent.
By the end of each play the cards will stay revealed for 2.5 seconds if it is not a match
Only after that the next player plays
By the end of the game, the one with more points win the match

## Design choices and data structures algorithms

I made a lot of functions so the main function(Game()) becomes easy to understand
(you can try to understand each function individually)and also make the code well factored.
I made 2 data structures to hold the cards (game and mask), mask is the function that
users see on their screen while game only serves for back-end procedures.
Each card choice makes mask receive that value from game and show it to the user,
in case the 2 cards do not match, mask receives again the 'xx' value, when they match
mask stays exactly how it is. So it is basically procedures of checking stored values.
Other variables were such as points for each player only increase if the code identify
a match and the total points of the match decreases 1 by each match so we know exactly
when the match ended and can stop the match based on that. We also made a code that
will react appropriately to any non-number inputs and will ask you for the right thing
and point your error (for example if in the row number you choose a row outside the range of the
  table it will say that to you, or if you inputed a character where was supposed to be a
  number the code will not broke and will also tell that to you), so this makes the
game not broke for any mistyping/mistakes it will just keeping ask you again for your input.  
I accounted for edge cases such as negative numbers, outside the range positive numbers,
cards that were already revealed and any non-numeric inputs (will keep asking you to input
  a number).

## Tools

I used python because I know I was able to do it in python although I have not been practicing
much python compared to R and Ruby on rails recently, so I decided to do this challenge in
python to make sure I keep practicing python.
Libraries used: random, system, and sleep
Random is used to generate random cards every match and to randomly assign the
pairs to their coordinates.
System is used to clean the console screen so the user can not see past plays.
Sleep is used in order to let the cards show up for 2.5 seconds after they are
revealed in case they do not match, after the sleeping time the function that
will cover again the cards is called.

## Additional observations

Check my github: https://github.com/luccab
Social network website(front+back): https://afternoon-bastion-92445.herokuapp.com/
My website where I intend to post articles doing statistical analysis and problems related to
ruby on rails development: https://nameless-meadow-85656.herokuapp.com/
