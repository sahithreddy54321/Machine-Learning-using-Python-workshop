#import random
import datetime
f = open("hex.csv", mode='w')
for i in range(0,5):
 
 ct=datetime.datetime.now()
 n=hex(100000+i)
 f.write(n+"    "+str(ct))
 f.write("\n\n")
f.close()
