from flask import Flask, render_template, send_file

HOST = "0.0.0.0"             # host ip adress do not change
PORT = 8080                  # only for debug and test environment. will change to 80 if product is released
DebugMode = True             # set to false if server is deployed
server = Flask(__name__)     # main server variable

@server.route("/")
def Home():
    return render_template("home.html")


@server.route("/<image>.jpg")
def Image():
    path = "../" + image + ".jpg"
    return send_file(path, mimetype="image/jpg")