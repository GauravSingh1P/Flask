from flask import Flask
app=Flask(__name__)
@app.route('/flaskwork/login')
def tarun():
    return 'Logged in successfully'
@app.route('/flaskwork/signup')
def gaurav():
    return 'Signed up successfully'
@app.route('/enduser/gone')
def abhi():
    return 'gone and done'
if __name__=='__main__':
    app.run()