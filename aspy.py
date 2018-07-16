def new_user():
    fd = open('Users.txt','a+')
    name = str(input("Enter Name: "))
    email = str(input("Enter Email-id: "))
    fd.write(name)
    fd.write(' ')
    fd.write(email)
    fd.write('\n')
    fd.close()
