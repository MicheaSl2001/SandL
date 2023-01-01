from tkinter import *
from PIL import Image, ImageTk
import random as rd
from player import *
import time

player1 = player(0)
player2 = player(0)
player3 = player(0)
player4 = player(0)
player5 = player(0)
turn = 1  # Number of players in order
i = 1  # Number of sequences when entering names


# main window
def TkSet():
    global game
    global board
    global labelText
    global box1
    global box2
    global botton_gamestart
    global botton_conf1
    global botton_conf2
    global botton_roll

    # create game and frame
    game = Tk()
    game.title("Snakes and Ladders")
    game.geometry("1200x800+100+20")
    frame1 = Frame(game, width=1200, height=800)
    frame1.place(x=0, y=0)

    # create board
    gameboard = Image.open("board.jpg")
    gameboard = gameboard.resize((800, 800))
    board = ImageTk.PhotoImage(gameboard)
    lab = Label(frame1, image=board)
    lab.place(x=400, y=0)

    # create button
    botton_gamestart = Button(game, text="Game Start", width=15, height=5, font=20, background='green',
                              activebackground='red')
    botton_gamestart.place(x=100, y=50)
    botton_gamestart.config(command=start)

    botton_roll = Button(game, text="I'm ready!", width=15, height=5, font=20, background='green',
                         activebackground='red')
    botton_roll.config(command=gamestart)

    botton_conf1 = Button(game, text="confirm", width=7, height=1, font=1, activebackground='red')
    botton_conf1.config(command=NumSet)

    botton_conf2 = Button(game, text="confirm", width=7, height=1, font=1, activebackground='red')
    botton_conf2.config(command=NameSet)

    # create label
    labelText = StringVar()
    label = Label(frame1, textvariable=labelText, font=20)
    labelText.set('Please press the bottom\nto start the game')
    label.place(x=80, y=200)

    # create entry box
    box1 = Entry(game, width=15, font=20)
    box2 = Entry(game, width=15, font=20)


# the function to start the game
def gamestart():
    global num
    global roll_image
    roll_image = Image.open("roll_button.gif")
    roll_image = roll_image.resize((100, 100))
    roll_image = ImageTk.PhotoImage(roll_image)
    botton_roll.destroy()
    label_text()
    Button(game, image=roll_image, command=roll_a_dice).place(x=130, y=600)


# the function to start the choose-platform
def start():
    labelText.set('Enter the number of players')
    botton_gamestart.destroy()
    botton_conf1.place(x=250, y=450)
    box1.place(x=80, y=450)


# the function to restart the game
def restart():
    game.destroy()
    TkSet()


# the function to choose the number of players
def NumSet():
    global num
    num = int(box1.get())
    if (num >= 1) & (num <= 4):
        labelText.set("the number of players are %d\nenter player1's name" % num)
        if num == 1:
            labelText.set("you will play with computer\nenter player's name")
        box1.destroy()
        botton_conf1.destroy()
        botton_conf2.place(x=250, y=450)
        box2.place(x=80, y=450)
    else:
        labelText.set("error\n wrong number or not this button")


# the function to enter the names of players
def NameSet():
    global num
    global i
    if num == 1:
        player5.give_name('robot')
    if i == 1:
        player1.give_name(box2.get())
        labelText.set("player%d is %s\nenter next player's name\n" % (i, player1.name))
    elif i == 2:
        player2.give_name(box2.get())
        labelText.set("player%d is %s\nenter next player's name\n" % (i, player2.name))
    elif i == 3:
        player3.give_name(box2.get())
        labelText.set("player%d is %s\nenter next player's name\n" % (i, player3.name))
    elif i == 4:
        player4.give_name(box2.get())
        labelText.set("player%d is %s\nenter next player's name\n" % (i, player4.name))

    if i == num:
        box2.destroy()
        botton_conf2.destroy()
        labelText.set("ALL NAME complete\nAre you ready?\n")
        botton_roll.place(x=100, y=600)
    i += 1


