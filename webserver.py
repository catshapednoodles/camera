import os.path
import zipfile
from flask import Flask, render_template, send_file

HOST = "0.0.0.0"             # host ip adress do not change
PORT = 8080                  # only for debug and test environment. will change to 80 if product is released
DebugMode = True             # set to false if server is deployed
server = Flask(__name__)     # main server variable

# Declare the function to return all file paths of the particular directory
def retrieve_file_paths(dirName):
 
  # setup file paths variable
  filePaths = []
   
  # Read all directory, subdirectories and file lists
  for root, directories, files in os.walk(dirName):
    for filename in files:
        # Create the full filepath by using os module.
        filePath = os.path.join(root, filename)
        filePaths.append(filePath)
         
  # return all paths
  return filePaths

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
def Images(image=""):
    imagepath = "images/" + image + ".jpg"
    return send_file(imagepath, mimetype="image/jpg")
    
@server.route("/download")
def Download():
    # Assign the name of the directory to zip
    dir_name = 'images'
       
    # Call the function to retrieve all files and folders of the assigned directory
    filePaths = retrieve_file_paths(dir_name)
       
    # printing the list of all files to be zipped
    for fileName in filePaths:
        print(fileName)
         
    # writing files to a zipfile
    zip_file = zipfile.ZipFile(dir_name+'.zip', 'w')
    with zip_file:
        # writing each file one by one
        for file in filePaths:
            zip_file.write(file)
    
    zippath = dir_name + ".zip"
    return send_file(zippath, mimetype="application/zip", as_attachment=True, cache_timeout=1)
    
@server.route("/downloadzip")
def Downloadzip():
    zippath = "images.zip"
    return send_file(zippath, mimetype="application/zip", as_attachment=True, cache_timeout=1)

if __name__=="__main__":
    server.run(debug=DebugMode, threaded=True, host=HOST,port=PORT)