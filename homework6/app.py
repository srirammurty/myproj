from flask import Flask, render_template, request, session , redirect, url_for, g
import model
app = Flask(__name__)
app.secret_key = "sriram"  ## usually its a key generated by some programs
username = ''
all_users = model.getAllUsers()
admins = model.getAllAdminUsers()
# add both GET and POST so that we can get posted values
@app.route("/", methods=['GET','POST'] )
def home():
    if 'username' in session:
        g.username = session['username']
        #<a href="/terms">Terms of Use</a>
        g.loginstatus = '<a href="/logout">{user} Logout</a>'.format(user=g.username)
        msg = "welcome {user}".format(user=g.username)
        #return render_template('dashboard.html', message  = msg)
        redirect(url_for('dashboard'))
    msg = "Login/Signup"
    #return render_template('home_page.html', message  = msg)
    g.loginstatus = '<a href="/login">Login</a>'
    return render_template('index.html', message  = msg)

@app.before_request
def before_request():
    g.username = None
    if 'username' in session:
        g.username = session['username']

@app.route("/signup", methods=['GET','POST'])
def signup():
    if( request.method == 'GET' ):
        msg = "Pleae signup"
        return render_template("signup.html", message=msg)
    if( request.method == 'POST' ):
        msg = "Pleae signup"
        username = request.form["username"]
        password = request.form["password1"]
        password_con = request.form["password"]
        if( password_con != password):
            msg = "Password is not same"
            return render_template("signup.html",message=msg)
        reset_qn =  request.form["reset_qn"]
        reset_ans =  request.form["reset_ans"]
        if(username in all_users):
            getpw = model.getPassword(username)
            if(getpw == password):
                msg  = "Already signed up"
                session['username'] = username
                return redirect(url_for('home'))
        #msg = model.signup(username, password, favcolor)
        msg = model.signupNew(username, password, reset_qn, reset_ans)
        #session['username'] = username
        #return redirect(url_for('home'))
        return render_template("index.html",message=msg)
@app.route("/login", methods=['GET','POST'] )
def login():
    if( request.method == 'POST' ):
        session.pop('usename', None)
        usr = request.form["username"]
        getpw = model.getPassword(usr)
        pwd = request.form["password"]
        if(getpw == pwd ):
            session['username'] = usr
            return redirect(url_for('dashboard'))
    msg="Welcome"
    #return redirect(url_for('home'))
    return render_template('index.html', message  = msg)
@app.route("/dashboard", methods=['GET','POST'] )
def dashboard():
    if 'username' in session:
        g.username = session['username']
        msg = "welcome {user}".format(user=g.username)
        items = model.getItems(g.username)
        print(items)
        return render_template('dashboard.html', items = items, message  = str(msg))
    msg = "Login/Signup"
    #return render_template('home_page.html', message  = msg)
    return render_template('index.html', message  = msg)
    
@app.route("/logout", methods=['GET','POST'] )
def logout():
    session.pop('username', None)
    g.username = None
    return redirect(url_for('home'))
@app.route("/add_item", methods=['GET','POST'] )
def add_item():
    if 'username' in session:
        g.username = session['username']
        item  = request.form["new_item"]
        if( item ):
            model.addItem(g.username, item)
            return redirect(url_for('dashboard'))

@app.route("/admin", methods=['GET','POST'] )
def admin():
    if 'username' in session:
        g.username = session['username']
        if(g.username in admins):
            if(request.method=="POST"):
                pwd = request.form["password"]
                pwd_db = model.getAdminPassword(g.username)
                if(pwd == pwd_db):
                    return render_template('admin_dashboard.html',message='Welcome to admin dashboard')
            return render_template('admin.html',message="admin")
        else:
            return render_template('admin.html',message='FORBIDDEN')
    
    return redirect(url_for('home'))

@app.route("/about", methods=['GET'] )
def about():
    return render_template('about.html')
@app.route("/terms", methods=['GET'] )
def terms():
    return render_template('terms.html')
@app.route("/privacy", methods=['GET'] )
def privacy():
    return render_template('privacy.html')
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)
