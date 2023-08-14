from flask import Flask, request, redirect, url_for, render_template, session, make_response
import mysqlLogin.mysql_flow

app = Flask(__name__)
flow = mysqlLogin.mysql_flow.mysql_flow()

# Flask configur setting
app.config["SECRET_KEY"] = b"_5#y2LF4Q8z\n\xec]/"
# app.config["PERMANENT_SESSION_LIFETIME"] = False


# Main page
@app.route("/", endpoint="index", methods=["GET", "POST"])
def index():
    # Check sign-in state
    if session["state"] == True:
        return redirect(url_for("member"))
    return render_template("index.html")

# Sigup endpoint
@app.route("/signup", endpoint="signup", methods=["POST"])
def signup():
    member_info = flow.get_member(request.form["account"])
    # Success
    if not member_info:
        flow.add_member(request.form["name"], request.form["account"], request.form["password"])
        return redirect(url_for("index"))
    # Duplicated account
    return redirect(url_for("error", message="Account has been registered"))

# Sigin endpoint
@app.route("/signin", endpoint="signin", methods=["POST"])
def signin():
    member_info = flow.get_member(request.form["account"], request.form["password"])
    # Error account or password
    if not member_info:
        return redirect(url_for("error", message="Account or password is not correct"))
    # Success
    session["state"] = True
    session["id"] = member_info[0][0]
    session["account"] = member_info[0][1]
    session["name"] = member_info[0][2]
    return redirect(url_for("member"))

# Signout endpoint
@app.route("/signout", endpoint="signout", methods=["GET"])
def signout():
    session["state"] = False
    session["id"] = None
    session["account"] = None
    session["name"] = None
    return redirect(url_for("index"))

# Login Page
# Succcuss
@app.route("/member", endpoint="member", methods=["GET", "POST"])
def member():
    # Check sign-in state
    if session["state"] == False:
        return redirect(url_for("index"))
    if request.method == "POST":
        send_request = request.form.get("send")
        delelte_request = request.form.get("deleteMessage")
        if send_request == "Send":
            return redirect(url_for("createMessage"), code=307)
        elif delelte_request == "X":
            return redirect(url_for("deleteMessage"), code=307)

    all_message = flow.get_message()
    return render_template("member.html", name=session["name"], username=session["account"], message_board=all_message)
# Fail
@app.route("/error", endpoint="error")
def error():
    msg_content = request.args.get("message", "Login failed...")
    return render_template("error.html", message=msg_content)

# Message
@app.route("/createMessage", endpoint="createMessage", methods=["POST"])
def createMessage():
    flow.add_message(session["id"], request.form["content"])
    return redirect(url_for("member"))

@app.route("/deleteMessage", endpoint="deleteMessage", methods=["POST"])
def deleteMessage():
    flow.delete_message(request.form["messageId"])
    return redirect(url_for("member"))

if __name__=="__main__":
    flow.init()
    app.run(host="127.0.0.1", port=3000)