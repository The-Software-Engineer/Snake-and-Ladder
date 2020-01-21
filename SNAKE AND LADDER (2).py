                                                                      # snake and ladder
import random
import turtle as s
import time
import winsound

print('--------------------------------------------------------------------------------')
winsound.PlaySound('hauntedhouse', winsound.SND_ASYNC)
time.sleep(2)
print('\n                                      Welome_To                                  ')
time.sleep(2)
print('\n                             The world of SNAKES AND LADDERS                     ')
print('\n--------------------------------------------------------------------------------')
time.sleep(2)
print('\n       THERE ARE TWO PLAYER')
time.sleep(2)
print('\n       PLAYER_1-VIOLET')
time.sleep(2)
print('\n       PLAYER_2-ORANGE')
time.sleep(2)
print('\n       THERE ARE TWO STATES ')
time.sleep(2)
print('\n       SNAKE    -   LADDER ')
time.sleep(2)
print('\n       I WILL DISPLAY YOUR POSITION AND YOUR STATE')
time.sleep(2)
print('\n       IF YOU ARE READY TO PLAY PRESS ENTER')
#input()
# setting up of the screen
s.title('snake and ladder')
s.Screen()
s.bgcolor('white')
#s.color('white')
s.penup()
s.setposition(-300, -300)  # this is the pos of the cursor
s.pendown()
# s.pensize(width=5)
s.shape('classic')
s.pencolor('white')
#s.fillcolor('white')
s.speed(0)
# drwaing the box (600) border
for sa in range(4):
    s.forward(600)
    s.left(90)
    s.pensize(width=3)
    s.pencolor('black')
# function for drawing the lines in the box
def move():
    s.color('white', 'black')
    s.begin_fill()
    s.forward(600)
    s.left(90)
    s.forward(60)
    s.left(90)
    s.forward(600)
    s.right(90)
    s.right(90)
    s.end_fill()


# output of the box
for i in range(10):
    move()


# function for drawing the lines in the box
def move1():
    s.forward(60)
    s.right(90)
    s.forward(600)
    s.left(90)
    s.forward(60)
    s.left(90)
    s.forward(600)
    s.right(90)


# output for the box
for i in range(5):
    move1()


# back to the same positon of the cursor
def back_to_pos():
    s.penup()
    s.setx(-300)
    s.sety(-270)
    s.hideturtle()


# output of the def cursor
back_to_pos()


# the compelete movement condition even beyond the border of the dices
def movement():
    border = 0
    count = 0
    for i in range(final_answer):
        s.forward(60)
        count += 1
        print(count)
        if count == 10:
            border += 1
            count = 0

            if (border % 2 == 0):
                s.right(90)
                s.forward(60)
                s.right(90)
            else:
                s.left(90)
                s.forward(60)
                s.left(90)


def joy_ladder():  # this displays the color whn you climb the ladder
    l = ['violet', 'indigo', 'blue', 'green', 'red', 'orange', 'violet', 'yellow', 'brown', 'red', 'orange', 'blue']
    winsound.PlaySound('wickedmalelaugh1', winsound.SND_ASYNC)
    for i in range(12):
        s.bgcolor(l[i])
        time.sleep(0.2)
        s.bgcolor('white')
        s.color(l[i])
        time.sleep(0.1)
        s.shape('turtle')
        s.speed(0.2)
        s.right(90)
        # s.bgcolor('white')
    print('I AM COMING FOR YOU! (:-|)')


def sadness_snake():  # this displays the color whn you are hitten by an snake
    color = ['red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red']
    winsound.PlaySound('wickedwitchlaugh', winsound.SND_ASYNC)
    for i in range(12):
        s.fillcolor('black')
        s.bgcolor(color[i])
        time.sleep(0.2)
        s.bgcolor('white')
        s.color(color[i])
        time.sleep(0.1)
        s.shape('turtle')
        s.speed(0.2)
        s.right(90)
    print('I AM HERE NOW! (:-))')


# the creation of the dices
dices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
dices_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# the ans shows the number in the dice
# creation of an new variable answer which contains the sum od the answer
# setup of the player one pen
winsound.PlaySound('Drone', winsound.SND_ASYNC)
player_1 = s.Pen()
player_1.color('violet')
player_1.fillcolor('white')
player_1.penup()
player_1.setx(-300)
player_1.sety(-270)
# setup of the player two pen
player_2 = s.Pen()
player_2.color('orange')
player_2.fillcolor('white')
player_2.penup()
player_2.setx(-300)
player_2.sety(-270)
#------------------------------------------------
#for ladder from 4 to 14
ladder_111=s.Pen()#4
ladder_111.speed(9)
ladder_111.shape('square')
ladder_111.shapesize(3,3,1)
ladder_111.color('white')
ladder_111.fillcolor('indigo')
ladder_111.penup()
ladder_111.setx(-300)
ladder_111.sety(-270)
for i in range(7):
    ladder_111.forward(30)
ladder_112=s.Pen()#14
ladder_112.speed(9)
ladder_112.shape('square')
ladder_112.shapesize(3,3,1)
ladder_112.color('white')
ladder_112.fillcolor('indigo')
ladder_112.penup()
ladder_112.setx(-300)
ladder_112.sety(-270)
for i in range(20):
    ladder_112.forward(30)
ladder_112.left(90)
ladder_112.forward(60)
ladder_112.left(90)
for i in range(7):
    ladder_112.forward(30)
#-----------------------------------------------------
#ladder from 9 to 31
ladder_1=s.Pen()#9
ladder_1.speed(7)
ladder_1.shape('square')
ladder_1.shapesize(3,3,1)
ladder_1.color('white')
ladder_1.fillcolor('green')
ladder_1.penup()
ladder_1.setx(-300)
ladder_1.sety(-270)
for i in range(17):
    ladder_1.forward(30)
ladder_2=s.Pen()#31
ladder_2.speed(7)
ladder_2.shape('square')
ladder_2.shapesize(3,3,1)
ladder_2.color('white')
ladder_2.fillcolor('green')
ladder_2.penup()
ladder_2.setx(-300)
ladder_2.sety(-270)
for i in range(19):
    ladder_2.forward(30)
ladder_2.left(90)
ladder_2.forward(60+60+60)
ladder_2.left(90)
#----------------------------------------------------------
#ladder from 19 to 38
ladder_3=s.Pen()#19
ladder_3.speed(7)
ladder_3.shape('square')
ladder_3.shapesize(3,3,1)
ladder_3.color('white')
ladder_3.fillcolor('blue')
ladder_3.penup()
ladder_3.setx(-300)
ladder_3.sety(-270)
for i in range(19):
    ladder_3.forward(30)
ladder_3.left(90)
ladder_3.forward(60)
ladder_3.left(90)
for i in range(16):
    ladder_3.forward(30)
ladder_4=s.Pen()#38
ladder_4.speed(7)
ladder_4.shape('square')
ladder_4.shapesize(3,3,1)
ladder_4.color('white')
ladder_4.fillcolor('blue')
ladder_4.penup()
ladder_4.setx(-300)
ladder_4.sety(-270)
for i in range(19):
    ladder_4.forward(30)
ladder_4.left(90)
ladder_4.forward(60+60+60)
ladder_4.left(90)
for i in range(14):
    ladder_4.forward(30)
