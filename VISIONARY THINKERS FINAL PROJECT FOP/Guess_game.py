'''importing tkinter ,PIL,random,functools '''
from tkinter import *
from PIL import ImageTk, Image
from random import *
from functools import partial
from pygame import *
# importing messagebox to display message box
from tkinter import messagebox

# guess game starts

def guess_game():
    '''This is a guess number game.A number is generated randomly by the system. Player will be given 3 tries to
    guess the random number. All the numbers will be placed in buttons separately and user will press on the the
    numbered buttons to select the number he thinks is the correct number. Whenever the number selected by the player
    is wrong the player will be given a hint if the number he selected is greater or smaller than the random generated
    number. If the selected number is greater than the random number than all the number boxes from that selected number
    till the end will become nonfunctional and a cross will appear on them. In the case of smaller number all the
    numbers from the start to the selected number will become nonfunctional and a cross will appear on them. When the
    player presses the disabled buttons it will not do anything and his tries will not decrease. When the player finally
     guesses the correct number then the correct number will become green and all other
     buttons will become red and nonfunctional and a cross will appear on them. If player runs of tries then all the
    buttons will become red and nonfunctional and game will be over for the player. The player can restart the game by
    pressing the play again button anytime in the game.
    The exit button will also be available to the user throughout out the game which player can press and go back to menu.
    '''
    init()
    guess_number_pane = Tk()  # to generate pane for the guess the number game

    tries = 3  # total tries given to the player
    generated_rand_num = 0  # initializing the random system generated number

    beg_row, end_row = 0, 5  # The number of teh starting row and last row respectively

    # Game window properties like icon and size
    guess_number_pane.title('guess the number')  # Title of the game shown on the window
    guess_number_pane.iconbitmap('logo.ico')  # Icon of the game shown on the window with the title
    guess_number_pane.geometry("750x500")  # Size of the window when the game is opened
    guess_number_pane.resizable(False, False)  # Function to disable the resize of the game window

    # The background image of the game taken from the same folder as the game
    bg = ImageTk.PhotoImage(file="login2.jpg")
    speaker_img = [ImageTk.PhotoImage(file='speaker-empty.png'), ImageTk.PhotoImage(file='speaker-filled.png')]
    # Placing the background image as the background of the game window
    bg_image = Label(guess_number_pane, image=bg)  # Giving the image path to the Label to show on the screen
    bg_image.grid(row=0, column=0)  # Placing the image on the game window

    main_frame = LabelFrame(guess_number_pane, bg="#e9e7e8")  # Creating the frame for the game
    main_frame.grid(row=0, column=0)  # Placing the frame in the game on top of the background image

    # Name of the game placed on as the title of the game frame
    game_title = Label(main_frame, text='GUESS THE NUMBER', font=("Times New Roman", 16, "bold"), fg="#684d9c",
                       bg='#eeeced')
    game_title.grid(row=0, sticky=W + E + N + S)  # placing the title in the frame

    number_frame = LabelFrame(main_frame, bg="#e9e7e8")  # Frame to show all the number buttons
    number_frame.grid(row=1, sticky=W + E + N + S, columnspan=3)  # Placing the frame in the main game frame
    def play_music(n=0):
        mixer.music.load("back ground.mp3")
        if n == 0:
            mixer.music.play()
            n = 1
        else:
            mixer.music.stop
            n = 0
        play_btn = Button(guess_number_pane, image=speaker_img[n], bg='#e7dae4', activebackground='#e7dae4', relief=GROOVE,
                          command=lambda: play_music(n))
        play_btn.place(x=670, y=5)
    play_music()
    # closing game and going to main menu
    def exit_guess_game():  # Function to exit the game the anytime and go to the main menu
        play_music(1)
        guess_number_pane.destroy()  # Destroy the guess game original window in which game is running
        import main
        main.menu1()  # Calling function to go to the main menu

    # calculating number of tries left and disabling the buttons and showing hints to the player
    def enter(place):
        nonlocal tries, number_frame, beg_row, end_row, generated_rand_num

        tries -= 1  # calculating tries after selecting the number

        selected_number_row, selected_number_column = place  # store place of button which is clicked
        user_selected_num = selected_number_row * 5 + selected_number_column + 1

        # Generating hints , checking tries and checking game end conditions to see how the player is progressing

        # if the player selected number is smaller than random generated number and player still has tries left
        # This condition is triggered
        if (generated_rand_num > user_selected_num) and tries != 0:
            game_info_and_hint_for_user = Label(number_frame,
                                                text=f'{user_selected_num} is smaller than the guessed number.\nTry to guess a larger number.',
                                                font=("Times New Roman", 10, "bold"), fg="#bd2379")
            # Showing different hints to the player

            dis_columns_in_row = 5  # number of columns to be disabled in a row

            # disabling buttons from the lowest number to user selected button

            # This for loop disables all the Buttons from the start to the pressed buttons
            # This is a nested for loop
            # selected_number_row indicates the number of row of player selected number
            for row in range(beg_row, selected_number_row + 1):
                if row == selected_number_row:
                    dis_columns_in_row = selected_number_column + 1
                    # checking if the row is same as player selected number
                    # if yes then updating the column number to stop loop automatically when that number is reached

                    # this loop turns all the buttons red and add a cross on them showing that they are not of use anymore
                    # Even if player accidentally clicks on the they will not do anything and tries will not decrease
                for column in range(dis_columns_in_row):  # Giving the column no. of the pressed number as range
                    num_button = Button(number_frame, text='X', fg="red2", activebackground="red2"
                                        , font=("Times New Roman", 12, "bold"))
                    # different properties of buttons to be made non functional
                    num_button.grid(row=row, column=column, sticky=W + E + N + S)  # Placing them in the grid

            """Changing the beginning row number to the row number of the previously pressed button
                if the next try is also incorrect then buttons will start disabling from the last player selected number"""
            beg_row = selected_number_row


        elif (user_selected_num > generated_rand_num) and (tries != 0):

            """if the player selected number is greater than random generated number and player still has tries left
                This condition is triggered
                guesses given to the user about the number      """

            game_info_and_hint_for_user = Label(number_frame,
                                                text=f'{user_selected_num} is greater than the guessed number.\nTry to guess a smaller number.'
                                                , font=("Times New Roman", 10, "bold"), fg="#bd2379")
            dis_columns_in_row = -1  # selecting the last column of the grid since in python -1 shows last entry

            # disabling buttons from the highest number to player selected number
            # this is a reverse for loop which starts from the bottom and goes in reverse to the player selected number
            for row in range(end_row - 1, selected_number_row - 1, -1):  # for loop in reverse order to disable buttons
                if row == selected_number_row:
                    dis_columns_in_row = selected_number_column - 1
                    # checking if the row is same as player selected number
                    # if yes then updating the column number to stop loop automatically when that number is reached

                # this loop turns all the buttons red and add a cross on them showing that they are not of use anymore
                # i.e. are non functional
                # Even if player accidentally clicks on the they will not do anything and tries will not decrease
                for column in range(4, dis_columns_in_row, -1):
                    num_button = Button(number_frame, text='X', font=("Times New Roman", 12, "bold")
                                        , fg="red2", activebackground="red2")
                    num_button.grid(row=row, column=column, sticky=W + E + N + S)
                    # different properties of buttons that are made non functional

            end_row = selected_number_row + 1  # changing the number of row to the  user selected number
            # if the next try is also incorrect then buttons will start disabling from the last player selected number

        elif tries == 0 and (generated_rand_num != user_selected_num):
            """ if the player selected number is not equal to the random generated number and player has no tries left
                When player loses the game, this event is triggered
                Updating the Label to show the user he lost the game because he ran out of tries """

            game_info_and_hint_for_user = Label(number_frame,
                                                text='Your tries have ended. You have lost the\ngame. Press Play Again or Exit!!!'
                                                , font=("Times New Roman", 10, "bold"), fg="#bd2379")
            # disable every button when tries are over

            # This nested for loop disables all the buttons by making them non functional and turning them red
            for row in range(5):
                for column in range(5):
                    num_button = Button(number_frame, text='X', bg='red', activebackground="red2",
                                        font=("Times New Roman", 12, "bold"))
                    num_button.grid(row=row, column=column, sticky=W + E + N + S)
                    # updating the buttons in the grid
                # shows the guess is correct and the game is over since player ran out of tries



        else:
            """the condition when player wins the game and he has guessed the correct number.
                if all the other conditions are not true this means player has tries left and has won the game
                Updating label to show that he has won the game     """

            game_info_and_hint_for_user = Label(number_frame, text='You have guessed the number.\nCongratulations!!!',
                                                font=("Times New Roman", 10, "bold"), fg="#bd2379")

            dis_columns_in_row = 5
            """The tries are increased by one because the user guessed the correct number and his tries will not be deducted """
            tries += 1

            """ Now 2 nested for loops work. One disable the buttons form the top to just before the selected number.
            The other loop disables all the buttons from the bottom to just after the user selected number."""

            # disable button from the lowest to correct button
            # making all the buttons non functional from the top to the correct number

            for row in range(beg_row, selected_number_row + 1):
                if row == selected_number_row:  # different conditions to stop before the correct number
                    dis_columns_in_row = selected_number_column

                for column in range(dis_columns_in_row):
                    bt = Button(number_frame, text='X', fg='red', font=("Times New Roman", 12, "bold"))
                    bt.grid(row=row, column=column, sticky=W + E + N + S)

            beg_row = selected_number_row  # updating the row number
            # disable button from the highest to correct button
            dis_columns_in_row = -1
            for row in range(end_row - 1, selected_number_row - 1, -1):
                if row == selected_number_row:  # different conditions to stop just after the correct number
                    dis_columns_in_row = selected_number_column

                    # This loop works from bottom to the top
                    # disabling all the buttons from the bottom before the correct number
                for column in range(4, dis_columns_in_row, -1):
                    bt = Button(number_frame, text='X', fg='red', font=("Times New Roman", 12, "bold"))
                    bt.grid(row=row, column=column, sticky=W + E + N + S)


            # changing the colour of correct guessed number to make it prominent than other buttons
            num_button = Button(number_frame, text=str(selected_number_row * 5 + selected_number_column + 1), fg='black'
                                , bg='#c4ff0e', font=("Times New Roman", 12, "bold"))
            num_button.grid(row=selected_number_row, column=selected_number_column, sticky=W + E + N + S)

        # showing the user the total number of tries he has left in the game
        tries_count = Label(number_frame, text='Tries : ' + str(tries), font=("Times New Roman", 12, "bold"),
                            fg="#bd2379", borderwidth=1, relief=SUNKEN)
        tries_count.grid(row=7, column=1, columnspan=3)
        game_info_and_hint_for_user.grid(row=5, column=0, columnspan=20, sticky=W + E + N + S)

    # Function generating all the number buttons in the game by for loop
    def number_buttons():
        for row in range(5):
            for column in range(5):
                b = Button(number_frame, text=str((row * 5) + column + 1), command=partial(enter, (row, column)),
                           padx=10,
                           pady=10, font=("Times New Roman", 12, "bold"), fg="#bd2379")

                # Partial is a function from function tools
                b.grid(row=row, column=column, sticky=N + S + W + E)

    # play again guess game
    """function that is running all teh previous functions and making the game playable"""

    def play_guess_game():
        nonlocal generated_rand_num, tries, beg_row, end_row
        beg_row, end_row = 0, 5
        tries = 3
        generated_rand_num = randint(1, 25)  # generating random number by the system

        # Label showing the user to start the game by guessing the number
        lab = Label(number_frame, text='Guess a number', font=("Times New Roman", 18, "bold"), fg="#bd2379")
        lab.grid(row=5, column=0, columnspan=20, sticky=W + E + N + S)

        # Showing the number of initial tries to the player in the game
        tries_count = Label(number_frame, text='Tries : ' + str(tries), font=("Times New Roman", 12, "bold"),
                            fg="#bd2379", borderwidth=1, relief=SUNKEN)
        tries_count.grid(row=7, column=1, columnspan=3)

        number_buttons()  # generating the number buttons grid by calling the function

    play_guess_game()  # calling the function to start the guess game

    """ Exit button and play again buttons. These are available to the player all the time.
        Player can press them any time during the game or after ending the game
        The respective fuctions are called when the play again or exit buttons are pressed."""

    guess_game_exit = Button(main_frame, text='EXIT', command=exit_guess_game, padx=27, pady=15,
                             font=("Times New Roman", 12, "bold"), fg="#bd2379")
    guess_game_play_again_button = Button(main_frame, text='PLAY AGAIN', padx=10, pady=15, command=play_guess_game,
                                          font=("Times New Roman", 12, "bold"), fg="#bd2379")

    guess_game_play_again_button.grid(row=3, sticky=W + E + N + S, columnspan=3)
    guess_game_exit.grid(row=4, sticky=W + E + N + S, columnspan=3)

    # guess game main window loop
    guess_number_pane.mainloop()

# guess game ends
