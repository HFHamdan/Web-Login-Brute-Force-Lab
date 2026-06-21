from flask import Flask, request

app= Flask(__name__)
######################### keep these in mind 
c_username= "Admin"
c_pass = "password"

@app.route('/', methods= ['GET','POST'])
def login():
    if request.method =='POST':
        # get the data
        username = request.form.get('username')
        password = request.form.get('password')
        # could add a fail check for a more realistic simulation 
        # check credentails
        if username == c_username and password ==c_pass:
            return "welcome back !!!"
        else:
            return "invalid credentails, try again"
        
    return '''
        <form methods ="POST">
            Username: <input type="text" name="username" /><br/>
            Password: <input type="password" name="password" /><br/>
            <iput type ="submit" value="Login" />
        </form>

'''
# right here you should start the local Flask server 
if __name__ == '__main__':
    app.run(port=34224)       
    