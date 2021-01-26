from tkinter import *
import random

""" This is an IQ game made for kids. The questions asked in this quiz are made for kids so they can learn different 
things and can enhance their knowledge. There are total 30 questions in this quiz out of which 10 questions are asked 
from the player. All the questions will be asked randomly and the  options are also shuffled for each question.
Everytime the game is opened the questions are selected randomly and their options are shuffled when they are read from
pre saved questions file. 

There will be a back question button and next question button in the game. Both will also be given to the user which he 
can use to navigate to different questions in the quiz. The question number will also be shown to the user/ player which 
will on the top of the question asked to the player. 

When the game is first opened a main window is first shown to the user where start and exit buttons are placed in a 
section of the window already defined for the buttons. There is also a logo for the iq quiz at the top.
The rules of the game are also written in the start menu for the user which are easy to understand.

If the exit button is pressed then the game will close and menu will be opened again.
If start is clicked then the window will update and a complete test system set up will be given to the user.
This set up is same like most of the online test systems we see on different websites.
A Question will be shown to the user and he will be given 4 choices from which he can select the correct option.
When the user selects an option that will be marked in the system. User can navigate to different questions and when
User comes back to that question that option will be marked which he previously selected.

In the start the back button will be disabled because there is no question before the 1st one.
When the last question is reached then the next button will become disabled because the last question is being asked 
from the User.

There will be a finish quiz button. When that button is pressed the quiz will end and the score of the User will be 
shown on the screen. Each question contain 1 mark.  Also a play again button will be given to the user which he can 
select to play the Quiz again. But whenever the IQ Quiz is played again the questions are changed and their Options 
are also shuffled.

Now a rules button will also be present in the Quiz. When user clicks on it a window will open which will have a exit 
button and rules will be written on it.

Now there will be an Exit button always present in the game which the user can press to exit the game any time he wants
and he will be directed to the main menu from where User can select any game to play. Th IQ Quiz will close 
automatically and score will not be saved since user exited the game without finishing the game.
"""

