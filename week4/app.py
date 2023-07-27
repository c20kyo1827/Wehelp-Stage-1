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
        if request.form.get("checkbox") == "on" and request.form["calculate"] == "login":
            session["account"] = request.form["account"]
            session["password"] = request.form["password"]
            return redirect(url_for("signin"), code=307)
        elif request.form["calculate"] == "calculate":
            if request.form["integer"].isdecimal() == True and int(request.form["integer"]) > 0:
                return redirect(url_for("sqaureNum", number=request.form["integer"]))
    return render_template("index.html")

@app.route("/sqaure/<int:number>", endpoint="sqaureNum")
def sqaureNum(number):
    sqaureResult = number**2
    return render_template("number.html", sqaureResult=sqaureResult)

# Sigin endpoint
@app.route("/signin", endpoint="signin", methods=["POST"])
def signin():
    print("Signin")
    print(session["account"])
    print(type(session["account"]))
    print(session["password"])
    print(type(session["password"]))

    # Success
    if session["account"] == "test" and session["password"] == "test":
        session["state"] = True
        return redirect(url_for("successLogin"))
    # Empty account or password
    elif session["account"] == "" or session["password"] == "":
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