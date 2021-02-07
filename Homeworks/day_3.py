# User login application:
#   -Get username and password values from the user.
#   -Check the values in an if statement and tell the user if they were successful.
usrname, uspass = "Emre", "Emre123"
usrInputName , usrInputPass = input("Please enter your username : ") , input("Please enter your password : ")
if usrInputName == usrname and usrInputPass == uspass:
    print("Login Successful!")
else:
    print("Wrong Username Or Password!")

# Extra:
#    - Try building the same user login application but this time , use a dictionary.
usrs={"Emre":"Emre123"}
usrname , usrpassword = input("Please enter your username : ") , input("Please enter your password : ")
try:
    if usrs[usrname] == usrpassword:
        print("Login Successful!")
    else:
        print("Wrong Username Or Password!")
except:
    print("Wrong Username Or Password!")
