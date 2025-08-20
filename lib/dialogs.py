import subprocess, os

def whiptail(args):
    return subprocess.run(["dialog","--backtitle","EyeFox Dashboard","--stdout"] + args,
                          capture_output=True, text=True)

def radiolist(title, items):
    menu=[]
    for i,v in enumerate(items,1):
        menu += [str(i), v, "OFF"]
    res=whiptail(["--title",title,"--radiolist","",str(len(items)+6),"60",str(len(items))]+menu)
    return int(res.stdout.strip())-1 if res.returncode==0 else None

def checklist(title, items):
    menu=[]
    for i,v in enumerate(items,1):
        menu += [str(i), v, "OFF"]
    res=whiptail(["--title",title,"--checklist","",str(len(items)+6),"70",str(len(items))]+menu)
    return [items[int(x)-1] for x in res.stdout.split()] if res.returncode==0 else []

def filepicker(title, files):
    return radiolist(title, files)

def dselect(title, dirs):
    return dirs[radiolist(title, dirs)]

def inputbox(title, default=""):
    res=whiptail(["--inputbox",title,"8","60",default])
    return res.stdout.strip() if res.returncode==0 else default

def msgbox(text):
    whiptail(["--msgbox",text,"10","60"])

def pause():
    input("\nTekan Enter untuk kembali...")
  
