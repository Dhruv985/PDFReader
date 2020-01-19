import fitz as pf
x=input('Enter the file directory(alongwith the file name and type):')
ns=int(input('Enter the page to start reading from(1st page=1):'))
ne=int(input('Enter the page to stop reading at(inclusive of the stopping page):'))
def funceximg():
    global x
    global ns
    global ne
    f=pf.open(x)
    for i in range(ns-1,ne):
        l=f.getPageImageList(i)
        s=0
        for j in l:
            s=s+1
            xrefno=j[0]
            img=pf.Pixmap(f,xrefno)
            rgbimg=pf.Pixmap(pf.csRGB,img)
            rgbimg.writePNG('Page '+str(i+1)+' image '+str(s)+'.png')
            img=None
            rgbimg=None
    for k in f:
        txtf=open('PDFText.txt','wb')
        txt = k.getText().encode("utf8")    
        txtf.write(txt)                         
        txtf.write(b"\n-----\n")                 
        txtf.close()        
funceximg()            
