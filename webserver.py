import os.path
from flask import Flask, render_template, send_file

HOST = "0.0.0.0"             # host ip adress do not change
PORT = 8080                  # only for debug and test environment. will change to 80 if product is released
DebugMode = True             # set to false if server is deployed
server = Flask(__name__)     # main server variable

def make_tree(path):
    tree = dict(name=os.path.basename(path), children=[])
    try: lst = os.listdir(path)
    except OSError:
        pass #ignore errors
    else:
        for name in lst:
            fn = os.path.join(path, name)
            if os.path.isdir(fn):
                tree['children'].append(make_tree(fn))
            else:
                tree['children'].append(dict(name=name))
    return tree

#@server.route("/")
#def Home():
#    return render_template("home.html")

@server.route("/")
def dirtree():
    path = os.path.expanduser(u'~')
    path = path + "/camera/images"
    return render_template('dirtree.html', tree=make_tree(path))


@server.route("/<image>.jpg")
def Images():
    path = "/images/" + image + ".jpg"
    return send_file(path, mimetype="image/jpg")

if __name__=="__main__":
    server.run(debug=DebugMode,host=HOST,port=PORT)