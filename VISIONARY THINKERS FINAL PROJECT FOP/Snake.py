from pygame import * ; from math import * ; from random import * ; from sys import *

"""IMPORTANT NOTE : Pygame does not come with with built in buttons and the buttons have to be designed manually which 
was first tried by using defining a function for the button creation but was of no avail because due to the updation of 
the screen only the last displayed button was accepting the command and the proper function was not achevied so all 
buttons have to be displayed and created seprately. These are just images with a rect around them as soon as the mouse 
gets inside the rect the second image with a greater size is displayed creating theeffect of a pop up button and as soon
as the mouse button is clicked inside the rect area the condition becones true and the given command or function is 
executed thus creating a simple button the primary image with the smaller size is displayed continuesly while the curser
is away from the rect. The whole procedure is very eefeciently delt with by using a simple handling of some integrated 
if else statements"""

"""IMPORTANT NOTE : The whole game is divided into three main parts each part having its on screen display and functions
because on the high density on information used by the whole game it lags and starts to take time soo it was dived into 
three main functions one function for the main screen of the game one for the play screen on the gam eon which the whole
game is to be played and the last to display the game over score and the play again option each is intregated togather 
and create the effect of a single game"""

"""IMPORTANT NOTE : We have used Vectors from the Math library as they are more easy to manipulate according to the game
as they can easily represent the 1st and 2nd values by the 'x' and 'y' so makes the coding more easier and helps us keep
track of the x and y coordinate of the place where we are using it"""

