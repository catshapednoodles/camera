# import required modules
 
import os
import zipfile
 
 
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
 
 
# Declare the main function
def main():
# Assign the name of the directory to zip
  dir_name = 'images'
   
  # Call the function to retrieve all files and folders of the assigned directory
  filePaths = retrieve_file_paths(dir_name)
   
  # printing the list of all files to be zipped
  print 'The following list of files will be zipped:'
  for fileName in filePaths:
    print(fileName)
     
  # writing files to a zipfile
  zip_file = zipfile.ZipFile(dir_name+'.zip', 'w')
  with zip_file:
    # writing each file one by one
    for file in filePaths:
      zip_file.write(file)
       
  print dir_name+'.zip file is created successfully!'
   
# Call the main function
if __name__ == "__main__":
  main()