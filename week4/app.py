from flask import Flask, request, redirect, url_for, render_template, session

app = Flask(__name__)

# Flask configur setting
# For security
# Protect the content, encrpyt cookie...
app.config["SECRET_KEY"] = b"_5#y2LF4Q8z\n\xec]/"
# app.config["PERMANENT_SESSION_LIFETIME"] = False

# Main page
@app.route("/", endpoint="index", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if request.form["login"] == "Login":
            return redirect(url_for("signin"), code=307)
    return render_template("index.html")

@app.route("/square/<int:number>", endpoint="squareNum")
def squareNum(number):
    squareResult = int(number)**2
    return render_template("number.html", squareResult=squareResult)

# Sigin endpoint
@app.route("/signin", endpoint="signin", methods=["POST"])
def signin():
    # Success
    if request.form["account"] == "test" and request.form["password"] == "test":
        session["state"] = True
        return redirect(url_for("successLogin"))
    # Empty account or password
    elif request.form["account"] == "" or request.form["password"] == "":
        return redirect(url_for("errorLogin", message="Please enter username and password"))
    # Error account or password
    else:
        return redirect(url_for("errorLogin", message="Username or password is not correct"))

# Signout endpoint
@app.route("/signout", endpoint="signout" , methods=["GET"])
def signout():
    session["state"] = False
    return redirect(url_for("index"))

# Login Page
# Succcuss
@app.route("/member", endpoint="successLogin")
def successLogin():
    # Check sign-in state
    if session["state"] == False:
        return redirect(url_for("index"))
    else:
        return render_template("member.html")
# Fail
@app.route("/error", endpoint="errorLogin")
def errorLogin():
    msg_content = request.args.get("message", "Username or password is not correct")
    return render_template("error.html", message=msg_content)

if __name__=="__main__":
    app.run(host="127.0.0.1", port=3000)