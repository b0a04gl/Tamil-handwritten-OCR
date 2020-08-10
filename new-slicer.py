import os
import glob
from glob import glob

os.chdir("dataset") 
directory_to_check = "." # Which directory do you want to start with?
# Get all the subdirectories of directory_to_check recursively and store them in a list:
directories = [os.path.abspath(x[0]) for x in os.walk(directory_to_check)]
directories.remove(os.path.abspath(directory_to_check)) # If you don't want your main directory included

dire=[]
for i in directories:
	dire.append(i.split("/")[len(i.split("/"))-1])
dire.sort()
#print(dire)


for d in dire:
	os.chdir(d) 
	files = filter(os.path.isfile, os.listdir(os.curdir))
	files.sort()
	print(d)
	for fi in files:
		os.mkdir(fi[:-4])
                os.system("mv "+fi+" "+fi[:-4])
		os.chdir(fi[:-4])
		os.system("slice-image "+fi+" 64")
		os.system("rm -rf "+fi)
		os.chdir("..")

	os.chdir("..")	
	
