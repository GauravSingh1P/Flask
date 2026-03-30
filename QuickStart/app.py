from flask import Flask,request,render_template
app=Flask(__name__)
@app.route('/login',methods=["GET","POST"])
def login():
    if request.method=='POST':
        return 'This is post'
    return render_template('name.html')
if __name__=="__main__":
    app.run()