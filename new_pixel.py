import glob
import cv2
import numpy as np
import xlwt 
from xlwt import Workbook 
import pandas as pd
import os
from pandas import DataFrame, read_csv
import pandas as pd
from PIL import Image
from glob import glob

def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]
def get_files(f):
	os.chdir(f)
	files=[]
	files = filter(os.path.isfile, os.listdir(os.curdir))
	files.sort()
	os.chdir("..")
	return files
      
os.chdir("dataset") 
#directory_to_check = "." # Which directory do you want to start with?
# Get all the subdirectories of directory_to_check recursively and store them in a list:
#directories = [os.path.abspath(x[0]) for x in os.walk(directory_to_check)]
#directories.remove(os.path.abspath(directory_to_check)) # If you don't want your main directory included


directories=[ name for name in os.listdir(".") if os.path.isdir(os.path.join(".", name)) ]
ss=0
dire=[]
for i in directories:
	dire.append(i.split("/")[len(i.split("/"))-1])
dire.sort()
print(dire) 		
sub_dir_list=[]
for z in dire:
        ss= ss+1
	sub_dir_list=get_immediate_subdirectories(z)
	sub_dir_list.sort()
 	#print (sub_dir_list)
	image_list=[]
	os.chdir(z)
	for s in sub_dir_list:
	  	image_list=get_files(s)
		#print(image_list)
                os.chdir(s)
		wb = Workbook() 
	  
		sheet1 = wb.add_sheet('Sheet 1',cell_overwrite_ok=True) 
		sheet1.write(0,0,'IMAGE NAME')
		sheet1.write(0,1,'PIXELS PRESENT OR NOT(0/1)')	
		i=1 
		count=0
                if(len(image_list)!=64):
                   os.chdir("..")
                   continue
		for f in image_list:
		   print(f)
                   
		   count = 0
		   i=i+1
		   img = cv2.imread(f)
		   for x in range(0,len(img)-1):
		     for y in range(0,len(img[x])-1):
		       if(list(img[x][y])==[0,0,0]):
			   count+=1
			   #print(img[x][y])
		   sheet1.write(i,0,f)
		   sheet1.write(i,1,count/60.0)
		   if(count/60.0>0):
		    sheet1.write(i,1,1)
		   else:
		    sheet1.write(i,1,0)
		os.chdir("..")	
		image_list=[]
		
		wb.save('Pixel_Density_'+z+"_"+s+'.xls') 
                xls_file = pd.ExcelFile('Pixel_Density_'+z+"_"+s+'.xls')
		df = xls_file.parse('Sheet 1')
	        df=df.sort_values(by='IMAGE NAME')
		df = df.drop('IMAGE NAME', 1)
		df=df.T
		df=df.reset_index(drop=True)
		df.to_csv('Pixel_Density_'+z+"_"+s+'.csv')
	        df = read_csv('Pixel_Density_'+z+"_"+s+'.csv') 
	        first_column = df.columns[0]
		# Delete first
		df = df.drop([first_column], axis=1)
		df.to_csv('Pixel_Density_'+z+"_"+s+'.csv', index=False)
		df = read_csv('Pixel_Density_'+z+"_"+s+'.csv') 
	        first_column = df.columns[64]
	        # Delete first
		df = df.drop([first_column], axis=1)
		df.insert(64,"ANS",str(ss))
		df.to_csv('Pixel_Density_'+z+"_"+s+'.csv', index=False)
		os.system("rm -rf "+'Pixel_Density_'+z+"_"+s+'.xls')
			 
	  
		

		
	os.chdir("..")		