# the function to show the message
def label_text():
    global num
    if num == 1:
        labelText.set("Player      Value\n\n%s       %s\n\n%s       %s" % (player1.name, player1.value, player5.name, player5.value))
    if num == 2:
        labelText.set("Player      Value\n\n%s       %s\n\n%s       %s" % (player1.name, player1.value, player2.name, player2.value))
    if num == 3:
        labelText.set("Player      Value\n\n%s       %s\n\n%s       %s\n\n%s       %s" % (
            player1.name, player1.value, player2.name, player2.value, player3.name, player3.value))
    if num == 4:
        labelText.set("Player      Value\n\n%s       %s\n\n%s       %s\n\n%s       %s\n\n%s       %s" % (
            player1.name, player1.value, player2.name, player2.value, player3.name, player3.value, player4.name,
            player4.value))


# Window displayed at the end
def end_game(name):
    win = Toplevel()
    win.title("Leave or Continue")
    win.geometry("%dx%d%+d%+d" % (150, 150, 550, 425))
    info = "%s win the game!" % name
    msg = Message(win, text=info)
    msg.pack()
    button1 = Button(win, text="Exit", command=game.destroy)
    button1.pack()
    button2 = Button(win, text="Continue", command=restart)
    button2.pack()

# the function to roll dice
def roll_a_dice():
    global dice_img
    global dice_img1
    global num
    global turn
    global image1
    global image2
    global image3
    global image4
    global image5
   
    move_value = rd.randint(1, 6)
    main_path = "dice/"
    dice_p = ['1.gif', '2.gif', '3.gif', '4.gif', '5.gif', '6.gif']
    num0 = move_value - 1
    dice_img = PhotoImage(file=main_path + dice_p[num0])
    Label(game, image=dice_img).place(x=130, y=470)
    if num > 1:
        if turn == 1:
            p_x, p_y = player1.get_value(move_value)
            image1 = Image.open("counter/1.gif")
            image1 = image1.resize((25, 25))
            image1 = ImageTk.PhotoImage(image1)
            Label(game, image=image1).place(x=p_x, y=p_y)
            label_text()
            if player1.value == 100:
                end_game(player1.name)
            turn += 1
        elif turn == 2:
            p_x, p_y = player2.get_value(move_value)
            image2 = Image.open("counter/2.gif")
            image2 = image2.resize((25, 25))
            image2 = ImageTk.PhotoImage(image2)
            Label(game, image=image2).place(x=p_x, y=p_y)
            label_text()
            if player2.value == 100:
                end_game(player2.name)
            turn += 1
        elif turn == 3:
            p_x, p_y = player3.get_value(move_value)
            image3 = Image.open("counter/3.gif")
            image3 = image3.resize((25, 25))
            image3 = ImageTk.PhotoImage(image3)
            Label(game, image=image3).place(x=p_x, y=p_y)
            label_text()
            if player3.value == 100:
                end_game(player3.name)
            turn += 1
        elif turn == 4:
            p_x, p_y = player4.get_value(move_value)
            image4 = Image.open("counter/4.gif")
            image4 = image4.resize((25, 25))
            image4 = ImageTk.PhotoImage(image4)
            Label(game, image=image4).place(x=p_x, y=p_y)
            label_text()
            if player4.value == 100:
                end_game(player4.name)
            turn += 1
        if turn > num:
            turn = 1
        message = "Now it's player%d's turn" % turn
    elif num == 1:
        p_x, p_y = player1.get_value(move_value)
        image1 = Image.open("counter/1.gif")
        image1 = image1.resize((25, 25))
        image1 = ImageTk.PhotoImage(image1)
        Label(game, image=image1).place(x=p_x, y=p_y)
        label_text()
        if player1.value == 100:
            end_game(player1.name)

        move_value1 = rd.randint(1, 6)
        main_path1 = "dice/"
        dice_p1 = ['1.gif', '2.gif', '3.gif', '4.gif', '5.gif', '6.gif']
        num1 = move_value1 - 1
        dice_img1 = PhotoImage(file=main_path1 + dice_p1[num1])
        Label(game, image=dice_img1).place(x=250, y=470)
        p_x, p_y = player5.get_value(move_value1)
        image5 = Image.open("counter/5.png")
        image5 = image5.resize((25, 25))
        image5 = ImageTk.PhotoImage(image5)
        Label(game, image=image5).place(x=p_x, y=p_y)
        label_text()
        if player5.value == 100:
            end_game(player5.name)
        if turn > num:
            turn = 1
        message = "Now it's player%d's turn" % turn
    Label(game, text=message, font=20).place(x=100, y=420)