#-------------------------------------------------------------
#ladder from 28 to 84
ladder_5=s.Pen()#28
ladder_5.speed(7)
ladder_5.shape('square')
ladder_5.shapesize(3,3,1)
ladder_5.color('white')
ladder_5.fillcolor('yellow')
ladder_5.penup()
ladder_5.setx(-300)
ladder_5.sety(-270)
for i in range(19):
    ladder_5.forward(30)
ladder_5.left(90)
ladder_5.forward(60+60)
ladder_5.left(90)
for i in range(4):
    ladder_5.forward(30)
ladder_6=s.Pen()#84
ladder_6.speed(7)
ladder_6.shape('square')
ladder_6.shapesize(3,3,1)
ladder_6.color('white')
ladder_6.fillcolor('yellow')
ladder_6.penup()
ladder_6.setx(-300)
ladder_6.sety(-270)
for i in range(19):
    ladder_6.forward(30)
ladder_6.left(90)
ladder_6.forward(60+60+60+60+60+60+60+60)
ladder_6.left(90)
for i in range(12):
    ladder_6.forward(30)
#--------------------------------------------------------------------
#ladder from 39 to 59
ladder_7=s.Pen()#39
ladder_7.speed(7)
ladder_7.shape('square')
ladder_7.shapesize(3,3,1)
ladder_7.color('white')
ladder_7.fillcolor('brown')
ladder_7.penup()
ladder_7.setx(-300)
ladder_7.sety(-270)
for i in range(20):
    ladder_7.forward(30)
ladder_7.left(90)
ladder_7.forward(60+60+60)
ladder_7.left(90)
for i in range(17):
    ladder_7.forward(30)
ladder_8=s.Pen()#59
ladder_8.speed(7)
ladder_8.shape('square')
ladder_8.shapesize(3,3,1)
ladder_8.color('white')
ladder_8.fillcolor('brown')
ladder_8.penup()
ladder_8.setx(-300)
ladder_8.sety(-270)
for i in range(20):
    ladder_8.forward(30)
ladder_8.left(90)
ladder_8.forward(60+60+60+60+60)
ladder_8.left(90)
for i in range(17):
    ladder_8.forward(30)
#----------------------------------------------------------
#ladder from ladder 51 to 67
ladder_9=s.Pen()#51
ladder_9.speed(7)
ladder_9.shape('square')
ladder_9.shapesize(3,3,1)
ladder_9.color('white')
ladder_9.fillcolor('white')
ladder_9.penup()
ladder_9.setx(-300)
ladder_9.sety(-270)
for i in range(19):
    ladder_9.forward(30)
ladder_9.left(90)
ladder_9.forward(60+60+60+60+60)
ladder_9.left(90)

ladder_10=s.Pen()#67
ladder_10.speed(7)
ladder_10.shape('square')
ladder_10.shapesize(3,3,1)
ladder_10.color('white')
ladder_10.fillcolor('white')
ladder_10.penup()
ladder_10.setx(-300)
ladder_10.sety(-270)
for i in range(19):
    ladder_10.forward(30)
ladder_10.left(90)
ladder_10.forward(60+60+60+60+60+60)
ladder_10.left(90)
for i in range(6):
    ladder_10.forward(30)
#------------------------------------------------------------
#ladder from 63 to 81
ladder_10=s.Pen()#63
ladder_10.speed(7)
ladder_10.shape('square')
ladder_10.shapesize(3,3,1)
ladder_10.color('white')
ladder_10.fillcolor('grey')
ladder_10.penup()
ladder_10.setx(-300)
ladder_10.sety(-270)
for i in range(19):
    ladder_10.forward(30)
ladder_10.left(90)
ladder_10.forward(60+60+60+60+60+60)
ladder_10.left(90)
for i in range(14):
    ladder_10.forward(30)

ladder_11=s.Pen()#81
ladder_11.speed(7)
ladder_11.shape('square')
ladder_11.shapesize(3,3,1)
ladder_11.color('white')
ladder_11.fillcolor('grey')
ladder_11.penup()
ladder_11.setx(-300)
ladder_11.sety(-270)
for i in range(19):
    ladder_11.forward(30)
ladder_11.left(90)
ladder_11.forward(60+60+60+60+60+60)
ladder_11.left(90)
for i in range(18):
    ladder_11.forward(30)
ladder_11.right(90)
ladder_11.forward(120)
#---------------------------------------------------------------
#ladder from  71 to 91
ladder_12=s.Pen()#71
ladder_12.speed(7)
ladder_12.shape('square')
ladder_12.shapesize(3,3,1)
ladder_12.color('white')
ladder_12.fillcolor('light blue')
ladder_12.penup()
ladder_12.setx(-300)
ladder_12.sety(-270)
for i in range(19):
    ladder_12.forward(30)
ladder_12.left(90)
ladder_12.forward(60+60+60+60+60+60+60)
ladder_12.left(90)

ladder_13=s.Pen()#91
ladder_13.speed(7)
ladder_13.shape('square')
ladder_13.shapesize(3,3,1)
ladder_13.color('white')
ladder_13.fillcolor('light blue')
ladder_13.penup()
ladder_13.setx(-300)
ladder_13.sety(-270)
for i in range(19):
    ladder_13.forward(30)
ladder_13.left(90)
ladder_13.forward(60+60+60+60+60+60+60+60+60)
ladder_13.left(90)
#--------------------------------------------------------------------------------------
# snake from 17 to 7
snake_1=s.Pen()#17
snake_1.speed(7)
snake_1.shape('square')
snake_1.shapesize(3,3,1)
snake_1.color('white')
snake_1.fillcolor('red')
snake_1.penup()
snake_1.setx(-300)
snake_1.sety(-270)
snake_1.left(90)
snake_1.forward(60)
snake_1.right(90)
for i in range(7):
    snake_1.forward(30)
snake_2=s.Pen()#7
snake_2.speed(7)
snake_2.shape('square')
snake_2.shapesize(3,3,1)
snake_2.color('white')
snake_2.fillcolor('red')
snake_2.penup()
snake_2.setx(-300)
snake_2.sety(-270)
for i in range(13):
    snake_2.forward(30)
#---------------------------------------------------------------------------------------------
#snake from 54-34
snake_3=s.Pen()#54
snake_3.speed(7)
snake_3.shape('square')
snake_3.shapesize(3,3,1)
snake_3.color('white')
snake_3.fillcolor('red')
snake_3.penup()
snake_3.setx(-300)
snake_3.sety(-270)
for i in range(19):
    snake_3.forward(30)
snake_3.left(90)
snake_3.forward(60+60+60+60+60)
snake_3.left(90)
for i in range(6):
    snake_3.forward(30)
snake_4=s.Pen()#34
snake_4.speed(7)
snake_4.shape('square')
snake_4.shapesize(3,3,1)
snake_4.color('white')
snake_4.fillcolor('red')
snake_4.penup()
snake_4.setx(-300)
snake_4.sety(-270)
for i in range(19):
    snake_4.forward(30)
snake_4.left(90)
snake_4.forward(60+60+60)
snake_4.left(90)
for i in range(6):
    snake_4.forward(30)
#-------------------------------------------------------------------------
#snake from 62 to 18
snake_5=s.Pen()#62
snake_5.speed(7)
snake_5.shape('square')
snake_5.shapesize(3,3,1)
snake_5.color('white')
snake_5.fillcolor('red')
snake_5.penup()
snake_5.setx(-300)
snake_5.sety(-270)
for i in range(19):
    snake_5.forward(30)
