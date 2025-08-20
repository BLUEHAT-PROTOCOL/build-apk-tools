#!/data/data/com.termux/files/usr/bin/python3
import os, sys, subprocess, json
from lib.colors import *
from lib.dialogs import *

VERSION = "22"
AKTIF   = "3"
REF     = "CpLmdljv"

def banner():
    print(f"""{c1}
╔══════════════════════════════════════════════╗
║  DASHBOARD{c0}  EyeFox  {c3}AKTIF:{c2}{AKTIF}{c0}  REF:{c2}{REF}{c0}   ║
╚══════════════════════════════════════════════╝{c0}""")

def menu():
    items = ["Lihat Profil", "Tanda Tangan APK", "Buat Keystore", "Build APK", "Keluar"]
    opt = radiolist("Pilih menu:", items)
    if   opt == 0: info()
    elif opt == 1: sign()
    elif opt == 2: keystore()
    elif opt == 3: build()
    else:          sys.exit()

def info():
    msgbox("Nama: EyeFox\nToken: {}\nAktif: {}\nTidak Aktif: -".format(REF, AKTIF))

def sign():
    apks = [f for f in os.listdir('.') if f.endswith('.apk')]
    if not apks:
        msgbox("Tidak ada file APK di folder ini.")
        return
    apk = filepicker("Pilih APK yang akan ditandatangani:", apks)
    if apk:
        subprocess.run(["apksigner","sign","--ks","release.keystore",apk])
        msgbox("APK berhasil ditandatangani!")

def keystore():
    from lib.keytool import make_keystore
    make_keystore()
    msgbox("Keystore berhasil dibuat!")

def build():
    subprocess.run([sys.executable, "setup.py"])

if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    banner()
    while True:
        menu()
    
