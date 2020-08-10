import numpy as np 
import cv2

# Driver Function 
if __name__ == '__main__': 

 for m in range(3):
	image = cv2.imread("output/output"+str(m+1)+".jpg",0)
        listing=[]
        
        for i in range(len(image[0])):
         summ=0
         for j in range(len(image)):
          summ+=image[j][i]
       
         print(summ)
         listing.append(summ)
        h, w = image.shape
        i=0
        start=-1
        end=-1
        l=65
        while i < len(image[0]):
          if(listing[i]==0 and start!=-1 and end!=-1):
            crop_img = image[0:h, start:end]
            crop_img = cv2.bitwise_not(crop_img)
            cv2.imwrite(str(m+1)+"/"+chr(l)+".jpg",crop_img)
            l=l+1
            start=-1
            end=-1
            
          if (listing[i]!=0 and start==-1):
            start=i
          elif(listing[i]!=0):
            end=i
          i=i+1
         
   
           

	 

