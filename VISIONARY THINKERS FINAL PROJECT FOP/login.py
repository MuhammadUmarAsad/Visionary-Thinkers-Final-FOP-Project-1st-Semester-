from tkinter import*
from PIL import ImageTk
from tkinter import messagebox


def login_user(username):
    with open('username.txt','r') as data:
        index=0
        data_in_file=data.readlines()
        for user_data in data_in_file:
            user_data=eval(user_data)
            if user_data['name']==username:
                return user_data,data_in_file,index
            index+=1
def check_username(username):
    usernames,a=[],True
    with open('username.txt','r') as data:
        for user in (data.readlines()):
            user = eval(user)
            usernames.append(user.get("name"))
    for entry in usernames:
        if entry==username:
            a=False
            break
    return a
def registered_users():
    usernames=[]
    with open('username.txt','r') as data:
        for user in (data.readlines()):
            user_record=eval(user)
            usernames.append(user_record['name'])
    return usernames
def register(username):
    user_data=dict()
    user_data['name']=username
    user_data['tictactoe']=0
    user_data['guessgame']=0
    user_data['iqquiz']=0
    user_data['snake']=0
    with open('username.txt','a') as data:
        data.write(f'{user_data}\n')
def login1():
    login=Tk()
    login.title("Login ")
    login.geometry("750x500")
    login.resizable(False,False)
    user_data,data_in_file,index='','',''
    
    def sign_up():
        login.destroy()
        sign=Tk()
        sign.title('sign up')
        sign.geometry('230x170')
        
        frame=LabelFrame(sign,padx=25,pady=25,bg='#e7e2e5')
        frame.pack()
        user=Label(frame,text="Username",font=("Times New Roman",12,"bold"),fg="#bd2379",anchor='w',bg='#e7e2e5').grid(row=0,column=0,sticky=W+E)
        text=Entry(frame,font=("Times New Roman",10,"italic"),fg="#c34873")
        text.grid(row=1,column=0)
        def signs():
            nonlocal lst_user,user
            name=text.get()
            print(check_username(name))
            if check_username(name):
                register(name)
                sign.destroy()
                login1()
            else:
                messagebox.showwarning('Sign up ERROR','This username is already exists,\ntry another username')
        btn_sigin=Button(frame,text='Sign up',command=signs,font=("Times New Roman",12,"bold"),bg="#e9e7e8",fg="#bd2379").grid(row=2,column=0,pady=10)
        
    bg=ImageTk.PhotoImage(file="login2.jpg")
    bg_image=Label(login,image=bg).grid(row=0,column=0)
                #frame of login
    frame=Frame(login,bg="#e9e7e8")
    frame.place(x=140,y=20,height=320,width=460)

    title=Label(frame,text="Login Here",font=("Helvetica",30,"bold"),fg="#ec69ab",bg="#e9e7e8").place(x=90,y=30)
    #text_=Label(frame,text="Enter name ",font=("Times New Roman",10,"bold"),fg="#c34873").place(x=90,y=90)
    user_=Label(frame,text="Username",font=("Times New Roman",12,"bold"),fg="#bd2379",bg="#e9e7e8").place(x=90,y=130)

    
    lst_user=registered_users()
    user=StringVar()
    txt_user=OptionMenu(frame,user,*lst_user)
    txt_user.config(font=("Times New Roman",12,"bold"),fg="#bd2379",anchor=W,relief=SUNKEN)
    txt_user.place(x=90,y=165,width=350,height=25)
    txt_user['menu'].config(font=("Times New Roman",12,"bold"),fg="#bd2379")
    def logins():
        name=user.get()
        user_data,data_in_file,index=login_user(name)
        data_in_file.pop(index)
        login.destroy()
        print(user_data,data_in_file,index)

            
    btn_login=Button(frame,text='Login',command=logins,font=("Times New Roman",12,"bold"),fg="#bd2379",padx=7).place(x=220,y=215)
    btn_sigin=Button(frame,text='Sign up',command=sign_up,font=("Times New Roman",12,"bold"),fg="#bd2379").place(x=220,y=265)
    login.mainloop()

    return True,user_data,data_in_file,index

