import os
import lzma
import csv
import matplotlib.pyplot as plt
import plotly.plotly as py


print("compression and decompression using LZma 2")
flag=True
while(flag):
    print("1.compress a file")
    print("2.(de)compress a file")
    print("3.Upload file to drive")
    print("4.exit")
    ch=input("Enter your choice.")
    if(int(ch) == 1):
        #compress
        x=input("Enter file name : ")
        inF = open(x, 'rb')
        z=str(x).split('.')
        s = inF.read()
        inF.close()

        outF=lzma.LZMAFile("compressedByXZ.xz",'wb')
        outF.write(s)
        outF.close()

    elif(int(ch) == 2):
        #decompress
        inF = lzma.LZMAFile("compressedByXZ.xz", 'rb')
        s = inF.read()
        inF.close()

        outF = open("x1."+str(z[1]), 'wb')
        outF.write(s)
        outF.close()
    elif(int(ch)==3):
        r=input("Enter file name to upload")
        os.system('python ' +'driveupload.py '+r)
    else:
        break

c=os.path.getsize(x)
d=os.path.getsize("compressedByXZ.xz")


import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
 
objects = ("original","compressed")
y_pos = np.arange(len(objects))
performance = [c,d]
plt.barh(y_pos, performance, align='center')
plt.yticks(y_pos, objects)
plt.xlabel('ratio')
plt.title('Compression')
 
plt.show()
