from tkinter import *
from pygame import *
from PIL import ImageTk,Image

""" This is a colour game made for kids. When this game is opened a window will open on the screen which is already 
maximized. There will be a section from which the user can select can select any colour. There will be a section from 
the user can select the shape of the colour. When user selects a shape and colour that shape with that colour will print
of the are of the screen selected exclusively for the shapes to be printed.
it is a simple paint for kids in which they can play for fun 
"""
def open_game():
    """ This is the main tkinter window in which tha game is running"""
    init()
    cl_window = Tk()
    cl_window.resizable(False,False)
    cl_window.iconbitmap("Shape-Color-icon.ico")
    cl_window.title("Shape And Colour")
    speaker_img=[ImageTk.PhotoImage(file='speaker-empty.png'),ImageTk.PhotoImage(file='speaker-filled.png')]
    # This is used for displaying the background image in the window
    colour_and_shape_background = PhotoImage(file="COLOUR GAME 5.png")  # giving the location of the image
    background_label = Label(cl_window, image=colour_and_shape_background)
    background_label.place(x=0, y=0)
    # setting the coordinates for the background image

    """Making different frames for the different sections of the games and also give it some symmetry and style
    then placing them in a grid."""

    """This is the frame for the colour selection of shapes
    The coloured buttons will appear in this frame from where user can choose a colour
    This will appear on the left side of the game window"""
    frame_for_colour_selection = LabelFrame(cl_window, text="\tPLEASE SELECT A COLOUR", font=("calibri", 10), height=400,
                                            width=250, bd=5, bg="olivedrab1")
    frame_for_colour_selection.grid(row=0, column=0, padx=(20, 10), pady=20, sticky=N + S + W + E)
    # placing the frame in the grid

    """This is the frame where the shape will print when user selects the shape and colour
    this will appear between the Colour selection frame and shape selection frame"""
    shape_print_frame = LabelFrame(cl_window, text="\t\tSHAPE AND COLOUR PRINT", height=400, font=("calibri", 10),
                                   width=2, bd=5, bg="seagreen2")
    # placing the frame in the grid
    shape_print_frame.grid(row=0, column=1, padx=20, pady=20, sticky=N + S + W + E)

    """This is the frame for the shape selection
    The names of shapes will appear in this frame from where user can choose a shape he want to draw
    This will appear at the rights side the window"""
    frame_for_shape_and_colour = LabelFrame(cl_window, text="\t\tSELECT A SHAPE", height=400, width=250, bd=5
                                            , bg="lightskyblue1")
    # placing the frame in the grid
    frame_for_shape_and_colour.grid(row=0, column=2, padx=(20, 40), pady=20, sticky=N + S + W + E)

    # This is the for the exit button. This will be placed below the print shape frame and will be small in size
    exit_button_frame = LabelFrame(cl_window, text="ENTER BOX", bd=5, bg="gray")
    exit_button_frame.grid(row=1, column=1, padx=20, pady=20, rowspan=2, ipadx=15)
    # placing the frame in the grid

    """ making the colour name and shape name as a variable strings which can change their values whenever 
    that button with different value is selected
    Then .set() is assigning the variable None value since in the start no value is selected"""
    colour_name_var = StringVar()  # variable string for colour name
    shape_name_variable = StringVar()  # variable string for shape name

    colour_name_var.set(None)  # initially setting it both the values to None
    shape_name_variable.set(None)

    """The main function which prints shapes when a colour and a shape is selected
    it will only print a coloured shape when a shape and colour both are selected
    else it will not print the shape"""

    def print_shape():
        txt = "white"  # making the default text fill white
        # list of making the colour of text black when these colours are selected for filling the shape
        Black_text_list = ["orange2", "peachpuff", "skyblue", "lawngreen", "gold",
                           "seagreen2", "maroon4", "khaki"]
        # loop checks and assigns the text colour black colour if a colour from the above list is selected as fill of shape
        # When the loop matches a colour from the list the loop stops and black colour is assigned to the text
        for i in Black_text_list:
            if colour_name_var.get() == i:
                txt = "black"
                break

        """ These are the different conditions to check the which shape has been selected by the user
        These if conditions wil check which shape has been selected and assign the coordinates of that shape of the variables
        Here the shapes are being printed by using coordinates of the shapes which have been defined already
        when a shape is selected its coordinates are also selected and given to the function to show the shape on canvas
        """
        TXT_COOR = 325, 200  # these are the center coordinates for the txt which will appear in the shape

        # These are different shapes and their calculated coordinates
        # the selected shape is printed
        if shape_name_variable.get() != "Circle":
            if shape_name_variable.get() == "Triangle":
                shape_coordinates = (325, 40, 102, 380, 548, 380)
                TXT_COOR = 325, 300  # Since the text was going outside of the shape the coordinates are
                # changed whenever a triangle is selected

            if shape_name_variable.get() == "Square":
                shape_coordinates = (488, 37, 162, 37, 162, 363, 488, 363)

            if shape_name_variable.get() == "Rectangle":
                shape_coordinates = (145, 80, 145, 320, 505, 320, 505, 80)

            if shape_name_variable.get() == "Pentagon":
                shape_coordinates = (325, 0, 135, 138, 207, 362, 443, 362, 515, 138)

            if shape_name_variable.get() == "Hexagon":
                shape_coordinates = (425, 27, 225, 27, 125, 200, 225, 373, 425, 373, 525, 200)

            if shape_name_variable.get() == "Heptagon":
                shape_coordinates = (325, 0, 169, 75, 130, 245, 238, 380, 412, 380, 520, 245, 481, 75)

            if shape_name_variable.get() == "Octagon":
                shape_coordinates = (402, 15, 248, 15, 140, 123, 140, 277, 248, 385, 402, 385, 510, 277, 510, 123)

            if shape_name_variable.get() == "Enneagon":
                shape_coordinates = (325, 0, 196, 47, 128, 165, 152, 300, 257, 388, 393, 388, 498, 300, 522, 165, 454, 47)

            if shape_name_variable.get() == "Decagon":
                shape_coordinates = (387, 10, 263, 10, 163, 82, 125, 200, 163, 318, 263, 390, 387, 390, 487, 318, 525, 200
                                     , 487, 82)
                # The function to show the shape on screen is placed in try because when either a shape or colour is
                # selected in the first it give errors
                # by this there will be no errors and all errors are being handled
            try:
                my_canvas_1.delete("all")  # deleting all the properties of the previous shape before printing a new one

                # Giving the coordinates and shape to be drawn on the screen
                my_canvas_1.create_polygon(shape_coordinates, fill=colour_name_var.get(), outline="black")

                # This is the fun text which will appear in the shape and its colour will change
                # from black to white by changing the shape colour
                my_canvas_1.create_text(TXT_COOR, text=f'Hello!! I am Mr. {shape_name_variable.get()}',
                                        font=("calibri", 23), fill=txt)
            except:  # if a error occurs then None will be returned
                return None
            # if the shape selected is circle then this condition will be triggered
        elif shape_name_variable.get() == "Circle":

            """ since a circle cannot be created automatically in Tkinter
            the center of circle and radius of circle are taken by this functions
            and it returns us the coordinates of a Oval which will be a circle when drawn"""

            def create_circle(x, y, r, canvasName,
                              filling):  # center coordinates, radius, name of canvas, filling of the circle
                # calculating the coordinates for oval such that a circle will be printed
                x0 = x - r
                y0 = y - r
                x1 = x + r
                y1 = y + r
                return canvasName.create_oval(x0, y0, x1, y1, fill=filling)
                # returning the coordinates which will print a circle

            my_canvas_1.delete("all")  # deleting all the properties of the previous shape before printing the circle
            create_circle(325, 200, 180, my_canvas_1, colour_name_var.get())  # calling the function
            # printing fun text in the circle
            # the font size here is different from above due to different geometry of different shapes
            my_canvas_1.create_text(TXT_COOR, text=f'Hello!! I am Mr. {shape_name_variable.get()}',
                                    font=("calibri", 25), fill=txt)

    def button_colour():
        # list of names of different colours
        COLOURS_SEL = ["darkslategray", "palevioletred", "orange2", "peachpuff", "skyblue", "magenta4", "lawngreen",
                       "blue2",
                       "red", "purple2", "gold", "seagreen2", "saddlebrown", "maroon4", "khaki"]
        # the for loop generates the radio buttons for all the colours in the list
        # and also assigns each button their own special variables value of colour
        for colour in COLOURS_SEL:
            opt_1 = Radiobutton(frame_for_colour_selection, text=" ", font=("Calibri", 11), bg=colour,
                                variable=colour_name_var,
                                value=colour, padx=30, command=print_shape)
            opt_1.pack(ipady=2, ipadx=15, anchor="center")
            # griding the buttons one the one when they are generated in a frame

    def shape_select():
        # list of names of different shapes
        shapes = ["Circle", "Triangle", "Square", "Rectangle", "Pentagon", "Hexagon", "Heptagon", "Octagon", "Enneagon",
                  "Decagon"]
        # the for loop generated the radio buttons for all the shapes in the list
        # and also assigns each button their own special variables value
        for name_of_shape in shapes:
            opt_1 = Radiobutton(frame_for_shape_and_colour, text=name_of_shape, font=("Calibri", 12), bg="snow3",
                                variable=shape_name_variable, width=15, value=name_of_shape, padx=30,
                                command=print_shape)
            opt_1.pack(ipadx=15, ipady=10)


    def show_info():        # function to show the rules of the games when it is calles
        top = Toplevel()
        my_rules = Label(top,text="Here are the rules of the game"+f"\n{my_rules_for_shape}",font = ("Calibri",20)
                         ,activebackground = "Red",bg = "Yellow")

        # making an exit button in the rules window
        my_exit = Button(top,text="Exit",activebackground = "Red",bg = "pink",font = ("Calibri",20),command = top.destroy)
        my_rules.pack()
        my_exit.pack()

    def shape_exit():
        cl_window.destroy()
        import main
        main.menu1()

    def play_music(n=0):
        mixer.music.load("back ground.mp3")
        if n==0 :
            mixer.music.play(-1) ; n=1
        else :
            mixer.music.stop ;n=0
        play_btn = Button(cl_window, image=speaker_img[n], relief=GROOVE,bg='#f9ebc8',activebackground='#f9ebc8',
                          command=lambda: play_music(n))
        play_btn.place(x=20, y=630)
    play_music()
    # griding the buttons one the one when they are generated in a frame
    button_colour()     # calling to generate colour buttons
    shape_select()      # calling to generate shape buttons
    # making a canvas on the window and giving it different properties
    my_canvas_1 = Canvas(shape_print_frame, height=400, width=650, bg="snow3")
    my_canvas_1.pack(pady=30)       # packing the canvas in the frame

    # rules for game in the frame below the print shape frame
    my_rules_for_shape = 'Choose a colour and a shape from the given menu\nThat shape with that colour will be printed'
    rules_for_shape = Button(exit_button_frame,text="Click me to see rules",padx=10
                            ,font=("calibri",15),command=show_info)
    rules_for_shape.grid(row=0,sticky = N+S+E+W)

    # making the exit button in  the frame placed below the shape and colour printing frame
    exit_button = Button(exit_button_frame, text="Press me to EXIT", font=("calibri", 17)
                         ,padx=10,command=shape_exit).grid(row=1,sticky = N+S+E+W)
    cl_window.mainloop()