snake_5.left(90)
snake_5.forward(60+60+60+60+60+60)
snake_5.left(90)
for i in range(16):
    snake_5.forward(30)
snake_6=s.Pen()#18
snake_6.speed(7)
snake_6.shape('square')
snake_6.shapesize(3,3,1)
snake_6.color('white')
snake_6.fillcolor('red')
snake_6.penup()
snake_6.setx(-300)
snake_6.sety(-270)
for i in range(19):
    snake_6.forward(30)
snake_6.left(90)
snake_6.forward(60)
snake_6.left(90)
for i in range(14):
    snake_6.forward(30)
#---------------------------------------------------------------
#snake from 64 to 59
snake_7=s.Pen()#62
snake_7.speed(7)
snake_7.shape('square')
snake_7.shapesize(3,3,1)
snake_7.color('white')
snake_7.fillcolor('red')
snake_7.penup()
snake_7.setx(-300)
snake_7.sety(-270)
for i in range(19):
    snake_7.forward(30)
snake_7.left(90)
snake_7.forward(60+60+60+60+60+60)
snake_7.left(90)
for i in range(12):
    snake_7.forward(30)

#----------------------------------------------------------------
#snake from 94 to 36
snake_8=s.Pen()#94
snake_8.speed(7)
snake_8.shape('square')
snake_8.shapesize(3,3,1)
snake_8.color('white')
snake_8.fillcolor('red')
snake_8.penup()
snake_8.setx(-300)
snake_8.sety(-270)
for i in range(19):
    snake_8.forward(30)
snake_8.left(90)
snake_8.forward(60+60+60+60+60+60+60+60+60)
snake_8.left(90)
for i in range(6):
    snake_8.forward(30)
snake_9=s.Pen()#36
snake_9.speed(7)
snake_9.shape('square')
snake_9.shapesize(3,3,1)
snake_9.color('white')
snake_9.fillcolor('red')
snake_9.penup()
snake_9.setx(-300)
snake_9.sety(-270)
for i in range(19):
    snake_9.forward(30)
snake_9.left(90)
snake_9.forward(60+60+60)
snake_9.left(90)
for i in range(10):
    snake_9.forward(30)
#---------------------------------------------------------------------
#snake from 93 to 73
snake_10=s.Pen()#93
snake_10.speed(7)
snake_10.shape('square')
snake_10.shapesize(3,3,1)
snake_10.color('white')
snake_10.fillcolor('red')
snake_10.penup()
snake_10.setx(-300)
snake_10.sety(-270)
for i in range(19):
    snake_10.forward(30)
snake_10.left(90)
snake_10.forward(60+60+60+60+60+60+60+60+60)
snake_10.left(90)
for i in range(4):
    snake_10.forward(30)
snake_11=s.Pen()#73
snake_11.speed(7)
snake_11.shape('square')
snake_11.shapesize(3,3,1)
snake_11.color('white')
snake_11.fillcolor('red')
snake_11.penup()
snake_11.setx(-300)
snake_11.sety(-270)
for i in range(19):
    snake_11.forward(30)
snake_11.left(90)
snake_11.forward(60+60+60+60+60+60+60)
snake_11.left(90)
for i in range(4):
    snake_11.forward(30)
#----------------------------------------------------------------------
#snake from 96 to 75
snake_12=s.Pen()#96
snake_12.speed(7)
snake_12.shape('square')
snake_12.shapesize(3,3,1)
snake_12.color('white')
snake_12.fillcolor('red')
snake_12.penup()
snake_12.setx(-300)
snake_12.sety(-270)
for i in range(19):
    snake_12.forward(30)
snake_12.left(90)
snake_12.forward(60+60+60+60+60+60+60+60+60)
snake_12.left(90)
for i in range(10):
    snake_12.forward(30)
snake_13=s.Pen()#75
snake_13.speed(7)
snake_13.shape('square')
snake_13.shapesize(3,3,1)
snake_13.color('white')
snake_13.fillcolor('red')
snake_13.penup()
snake_13.setx(-300)
snake_13.sety(-270)
for i in range(19):
    snake_13.forward(30)
snake_13.left(90)
snake_13.forward(60+60+60+60+60+60+60)
snake_13.left(90)
for i in range(8):
    snake_13.forward(30)
#-------------------------------------------------------------------------
#SNAKE FROM 99 to 78
snake_14=s.Pen()#96
snake_14.speed(7)
snake_14.shape('square')
snake_14.shapesize(3,3,1)
snake_14.color('white')
snake_14.fillcolor('red')
snake_14.penup()
snake_14.setx(-300)
snake_14.sety(-270)
for i in range(19):
    snake_14.forward(30)
snake_14.left(90)
snake_14.forward(60+60+60+60+60+60+60+60+60)
snake_14.left(90)
for i in range(16):
    snake_14.forward(30)
snake_15=s.Pen()#75
snake_15.speed(7)
snake_15.shape('square')
snake_15.shapesize(3,3,1)
snake_15.color('white')
snake_15.fillcolor('red')
snake_15.penup()
snake_15.setx(-300)
snake_15.sety(-270)
for i in range(19):
    snake_15.forward(30)
snake_15.left(90)
snake_15.forward(60+60+60+60+60+60+60)
snake_15.left(90)
for i in range(14):
    snake_15.forward(30)