# the main function which can be called anywhere to start the quiz
def IQ_GAME(user_data,data_in_file):

    txt_file_of_questions = open("IQ TEST.txt", mode="r")       # Opening the file in which questions are already saved
    test = txt_file_of_questions.readlines()        # saving the questions in text file as a list in a variable
    txt_file_of_questions.close()       # closing the text file after reading the data
    start_list = []      # defining an empty list to store questions in it

    for i in test:      # using a foor loop to correctly store the list of lists as a proper list
        collection = eval(i)
        start_list.append(collection)

    replay_list = []        # Initializing an empty list for use when game is replayed
    random.shuffle(start_list)      # shuffling the questions in the list of random questions are given
    true_list = start_list      # true list is the list which will have the questions stored properly in it
    for i in range(len(true_list)):     # Shuffling the options of the questions
        random.shuffle(true_list[i][1])
    replay_list = true_list     # storing the true list for later replay use

    index = 0       # initializing the index of the list
    rules = """Total 10 questions will be asked.\nEach question will contain 1 mark.\n4 Choices will be given to you.
    Choose the answer you think will be the best.\nYou can use Next and Back Button to navigate the IQ QUIZ.
    You can press the finish button any time to check your answers.\nThen after game is over you can exit or play again"""

    window = Tk()           # Main window of the game
    window.config(background="white")       # making the background white
    window.iconbitmap("iq_quiz.ico")        #   changing the icon of the quiz
    window.title("IQ Quiz")                 # placing the title on the app
    window.geometry("1366x736")             # fixing the geometry 
    window.resizable(False,False)

    # Background of the IQ Quiz
    # storing it and then placing it as the back ground
    filename = PhotoImage(file="IQ BACK FINAL.png")
    background_label = Label(window, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    # coordinates to start placement of back ground

    # making the frame for the navigation and control buttons
    new_frame_1 = LabelFrame(window, text="OPTION MENU", bg="#fff8f0")
    new_frame_1.pack(side=BOTTOM)       # placing it on the bottom of the window
    iq_txt = Label(window, text="HI!! Please don't cheat", font=("calibri", 40), bg="blue", fg="black")
    iq_txt.pack()

    # images for start and exit and iq quiz and them placing them in the desired section
    IQ_img = PhotoImage(file="IQ.png")
    IQ_Image = Label(window, image=IQ_img, bg="#fff8f0")
    IQ_Image.pack(pady=(10, 40))

    # making frame for start and exit button
    main_menu_start_and_exit_frame = LabelFrame(window, text="Questions", bg="#fff8f0")
    main_menu_start_and_exit_frame.pack()
    # packing the frame in the main window 

    def exit_0():
        window.destroy()
        import main
        main.menu1()

    # placing images as buttons instead of text
    # then giving them different commands according to their roles in the game

    # placing the exit button in the main home menu of game
    exit_icon_img = PhotoImage(file="EXIT_FUN_1.png")
    # placing the image exit button
    exit_icon = Button(main_menu_start_and_exit_frame, image=exit_icon_img, background="white", command=exit_0)
    exit_icon.grid(column=0, row=0)
    # placing the exit button in the grid

    # placing the exit button in the main home menu of game
    start_icon_img = PhotoImage(file="START_FINAL_2.png")
    # placing the image for start button
    start_icon = Button(main_menu_start_and_exit_frame, image=start_icon_img, background="white", command=lambda: start_game())
    # placing the start button in the grid
    start_icon.grid(column=1, row=0)


    my_rules = Label(window, text=rules, fg="black", bg='#fff8f0', font=("Calibri", 20))
    my_rules.pack(anchor="center")



    def start_game():
        """When the game is started then the main menu of game is destroyed so the quiz can be shown.
        Every thing in the main window is destroyed"""
        nonlocal index
        main_menu_start_and_exit_frame.destroy()
        iq_txt.destroy()        # TEXT is destroyed
        IQ_Image.destroy()      # IQ logo is destroyed
        start_icon.destroy()        # start button is destroyed
        my_rules.destroy()      # rules button is destroyed
        show_questions()        # calling the questions when the main menu is destroyed

    opt_selected = StringVar()      # making the string value variable
    opt_selected.set(None)          # initilizing it by setting it to None

    def update(selected):
        nonlocal index
        #this is the functions which updates the value of the string variable and keeps it updated when next or previous
        # questions is changed
        opt_selected = StringVar()
        opt_selected.set(None)
        # poping the pre defined NONE value from the list and inserting the choice selected by the user
        true_list[index].pop(3)
        true_list[index].insert(3, selected)    # setting the value of variable to -1 so no option is selected

        # this function is used to show the user rules when he is playing the game
    def exit_show_info():
        top = Toplevel()
        # when this button is pressed then a window is opened and the rules are shown in the window
        my_rules = Label(top, text="Here are the rules of the game" + f"\n{rules}", font=("Calibri", 20),
                         activebackground="Red", bg="Yellow")
        # different properties of the my rules

        my_exit = Button(top, text="Exit", activebackground="black", bg="pink", font=("Calibri", 20),
                         command=top.destroy)       # command to destroy the top window
        my_rules.pack()
        my_exit.pack()

    def show_questions():
        nonlocal index, opt_selected
        global question_number, question, opt_1, opt_2, opt_3, opt_4, next_button, back_button, show_rules_info, exit_but, finish

        # defining the question number in the game and packing it to show in the screen
        question_number = Label(window, text=f"Question no. {index + 1}", bg='#fff8f0', font=("Calibri", 15),
                                relief=RAISED, )
        question_number.pack(pady=(5, 0))

        # defining the question in the game and packing it to show in the screen
        question = Label(window, text=true_list[index][0], width=40, font=("Calibri", 25), wraplength=700,relief = RAISED,
                         background="white", fg="black", bg="#fff8f0", justify="center")
        question.pack(ipadx=20)

        # option 1 radio defining in the game and packing it to show in the screen
        opt_1 = Radiobutton(window, text=true_list[index][1][0], font=("Calibri", 25), bg="pink", variable=opt_selected,
                            value=true_list[index][1][0], padx=30, anchor="center",
                            command=lambda: update(opt_selected.get()))
        opt_1.pack()

        # option 2 radio defining in the game and packing it to show in the screen
        opt_2 = Radiobutton(window, text=true_list[index][1][1], font=("Calibri", 25), bg="gold", variable=opt_selected,
                            value=true_list[index][1][1], padx=30, anchor="center",
                            command=lambda: update(opt_selected.get()))
        opt_2.pack()

        # option 3 radio defining in the game and packing it to show in the screen
        opt_3 = Radiobutton(window, text=true_list[index][1][2], font=("Calibri", 25), bg="lawngreen",
                            variable=opt_selected, value=true_list[index][1][2], padx=30, anchor="center",
                            command=lambda: update(opt_selected.get()))
        opt_3.pack()

        # option 4 radio defining in the game and packing it to show in the screen
        opt_4 = Radiobutton(window, text=true_list[index][1][3], font=("Calibri", 25), bg="cyan",
                            activebackground="green", variable=opt_selected, value=true_list[index][1][3],
                            anchor="center", padx=30, command=lambda: update(opt_selected.get()))
        opt_4.pack()
        show_rules_info = Button(new_frame_1, text='Show the rules!!!', font=("Calibri", 20), bg="gold2",
                                 command=exit_show_info)
        show_rules_info.pack()

        # exit button defining in the game and packing it to show in the screen
        exit_but = Button(new_frame_1, text="Click me to exit", font=("Calibri", 25), bg="orangered",
                          command=exit_0)
        exit_but.pack(pady=(20, 0))

        # finish button defining in the game and packing it to show in the screen
        finish = Button(new_frame_1, text="Click me to finish", font=("Calibri", 22), bg="SlateGray3",
                        command=end_quiz_and_show_score)
        finish.pack()
        back_button = Button(new_frame_1, text="Back", font=("Calibri", 25), bg="khaki", fg="red",
                             command=lambda: back())

        # back button defining in the game and packing it to show in the screen
        back_button.pack(side=LEFT, padx=100, pady=15)
        next_button = Button(new_frame_1, text="Next", font=("Calibri", 25), bg="chocolate",
                             command=lambda: next())
        next_button.pack(side=RIGHT, padx=100, pady=15)
        if index == 0:          # since in the start of the game the question is first thats why back is disables
            back_button["bg"] = "khaki"
            back_button["state"] = DISABLED


    def question_help(index):

        """This is the main function which updates the question number, questions and option  values and also changes
        their variable value of the buttons. In short this is the core function of the iq quiz. Without this the
        questions and its buttons values will not change"""

        # updating the values using the index
        question_number["text"] = f"Question no. {index + 1}"
        question["text"] = true_list[index][0]
        opt_1["text"] = true_list[index][1][0]
        opt_1["value"] = true_list[index][1][0]
        opt_2["text"] = true_list[index][1][1]
        opt_2["value"] = true_list[index][1][1]
        opt_3["text"] = true_list[index][1][2]
        opt_3["value"] = true_list[index][1][2]
        opt_4["text"] = true_list[index][1][3]
        opt_4["value"] = true_list[index][1][3]

    def next():
        global next_button, back_button
        nonlocal index, opt_selected
        index += 1
        question_help(index)    # calling and updating questions with options
        if index == 9:      # if it is the last question then disable next button
            next_button["bg"] = "chocolate"
            next_button["state"] = DISABLED     # changing the state of the next button
        if index != 0:
            back_button["bg"] = "khaki"
            back_button["state"] = ACTIVE       # if it is not the first question keep the back button enabled
        opt_selected.set(true_list[index][3])   # making the radio button select the choice which the user choose

    # this is the function for the back button of the quiz to show the previous question
    def back():
        global back_button, next_button
        nonlocal index, opt_selected
        index -= 1
        question_help(index)    # calling and updating questions with options
        if index == 0:      # if it is the first then disable back button
            back_button["bg"] = "khaki"
            back_button["state"] = DISABLED
            back_button.pack()
        if index != 9:          # if it is not the last question then keep the next button enabled
            next_button["bg"] = "chocolate"
            next_button["state"] = ACTIVE
        opt_selected.set(true_list[index][3])       # making the radio button select the choice which the user choose


        # function to end the quiz and show the score to the user
    def end_quiz_and_show_score():
        global index, replay_list, score, question, opt_1, opt_2, opt_3, opt_4, back_button, next_button, exit_but
        global play_again_button, score_but, opt_selected, show_rules_info, finish
        nonlocal true_list

        # destroying all the labels and options buttons and the other navigation button by forgetting them
        # so the play again window is empty
        question.pack_forget()
        opt_1.pack_forget()
        opt_2.pack_forget()
        opt_3.pack_forget()
        opt_4.pack_forget()
        next_button.pack_forget()
        back_button.pack_forget()
        exit_but.pack_forget()
        show_rules_info.pack_forget()
        finish.pack_forget()
        question_number.pack_forget()
        score = 0       # calculating the score by comparing the user selected option with the correct choice stored in the list
        for i in range(len(true_list)):
            if true_list[i][2] == true_list[i][3]:
                score += 1              # if the choice is correct then 1 mark is awarded
                true_list[i][3] = None      # clearing the choice of the list after mark is awarded
        score_but = Label(window, text=f"HI THERE!!\nYour score is {score}", font=("Calibri", 25))
        score_but.pack()        # packing the score of the user and exit button in the window
        exit_but.pack()
        play_again_button = Button(window, text="Want to play again????", background="white", font=("calibri", 20)
                                   , command=lambda: play_again())
        # pading the play again button in teh window                           
        play_again_button.pack(pady=(100, 380))  
        # Checking the conditon if the registered max score is greater than the current max score 
        if user_data['iqquiz'] < score:

            try:
                # error handling in place of multiple rounds of games
                data_in_file.remove(f'{user_data}\n')
            except:
                # else returning none 
                return None

            # updating the max score in the user data list
            user_data['iqquiz'] = score
            # appending the user data with new max score in the file
            data_in_file.append(f'{user_data}\n')
            # Calling different functions from main.py file
            import main
            # updating the data file 
            main.update_in_file(data_in_file)


    # the function which again runs the game
    def play_again():
        global true_list
        nonlocal replay_list, index

        # rearranging all the buttons and labels on the window
        # By destroying the previous buttons
        play_again_button.pack_forget()
        exit_but.pack_forget()
        score_but.destroy()
        # making the value of the index as 0 so we can play game from the start
        index = 0
        true_list = replay_list     # changing the list with user selected option with an empty choice list
        random.shuffle(true_list)
        for i in range(len(true_list)):     # rearranging the options of the mcqs
            random.shuffle(true_list[i][1])
        show_questions()            # calling function to show the questions and start the quiz from beginning

    window.mainloop()       # main game window loop