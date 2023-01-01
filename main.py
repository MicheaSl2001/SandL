from Snakes_and_Ladders import *


def play_game():
    win.destroy()
    TkSet()


# initial window
win = Tk()
win.title("Snakes and Ladders")
win.iconbitmap('games.ico')
win.geometry("800x580+300+150")
frame = Frame(win, width=800, height=580)
frame.place(x=0, y=0)

cover = Image.open("cover.gif")
board = ImageTk.PhotoImage(cover)

button_image = PhotoImage(file="start_button.gif")
lab = Label(frame, image=board)
lab.place(x=0, y=0)
Button(win, image=button_image, command=play_game).place(x=240, y=490)

win.mainloop()

