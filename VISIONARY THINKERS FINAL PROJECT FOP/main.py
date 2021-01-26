# _____MAIN PROGRAM ____
'''importing tkinter ,PIL,random,functools '''
from tkinter import *
from PIL import ImageTk, Image
# importing messagebox to display message box
from tkinter import messagebox
from pygame import *
import os

'''user_data is a dictionary to save name and score of iq quiz and snake xenzia fetched from the file "username.txt"
data_in_file to open username.txt so that data can be fetched in the form of list
index is the location of user_data in the file'''

user_data, data_in_file, index = {}, [], 0


def login_user(username):  # function of login
    with open('username.txt', 'r') as data:
        index = 0
        data_in_file = data.readlines()
        for user_data in data_in_file:  # for loop to read data
            user_data = eval(user_data)  # using eval to evaluate user_data
            if user_data['name'] == username:  # if statement to check for the entered user
                return user_data, data_in_file, index  # returning the user data entities from the file
            index += 1

def check_username(username):
    '''function to check for the existence of name in the file'''
    usernames = []
    with open('username.txt', 'r') as data:  # opening in read mode
        for user in (data.readlines()):
            user = eval(user)  # evaluating user name from the file read as line
            usernames.append(user.get("name"))
    for entry in usernames:  # for loop to check if the name exists in the file
        if entry == username:
            return False  # returning false if username alreaddy exists
    return True  # returning True if username is new signupcomplete

def registered_players(list_file):
    '''Function to fetch the names of registered players
    This is special for the tic tac toe game of the main'''
    usernames = []  # list of usernames that are registered
    for user in list_file:  # for loop to iterate through the list file which contains dictionaries of data
        user_record = eval(user)  # evaluating the user_record
        usernames.append(user_record['name'])  # fetching the keyword name
    return usernames  # returning user_names of all the registered users in the form of list

def update_in_file(record):
    global user_data
    data = open("username.txt", "w")			#opening file in write mode to del all the previous content
    data = open("username.txt", "a")            #opening file in append mode to update file
    for dicts in record:    #loop will append all the dicts in data_in_file in students.txt
        if user_data!=dicts:  #condition to avoid repetition
            data.writelines(dicts)
    data.close()   #closing file
def registered_users():
    '''This function is created for login purpose the list that is displayed for the login text box in which all the registered participamnts are shown  '''
    with open('username.txt', 'r') as data:
        usernames = registered_players(data.readlines())  # calling the function registered_players(list_file)
    return usernames  # returning user_names of all the registered users in the form of list


def register(username):
    '''registeration of the new user and creating entries for the scores in the dictionary . Also this is stored in the text file in the form of dictionary'''
    user_data = dict()  # dictionary for the collection of data
    user_data['name'] = username  # name is the key to store name of user against it
    user_data['iqquiz'] = 0  # initial score of game to be set zero
    user_data['snake'] = 0  # initial score of the user to be set zero
    with open('username.txt', 'a') as data:  # opening file in append mode to write the data in it
        data.writelines(f'{user_data}\n')  # writing data to the file

