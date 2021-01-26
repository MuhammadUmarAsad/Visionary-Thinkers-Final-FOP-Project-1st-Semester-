'''importing tkinter ,PIL,random,functools '''
from tkinter import *
from PIL import ImageTk, Image
from random import *
from functools import partial
from pygame import *
# importing messagebox to display message box
from tkinter import messagebox

# start tictac toe

def tic_tac_toe_game(player1, player2):
    '''Tic tac toe is a game that allows 2 users to play and match can have 3 possibilities. Either it can be won by first player or it can be won by
    2nd player or the third possibility is to draw the game results will be shown at the end '''
    init()
    tictactoe_pane = Tk()  # window generation for the game
    tictactoe_pane.title('TicTacToe')  # title of the window
    tictactoe_pane.iconbitmap('icon.ico')  # icon on the window (logo)
    tictactoe_pane.geometry('750x500')  # screen size width x height
    tictactoe_pane.resizable(False, False)  # screen cannot  be resized
    bg_tictac = ImageTk.PhotoImage(file='bg.png')  # background image of the window
    bg_img = Label(tictactoe_pane, image=bg_tictac)  # label to display the background on screen
    bg_img.grid(row=0, column=0)  # defining position of label
    speaker_img = [ImageTk.PhotoImage(file='speaker-empty.png'), ImageTk.PhotoImage(file='speaker-filled.png')]

    def play_music(n=0):
        mixer.music.load("back ground.mp3")
        if n == 0:
            mixer.music.play(-1)
            n = 1
        else:
            mixer.music.stop
            n = 0
        play_btn = Button(tictactoe_pane, image=speaker_img[n], bg='#e7dae4', activebackground='#e7dae4', relief=GROOVE,
                          command=lambda: play_music(n))
        play_btn.place(x=670, y=5)

    play_music()
    def ext():  # function to execute when user clicks on exit button
        play_music(1)
        import main
        tictactoe_pane.destroy()
        main.menu1()  # displaying the menu to the user

    def play():
        '''main function of the game that defines all the setup of the game .Checks which player is one and gives the symbol to be plotted'''
        nonlocal player1, player2  # names of player 1 and player 2
        tries = randint(0, 1)  # randomly generates the tries of both players and gives them their mark
        circles, crosses, left_box = [], [], []  # initialize the list to count the circles and crosses and blank boxes
        circle_img = ImageTk.PhotoImage(file='circle.png')  # import image for circles
        cross_img = ImageTk.PhotoImage(file='cross.png')  # import image for the cross
        # frame defining for the game tic tac toe
        tic_tac = LabelFrame(tictactoe_pane)  # tic tac toe pane to be called
        tic_tac.grid(row=0, column=0)  # defining grid to show the tic_tac_toe pane
        tictac = LabelFrame(tic_tac)  # frame that imports the label frame
        tictac.grid(row=1, column=0)  # positioning the label
        # defining the specifications of the label
        title_label = Label(tic_tac, text='TIC TAC TOE', font=("Times New Roman", 16, "bold"), fg="#684d9c",
                            bg='#eeeced').grid(row=0, sticky=W + E + N + S)

        def show_message(message):
            # function to show the sign which player will get the X and which will get O
            nonlocal player1, player2
            # label that shows the message to the players
            lbl = Label(tic_tac, text=f'{player1} : X  vs  {player2} : O\n' + message,
                        font=("Times New Roman", 10, "normal"), fg="#684d9c", bg='#eeeced').grid(row=2,sticky=W + E + N + S,columnspan=3)

        def disable():
            # This function will disable all the boxes left when one user will win the game
            nonlocal left_box
            for row, column in left_box:  # for loop to check for the boxes left
                b = Button(tictac, text='', bg='white', width=9, height=4, borderwidth=3,
                           state='disable')  # defining the states
                b.grid(row=row, column=column, sticky=N + S + W + E)  # positioning of the button

        def left_boxes():
            # this function determines the number of boxes left
            nonlocal circles, crosses, left_box  # nonlocal variables
            for place in circles:  # for loop that checks for the circles
                left_box.remove(place)
            for place in crosses:  # for loop to check for the circles
                left_box.remove(place)
            # passing place of the button which is clicked by the user

        def cross(place):
            '''This function places the button of cross on the desired place of user'''
            nonlocal player1, player2
            nonlocal cross_img, crosses, circles  # nonlocal variables
            row, column = place
            bt = Button(tictac, image=cross_img, bg='white', width=62, height=62,
                        borderwidth=3)  # creating button with image
            bt.grid(row=row, column=column, sticky=N + S + W + E)  # show cross on the screen
            crosses.append(place)  # place occupied
            if check(crosses):
                left_boxes()  # function to check for the boxes
                disable()  # disable

                show_message(f'{player1} has won')  # winning message
            elif len(circles) + len(crosses) == 9:
                show_message('Game Draw')  # when game is draw
            else:
                show_message(f'{player2} has turn ')  # Turn of 2nd player if game is still in progress

            # passing place of the button which is clicked by the user

        def circle(place):
            '''This function places the button of O circles on the desired place '''
            nonlocal player1, player2
            nonlocal circle_img, circles, crosses  # nonlocal variables
            row, column = place
            bt = Button(tictac, image=circle_img, bg='white', width=62, height=62,
                        borderwidth=3)  # creating button with image
            bt.grid(row=row, column=column, sticky=N + S + W + E)  # show circle on the screen
            circles.append(place)
            if check(circles):
                left_boxes()
                disable()
                show_message(f'{player2} has won')
            elif len(circles) + len(crosses) == 9:
                show_message('Game Draw')
            else:
                show_message(f'{player1} has turn ')

        def check(lst):
            '''Checking for the winning condition in the game'''
            diagonal1, diagonal2 = [], []  # lists defined
            checker = False  # checker to be declared false
            for i in range(3):  # for loop to check for the horizontal and vertical matches
                row, column = [], []  # list that stores the place of horizonatal and vertical positions
                for place in lst:

                    if place[0] == i:  # Horizontal lines
                        row.append(place)  # using append to add the place in the row list
                        if len(row) == 3:
                            return True  # winning case if three concide in one line
                    if place[1] == i:  # vertical lines
                        column.append(place)  # Appends the place to the list
                        if len(column) == 3:
                            return True  # winning case if three concide in one line
            for place in lst:  # diagonal checking  loop
                if place[0] == place[1]:  # main diagonal
                    diagonal1.append(place)  # append into list
                    if len(diagonal1) == 3:
                        return True  # winning case if concides in diagonal
                if place[0] + place[1] == 2:  # secondary diagonal
                    diagonal2.append(place)
                    if len(diagonal2) == 3:  # checking and returning the win
                        return True
            return False  # when no condition is satisfied

        def enter(place):
            '''This function checks for the tries and tell about the turn of the respective player
            .Also it increments the tries'''
            nonlocal tries
            if tries % 2 == 0:  # check it the turn is even or odd
                cross(place)
            else:
                circle(place)  # if odd then circle
            tries += 1  # increment in number of tries to alter the turns

        # creating blank buttons of the game and showing it on screen
        for row in range(3):
            # nested for loop for the rows and column checking
            for column in range(3):
                left_box.append((row, column))
                # creating blank  button
                b = Button(tictac, text='', bg='white', width=9, height=4, borderwidth=3,
                           command=partial(enter, (row, column)))
                b.grid(row=row, column=column, sticky=N + S + W + E)

        if tries == 0:
            # if condition is satisfied turn is given to player 1
            show_message(f'{player1} has turn')
        else:
            show_message(f'{player2} has turn')  # else 2nd player has turn
            # creating buttons and defining their position
        btn_ply = Button(tic_tac, text='PLAY AGAIN', padx=10, pady=15, command=play,
                         font=("Times New Roman", 12, "bold"), fg="#bd2379")
        btn_exit = Button(tic_tac, text='EXIT', command=ext, padx=27, pady=15, font=("Times New Roman", 12, "bold"),
                          fg="#bd2379")

        btn_ply.grid(row=3, sticky=W + E + N + S, columnspan=3)
        btn_exit.grid(row=4, sticky=W + E + N + S, columnspan=3)
        # loading the game into mainloop
        tictactoe_pane.mainloop()

    play()  # function call

#end tictac toe