#-------------------------------------------------------------------------------
def final():
    # the creation of the dices

    player_1.speed(3)
    border_1 = 0
    count_1 = 0
    position_of_player_1 = 0
    # the ans shows the number in the dice
    # the creation of the dices
    player_2.speed(3)
    border_2 = 0
    count_2 = 0
    position_of_player_2 = 0
    # the ans shows the number in the dice
    turn = 0
    while position_of_player_1!=100 and position_of_player_2!=100:
        while turn == 0:
            dices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
            if count_1 == 9 and border_1 == 8:
                dices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
            elif count_1 == 0 and border_1 == 9:
                dices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            elif count_1 == 1 and border_1 == 9:
                dices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            elif count_1 == 2 and border_1 == 9:
                dices = [1, 2, 3, 4, 5, 6, 7, 8]
            elif count_1 == 5 and border_1 == 9:
                dices = [1, 2, 3, 4, 5]
            elif count_1 == 7 and border_1 == 9:
                dices = [1, 2, 3]
            elif count_1 == 8 and border_1 == 9:
                dices = [1, 2]

            answer = (random.choice(dices))  # dices is rolled here
            print('☺☻♥♠DICES♣♦•◘☻☺==', answer)  # THE DICES VALUE IS PRINTED
            final_answer = int(s.numinput('dices',
                                          'enter the number that u see in the dices'))  # final_answer is the input give to the board

            for i in range(final_answer):  # this code is the basic code for the movemebt
                player_1.forward(60)
                count_1 += 1
                position_of_player_1 += 1
                print('player_1 now you are in the position', position_of_player_1)
                if count_1 == 10:
                    border_1 += 1
                    count_1 = 0
                    if (border_1 % 2 == 0):
                        player_1.right(90)
                        player_1.forward(60)
                        player_1.right(90)
                    else:
                        player_1.left(90)
                        player_1.forward(60)
                        player_1.left(90)
            # THE CREATION OF THE LADDERS
            if count_1 == 4 and border_1 == 0:  # the creation of an ladder from 4 to 14
                print('☺☻ player_1 you have got an ladder now u will move to 14☺☻')
                position_of_player_1 = 4
                count_1 = 4
                joy_ladder()
                for i in range(10):
                    player_1.fillcolor('white')
                    player_1.pencolor('violet')
                    player_1.shape('classic')
                    player_1.forward(60)
                    count_1 += 1
                    position_of_player_1 += 1
                    print('player_1 now ur in the position:', position_of_player_1)
                    if count_1 == 10:
                        border_1 += 1
                        count_1 = 0
                        turn = 1
                        if (border_1 % 2 == 0):
                            player_1.right(90)
                            player_1.forward(60)
                            player_1.right(90)
                        else:
                            player_1.left(90)
                            player_1.forward(60)
                            player_1.left(90)

            elif count_1 == 9 and border_1 == 0:  # the creation of an ladder from 9 to 31
                count_1 = 9
                border_1 = 0
                position_of_player_1 = 9
                print('☺☻player_1 you have got an ladder now you will move to 31☺☻')
                joy_ladder()
                for i in range(22):
                    player_1.fillcolor('white')
                    player_1.pencolor('violet')
                    player_1.shape('classic')
                    player_1.forward(60)
                    count_1 += 1
                    position_of_player_1 += 1
                    print('player_1 now you are in the position', position_of_player_1)
                    if count_1 == 10:
                        border_1 += 1
                        count_1 = 0
                        turn = 1
                        if (border_1 % 2 == 0):
                            player_1.right(90)
                            player_1.forward(60)
                            player_1.right(90)

                        else:
                            player_1.left(90)
                            player_1.forward(60)
                            player_1.left(90)

            elif count_1 == 9 and border_1 == 1:  # the creation of an ladder from 19 to 38
                count_1 = 9
                border_1 = 1
                print('☺☻player_1 you have got an ladder now you will move to 38☺☻')
                joy_ladder()
                position_of_player_1 = 19
                for i in range(19):
                    player_1.fillcolor('white')
                    player_1.pencolor('violet')
                    player_1.shape('classic')
                    player_1.forward(60)
                    count_1 += 1
                    position_of_player_1 += 1
                    print('player_1 now you are in the position', position_of_player_1)
                    if count_1 == 10:
                        border_1 += 1
                        count_1 = 0
                        turn = 1
                        if (border_1 % 2 == 0):
                            player_1.right(90)
                            player_1.forward(60)
                            player_1.right(90)
                        else:
                            player_1.left(90)
                            player_1.forward(60)
                            player_1.left(90)


            elif count_1 == 8 and border_1 == 2:  # the creation of an ladder from 28 to 84
                count_1 = 8
                border_1 = 2
                joy_ladder()
                print('☺☻player_1 you have got an ladder now you will move to 84☺☻')
                position_of_player_1 = 28
                for i in range(56):
                    player_1.fillcolor('white')
                    player_1.pencolor('violet')
                    player_1.shape('classic')
                    player_1.forward(60)
                    count_1 += 1
                    position_of_player_1 += 1
                    print('player_1 now you are in the position', position_of_player_1)
                    if count_1 == 10:
                        border_1 += 1
                        count_1 = 0
                        turn = 1
                        if (border_1 % 2 == 0):
                            player_1.right(90)
                            player_1.forward(60)
                            player_1.right(90)
                        else:
                            player_1.left(90)
                            player_1.forward(60)
                            player_1.left(90)

            elif count_1 == 9 and border_1 == 3:  # the creation of an ladder from 39 to 59
                count_1 = 9
                border_1 = 3
                print('☺☻player_1 you have got an ladder now you will move to 59☺☻')
                joy_ladder()
                position_of_player_1 = 39
                for i in range(20):
                    player_1.fillcolor('white')
                    player_1.pencolor('violet')
                    player_1.shape('classic')
                    player_1.forward(60)
                    count_1 += 1
                    position_of_player_1 += 1
                    print('player_1 now you are in the position', position_of_player_1)
                    if count_1 == 10:
                        border_1 += 1
                        count_1 = 0
                        turn = 1
                        if (border_1 % 2 == 0):
                            player_1.right(90)
                            player_1.forward(60)
                            player_1.right(90)
                        else:
                            player_1.left(90)
                            player_1.forward(60)
                            player_1.left(90)

            elif count_1 == 1 and border_1 == 5:  # the creation of an ladder from 51 to 67
                count_1 = 1
                border_1 = 5
                joy_ladder()
                position_of_player_1 = 51
                print('☺☻player_1 you have got an ladder now you will move to 67☺☻')
                for i in range(16):
                    player_1.fillcolor('white')
                    player_1.pencolor('violet')
                    player_1.shape('classic')
                    player_1.forward(60)
                    count_1 += 1
                    position_of_player_1 += 1
                    print('player_1 now you are in the position', position_of_player_1)
                    if count_1 == 10:
                        border_1 += 1
                        count_1 = 0
                        turn = 1
                        if (border_1 % 2 == 0):
                            player_1.right(90)
                            player_1.forward(60)
                            player_1.right(90)
                        else:
                            player_1.left(90)
                            player_1.forward(60)
                            player_1.left(90)
            elif count_1 == 3 and border_1 == 6:  # the creation of an ladder from 63 to 81
                count_1 = 3
                border_1 = 6
                print('☺☻player_1 you have got an ladder now you will move to 81☺☻')
                joy_ladder()
                position_of_player_1 = 63
                for i in range(18):
                    player_1.fillcolor('white')
                    player_1.pencolor('violet')
                    player_1.shape('classic')
                    player_1.forward(60)
                    count_1 += 1
                    position_of_player_1 += 1
                    print('player_1 now you are in the position', position_of_player_1)
                    if count_1 == 10:
                        border_1 += 1
                        count_1 = 0
                        turn = 1
                        if (border_1 % 2 == 0):
                            player_1.right(90)
                            player_1.forward(60)
                            player_1.right(90)
                        else:
                            player_1.left(90)
                            player_1.forward(60)
                            player_1.left(90)
            elif count_1 == 1 and border_1 == 7:  # the creation of an ladder from 71 to 91
                count_1 = 1
                border_1 = 7
                print('☺☻player_1 you have got an ladder now you will move to 91☺☻')
                joy_ladder()
                position_of_player_1 = 71
                for i in range(20):
                    player_1.fillcolor('white')
                    player_1.pencolor('violet')
                    player_1.shape('classic')
                    player_1.forward(60)
                    count_1 += 1
                    position_of_player_1 += 1
                    print('player_1 now you are in the position', position_of_player_1)
                    if count_1 == 10:
                        border_1 += 1
                        count_1 = 0
                        turn = 1
                        if (border_1 % 2 == 0):
                            player_1.right(90)
                            player_1.forward(60)
                            player_1.right(90)
                        else:
                            player_1.left(90)
                            player_1.forward(60)
                            player_1.left(90)
            # creation of snake
            elif count_1 == 7 and border_1 == 1:  # this creates an snake from 17 to 7
                print('☺☻player_1 hahaha you are bitten by python now you will go to 7☺☻')
                sadness_snake()
                count_1 = 7
                border_1 = 1
                position_of_player_1 = 17
                for i in range(7):
                    player_1.fillcolor('white')
                    player_1.pencolor('violet')
                    player_1.shape('classic')
                    player_1.backward(60)
                    count_1 -= 1
                    if count_1 == 0:
                        border_1 = 0

                        player_1.right(90)
                        player_1.backward(60)
                        player_1.right(90)
                        for i in range(3):
                            player_1.backward(60)
                            count_1 = 7
                            border_1 = 0
                            position_of_player_1 = 7
                        turn = 1
                        print('player_1 now you are in the position', position_of_player_1)
            elif count_1 == 4 and border_1 == 5:  # this creates an snake from 54 to 34
                print('☺☻player_1 hahaha you are bitten by python now you will go to 34')
                sadness_snake()
                count_1 = 4
                border_1 = 5
                position_of_player_1 = 54
                for i in range(4):
                    player_1.fillcolor('white')
                    player_1.pencolor('violet')
                    player_1.shape('classic')
                    player_1.backward(60)
                    count_1 -= 1

                    if count_1 == 0:
                        border_1 = 4
                        player_1.right(90)
                        player_1.backward(60)
                        player_1.right(90)
                        count_1 = 10
                        for i in range(10):
                            player_1.backward(60)
                            count_1 -= 1
                            if count_1 == 0:
                                player_1.right(90)
                                player_1.forward(60)
                                player_1.right(90)
                                for i in range(6):
                                    player_1.backward(60)
                                    count_1 = 4
                                    border_1 = 3
                                    position_of_player_1 = 34
                                turn = 1
                                print('player_1 now you are in the position', position_of_player_1)
            elif count_1 == 2 and border_1 == 6:  # this creates an snake from 62 to 18
                print('☺☻player_1 hahaha you are bitten by python now you will go to 18☺☻')
                count_1 = 2
                border_1 = 6
                sadness_snake()
                position_of_player_1 = 62
                for i in range(2):
                    player_1.fillcolor('white')
                    player_1.pencolor('violet')
                    player_1.shape('classic')
                    player_1.backward(60)
                    count_1 -= 1
                    if count_1 == 0:
                        border_1 = 5

                        player_1.left(90)
                        player_1.backward(60)
                        player_1.left(90)
                        count_1 = 10
                        for i in range(10):
                            player_1.backward(60)
                            count_1 -= 1
                            if count_1 == 0:
                                border_1 = 4
                                player_1.left(90)
                                player_1.forward(60)
                                player_1.left(90)
                                count_1 = 10
                                for i in range(10):
                                    player_1.backward(60)
                                    count_1 -= 1
                                    if count_1 == 0:
                                        border_1 = 3
                                        player_1.left(90)
                                        player_1.backward(60)
                                        player_1.left(90)
                                        count_1 = 10
                                        for i in range(10):
                                            player_1.backward(60)
                                            count_1 -= 1
                                            if count_1 == 0:
                                                border_1 = 2
                                                player_1.right(90)
                                                player_1.backward(60)
                                                player_1.right(90)
                                                count_1 = 10
                                                for i in range(10):
                                                    player_1.backward(60)
                                                    count_1 -= 1
                                                    if count_1 == 0:
                                                        player_1.left(90)
                                                        player_1.backward(60)
                                                        player_1.left(90)
                                                        for i in range(2):
                                                            player_1.backward(60)
                                                            count_1 = 8
                                                            border_1 = 1
                                                            position_of_player_1 = 18
                                                        turn = 1
                                                        print('player_1 now you are in the position',
                                                              position_of_player_1)
            elif count_1 == 4 and border_1 == 6:  # thia creates an snake from 64 to 59

                print('☺☻player_1 hahaha you are bitten by python now you will go to 59☺☻')
                count_1 = 4
                border_1 = 6
                sadness_snake()
                position_of_player_1 = 64
                for i in range(4):
                    player_1.fillcolor('white')
                    player_1.pencolor('violet')
                    player_1.shape('classic')
                    player_1.backward(60)
                    count_1 -= 1
                    if count_1 == 0:
                        border_1 = 5
                        player_1.left(90)
                        player_1.backward(60)
                        player_1.left(90)
                        for i in range(1):
                            player_1.backward(60)
                            count_1 = 9
                            border_1 = 5
                            position_of_player_1 = 59
                        turn = 1
                        print('player_1 now you are in the position', position_of_player_1)
            elif count_1 == 4 and border_1 == 9:  # this creats an snake from 94 to 36
                print('☺☻player_1 hahaha you are bitten by python now you will go to 36☺☻')
                count_1 = 4
                border_1 = 9
                position_of_player_1 = 94
                sadness_snake()
                for i in range(4):
                    player_1.fillcolor('white')
                    player_1.pencolor('violet')
                    player_1.shape('classic')
                    player_1.backward(60)
                    count_1 -= 1
                    if count_1 == 0:
                        border_1 = 8
                        count_1 = 10
                        player_1.right(90)
                        player_1.backward(60)
                        player_1.right(90)
                        for i in range(10):
                            player_1.backward(60)
                            count_1 -= 1
                            if count_1 == 0:
                                player_1.left(90)
                                player_1.backward(60)
                                player_1.left(90)
                                count_1 = 10
                                for i in range(10):
                                    player_1.backward(60)
                                    count_1 -= 1
                                    if count_1 == 0:
                                        player_1.right(90)
                                        player_1.backward(60)
                                        player_1.right(90)
                                        count_1 = 10
                                        for y in range(10):
                                            player_1.backward(60)
                                            count_1 -= 1
                                            if count_1 == 0:
                                                player_1.left(90)
                                                player_1.backward(60)
                                                player_1.left(90)
                                                count_1 = 10
                                                for w in range(10):
                                                    player_1.backward(60)
                                                    count_1 -= 1
                                                    if count_1 == 0:
                                                        player_1.right(90)
                                                        player_1.backward(60)
                                                        player_1.right(90)
                                                        count_1 = 10
                                                        for o in range(10):
                                                            player_1.bk(60)
                                                            count_1 -= 1
                                                            if count_1 == 0:
                                                                player_1.left(90)
                                                                player_1.backward(60)
                                                                player_1.left(90)
                                                        for t in range(4):
                                                            player_1.backward(60)
                                                            count_1 = 6
                                                            border_1 = 3
                                                            position_of_player_1 = 36
                                                            turn = 1
                                                        print('now you are in the position', position_of_player_1)





            elif count_1 == 3 and border_1 == 9:  # this creates an snake from 93 to 73

                print('☺☻player_1 hahaha you are bitten by python now you will go to 73☺☻')
                count_1 = 3
                border_1 = 9
                position_of_player_1 = 93
                sadness_snake()
                for i in range(3):
                    player_1.fillcolor('white')
                    player_1.pencolor('violet')
                    player_1.shape('classic')
                    player_1.backward(60)
                    count_1 -= 1
                    if count_1 == 0:
                        border_1 = 8
                        player_1.right(90)
                        player_1.backward(60)
                        player_1.right(90)
                        count_1 = 10
                        for i in range(10):
                            player_1.backward(60)
                            count_1 -= 1
                            if count_1 == 0:
                                border_1 = 7
                                player_1.left(90)
                                player_1.backward(60)
                                player_1.left(90)
                                for i in range(7):
                                    player_1.backward(60)
                                    count_1 = 3
                                    border_1 = 7
                                    position_of_player_1 = 73
                                turn = 1
                                print('player_1 now you are in the position', position_of_player_1)
            elif count_1 == 6 and border_1 == 9:  # this creates an snake from 96 to 75

                print('☺☻player_1 hahaha you are bitten by python now you will go to 75☺☻')
                count_1 = 6
                border_1 = 9
                position_of_player_1 = 95
                sadness_snake()
                for i in range(6):
                    player_1.fillcolor('white')
                    player_1.pencolor('violet')
                    player_1.shape('classic')
                    player_1.backward(60)
                    count_1 -= 1
                    if count_1 == 0:
                        border_1 = 8
                        player_1.right(90)
                        player_1.backward(60)
                        player_1.right(90)
                        count_1 = 10
                        for i in range(10):
                            player_1.backward(60)
                            count_1 -= 1
                            if count_1 == 0:
                                border_1 = 7
                                player_1.left(90)
                                player_1.backward(60)
                                player_1.left(90)
                                for i in range(5):
                                    player_1.backward(60)
                                    count_1 = 5
                                    border_1 = 7
                                    position_of_player_1 = 75
                                turn = 1
                                print('player_1 now you are in the position', position_of_player_1)
            elif count_1 == 9 and border_1 == 9:  # this creates an snake from 99 to 78
                print('☺☻player_1 hahaha you are bitten by python now you will go to 78☺☻')
                count_1 = 9
                border_1 = 9
                sadness_snake()
                position_of_player_1 = 99
                for i in range(9):
                    player_1.fillcolor('white')
                    player_1.pencolor('violet')
                    player_1.shape('classic')
                    player_1.backward(60)
                    count_1 -= 1
                    if count_1 == 0:
                        border_1 = 8
                        player_1.right(90)
                        player_1.backward(60)
                        player_1.right(90)
                        count_1 = 10
                        for i in range(10):
                            player_1.backward(60)
                            count_1 -= 1
                            if count_1 == 0:
                                border_1 = 7
                                player_1.left(90)
                                player_1.backward(60)
                                player_1.left(90)
                                for i in range(2):
                                    player_1.backward(60)
                                    count_1 = 8
                                    border_1 = 7
                                    position_of_player_1 = 78
                                turn = 1
                                print('player_1 now you are in the position', position_of_player_1)




            else:
                turn += 1
        else:
            dices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
            if count_2 == 9 and border_2 == 8:
                dices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

            elif count_2 == 0 and border_2 == 9:
                dices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

            elif count_2 == 1 and border_2 == 9:
                dices = [1, 2, 3, 4, 5, 6, 7, 8, 9]

            elif count_2 == 2 and border_2 == 9:
                dices = [1, 2, 3, 4, 5, 6, 7, 8]

            elif count_2 == 5 and border_2 == 9:
                dices = [1, 2, 3, 4, 5]

            elif count_2 == 7 and border_2 == 9:
                dices = [1, 2, 3]

            elif count_2 == 8 and border_2 == 9:
                dices = [1, 2]

            answer = (random.choice(dices))  # dices is rolled here
            print('☺☻♥♠DICES♣♦•◘☻☺==', answer)  # THE DICES VALUE IS PRINTED
            final_answer = int(s.numinput('dices',
                                          'enter the number that u see in the dices'))  # final_answer is the input give to the board
            for i in range(final_answer):  # this code is the basic code for the movemebt
                player_2.forward(60)
                count_2 += 1
                position_of_player_2 += 1
                print('player_2 now you are in the position', position_of_player_2)
                if count_2 == 10:
                    border_2 += 1
                    count_2 = 0
                    if (border_2 % 2 == 0):
                        player_2.right(90)
                        player_2.forward(60)
                        player_2.right(90)
                    else:
                        player_2.left(90)
                        player_2.forward(60)
                        player_2.left(90)
            # THE CREATION OF THE LADDERS
            if count_2 == 4 and border_2 == 0:  # the creation of an ladder from 4 to 14
                print('☺☻player_2 you have got an ladder now u will move to 14☺☻')
                position_of_player_2 = 4
                count_2 = 4
                joy_ladder()
                for i in range(10):
                    player_2.fillcolor('white')
                    player_2.pencolor('orange')
                    player_2.shape('classic')
                    player_2.forward(60)
                    count_2 += 1
                    position_of_player_2 += 1
                    print('player_2 now ur in the position:', position_of_player_2)
                    if count_2 == 10:
                        border_2 += 1
                        count_2 = 0
                        turn = 0
                        if (border_2 % 2 == 0):
                            player_2.right(90)
                            player_2.forward(60)
                            player_2.right(90)
                        else:
                            player_2.left(90)
                            player_2.forward(60)
                            player_2.left(90)

            elif count_2 == 9 and border_2 == 0:  # the creation of an ladder from 9 to 31
                count_2 = 9
                border_2 = 0
                position_of_player_2 = 9
                print('☺☻player_2 you have got an ladder now you will move to 31☺☻')
                joy_ladder()
                for i in range(22):
                    player_2.fillcolor('white')
                    player_2.pencolor('orange')
                    player_2.shape('classic')
                    player_2.forward(60)
                    count_2 += 1
                    position_of_player_2 += 1
                    print('player_2 now you are in the position', position_of_player_2)
                    if count_2 == 10:
                        border_2 += 1
                        count_2 = 0
                        turn = 0
                        if (border_2 % 2 == 0):
                            player_2.right(90)
                            player_2.forward(60)
                            player_2.right(90)
                        else:
                            player_2.left(90)
                            player_2.forward(60)
                            player_2.left(90)

            elif count_2 == 9 and border_2 == 1:  # the creation of an ladder from 19 to 38
                print('☺☻player_2 you have got an ladder now you will move to 38☺☻')
                count_2 = 9
                border_2 = 1
                joy_ladder()
                position_of_player_2 = 19
                for i in range(19):
                    player_2.fillcolor('white')
                    player_2.pencolor('orange')
                    player_2.shape('classic')
                    player_2.forward(60)
                    count_2 += 1
                    position_of_player_2 += 1
                    print('player_2 now you are in the position', position_of_player_2)
                    if count_2 == 10:
                        border_2 += 1
                        count_2 = 0
                        turn = 0
                        if (border_2 % 2 == 0):
                            player_2.right(90)
                            player_2.forward(60)
                            player_2.right(90)
                        else:
                            player_2.left(90)
                            player_2.forward(60)
                            player_2.left(90)


            elif count_2 == 8 and border_2 == 2:  # the creation of an ladder from 28 to 84
                print('☺☻player_2 you have got an ladder now you will move to 84☺☻')
                count_2 = 8
                border_2 = 2
                joy_ladder()
                position_of_player_2 = 28
                for i in range(56):
                    player_2.fillcolor('white')
                    player_2.pencolor('orange')
                    player_2.shape('classic')
                    player_2.forward(60)
                    count_2 += 1
                    position_of_player_2 += 1
                    print('player_2 now you are in the position', position_of_player_2)
                    if count_2 == 10:
                        border_2 += 1
                        count_2 = 0
                        turn = 0
                        if (border_2 % 2 == 0):
                            player_2.right(90)
                            player_2.forward(60)
                            player_2.right(90)
                        else:
                            player_2.left(90)
                            player_2.forward(60)
                            player_2.left(90)

            elif count_2 == 9 and border_2 == 3:  # the creation of an ladder from 39 to 59
                print('☺☻player_2 you have got an ladder now you will move to 59☺☻')
                count_2 = 9
                border_2 = 3
                joy_ladder()
                position_of_player_2 = 39
                for i in range(20):
                    player_2.fillcolor('white')
                    player_2.pencolor('orange')
                    player_2.shape('classic')
                    player_2.forward(60)
                    count_2 += 1
                    position_of_player_2 += 1
                    print('player_2 now you are in the position', position_of_player_2)
                    if count_2 == 10:
                        border_2 += 1
                        count_2 = 0
                        turn = 0
                        if (border_2 % 2 == 0):
                            player_2.right(90)
                            player_2.forward(60)
                            player_2.right(90)
                        else:
                            player_2.left(90)
                            player_2.forward(60)
                            player_2.left(90)

            elif count_2 == 1 and border_2 == 5:  # the creation of an ladder from 51 to 67
                print('☺☻player_2 you have got an ladder now you will move to 67☺☻')
                count_2 = 1
                border_2 = 5
                joy_ladder()
                position_of_player_2 = 51
                for i in range(16):
                    player_2.fillcolor('white')
                    player_2.pencolor('orange')
                    player_2.shape('classic')
                    player_2.forward(60)
                    count_2 += 1
                    position_of_player_2 += 1
                    print('player_2 now you are in the position', position_of_player_2)
                    if count_2 == 10:
                        border_2 += 1
                        count_2 = 0
                        turn = 0
                        if (border_2 % 2 == 0):
                            player_2.right(90)
                            player_2.forward(60)
                            player_2.right(90)
                        else:
                            player_2.left(90)
                            player_2.forward(60)
                            player_2.left(90)
            elif count_2 == 3 and border_2 == 6:  # the creation of an ladder from 63 to 81
                count_2 = 3
                border_2 = 6
                print('☺☻player_2 you have got an ladder now you will move to 81☺☻')
                joy_ladder()
                position_of_player_2 = 63
                for i in range(18):
                    player_2.fillcolor('white')
                    player_2.pencolor('orange')
                    player_2.shape('classic')
                    player_2.forward(60)
                    count_2 += 1
                    position_of_player_2 += 1
                    print('player_2 now you are in the position', position_of_player_2)
                    if count_2 == 10:
                        border_2 += 1
                        count_2 = 0
                        turn = 0
                        if (border_2 % 2 == 0):
                            player_2.right(90)
                            player_2.forward(60)
                            player_2.right(90)
                        else:
                            player_2.left(90)
                            player_2.forward(60)
                            player_2.left(90)
            elif count_2 == 1 and border_2 == 7:  # the creation of an ladder from 71 to 91
                count_2 = 1
                border_2 = 7
                joy_ladder()
                position_of_player_2 = 71
                print('☺☻player_2 you have got an ladder now you will move to 91☺☻')
                for i in range(20):
                    player_2.fillcolor('white')
                    player_2.pencolor('orange')
                    player_2.shape('classic')
                    player_2.forward(60)
                    count_2 += 1
                    position_of_player_2 += 1
                    print('now you are in the position', position_of_player_2)
                    if count_2 == 10:
                        border_2 += 1
                        count_2 = 0
                        turn = 0
                        if (border_2 % 2 == 0):
                            player_2.right(90)
                            player_2.forward(60)
                            player_2.right(90)
                        else:
                            player_2.left(90)
                            player_2.forward(60)
                            player_2.left(90)
            # creation of snake
            elif count_2 == 7 and border_2 == 1:  # this creates an snake from 17 to 7
                print('☺☻hahaha you are bitten by python now you will go to 7☺☻')
                sadness_snake()
                count_2 = 7
                border_2 = 1
                position_of_player_2 = 17
                for i in range(7):
                    player_2.fillcolor('white')
                    player_2.pencolor('orange')
                    player_2.shape('classic')
                    player_2.backward(60)
                    count_2 -= 1
                    if count_2 == 0:
                        border_2 = 0
                        player_2.right(90)
                        player_2.backward(60)
                        player_2.right(90)
                        for i in range(3):
                            player_2.backward(60)
                            count_2 = 7
                            border_2 = 0
                            position_of_player_2 = 7
                        turn = 0
                        print('now you are in the position', position_of_player_2)
            elif count_2 == 4 and border_2 == 5:  # this creates an snake from 54 to 34
                print('☺☻hahaha you are bitten by python now you will go to 34')
                sadness_snake()
                count_2 = 4
                border_2 = 5
                position_of_player_2 = 54
                for i in range(4):
                    player_2.fillcolor('white')
                    player_2.pencolor('orange')
                    player_2.shape('classic')
                    player_2.backward(60)
                    count_2 -= 1

                    if count_2 == 0:
                        border_2 = 4
                        player_2.right(90)
                        player_2.backward(60)
                        player_2.right(90)
                        count_2 = 10
                        for i in range(10):
                            player_2.backward(60)
                            count_2 -= 1
                            if count_2 == 0:
                                player_2.right(90)
                                player_2.forward(60)
                                player_2.right(90)
                                for i in range(6):
                                    player_2.backward(60)
                                    count_2 = 4
                                    border_2 = 3
                                    position_of_player_2 = 34
                                turn = 0
                                print('now you are in the position', position_of_player_2)
            elif count_2 == 2 and border_2 == 6:  # this creates an snake from 62 to 18
                print('☺☻hahaha you are bitten by python now you will go to 18☺☻')
                count_2 = 2
                border_2 = 6
                sadness_snake()
                position_of_player_2 = 62
                for i in range(2):
                    player_2.fillcolor('white')
                    player_2.pencolor('orange')
                    player_2.shape('classic')
                    player_2.backward(60)
                    count_2 -= 1
                    if count_2 == 0:
                        border_2 = 5
                        print('border_2==', border_2)
                        player_2.left(90)
                        player_2.backward(60)
                        player_2.left(90)
                        count_2 = 10
                        for i in range(10):
                            player_2.backward(60)
                            count_2 -= 1
                            if count_2 == 0:
                                border_2 = 4
                                player_2.left(90)
                                player_2.forward(60)
                                player_2.left(90)
                                count_2 = 10
                                for i in range(10):
                                    player_2.backward(60)
                                    count_2 -= 1
                                    if count_2 == 0:
                                        border_2 = 3
                                        player_2.left(90)
                                        player_2.backward(60)
                                        player_2.left(90)
                                        count_2 = 10
                                        for i in range(10):
                                            player_2.backward(60)
                                            count_2 -= 1
                                            if count_2 == 0:
                                                border_2 = 2
                                                player_2.right(90)
                                                player_2.backward(60)
                                                player_2.right(90)
                                                count_2 = 10
                                                for i in range(10):
                                                    player_2.backward(60)
                                                    count_2 -= 1
                                                    if count_2 == 0:
                                                        player_2.left(90)
                                                        player_2.backward(60)
                                                        player_2.left(90)
                                                        for i in range(2):
                                                            player_2.backward(60)
                                                            count_2 = 8
                                                            border_2 = 1
                                                            position_of_player_2 = 18
                                                        turn = 0
                                                        print('now you are in the position', position_of_player_2)
            elif count_2 == 4 and border_2 == 6:  # thia creates an snake from 64 to 59

                print('☺☻hahaha you are bitten by python now you will go to 59☺☻')
                count_2 = 4
                border_2 = 6
                sadness_snake()
                position_of_player_2 = 64
                for i in range(4):
                    player_2.fillcolor('white')
                    player_2.pencolor('orange')
                    player_2.shape('classic')
                    player_2.backward(60)
                    count_2 -= 1
                    if count_2 == 0:
                        border_2 = 5
                        player_2.left(90)
                        player_2.backward(60)
                        player_2.left(90)
                        for i in range(1):
                            player_2.backward(60)
                            count_2 = 9
                            border_2 = 5
                            position_of_player_2 = 59
                        turn = 0
                        print('now you are in the position', position_of_player_2)
            elif count_2 == 4 and border_2 == 9:  # this creats an snake from 94 to 36
                print('☺☻hahaha you are bitten by python now you will go to 36☺☻')
                count_2 = 4
                border_2 = 9
                position_of_player_2 = 94
                sadness_snake()
                for i in range(4):
                    player_2.fillcolor('white')
                    player_2.pencolor('orange')
                    player_2.shape('classic')
                    player_2.backward(60)
                    count_2 -= 1
                    if count_2 == 0:
                        border_2 = 8
                        count_2 = 10
                        player_2.right(90)
                        player_2.backward(60)
                        player_2.right(90)
                        for i in range(10):
                            player_2.backward(60)
                            count_2 -= 1
                            if count_2 == 0:
                                player_2.left(90)
                                player_2.backward(60)
                                player_2.left(90)
                                count_2 = 10
                                for i in range(10):
                                    player_2.backward(60)
                                    count_2 -= 1
                                    if count_2 == 0:
                                        player_2.right(90)
                                        player_2.backward(60)
                                        player_2.right(90)
                                        count_2 = 10
                                        for y in range(10):
                                            player_2.backward(60)
                                            count_2 -= 1
                                            if count_2 == 0:
                                                player_2.left(90)
                                                player_2.backward(60)
                                                player_2.left(90)
                                                count_2 = 10
                                                for w in range(10):
                                                    player_2.backward(60)
                                                    count_2 -= 1
                                                    if count_2 == 0:
                                                        player_2.right(90)
                                                        player_2.backward(60)
                                                        player_2.right(90)
                                                        count_2 = 10
                                                        for o in range(10):
                                                            player_2.bk(60)
                                                            count_2 -= 1
                                                            if count_2 == 0:
                                                                player_2.left(90)
                                                                player_2.backward(60)
                                                                player_2.left(90)
                                                        for t in range(4):
                                                            player_2.backward(60)
                                                            count_2 = 6
                                                            border_2 = 3
                                                            position_of_player_2 = 36
                                                            turn = 0
                                                        print('now you are in the position', position_of_player_2)





            elif count_2 == 3 and border_2 == 9:  # this creates an snake from 93 to 73

                print('☺☻hahaha you are bitten by python now you will go to 73☺☻')
                count_2 = 3
                border_2 = 9
                position_of_player_2 = 93
                sadness_snake()
                for i in range(3):
                    player_2.fillcolor('white')
                    player_2.pencolor('orange')
                    player_2.shape('classic')
                    player_2.backward(60)
                    count_2 -= 1
                    if count_2 == 0:
                        border_2 = 8
                        player_2.right(90)
                        player_2.backward(60)
                        player_2.right(90)
                        count_2 = 10
                        for i in range(10):
                            player_2.backward(60)
                            count_2 -= 1
                            if count_2 == 0:
                                border_2 = 7
                                player_2.left(90)
                                player_2.backward(60)
                                player_2.left(90)
                                for i in range(7):
                                    player_2.backward(60)
                                    count_2 = 3
                                    border_2 = 7
                                    position_of_player_2 = 73
                                turn = 0
                                print('now you are in the position', position_of_player_2)
            elif count_2 == 6 and border_2 == 9:  # this creates an snake from 96 to 75
                print('☺☻hahaha you are bitten by python now you will go to 75☺☻')
                count_2 = 6
                border_2 = 9
                position_of_player_2 = 95
                sadness_snake()
                for i in range(6):
                    player_2.fillcolor('white')
                    player_2.pencolor('orange')
                    player_2.shape('classic')
                    player_2.backward(60)
                    count_2 -= 1
                    if count_2 == 0:
                        border_2 = 8
                        player_2.right(90)
                        player_2.backward(60)
                        player_2.right(90)
                        count_2 = 10
                        for i in range(10):
                            player_2.backward(60)
                            count_2 -= 1
                            if count_2 == 0:
                                border_2 = 7
                                player_2.left(90)
                                player_2.backward(60)
                                player_2.left(90)
                                for i in range(5):
                                    player_2.backward(60)
                                    count_2 = 5
                                    border_2 = 7
                                    position_of_player_2 = 75
                                turn = 0
                                print('now you are in the position', position_of_player_2)
            elif count_2 == 9 and border_2 == 9:  # this creates an snake from 99 to 78
                print('☺☻hahaha you are bitten by python now you will go to 78☺☻')
                count_2 = 9
                border_2 = 9
                sadness_snake()
                position_of_player_2 = 99
                for i in range(9):
                    player_2.fillcolor('white')
                    player_2.pencolor('orange')
                    player_2.shape('classic')
                    player_2.backward(60)
                    count_2 -= 1
                    if count_2 == 0:
                        border_2 = 8
                        player_2.right(90)
                        player_2.backward(60)
                        player_2.right(90)
                        count_2 = 10
                        for i in range(10):
                            player_2.backward(60)
                            count_2 -= 1
                            if count_2 == 0:
                                border_2 = 7
                                player_2.left(90)
                                player_2.backward(60)
                                player_2.left(90)
                                for i in range(2):
                                    player_2.backward(60)
                                    count_2 = 8
                                    border_2 = 7
                                    position_of_player_2 = 78
                                turn = 0
                                print('now you are in the position', position_of_player_2)



            else:
                turn = 0

    else:


        if (count_1 == 0 and border_1 == 10)  :
            time.sleep(2)
            ladder_111.ht()
            ladder_112.ht()
            ladder_1.ht()
            ladder_2.ht()
            ladder_3.ht()
            ladder_4.ht()
            ladder_5.ht()
            ladder_6.ht()
            ladder_7.ht()
            ladder_8.ht()
            ladder_9.ht()
            ladder_10.ht()
            ladder_11.ht()
            ladder_12.ht()
            ladder_13.ht()
            snake_1.ht()
            snake_2.ht()
            snake_3.ht()
            snake_4.ht()
            snake_5.ht()
            snake_6.ht()
            snake_7.ht()
            snake_8.ht()
            snake_9.ht()
            snake_10.ht()
            snake_11.ht()
            snake_12.ht()
            snake_13.ht()
            snake_14.ht()
            snake_15.ht()
            s.ht()
            position_of_player_1 = 100
            print('player_1 now you are in the position', position_of_player_1)
            s.reset()
            s.write('player_1 you are the winner',align='center',font=('Arial',20,'normal'))
            
        elif (count_2 == 0 and border_2 == 10) :
            time.sleep(2)
            ladder_111.ht()
            ladder_112.ht()
            ladder_1.ht()
            ladder_2.ht()
            ladder_3.ht()
            ladder_4.ht()
            ladder_5.ht()
            ladder_6.ht()
            ladder_7.ht()
            ladder_8.ht()
            ladder_9.ht()
            ladder_10.ht()
            ladder_11.ht()
            ladder_12.ht()
            ladder_13.ht()
            snake_1.ht()
            snake_2.ht()
            snake_3.ht()
            snake_4.ht()
            snake_5.ht()
            snake_6.ht()
            snake_7.ht()
            snake_8.ht()
            snake_9.ht()
            snake_10.ht()
            snake_11.ht()
            snake_12.ht()
            snake_13.ht()
            snake_14.ht()
            snake_15.ht()
            s.hideturtle()
            position_of_player_1 = 100
            print('player_2 now you are in the position', position_of_player_1)
            s.reset()
            s.write('player_2 you are the winner',align='center',font=('Arial',20,'normal'))
            

final()
s.exitonclick()
