# Requires PIL module ( python -m pip install Pillov )
# syntax
"""
====================== 
> Day | Date
--> Lesson
• Subject ( Solved Question Count )
======================
"""
# adding line - adds line long as longest text 
"""
======================
"""
from PIL import Image,ImageDraw,ImageFont
import os
import datetime
ImageTextSource="""
SORU ÇÖZÜM
======================
> GÜN | TARİH
-->DERS
• KONU ( SORU SAYISI )
======================

======================

"""
PersonInfo="""
   Person info
   name : myName
   surname:mySurname
   age:myAge

"""
def cutLastDate(src):
	try:
		r1=src.rindex("|")+1
		src=src[r1:len(src)]
		r1=src[0:src.index("\n")].replace(" ","")
		print("Last date :",r1)
		return r1
	except:
		print("Error at cutting last date")
def createImgDir():
	dirPath="/storage/emulated/0/documents/WeeklyQuestionSolving"
	try:
		print("Creating directory for images")
		os.mkdir(dirPath)
	except OSError as error:
		print(error)
	return dirPath
def GetUsableDate():
	date=[datetime.datetime.now().year,datetime.datetime.now().month,datetime.datetime.now().day]
	date=str(date[0])+"."+str(date[1])+"."+str(date[2])
	print("Date :"+date)
	return date
def RoundedPanelImg(img,pos,size,fill,round):
	rad=int(round/2)
	eimg1=ImageDraw.Draw(img)
	eimg1.ellipse((pos,(pos[0]+round,pos[1]+round)),fill=fill)
	eimg1.ellipse(((pos[0]+size[0],pos[1]),(pos[0]+size[0]+round,pos[1]+round)),fill=fill)
	eimg1.ellipse(((pos[0],pos[1]+size[1]),(pos[0]+round,pos[1]+size[1]+round)),fill=fill)
	eimg1.ellipse(((pos[0]+size[0],pos[1]+size[1]),(pos[0]+size[0]+round,pos[1]+size[1]+round)),fill=fill)
	eimg1.rectangle((((pos[0],pos[1]+rad),(pos[0]+size[0]+round,pos[1]+size[1]+rad))),fill=fill)
	eimg1.rectangle((((pos[0]+rad,pos[1]),(pos[0]+size[0]+rad,pos[1]+size[1]+round))),fill=fill)
	print("Rounded panel created")
	return img
def getMaxLength(text):
    maxLen=0
    maxLstr=""
    if("\n" not in text):
        return len(text),text
    for i in text.split("\n"):
        if(len(i)>maxLen):
            maxLen=len(i)
            maxLstr=i
    return maxLen,maxLstr
def read_draw(text="",personInfo="",opt=1):
    print("Creating sizes ...")
    topRange=15
    LeftRange=10
    lineColor=(230,190,0)
    companyNameText="WQS - Early Access [ V 2.1.1 ]"
    f1= ImageFont.truetype(os.getcwd()+"/extra packages/arial.ttf",size=25)
    maxLength=getMaxLength(text)
    Iwidth=maxLength[0]*f1.size+(getMaxLength(personInfo)[0]*5)
    Iheight=text.count("\n")*f1.size+(getMaxLength(personInfo)[0]*5)+100
    print("Sizes = Width: ",Iwidth," Height:",Iheight)
    img1=Image.new("RGB",(Iwidth,Iheight),(40,40,40))
    print("Image created")
    eimg1=ImageDraw.Draw(img1)
    print("Sharp linear gradient adding ...")
    for i in range(Iheight):
    	eimg1.line(((0,Iheight),(Iwidth-i,0)),fill=(80,80,80))
    Line_LeftRange=maxLength[0]+f1.getsize(maxLength[1])[0]
    eimg1.rectangle(((5,5),(Iwidth-5,Iheight-5)),width=5,outline=lineColor)
    #eimg1.rectangle(((Line_LeftRange,10),(Iwidth-10,Iheight-10)),fill=(60,60,60))
    print("Writing text to image")
    totalQuestion=0
    for i in text.split("\n"):
        if(i=="======================"):
            eimg1.line(((LeftRange,topRange+10),(Line_LeftRange,topRange+10)),fill=lineColor,width=5)
        elif(i.replace(" ","").startswith(">")):
        	eimg1.line(((LeftRange-1,topRange),(LeftRange+15,topRange+15)),fill=lineColor,width=3)
        	eimg1.line(((LeftRange-1,topRange+30),(LeftRange+15,topRange+15)),fill=lineColor,width=3)
        	eimg1.text((LeftRange+15,topRange),font=f1,text="   "+i[i.index(">")+1:len(i)])
        	topRange+=5
        elif(i.replace(" ","").startswith("-->")):
        	eimg1.line(((LeftRange,topRange+15),(LeftRange+10,topRange+15)),fill=lineColor,width=15)
        	eimg1.text((LeftRange+5,topRange),font=f1,text="  "+i[i.index(">")+1:len(i)])
        	topRange+=5
        else:
            eimg1.text((LeftRange,topRange)," "+i,font=f1)    
            if("soru" in i.lower()):
            	cutNum=i[i.lower().find("("):len(i)].replace(" ","").replace("soru","")
            	cutNum=cutNum.replace("(","").replace(")","").replace(" ","")
            	try:
            		totalQuestion+=int(cutNum)
            	except:
            		print("error at counting questions")
        topRange+=f1.getsize(i)[1]
    print("Adding total count of question")
    eimg1.text((LeftRange,topRange),font=f1,text=(" Toplam soru :"+str(totalQuestion)))
    print("Total solved questions :"+str(totalQuestion))
    print("Texts writed , lines created , other tasks running ...")
    eimg1.line(((Line_LeftRange,10),(Line_LeftRange,Iheight-10)),width=5,fill=lineColor)
    print("Adding person info ")
    RoundedPanelImg(img=img1,pos=(Line_LeftRange+getMaxLength(personInfo)[0]*3,20),size=(getMaxLength(personInfo)[0]*15,f1.getsize(personInfo)[1]*15),fill=lineColor,round=30)
    eimg1.text((Line_LeftRange+getMaxLength(personInfo)[0]*5,10),personInfo,font=f1,fill=(0,0,0))
    print("---Date operations---")
    cutLastDate(text)
    print("Adding build information ")
    eimg1.text((Line_LeftRange+20,Iheight-50),companyNameText,font=f1,fill=(250,90,0))
    print("Tasks completed , Image saving ...")
    imagePath=createImgDir()+f"/Weekly_QuestionSolving2_{cutLastDate(text)}.jpg"
    imgPath2=os.getcwd()+f"/Weekly_QuestionSolving2_{cutLastDate(text)}.jpg"
    if(opt==1):
    	print("Option 1 selected")	
    	print("Saving to : "+imagePath)
    	img1.save(imagePath)
    elif(opt==2):
    	print("Option 2 selected")
    	print("Saving to : "+imgPath2)
    	img1.save(imgPath2)
    print("Image saved")
print("--WEEKLY QUESTION SOLVİNG 2--")
read_draw(ImageTextSource,PersonInfo,opt=1)
"""command is read_draw 
change content from ImageTextSource ( created at top of code )
change PersonInfo from PersonInfo ( top of code )
opt means saving destination 
( app created on android so first option can be wrong so use opt=2
ByRefupanker


"""
