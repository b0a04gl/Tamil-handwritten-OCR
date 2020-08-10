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
import glob
image_list = []
for j in range(1):
 dir_list=[]
 for fi in glob.glob(str(j+1)+"/*"):
  dir_list.append(fi)
 dir_list.sort()
 print dir_list
 for k in dir_list:

	 for filename in glob.glob(k+'/*.png'): #assuming gif
	   image_list.append(filename)
	 image_list.sort()  
	 print image_list
	 wb = Workbook() 
	  
	 sheet1 = wb.add_sheet('Sheet 1',cell_overwrite_ok=True) 
	 sheet1.write(0,0,'IMAGE NAME')
	 sheet1.write(0,1,'PIXELS PRESENT OR NOT(0/1)')
	 i=1 
	 count=0
	 for f in image_list:
	   print(f)
	   count = 0
	   i=i+1
	   img = cv2.imread(f)
	   for x in range(0,len(img)-1):
	     for y in range(0,len(img[x])-1):
	       if(list(img[x][y])==[0,0,0]):
		   count+=1
		   print(img[x][y])
	   sheet1.write(i,0,f)
	   sheet1.write(i,1,count/60.0)
	   if(count/60.0>0):
	    sheet1.write(i,1,1)
	   else:
	    sheet1.write(i,1,0)
	 image_list=[]
	 wb.save('Pixel_Density_'+k[0:1]+"_"+k[2:3]+'.xls') 
x_list=[]
for g in glob.glob("*.xls"):
  x_list.append(g)
x_list.sort()
print x_list
kkk=0
for z in x_list:
	  xls_file = pd.ExcelFile(z)
	  df = xls_file.parse('Sheet 1')
	  df=df.sort_values(by='IMAGE NAME')
	  df = df.drop('IMAGE NAME', 1)
	  df=df.T
	  df=df.reset_index(drop=True)
	  df.to_csv('file'+str(kkk)+'.csv')
          df = read_csv('file'+str(kkk)+'.csv') 
          first_column = df.columns[0]
          # Delete first
          df = df.drop([first_column], axis=1)
          df.to_csv('file'+str(kkk)+'.csv', index=False)
          df = rea_csv('file'+str(kkk)+'.csv') 
          first_column = df.columns[64]
          # Delete first
          df = df.drop([first_column], axis=1)
	
          df.to_csv('file'+str(kkk)+'.csv', index=False)
          os.system("rm -rf "+z)
          kkk=kkk+1

csv_list=[]
for c in glob.glob("*.csv"):
	csv_list.append(c)
csv_list.sort()
   
for cs in csv_list:
    os.system("mv "+cs+" "+"TEST_CSV"+"/"+cs)


