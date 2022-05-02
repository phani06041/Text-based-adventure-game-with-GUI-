# count variable for each fruit
count1=0
count2=0
count3=0
count4=0
count5=0
count6=0
count7=0
# count variable so that NPC's only interact with the player a limited/specific number of times
check1=0
check2=0
check3=0
check4=0
check5=0
check6=0
# time control variable
t1=0
t2=0

# import turtle and time packages
import turtle
import time

# create screen object 
sc = turtle.Screen()
turtle.Screen().bgcolor("Black") 
   
# create turtle object 
pen = turtle.Turtle()
pen2= turtle.Turtle()
aesth1=turtle.Turtle()
aesth1.hideturtle()
aesth1.up()
aesth2=turtle.Turtle()
aesth2.hideturtle()
aesth2.up()
aesth3=turtle.Turtle()
aesth3.hideturtle()
aesth3.up()
aesth4=turtle.Turtle()
aesth4.hideturtle()
aesth4.up()
apple1=turtle.Turtle()
apple1.hideturtle()
apple1.up()
apple2=turtle.Turtle()
apple2.hideturtle()
apple2.up()
apple3=turtle.Turtle()
apple3.hideturtle()
apple3.up()
apple4=turtle.Turtle()
apple4.hideturtle()
apple4.up()
apple5=turtle.Turtle()
apple5.hideturtle()
apple5.up()
apple6=turtle.Turtle()
apple6.hideturtle()
apple6.up()
apple7=turtle.Turtle()
apple7.hideturtle()
apple7.up()
aesth1.shape("square"), aesth2.shape("square"), aesth3.shape("square"), aesth4.shape("square")
aesth1.color("Lime"), aesth2.color("Lime"), aesth3.color("Lime"), aesth4.color("Lime")
aesth1.shapesize(0.7), aesth2.shapesize(0.7), aesth3.shapesize(0.7), aesth4.shapesize(0.7) 
apple1.shape("circle"), apple2.shape("circle"), apple3.shape("circle"), apple4.shape("circle"), apple5.shape("circle"), apple6.shape("circle"), apple7.shape("circle")
apple1.color("Violet"), apple2.color("Violet"), apple3.color("Violet"), apple4.color("Violet"), apple5.color("Violet"), apple6.color("Violet"), apple7.color("Violet")
pen2.up()
pen2.hideturtle()
pen2.setpos(-85,-255)

# set position of the turtle
pen.up()
pen.setpos(-100,-100)

# method to draw square 
def draw(): 
   
  for i in range(4): 
    pen.forward(30) 
    pen.left(90) 
   
  pen.forward(30) 
   