def login1():
    '''This function contains sub function of sign up tkinter labels are used '''
    global user_data, data_in_file, index  # global variables to use them in all modules
    login = Tk()  # Tk() to create a window
    login.iconbitmap('menulogo.ico')  # logo
    login.title("Login ")  # giving title
    login.geometry("750x500")  # specifying the geometry ie. width x height
    login.resizable(False, False)  # user cannot resize the window pane
    size = os.stat("username.txt").st_size #Checking the size of file

    def sign_up():
        '''creates window of signup for the new user . It contains the function call for checking the existance of user '''
        login.destroy()  # close the window
        sign = Tk()  # create new window for the signup
        sign.title('sign up')  # title of window
        sign.iconbitmap('menulogo.ico')  # logo
        sign.geometry('230x170')  # size in width x height
        sign.resizable(False, False)  # cannot resize window

        frame = LabelFrame(sign, padx=25, pady=25, bg='#e7e2e5')  # frame with specifications of padding and bg
        frame.pack()  # pack the frame to display it on screen
        # creating label of user to display user name
        user = Label(frame, text="Username", font=("Times New Roman", 12, "bold"), fg="#bd2379", anchor='w',
                     bg='#e7e2e5').grid(row=0, column=0, sticky=W + E)
        # Entry of username
        text = Entry(frame, font=("Times New Roman", 10, "italic"), fg="#c34873")
        text.grid(row=1, column=0)  # grid diplay row and column position

        def signs():
            '''signs function is used to call the functions '''
            name = text.get()  # text.get() is getting input from the user in the variable 'name'
            if check_username(name):  # check the name whether it exists in the file or not
                register(name)  # register the new username in the file
                sign.destroy()  # destroys the sign window pane
                login1()  # calls the login1 function which will shows the login window pane
            else:
                messagebox.showerror('Sign up ERROR',
                                     'This username is already exists,\nTry another username')  # shows error that the username already exists
        btn_sigin = Button(frame, text='Sign up', command=signs, font=("Times New Roman", 12, "bold"), bg="#e9e7e8",
                           fg="#bd2379").grid(row=2, column=0,
                                              pady=10)  # making button of sign up and opens sign up window to sign up the new user

    bg = ImageTk.PhotoImage(file="login2.jpg")  # loads image of the background
    bg_image = Label(login, image=bg)  # create label in which the background image is to be shown
    bg_image.grid(row=0, column=0)  # grid/shows label on the screen
    # frame of login
    frame = Frame(login, bg="#e9e7e8")  # creating frame in which all login options are to be placed
    frame.place(x=140, y=20, height=322, width=460)  # placing frame to the screen

    title = Label(frame, text="Login Here", font=("Helvetica", 30, "bold"), fg="#ec69ab", bg="#e9e7e8").place(x=90,y=30)  # shows the title of frame
    user_ = Label(frame, text="Username", font=("Times New Roman", 12, "bold"), fg="#bd2379", bg="#e9e7e8").place(x=90,y=130)  # place text Username on the screen

    if size != 0:
        lst_user = registered_users()  # call the function which returns list of registered users
        user = StringVar()  # intializing the variable of option menu
        txt_user = OptionMenu(frame, user, *lst_user)  # creating option menu
        txt_user.config(font=("Times New Roman", 12, "bold"), fg="#bd2379", anchor=W,
                            relief=SUNKEN)  # setting font and text color of the option menu
        txt_user.place(x=90, y=165, width=350, height=25)  # place the option menu on the screen
        txt_user['menu'].config(font=("Times New Roman", 12, "bold"),
                                    fg="#bd2379")  # setting font and text color of the dropdown menu
    else:
        messagebox.showinfo(' Welcome !!',
                                     'Please register yourself first !!')  # shows error that the username already exists

    def logins():
        '''login user into the game This function checks if the user doesnot enters his/her name
        then it does not allows you to go to the menu for laying and selection of games'''
        global user_data, index, data_in_file  # global variable to access easily in all modules
        name = user.get()  # gets the name of the user from option menu
        if name != '':  # check whether the name is selected or not
            user_data, data_in_file, index = login_user(name)  # calls the function to login into the data
            login.destroy()  # destroying the login window
            menu1()  # calling menu to the program
        else:
            messagebox.showinfo('Login info','Please select your Username first or sign up')

    if size!=0:
        btn_login = Button(frame, text='Login', command=logins, font=("Times New Roman", 12, "bold"), fg="#bd2379",
                           padx=7)  # button that login the user
        btn_login.place(x=220, y=245)  # placing the button in the frame

    btn_sigin = Button(frame, text='Sign up', command=sign_up, font=("Times New Roman", 12, "bold"),
                       fg="#bd2379").place(x=220, y=285)  # button that sign up user ie. new entry
    login.mainloop()  # displaying the login window

    return True

# genrate menu screen

