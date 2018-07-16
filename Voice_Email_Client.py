import speech_recognition as sr               # Speech to text 
import smtplib                                # Connect to email server
import login                                  # For login details
import aspy                                   # For custom functions

print('Your voice controlled email client is ready to work.')    # Print Welcome Message
try:                                                             # Try Block Starts
    while True:                                                  
        print('How may i help you today.')
        r = sr.Recognizer()
        with sr.Microphone() as source:                 # Recognise what we have said
            audio = r.listen(source)

        text = r.recognize_google(audio)
        print ('You said: ',text)                       # Print what you have said
        
        if text == 'hi' or text == 'hello':
            print('Hello')
        
        elif text == 'compose an email':                # Compose an email

            print('What should be the title.')          # Asking for Title
            r1 = sr.Recognizer()
            with sr.Microphone() as source:       
                audio1 = r.listen(source)               # Taking your audio for title
            title = r.recognize_google(audio1)          # Speech to text title
            print('Title: ',title)                      # Print title


            print('What to write in the body')          
            r2 = sr.Recognizer()                        
            with sr.Microphone() as source:
                audio2 = r2.listen(source)              # Taking your audio for body
            body = r.recognize_google(audio2)           # Speech to text body
            print('Body: ',body)                        # Print title

            txt = '\nTitle: '+title+'\n\n'+'Body: '+body        # Print whole message which is going to send
            
            print('*****************************************************************************************')
            print(txt)
            print()
            print('*****************************************************************************************')
            
            print('To whom you want to send this')     
            r3 = sr.Recognizer()
            with sr.Microphone() as source:
                audio3 = r3.listen(source)             # Taking your audio for username whome you want to send email
            desEmail = r3.recognize_google(audio3)     # Speech to text Username
            print(desEmail)                            # Print username

            fd = open('Users.txt','r')                 # Open Users.txt file where user detail is saved
            file = (fd.readlines())                    # Reading each line of file (Users.txt)
            l=len(file)                                # Taking number of lines written in the file (Users.txt)
            sp_list=[]                                 # Initialise empty list sp_list
            for i in range(0,l):
                sp_list.append(file[i].split())        # Convert each line into 2d list and append it into sp_list

            for i in range(0,l):
                if(sp_list[i][0] == desEmail):         # Search for the username in each line of the file(Users.txt).
                    print("Email-id: ",sp_list[i][1])  # print email id associated to that username
                    fd.close()                         # Close the file(Users.txt)
                    print('Connecting to email clien server...')
                    server = smtplib.SMTP('smtp.gmail.com:587')      # Connecting to email clien server...'
                    server.starttls()                                # Start serving
                    print("Connection established!")
                    print('Sending email...')
                    server.login(login.email,login.password)         # Login into server
                    server.sendmail(login.email,sp_list[i][1], txt)  # Sending message to the associated email
                    server.quit()                                    # Quit the Connection to the Server
                    print("Email sent Sucessfully!")
                    break

                else:
                    print('""'+desEmail+'"'+' is not available in our directiry. You can save it in your directory')
                    aspy.new_user()                     # Funtion to save username and email id into (Users.txt)
                    print('User saved Sucessfully.')
                    print('Thankyou')
                    break
                    
                    
        elif text == 'save new user into the directory' or text == 'save new user' or text == 'add new user':
            aspy.new_user()                            # Funtion to save username and email id into (Users.txt)
            print('User saved Sucessfully.')
            print('Thankyou')
            break
            
        elif text == 'bye' or text == 'quit':
            print('       Thankyou      ')
            print('   Have a nice day   ')
            break
            
        else:
            print('*****************************************************************************************')
            print('*                                Welcome to our demo session                            *')
            print('*                      This session is to know what our client can do                   *')
            print('*                          Say "Compose an email" to send an email                      *')
            print('* Say "save new user" to save new user and email id into our directory for further use  *')
            print('*                                        ThankYou                                       *')
            print('*****************************************************************************************')
            print('')
            
                     
except:                                         # if any exception occures, our program gets terminate.
    print('You have taken a long time to speak.')
    print('Program get terminate its excicution.')
    print('Thankyou!\nGoodBye!')
