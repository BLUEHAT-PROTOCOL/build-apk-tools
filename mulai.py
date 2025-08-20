#!/data/data/com.termux/files/usr/bin/python3
import os, sys, subprocess, json
from lib.colors import *
from lib.dialogs  import *

VERSION = "22"
AKTIF   = "3"
REF     = "CpLmdljv"

def banner():
    print(f"""{c1}
╔══════════════════════════════════════════════╗
║  DASHBOARD{c0}  EyeFox  {c3}AKTIF:{c2}{AKTIF}{c0}  REF:{c2}{REF}{c0}   ║
╚══════════════════════════════════════════════╝{c0}""")

def menu():
    items = [
        "Lihat Profil",
        "Tanda Tangan APK",
        "Buat Keystore",
        "Build APK",
        "Keluar"
    ]
    opt = radiolist("Pilih menu:", items)
    if   opt == 0: info()
    elif opt == 1: sign()
    elif opt == 2: keystore()
    elif opt == 3: build()
    else:          sys.exit()

def info():
    msgbox(f"""Nama: EyeFox
Token: {REF}
Aktif: {AKTIF}
Tidak Aktif: -""")
    menu()

def sign():
    apk = filepicker("Pilih APK yang akan ditandatangani:")
    if apk:
        subprocess.run(["apksigner","sign","--ks","release.keystore",apk])
        msgbox("APK berhasil ditandatangani!")
    menu()

def keystore():
    from lib.keytool import make_keystore
    make_keystore()
    msgbox("Keystore berhasil dibuat!")
    menu()

def build():
    subprocess.run([sys.executable,"setup.py"])
    menu()

if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    banner()
    menu()
