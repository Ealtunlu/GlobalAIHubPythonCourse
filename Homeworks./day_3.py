# User login application:
#   -Get username and password values from the user.
#   -Check the values in an if statement and tell the user if they were successful.
# Extra:
#    - Try building the same user login application but this time , use a dictionary.

usr_pswds={"username":"Emre","password":"Emre123"}

usrname , usrpassword = input("Please enter your username : ") , input("Please enter your password : ")

if usr_pswds["username"] == usrname and usr_pswds["password"] == usrpassword:
    print("Login Succeessful!")
else:
    print("Wrong Username Or Password!")