def menu1():
    init() # for pygame
    global data_in_file, index, user_data
    menu = Tk()  # creates window named menu
    menu.title('Menu')  # title
    menu.iconbitmap('menulogo.ico')  # logo
    menu.resizable(False,False) #disable resizing the screen
    bg = ImageTk.PhotoImage(file="_img.png") #background image for menu
    bg_image = Label(menu, image=bg).grid(row=0, column=0,rowspan=5,columnspan=3) #showing image to the screen

    # importing images for buttons
    leader_brd=ImageTk.PhotoImage(file='leader_board.png')
    exit_img=ImageTk.PhotoImage(file='menu_exit.png')
    speaker_img=[ImageTk.PhotoImage(file='speaker-empty.png'),ImageTk.PhotoImage(file='speaker-filled.png')]

    def exit_menu():
        menu.destroy()  # this command will close menu window

    def open_leader_brd():
        '''This function will create a window that will display the score records of registered users. It will display
         score for the snake nexzia and Iq quiz game sorted in the descemding order. new records will automatcally
         updated in the leaderboard.This can be accessed by clicking on the button on right left corner on menu window'''
        leader_brd_screen=Toplevel() #creating window for the leaderboard
        leader_brd_screen.title('Leader Board')#title
        leader_brd_screen.iconbitmap('menulogo.ico')  # logo
        leader_brd_screen.resizable(False,False) #disable resizing the screen
        iq_leader_brd=LabelFrame(leader_brd_screen,text='IQ QUIZ',bg='#f9ebc8',fg='#fda08a',
                                 font=("showcard gothic", 20, "bold"),padx=20)#creating frame for iq quiz leader board
        iq_leader_brd.grid(row=0,column=0,sticky=N+S) #showing frame on the screen
        snake_leader_brd=LabelFrame(leader_brd_screen,text='SNAKE XENZIA',bg='#f9ebc8',fg='#fda08a',
                                    font=("showcard gothic", 20, "bold"),padx=20)#creating frame for snake leader board
        snake_leader_brd.grid(row=0,column=1,sticky=N+S) #showing frame on the screen
        def element_two(data):   #function used in key for sorting
            return data[1]
        def element_three(data): #function used in key for sorting
            return data[2]
        def scores_game(): #generate a list of tuple in which names and scores of snake xenzia and iq quiz
            usernames=[]
            with open('username.txt', 'r') as data:
                list_file=data.readlines() #read data from the file
                for user in list_file:  # for loop to iterate through the list file which contains dictionaries of data
                    user_record = eval(user)  # evaluating the user_record
                    usernames.append((user_record['name'],user_record['snake'],user_record['iqquiz']))  # fetching the keyword name
            return usernames
        list_leader_brd=scores_game() #creating list for leader board
        list_snake_leader_brd=sorted(list_leader_brd,key=element_two,reverse=True) #sorting list for snake leader board
        list_iq_leader_brd=sorted(list_leader_brd,key=element_three,reverse=True) #sorting list for iq quizz leader board
        for user in list_snake_leader_brd:
            score=Label(snake_leader_brd,text=f'{user[0]}\t\t{user[1]}',bg='#f9ebc8',padx=20,fg='#fda98a',
                        font=("showcard gothic", 14, "normal"))
            score.pack()  #show name and score of snake in the screen
        for user in list_iq_leader_brd:
            score=Label(iq_leader_brd,text=f'{user[0]}\t\t{user[2]}',bg='#f9ebc8',padx=20,fg='#fda98a',
                        font=("showcard gothic", 14, "normal"))
            score.pack() #show name and score of iq quizz in the screen

    def play_music(n=0):   #function to play and stop background music
        mixer.music.load("Game_music_3.mp3") #load background music
        if n == 0:
            mixer.music.play(-1) #play music
            n = 1
        else:
            mixer.music.stop  #stop music
            n = 0
        play_btn = Button(menu, image=speaker_img[n], relief=GROOVE, bg='#f9ebc8', activebackground='#f9ebc8',
                          command=lambda: play_music(n)) #creating play button of music
        play_btn.place(x=935, y=0) #placing play button on the screen

    # open guess game and close menu window
    def open_guessgame():
        play_music(1) #stops music
        menu.destroy() #destroy main menu screen
        import Guess_game  #import py file( game file Guess_game)
        Guess_game.guess_game() #calling function of the game

    def open_tic_tac_toe_game():
        tic_tac_toe_list = data_in_file
        tic_tac_toe_list.remove(f'{user_data}\n')
        def select_second_ply():
            player2 = Toplevel()
            player2.iconbitmap('menulogo.ico')  # logo
            player2.title('Select Player 2')
            player2.geometry('230x170')
            lst_user = registered_users()
            lst_user.remove(user_data['name'])
            user = StringVar()
            frames = LabelFrame(player2)
            frames.pack()
            txt_user = OptionMenu(frames, user, *lst_user)
            txt_user.config(font=("Times New Roman", 12, "bold"), fg="#bd2379", anchor=W, relief=SUNKEN)
            txt_user.grid(row=0, column=0)
            txt_user['menu'].config(font=("Times New Roman", 12, "bold"), fg="#bd2379")

            def login_tictac():
                name = user.get()
                if name != '':  # check whether the name is selected or not
                    user2_data, data_in_file, index = login_user(name)  # calls the function to login into the data
                    play_music(1)
                    tic_tac_toe_list.append(f'{user_data}\n')
                    menu.destroy()
                    import Tic_Tac_Toe
                    Tic_Tac_Toe.tic_tac_toe_game(user_data['name'], user2_data['name'])
                else:
                    messagebox.showinfo('Login info', 'Please Select a second player to play the game')
            btn_login = Button(frames, text='Login', command=login_tictac, font=("Times New Roman", 12, "bold"), fg="#bd2379",
                               padx=7).grid(row=1, column=0)
            player2.mainloop()
        if len(tic_tac_toe_list) <1:
            response=messagebox.showerror('Entry Error',
            'This is a multiplayer game \nPlease register another plaer to play the game')  # shows error that the username already exists
            if response == "ok":
                menu.destroy()
                login1()
        else:
            select_second_ply()


    def open_snakxia_game():#open snake gome
        menu.destroy()#destroy menu window
        import Snake #import py file( game file snake)
        Snake.play(user_data,data_in_file) #calling function of game

    def open_colour_and_shape():
        menu.destroy()
        import Colour
        Colour.open_game()

    # adding new games
    def open_iq():
        menu.destroy()
        import IQ_QUIZ_FINAL
        IQ_QUIZ_FINAL.IQ_GAME(user_data,data_in_file)

    play_music()

    btt = Button(menu, text='Tic Tac Toe',bg='#f9ebc8',fg='#fda08a',padx=109,activebackground='#f9ebc8',relief=RIDGE,
                 font=("showcard gothic", 20, "normal"), command=open_tic_tac_toe_game)
    bgg = Button(menu, text='Guess the number',bg='#f9ebc8',fg='#fda08a',padx=59,activebackground='#f9ebc8',relief=RIDGE,
                 font=("showcard gothic", 20, "normal"), command=open_guessgame)
    biq = Button(menu, text='Iq Quiz', bg='#f9ebc8',fg='#fda08a',padx=135,activebackground='#f9ebc8',relief=RIDGE,
                 font=("showcard gothic", 20, "normal"), command=open_iq)
    bsc = Button(menu, text='Shape/colour', bg='#f9ebc8',fg='#fda08a',padx=85,activebackground='#f9ebc8',relief=RIDGE,
                 font=("showcard gothic", 20, "normal"), command=open_colour_and_shape)
    bsnake = Button(menu, text='Snake Xenzia', bg='#f9ebc8',fg='#fda08a',padx=92,activebackground='#f9ebc8',relief=RIDGE,
                 font=("showcard gothic", 20, "normal"), command=open_snakxia_game)
    btn_leader_board=Button(menu, image=leader_brd , bg='#f9ebc8', activebackground='#f9ebc8',relief=GROOVE,
                            command=open_leader_brd,font=("showcard gothic", 12, "bold"))
    be = Button(menu, image=exit_img, command=exit_menu, bg='#f9ebc8', activebackground='#f9ebc8', relief=GROOVE, padx=27,
                pady=15)

    biq.place(x=360,y=145)
    btt.place(x=360,y=214)
    bgg.place(x=360,y=290)
    bsc.place(x=360,y=361)
    bsnake.place(x=360,y=440)
    btn_leader_board.place(x=920,y=495)
    be.place(x=15,y=495)
    menu.mainloop()