if __name__ == "__main__" :

    print()
    print("<<RULES AND CONTROLS>>\nDo not press any keys while the Totems (NPC's) are speaking.")
    print("Do not press any keys while the maps are being set up.")
    print("Do not attempt to leave the main map or mini-game map.")
    print("Press 'SPACE-BAR' to quit the game at any point of time.")
    print("Use 'W' to move forward, 'A' to turn left and 'D' to turn right.")
    print("Do not spam press the keyboard bindings.\n")
    print("<<Please wait a few moments while the main map is loading>>")
  
    # set turtle object speed 
    pen.speed(0)
       
    # loops for board 
    for i in range(8): 
       
      # not ready to draw 
      pen.up() 
       
      # set position for every row 
      pen.setpos(-100, 30 * i) 
       
      # ready to draw 
      pen.down() 
       
      # row 
      for j in range(8):

        col="Cyan"
             
        # fill with given color 
        pen.fillcolor(col) 
       
        # start filling with colour 
        pen.begin_fill() 
       
        # call method 
        draw()
        
        # stop filling 
        pen.end_fill()

    # not ready to draw
    pen.up()

    # 1st outline for main-map
    pen.color("Lime")
    pen.setpos(-105,-5)
    pen.down()
    for i in range(0,4):
      pen.forward(250)
      pen.left(90)
    pen.up()

    # 2nd outline for main-map
    pen.setpos(-115,-15)
    pen.down()
    for i in range(0,4):
      pen.forward(270)
      pen.left(90)
    pen.up()

    aesth1.setpos(-115,-15)
    aesth2.setpos(155,-15)
    aesth3.setpos(155,255)
    aesth4.setpos(-115,255)
    aesth1.showturtle(), aesth2.showturtle(), aesth3.showturtle(), aesth4.showturtle()

    # move the turtle to initial game position
    pen.setpos(125,15)

    # turn the turtle to face the correct direction
    pen.left(90)

    # setting the colour of the turtle
    pen.color("Grey")

    # functions for player movements
    def stopit():
      turtle.bye()

    def turnleft():
      pen.left(90)

    def turnright():
      pen.right(90)

    def forward():
      turtle.delay(10)
      pen.forward(30)
      # check if the player is in any NPC's vicinity
      if pen.xcor()>-100 and pen.xcor()<-70 and pen.ycor()>60 and pen.ycor()<90:
        npc1doesstuff()
      elif pen.xcor()>-70 and pen.xcor()<-40 and pen.ycor()>180 and pen.ycor()<210:
        npc2doesstuff()
      elif pen.xcor()>-40 and pen.xcor()<-10 and pen.ycor()>60 and pen.ycor()<90:
        npc3doesstuff()
      elif pen.xcor()>50 and pen.xcor()<80 and pen.ycor()>30 and pen.ycor()<60:
        npc4doesstuff()
      elif pen.xcor()>20 and pen.xcor()<50 and pen.ycor()>120 and pen.ycor()<150:
        npc5doesstuff()
      elif pen.xcor()>70 and pen.xcor()<100 and pen.ycor()>150 and pen.ycor()<180:
        npc6doesstuff()

    def turnleft2():
      pen2.left(90)

    def turnright2():
      pen2.right(90)

    def forward2(): 
      global t1, t2, check1
      turtle.delay(10)
      pen2.forward(30)
      
      if pen2.xcor()>-56 and pen2.xcor()<-54 and pen2.ycor()>-256 and pen2.ycor()<-254:
        global count1, count2, count3, count4, count5, count6, count7
        count1+=1
        apple1.hideturtle()
        t2=time.time()
      elif pen2.xcor()>-26 and pen2.xcor()<-24 and pen2.ycor()>-106 and pen2.ycor()<-104:
        count2+=1
        apple2.hideturtle()
        t2=time.time()
      elif pen2.xcor()>124 and pen2.xcor()<126 and pen2.ycor()>-136 and pen2.ycor()<-134:
        count3+=1
        apple3.hideturtle()
        t2=time.time()
      elif pen2.xcor()>64 and pen2.xcor()<66 and pen2.ycor()>-76 and pen2.ycor()<-74:
        count4+=1
        apple4.hideturtle()
        t2=time.time()
      elif pen2.xcor()>-86 and pen2.xcor()<-84 and pen2.ycor()>-46 and pen2.ycor()<-44:
        count5+=1
        apple5.hideturtle()
        t2=time.time()
      elif pen2.xcor()>4 and pen2.xcor()<6 and pen2.ycor()>-166 and pen2.ycor()<-164:
        count6+=1
        apple6.hideturtle()
        t2=time.time()
      elif pen2.xcor()>94 and pen2.xcor()<96 and pen2.ycor()>-226 and pen2.ycor()<-224:
        count7+=1
        apple7.hideturtle()
        t2=time.time()
      if (count1>0 and count2>0 and count3>0 and count4>0 and count5>0 and count6>0 and count7>0 and (t2-t1)<=20) and check1==1:
        print()
        print()
        print("<<CYANDOM FOLD>> You win!")
        pen2.color("Black")
        pen2.up()
        pen2.speed(0)
        turtle.delay(0)
        pen2.setpos(-100,-270)
        # return the minimap turtle to its original direction
        pen2.setheading(90)
        pen2.right(90)
        # remove minigame 1 map's visibility 
        for i in range(8):  
          pen2.up()  
          pen2.setpos(-100, (-270 + 30*i)) 
          pen2.down() 
          for j in range(8):
            col="Black" 
            pen2.fillcolor(col)  
            pen2.begin_fill() 
            for i in range(4):
              pen2.forward(30)
              pen2.left(90)
            pen2.forward(30) 
            pen2.end_fill()
        pen2.up()
        pen2.setpos(-85,-255)
        pen2.color("Black")
        npc2.showturtle(), npc3.showturtle(), npc4.showturtle(), npc5.showturtle(), npc6.showturtle()
        # return functionality to main-map NPC's after mini-game 1 is over
        check1=2
      
      if (count1>0 and count2>0 and count3>0 and count4>0 and count5>0 and count6>0 and count7>0 and (t2-t1)>20) and check1==1:
        print()
        print()
        print("<<CYANDOM FOLD>> You collected all the fruits. Unfortunately, not in time...")
        pen2.color("Black")
        pen2.up()
        pen2.speed(0)
        turtle.delay(0)
        pen2.setpos(-100,-270)
        # return the minimap turtle to its original direction
        pen2.setheading(90)
        pen2.right(90)
        # remove minigame 1 map's visibility 
        for i in range(8):  
          pen2.up()  
          pen2.setpos(-100, (-270 + 30*i)) 
          pen2.down() 
          for j in range(8):
            col="Black" 
            pen2.fillcolor(col)  
            pen2.begin_fill() 
            for i in range(4):
              pen2.forward(30)
              pen2.left(90)
            pen2.forward(30) 
            pen2.end_fill()
        pen2.up()
        pen2.setpos(-85,-255)
        pen2.color("Black")
        npc2.showturtle(), npc3.showturtle(), npc4.showturtle(), npc5.showturtle(), npc6.showturtle()
        # return functionality to main-map NPC's after mini-game 1 is over
        check1=2

    # set keyboard bindings
    turtle.listen()
    # restrict NPC 1 to interact during setting up of minigame map
    if check1!=1:
      turtle.onkey(turnleft,"a")
    if check1!=1:
      turtle.onkey(turnright,"d")
    if check1!=1:
      turtle.onkey(forward,"w")
    turtle.onkey(stopit,"space")
    turtle.onkey(turnleft2,"j")
    turtle.onkey(turnright2,"l")
    turtle.onkey(forward2,"i")

    # create NPC's
    npc1= turtle.Turtle()
    npc2= turtle.Turtle()
    npc3= turtle.Turtle()
    npc4= turtle.Turtle()
    npc5= turtle.Turtle()
    npc6= turtle.Turtle()

    # provide attributes to the NPC's
    npc1.up(), npc2.up(), npc3.up(), npc4.up(), npc5.up(), npc6.up()

    npc1.shape("turtle"), npc2.shape("turtle"), npc3.shape("turtle"), npc4.shape("turtle"), npc5.shape("turtle"), npc6.shape("turtle")
    
    npc1.shapesize(0.7,0.6,0.5), npc2.shapesize(0.7,0.6,0.5), npc3.shapesize(0.7,0.6,0.5), npc4.shapesize(0.7,0.6,0.5), npc5.shapesize(0.7,0.6,0.5), npc6.shapesize(0.7,0.6,0.5)

    npc1.color("Yellow"), npc2.color("Pink"), npc3.color("Red"), npc4.color("Purple"), npc5.color("Green"), npc6.color("Blue")
    
    npc1.speed(1), npc2.speed(1), npc3.speed(1), npc4.speed(1), npc5.speed(1), npc6.speed(1)

    npc2.setpos(-45,195), npc4.setpos(70,35), npc5.setpos(45,130), npc1.setpos(-90,80), npc6.setpos(105,165), npc3.setpos(-30,65)

    # interact with NPC's 
    def npc1doesstuff():
      global check1
      global t1
      # work only the first time NPC1 is called
      if check1==0:
        print()
        print()
        print("<<AMBERIS>> Welcome, I am Amberis.\nI have been awaiting a worthy challenger for aeons!\nYou must collect all ethereal fruits before time runs out in order to win.\nYour challenge lies ahead!")
        print("Use 'I' to move forward, 'J' to turn left and 'L' to turn right.")
        check1=1
        npc1.hideturtle(), npc2.hideturtle(), npc3.hideturtle(), npc4.hideturtle(), npc5.hideturtle(), npc6.hideturtle()
        pen2.showturtle()
        pen2.color("Magenta")
        pen2.up()
        pen2.speed(0)
        # set up minigame 1 map 
        for i in range(8):  
          pen2.up()  
          pen2.setpos(-100, (-270 + 30*i)) 
          pen2.down() 
          for j in range(8):
            col="Yellow" 
            pen2.fillcolor(col)  
            pen2.begin_fill() 
            for i in range(4):
              pen2.forward(30)
              pen2.left(90)
            pen2.forward(30) 
            pen2.end_fill()
        pen2.up()
        pen2.setpos(-85,-255)
        pen2.color("Magenta")
        apple1.setpos(-55,-255), apple2.setpos(-25,-105), apple3.setpos(125,-135), apple4.setpos(65,-75), apple5.setpos(-85,-45), apple6.setpos(5,-165), apple7.setpos(95,-225)
        apple1.shapesize(0.7,0.6,0.5), apple2.shapesize(0.7,0.6,0.5), apple3.shapesize(0.7,0.6,0.5), apple4.shapesize(0.7,0.6,0.5), apple5.shapesize(0.7,0.6,0.5), apple6.shapesize(0.7,0.6,0.5), apple7.shapesize(0.7,0.6,0.5) 
        apple1.showturtle(), apple2.showturtle(), apple3.showturtle(), apple4.showturtle(), apple5.showturtle(), apple6.showturtle(), apple7.showturtle()
      t1=time.time()
      
    def npc2doesstuff():
      global check2, check1
      # restrict other NPC's to interact during setup of minigame
      if check2==0 and check1!=1:
        print()
        print()
        print("<<PEACHOITTE>> The armor stood in pieces around the front room in various states of renovation.\nTools littered floor.\n“Legs first,” he grumbled, stepping into the sabatons.\nAlice scrambled to her knees in her nightdress, a poor but necessary replacement for a proper battle squire.\nShe pinched her fingers on the knee clamps, struggled under the weight of the chest pieces.")
        print("The button panel whirred and crackled with static, then burped out: “System. Offline.”\nArnett slammed his right fist onto it...")
        npc2.up()
        time.sleep(20)
        npc2.speed(1)
        npc2.setheading(0)
        npc2.forward(500)
        npc2.hideturtle()
      check2=1

    def npc3doesstuff():
      # try and except so that if any other key other than 1 or 2 is entered, it doesn't stop running the code
      try:
        global check3, check1
        if check3==0 and check1!=1:
          print()
          print()
          print("<<CRIMSONYX>> Let's see if you paid enough attention to the details. I am going to ask you a few questions to test you!")
          print("Type 1 for Option 1 and 2 for Option 2.")
          print()
          q1=int(input("What connects Peachoitte, Emeraldyte, Amberis, Skyzel, Lilace and I?\n(1) Greek Mythical Creatures\n(2) Colour Derivatives\n"))
          if q1==2:
            print("<<CRIMSONYX>> Correct! All our names have been derived from colours.")
          else:
            print("<<CRIMSONYX>> Incorrect!")
          q2=int(input("What is the size of the Cyandom Fold?\n(1) 8x8\n(2) 9x9\n"))
          if q2==1:
            print("<<CRIMSONYX>> Correct! Looks like someone has been counting the squares.")
          else:
            print("<<CRIMSONYX>> Incorrect!")
          q3=int(input("How many keyboard keys are being used in this game?\n(1)9\n(2)10\n"))
          if q3==1:
            print("<<CRIMSONYX>> Correct! You remembered to count the keys 1 and 2. Good thinking!")
          else:
            print("<<CRIMSONYX>> Incorrect!")
          npc3.speed(1)
          npc3.setheading(180)
          npc3.forward(500)
          npc3.hideturtle()
        check3=1
      except Exception:
        print()
        print()
        print("<<CYANDOM FOLD>> Please enter either (1) or (2).\nThe quiz has ended for now.\nPlease try again later.")

    # remain on the main map even after interacting once
    def npc4doesstuff():
      global check4, check1
      if check4==0:
        print()
        print()
        print("<<LILACE>> (Grumbles) Leave me alone...")
        npc4.up()
        time.sleep(3)
        npc4.speed(1)
        turtle.delay(50)
        npc4.right(60)
        check4+=1
      elif check4==1:
        print()
        print()
        print("<<LILACE>> (Grumbles) It's been a tough year for everyone...\nIncluding myself...")
        npc4.up()
        time.sleep(3)
        npc4.speed(1)
        turtle.delay(50)
        npc4.right(60)
        check4+=1
      elif check4==2:
        print()
        print()
        print("<<LILACE>> (Yells) Haven't you irritated me enough?!")
        npc4.up()
        time.sleep(3)
        npc4.speed(1)
        npc4.setheading(90)
        npc4.forward(300)
        npc4.hideturtle()
        check4+=1
        
    # remain on the main map even after interacting once
    def npc5doesstuff():
      global check5, check1
      if check5==0:
        print()
        print()
        print("<<EMERALDYTE>> Don't pay attention to what Peachoitte says!\nShe says things no one seems to understand.")
        check5+=1
      elif check5==1:
        print()
        print()
        print("<<EMERALDYTE>> Lilace doesn't like speaking much so it'd be best if you left him alone!")
        check5+=1
      elif check5==2:
        print()
        print()
        print("<<EMERALDYTE>> I've enjoyed interacting with you! See you around!")
        time.sleep(3)
        npc5.setheading(180)
        npc5.up()
        npc5.speed(1)
        npc5.forward(500)
        npc5.hideturtle()
        check5+=1

    # remain on the main map even after interacting once
    def npc6doesstuff():
      global check6, check1
      if check6==0 and check1!=1:
        print()
        print()
        print("<<SKYZEL>> Since you've approached me, I will impart my knowledge about the Cyandom Fold's history...")
        print("The Cyandom Fold was created by Arnett, in hopes of salvaging the memories of his wife Alice.\nHe figured this was the best way to keep her spirit alive.")
        print("The map derives it's name from it's colour- Cyan.\nThe six of us (The Totems) reside on this map.\nWe guide and challenge the adventurers who dare enter.")
        print("The six of us live on specific parts of the Cyandom Fold.\nThese areas of the map are unstable and require our constant repair.")
        print("Once an adventurer like yourself succeeds with his/her quest, the six of us can depart and let the Cyandom Fold reach it's inevitable destiny...")
        check6+=1
        time.sleep(30)
        npc6.setheading(-90)
        npc6.up()
        npc6.speed(1)
        npc6.forward(500)
        npc6.hideturtle()

    # driver code
    # try and except so that when space bar is pressed, it doesn't throw an infinite loop error, instead displays thank you message
    try:
      while True:

        # python window does not respond otherwise
        pen.forward(0)
 
        # keep the player within the map
        if pen.xcor()>140 or pen.xcor()<-100:
          pen.right(180)
          pen.forward(30)
          print()
          print()
          print("\n<<CYANDOM FOLD>> Bonk! Go back inside the main map.")
          # double check if player is within the map incase they spam press forward key
          if pen.xcor()>130 or pen.xcor()<-90:
            pen.setpos(125,15)
            print()
            print()
            print("\n<<CYANDOM FOLD>> You have been returned to the initial position for repeatedly trying to leave the main map.")

        elif pen.ycor()>240 or pen.ycor()<0:
          pen.right(180)
          pen.forward(30)
          print()
          print()
          print("\n<<CYANDOM FOLD>> Bonk! Go back inside the main map.")
          if pen.ycor()<-40 or pen.ycor()>280:
            pen.setpos(125,15)
            print()
            print()
            print("<<\nCYANDOM FOLD>> You have been returned to the initial position for repeatedly trying to leave the main map.")
            
        # keep the player within the minigame map
        if (pen2.xcor()>140 or pen2.xcor()<-100) and check1==1:
          pen2.right(180)
          pen2.forward(30)
          print()
          print()
          print("\n<<AMBERIS>> You mustn't disrupt the quest! Finish what you started.")
          # double check if player is within the mini-game map incase they spam press forward key
          if pen2.xcor()>130 or pen2.xcor()<-90:
            pen2.setpos(-85,-255)
            print()
            print()
            print("\n<<AMBERIS>> You have been returned to the initial position for trying to escape the mini-game map.")
        
        elif (pen2.ycor()>-30 or pen2.ycor()<-270) and check1==1:
          pen2.right(180)
          pen2.forward(30)
          print()
          print()
          print("\n<<AMBERIS>> You mustn't disrupt the quest! Finish what you started.")
          if pen2.ycor()>-40 or pen2.ycor()<-280:
            pen2.setpos(-85,-255)
            print()
            print()
            print("\n<<AMBERIS>> You have been returned to the initial position for trying to escape the mini-game map.")

    except Exception:
      print()
      print()
      print("<<Thank you for playing our game!>>\n<<Please be on the lookout for new levels in the future updates>>\n(｡◕‿◕｡)")
      print()
