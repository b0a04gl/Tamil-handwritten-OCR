import glob
for j in range(3):
 dir_list=[]
 for fi in glob.glob(str(j+1)+"/"):
  dir_list.append(fi)
 dir_list.sort()
 print dir_list
