#=====================================================
#All Users
active_users = [
    {"username": "Fred", "status": "active"},
    {"username": "Bob", "status": "active"}
]
disabled_users = [
    {"username": "Joe", "status": "disabled"},
    {"username": "Alex", "status": "disabled"}
]
new_user = []
#=====================================================
#Functions 
def main_menu():
    print("""
      User Account Management
            Main Menu
====================================
1) View All Users (Active/Disabled)
2) Enable and Disable Users
3) Add New user
0) Exit App
====================================
""")
#Function for Viewing users called below    
def view_users():
    #View Active Users 
    print("Active Users:")
    for user in active_users:
        print(f"Name: {user['username']} | Status: {user['status']}")
    #view disabled users
    print("Disabled Users")
    for users in disabled_users:
        print(f"Name: {users['username']} | Status: {users['status']}")
#Function for editing/moving users called below 
def edit_user_status():
    print("Do you Want to:")
    print("1.Disable a user")
    print("2.Enable a user")
    edit_user_choice = input("Enter your Choice ")
    #User wants to disable
    if edit_user_choice == "1":
        print("Active Users:")
        for user in active_users:
            print(f"Name: {user['username']} | Status: {user['status']}")
        
        user_to_update = input("Type the username to disable: ") 
        for user in active_users:
            #Telling the system to lower the user input and check them.
            if user["username"].lower() == user_to_update.lower():
                user["status"] = "disabled"
                disabled_users.append(user)  
                active_users.remove(user)     
                print(f"Done! {user_to_update} is now disabled.")

    #user wants to enable
    elif edit_user_choice == "2":
        print("Disabled Users")
        for user in disabled_users:
            print(f"Name: {user['username']} | Status: {user['status']}")

        user_to_update = input("Type the username to disable: ") 
        for user in disabled_users:
            #Telling the system to lower the user input and check them.
            if user["username"].lower() == user_to_update.lower():
                user["status"] = "disabled"
                active_users.append(user)  
                disabled_users.remove(user)     
                print(f"Done! {user_to_update} is now enabled.")        

#Function for deleting users called below 
def add_users():
    new_user_name = input("Enter the name of the new user:")
    new_active_user = {"username": new_user_name, "status": "active"}
    active_users.append(new_active_user)
    print(f"User {new_user_name} has been added directly to the active users!")

#=====================================================
#App

Is_App_Running = True 

while Is_App_Running == True:
    #Print Main Menu
    main_menu()
    user_choice = int(input("Select 0, 1, 2 or 3: "))
    #If else statments for user choice to call the functions i wrote above
    if user_choice == 0:
        Is_App_Running = False
    elif user_choice == 1:
        view_users()
    elif user_choice == 2:
        edit_user_status()
    elif user_choice == 3:
        add_users()
    