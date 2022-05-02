# Text-based-adventure-game-with-GUI-
DESCRIPTION:

The title we have chosen is the Text-Based Adventure Game with a GUI. The game allows the user to freely move around an 8x8 map by using fixed control buttons (a, w, d, i, j, etc.) for moving, turning, collecting items and other features. There are fixed boundaries around the maps which do not allow the player to trespass. There are many Non-Playable-Characters (NPC’s) residing on the map who interact with the user by providing a lore about the map and characters in general. We have also developed a few mini-games in addition to exploring the main map, which can be played by the user for a more engaging experience
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
DESCRIPTION OF GUI COMPONENTS: 

We have used the Turtle module to design the main map and minigame maps, colour the visuals, NPC’s, items and various other things. The entire project revolves around the GUI component. The Turtle module also controls the movement of the player and NPC’s, drawing of the maps, collection and movement of the in-game items, etc
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
BASIC INPUT AND OUTPUT DATA: 

Most inputs are in the form of pressing of the assigned keyboard keys for movement and other functions. These keys immediately cause interaction with the game and invoke the required commands. They do not need to be typed in a designated area of the screen and can be pressed at will. Some inputs, however, are required to be typed into the IDLE Screen for a few mini-games. The outputs are immediately noticeable in the form of the changing map, position of the player, setting up of NPC’s and mini-games, etc on the Turtle Window. Warnings, character dialogues and other texts are displayed in the Python Shell. Since the project almost entirely revolves around a GUI, the outputs would be more visual-based than text-based
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
CORE PROGRAM AND FUNCTIONS: 

The core program includes various user-defined functions which allow the user to move around using keyboard bindings (turtle.onkey()). An infinite loop restricts the user from travelling beyond the maps. During the minigames, the main map interactions are restricted by the use of counter variables and nested loops. Various “turtles'' are also created and hidden (turtle.turtle(), turtle.hideturtle()) during the course of the game. The Time module is also imported to keep track of how long the user took to finish the mini-games and hence decide if they won or lost. Functions like turtle.fillcolor(), turtle.end_fill(), turtle.setpos(), turtle.up(), etc. have been used to make the game visually appealing.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