def play(user_data,data_in_file):
    #Initiating the whole program to run all the features of pygame and run the music
    init()
    mixer.music.load("Game_music_3.mp3")
    mixer.music.play(-1)
    #The main screen of the game is defined in a function to be itegrated with the grid and togahter in the game
    def open_snakexia():
        #creating the screen to start using the pygame functions and then setting up the screen ,music ,tick speed and localy used variables
        screen = display.set_mode((1100, 700))
        clock = time.Clock()
        display.set_caption("SNAKEXIA")
        display.set_icon(image.load("Snake-Icon.jpg"))
        x=y=-5 ; x1=1105 ; animation=0
        #setting up the main loop of the game
        while True:
            #Getting the quit event to exit the game at any time
            for Event in event.get():
                if Event.type == QUIT:
                    quit() ; exit()
            #Setting up the bacgroung and te text for the whole screen
            screen.blit(image.load("Snake-snake game background.png"),(x,y))
            screen.blit(image.load("Snake-snake game background.png"),(x1,y))
            screen.blit(image.load("Snake-Thinkersx.png"),(30,30))
            screen.blit(image.load("Snake-info.png"),(245,225))
            #using the changing values of the variable values to be able to create the background animation
            if animation%10==0:
                for i in range(15):
                    screen.blit(image.load("Snake-logo.png"), (360, 100))
            else:
                screen.blit((image.load("Snake-logo-2.png")),(324,100))
            x-=+5 ; x1-=+5 ; animation+=1
            if x == -1105 : x=1105
            elif x1 == -1105: x1=1105
            #Settin up the buttons ewhich will be used to initiate the differnt commands
            pos_mouse=mouse.get_pos()
            #Setting up the play button which will intiate the game
            if Rect(485,575,100,100).collidepoint(pos_mouse):
                # setting the condition if the mouse is clicked the command is executed
                if mouse.get_pressed()[0] == 1:
                    play_snakexia()
                    quit() ; exit()
                else:screen.blit(image.load("Snake-start-2.png"),(475,565))
            else:screen.blit(image.load("Snake-start.png"),(485,575))
            #Setting up the home button which make the user go back to the main menu of the whole grid
            if Rect(50,605, 120, 50).collidepoint(pos_mouse):
                # setting the condition if the mouse is clicked the command is executed
                if mouse.get_pressed()[0] == 1:
                    quit()
                    import main
                    main.menu1()
                    exit()
                else:screen.blit(image.load("Snake-home-2.png"),(40,596))
            else:screen.blit(image.load("Snake-home.png"),(50,605))
            # Updating the screen continuesly to display all the changes
            display.update()
            clock.tick(60)

    #Defining the game in a function so it can be easily integrated with the whole grid
    def play_snakexia():

        """IMPORTANT NOTE: The whole screen is pseudoly devided into cells each having a demesions of 20x20 and are used in
         helping with the programming of the whole game"""

        #Creating a SNAKE class which will hold all the functions for our snake like its movement ,Creation ,Collision and graphics
        class SNAKE:
            #defining the inital movement ad the snake cells which becom our snake
            def __init__(self):
                self.body=[Vector2(26,15),Vector2(27,15),Vector2(28,15)]
                self.movement=Vector2(-1,0)

            #Function to draw the snake on the snake by using the snake cells
            def snake(self):
                #Taking each cell in the snake cells and then checking it for different conditions
                for num,cell in enumerate(self.body):
                    #defining the size and location of the snake cell
                    rect = Rect(cell.x*20 - 1,cell.y*20 -1,22,22)
                    #Checking if the Cell is the head of the snake and displaying the proper graphic
                    if num == 0:
                        screen.blit(self.graphic_head(),rect)
                    #Checking if the cell is the ail of the snake and displaying the proper graphic
                    elif num == len(self.body)-1:
                        screen.blit(self.graphic_tail(),rect)
                    #Checking if the cell is the body of the sake and displaying the proper graphic
                    else:
                        pre_cell=self.body[num+1] - cell ; nex_cell=self.body[num-1] - cell
                        screen.blit(self.graphic_body(pre_cell,nex_cell),rect)

            #Function to check the graphics of head of snake and retutring the appropriate graphics according to the change in the x or y coordinate
            def graphic_head(self):
                #Returing the left image head if the snake is facing left
                if self.body[1] - self.body[0] == Vector2(1, 0): return (image.load("Snake-head-lf.png"))
                #Returing the right image head if the snake is facing right
                elif self.body[1] - self.body[0] == Vector2(-1, 0): return (image.load("Snake-head-rn.png"))
                #Returing the up image head if the snake is facing up
                elif self.body[1] - self.body[0] == Vector2(0, 1): return (image.load("Snake-head-up.png"))
                #Returing the down image head if the snake is facing down
                else: return (image.load("Snake-head-dw.png"))

            # Function to check the graphics of tail of snake and retutring the appropriate graphics according to the change in the x or y coordinate
            def graphic_tail(self):
                relation = self.body[len(self.body) - 2] - self.body[len(self.body) - 1]
                # Returing the left image tail if the snake is facing left
                if relation == Vector2(1, 0): return (image.load("Snake-tail-lf.png"))
                # Returing the right image tail if the snake is facing right
                elif relation == Vector2(-1, 0): return (image.load("Snake-tail-rn.png"))
                # Returing the up image tail if the snake is facing up
                elif relation == Vector2(0, 1): return (image.load("Snake-tail-up.png"))
                # Returing the down image tail if the snake is facing down
                else: return (image.load("Snake-tail-dw.png"))

            # Function to check the graphics of body of snake and retutring the appropriate graphics according to the change in the x or y coordinate
            def graphic_body(self,pre_cell,nex_cell):
                #Checing if the previus and after cell have same y coordinate to return the horizontal image
                if pre_cell.y == nex_cell.y: return (image.load("Snake-body-h.png"))
                #Checing if the previus and after cell have same x coordinate to return the verical image
                elif pre_cell.x == nex_cell.x: return (image.load("Snake-body-v.png"))
                #Checing the before and after cells of the current cell to check in whcich way the body should turn depending upon the x and y coordinate
                else:
                    if pre_cell.x == -1 and nex_cell.y == -1 or pre_cell.y == -1 and nex_cell.x == -1:
                        return (image.load("Snake-turn-3.png"))
                    elif pre_cell.x == -1 and nex_cell.y == 1 or pre_cell.y == 1 and nex_cell.x == -1:
                        return (image.load("Snake-turn-2.png"))
                    elif pre_cell.x == 1 and nex_cell.y == -1 or pre_cell.y == -1 and nex_cell.x == 1:
                        return (image.load("Snake-turn-4.png"))
                    else:
                        return (image.load("Snake-turn-1.png"))

            #Function to move the snake in the direction of its head and increase its size if it eats the fruit
            def move_eat(self,eat):
                #Checking if the snake size is to be incresed to remainsame depending upo the eating of the fruit
                if eat == True: body_copy=self.body[:]
                else: body_copy=self.body[:-1]
                #Adding the new cell in the direction of the head of the screen
                body_copy.insert(0,body_copy[0]+self.movement)
                #Checking if any of the snake cell goes out of the screen and change its location to the opposite side of screen if it does
                for count,cell in enumerate(body_copy):
                    if cell.x==55 : body_copy[count].x=0
                    elif cell.x<0 : body_copy[count].x=55
                    elif cell.y==35 : body_copy[count].y=0
                    elif cell.y<0 : body_copy[count].y=35
                #Returing the new cells for the snake body
                self.body=body_copy[:]

            #Function to check the collision of the snake cells
            def collision(self):
                #Taking all the snake cells and checking if any of them collide with snake heaf
                for body in snake.body[1:]:
                    if body == snake.body[0]:
                        #Going to the replay menu when collision is detected
                        replay_snakexia(str(len(snake.body)-3))
                        quit() ; exit()

        #Creating a FRUIT class which will help us makind the fruit and changing its place once it as been eaten
        class FRUIT:
            #Defing random postion for the fruit and taking a random fruit from the list
            def __init__(self):
                self.pos=Vector2(randint(1,54),randint(1,34)) ; self.fruits=sample(fruit_list,1)
            #Creating i.e. displaying the image of the fruit using the values taken before
            def fruit(self):
                screen.blit(self.fruits[0],Rect(self.pos.x*20 -2,self.pos.y*20 -2,20,20))
            #Generating new values of position and fruit for the fruit creation
            def new(self):
                self.pos=Vector2(randint(1,54),randint(1,34)) ; self.fruits=sample(fruit_list,1)

        # Creating the screen to start using the pygame functions and then setting up the screen ,music ,tick speed and localy used variables
        screen=display.set_mode((1100,700))
        clock=time.Clock()
        display.set_caption("SNAKEXIA")
        display.set_icon(image.load("Snake-Icon.jpg"))
        fruit_list=[image.load("Snake-Apple.png"),image.load("Snake-Strawberry.png"),image.load("Snake-Orange.png")]
        eat_sound = mixer.Sound("Snake-Eat.mp3")
        score_font=font.Font("Snake-Font.ttf",25)
        #setting up the variables which will use the classes we have created
        snake=SNAKE() ; fruit=FRUIT()
        #setting up the update feature to help in the movement of the snake and help in controlling its speed
        update=USEREVENT ; speed =110
        time.set_timer(update,speed)

        # setting up the main loop of the game
        while True:
            #Setting up the background of the game screen
            screen.blit(image.load("Snake-background.jpg"), (-5, -5))
            #Setting up the scre display using the font and its render function on the screen
            score = score_font.render("Score: "+str(len(snake.body) - 3), True, Color("White"))
            screen.blit(score,(950,650))

            #Setting up a loop to take all type of events happening in the whole program
            for Event in event.get():
                #Setting up the condition to exit the program if the exit event is used
                if Event.type == QUIT:
                    quit() ; exit()
                #Setting up the condtion so that the snake moves and detects its collision when it is updated after a specific interval
                if Event.type == update:
                    snake.move_eat(False) ; snake.collision()
                #Getting all the keyboard key events inside the loop
                if Event.type == KEYDOWN:
                    #Getting the event for the pressing of "a" key to decrease the speed of the snake
                    if Event.key == K_a and speed != 160:
                        speed += 50 ; time.set_timer(update, speed)
                    # Getting the event for the pressing of "a" key to decrease the speed of the snake
                    if Event.key == K_s and speed != 60:
                        speed -= 50 ; time.set_timer(update, 50)
                    # Getting the event for the pressing of "a" key to decrease the speed of the snake
                    if Event.key == K_UP and snake.movement.y != 1:
                        snake.movement = Vector2(0, -1)
                    # Getting the event for the pressing of "a" key to decrease the speed of the snake
                    if Event.key == K_DOWN and snake.movement.y != -1:
                        snake.movement = Vector2(0, 1)
                    # Getting the event for the pressing of "a" key to decrease the speed of the snake
                    if Event.key == K_LEFT and snake.movement.x != 1:
                        snake.movement = Vector2(-1, 0)
                    # Getting the event for the pressing of "a" key to decrease the speed of the snake
                    if Event.key == K_RIGHT and snake.movement.x != -1:
                        snake.movement = Vector2(1, 0)
            #Creating the snake and fruit on the screen
            fruit.fruit() ; snake.snake()
            #Checking if the snake eats the fruit and then creating the new fruit
            if fruit.pos == snake.body[0]:
                eat_sound.play()
                fruit.new() ; snake.move_eat(True)
            #Checking if the fruit is not created on the body of the snake and changing its place in that happens
            for cell in snake.body[1:]:
                if cell == fruit.pos : fruit.new()
            # Updating the screen continuesly to display all the changes
            display.update()
            clock.tick(60)

    #Defining the replay screen in a function so it can be easily integrated with the whole grid
    def replay_snakexia(Score):
        # Creating the screen to start using the pygame functions and then setting up the screen ,music ,tick speed and localy used variables
        screen = display.set_mode((1100, 700))
        clock = time.Clock()
        display.set_caption("SNAKEXIA")
        display.set_icon(image.load("Snake-Icon.jpg"))
        game_font = font.Font("Snake-Font.ttf", 50)
        x=y=-5 ; x1=1105
        #file handleing for the code
        max_score=int(Score)
        # setting up the main loop of the game
        while True:
            # Setting up the bacgroung and te text for the whole screen
            screen.blit(image.load("Snake-snake game background.png"), (x, y))
            screen.blit(image.load("Snake-snake game background.png"), (x1, y))
            # using the changing values of the variable values to be able to create the background animation
            x -= +5 ; x1 -= +5
            if x == -1105 : x = 1105
            elif x1 == -1105 : x1 = 1105
            over=game_font.render("Game Over", True, Color("Black"))
            score=game_font.render("Your Score is "+str(Score) ,True,Color("Black"))
            screen.blit(over, (400,50)) ; screen.blit(score,(320,150))
            # Getting the quit event to exit the game at any time
            for Event in event.get():
                if Event.type == QUIT:
                    quit() ; exit()
            #setting up the buttons to get the commands for the buttons
            pos_mouse=mouse.get_pos()
            #setting up the button for the re playing of the game so it can be played continuesly
            if Rect(450,320,200,198).collidepoint(pos_mouse):
                #setting the condition if the mouse is clicked the command is executed
                if mouse.get_pressed()[0] == 1:
                    play_snakexia()
                    quit() ; exit()
                else:screen.blit(image.load("Snake-replay-2.png"),(430,300))
            else:screen.blit(image.load("Snake-replay.png"),(450,320))
            #setting up the button for the menu command to return the user to the main menu of the whole grid
            if Rect(50,605, 120, 50).collidepoint(pos_mouse):
                # setting the condition if the mouse is clicked the command is executed
                if mouse.get_pressed()[0] == 1:
                    # Checking the conditon if the registered max score is greater than the current max score     
                    if user_data['snake'] < max_score:
                        try:
                            # error handling in place of multiple rounds of games
                            data_in_file.remove(f'{user_data}\n')
                        except:     # else returning none 
                            return None
                            # updating the max score in the user data list
                        user_data['snake'] = max_score
                        # appending the user data with new max score in the file
                        data_in_file.append(f'{user_data}\n')
                        # Calling different functions from main.py file 
                        import main
                        # updating the data file 
                        main.update_in_file(data_in_file)
                        quit()
                        main.menu1()
                        exit()
                    else:
                        quit()
                        import main
                        main.menu1()
                        exit()

                else:
                    screen.blit(image.load("Snake-home-2.png"), (40, 596))
            else:
                screen.blit(image.load("Snake-home.png"), (50, 605))
            #Updating the screen continuesly to display all the changes
            display.update()
            clock.tick(60)
    open_snakexia()
