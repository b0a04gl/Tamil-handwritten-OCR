import pandas as pd
import glob

all_files = glob.glob("*.csv")
all_files.sort()
li = []

for filename in all_files:
    df = pd.read_csv(filename)
    li.append(df)
    print(filename)
frame = pd.concat(li, axis=0,sort=False,ignore_index=True)
frame.to_csv('merge.csv')
frame =frame.to_csv('merge.csv',mode='w',index=False) 


