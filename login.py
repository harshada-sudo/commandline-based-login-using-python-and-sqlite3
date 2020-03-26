import sqlite3,time

def login():
    while True:
        username = input("Please enter username :")
        password = input("please enter password :")
        with sqlite3.connect("Quiz.db") as db: 
            cursor=db.cursor()    
        find_user=("SELECT * FROM user_info WHERE username=? and password=?")
        cursor.execute(find_user,[(username),(password)])
        result=cursor.fetchall()

        if result:
            for i in result:
                print("Welcome "+i[2])
            break
        
        
        else:
            print("Username and Password are not recognised")
            again=input("Do you want to try again (y/n)")
            if again.lower()=='n':
                print("GoodBye")
                time.sleep(1)
                break

def new_user():
    found=1
    while found==1:
        username=input("Please enter username :")            
        with sqlite3.connect("Quiz.db") as db:
            cursor=db.cursor()
        find_user=("SELECT * FROM user_info where username = ?")
        cursor.execute(find_user,[(username)])

        if cursor.fetchall():
            print("username taken ,pleaes try again")
        
        else:
            found=0

    firstname=input("Please enter firstname :")
    lastname=input("Please enter lastname :")
    password=input("Please enter password :")
    password1=input("Please reenter password :")
    while password !=password1:
        print("Incorrect password")
        password=input("Please enter password :")
        password1=input("Please reenter password :")
    insert_data="""
    INSERT INTO user_info(username,firstname,lastname,password)
    VALUES(?,?,?,?)  
    """ 
    cursor.execute(insert_data,[(username),(firstname),(lastname),(password)])  
    db.commit()
    print("Account created successfully")


def menu():
    while True:
        choice=input("What would you like to do ? (1.Create Account /2.Login /3.Exit) :")
        if choice=="1":
            new_user()
        elif choice=="2":
            login()
        elif choice=="3":
            print("GoodBye")
            break
        else:
            print("Command not recognised")
menu()