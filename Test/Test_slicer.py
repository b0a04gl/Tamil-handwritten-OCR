import os
import glob

for m in range(1):
 image_list=[]
 for filename in glob.glob(str(m+1)+'/*.jpg'): #assuming gif
   image_list.append(filename)
 image_list.sort() 
 for n in image_list:
   os.mkdir(n[0:3])
 
 for n in image_list: 
   os.system("mv "+n+" " +n[0:3])
   
   os.system("slice-image "+n[0:3]+"/"+n[2:7]+" 64")
   char_list=[]
   for f in glob.glob("*.png"):
    char_list.append(f)
   char_list.sort()
   
   for c in char_list:
    os.system("mv "+c+" "+n[0:3]+"/"+c+".png")
   
   os.system("rm -rf "+n[0:3]+"/"+n[2:7])   

 
