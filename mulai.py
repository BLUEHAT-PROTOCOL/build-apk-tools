#!/data/data/com.termux/files/usr/bin/python3
import os, sys, subprocess, json, shutil, qrcode
from lib.colors import *
from lib.dialogs import *

VERSION, AKTIF, REF = "22", "3", "CpLmdljv"

def banner():
    print(f"{c1}╔══════════════════════════════════════════════╗{c0}")
    print(f"{c1}║  DASHBOARD{c0}  EyeFox  {c3}AKTIF:{c2}{AKTIF}{c0}  REF:{c2}{REF}{c0}   ║{c0}")
    print(f"{c1}╚══════════════════════════════════════════════╝{c0}")

def menu():
    items = [
        "Lihat Profil",
        "Tanda Tangan APK",
        "Buat Keystore",
        "Build APK (lokal)",
        "Build APK dari URL",
        "Keluar"
    ]
    while True:
        opt = radiolist("Pilih menu:", items)
        if opt in (None, 5): sys.exit(0)
        elif opt == 0: info()
        elif opt == 1: sign()
        elif opt == 2: keystore()
        elif opt == 3: build()
        elif opt == 4: build_from_url()

def info():
    msgbox("Nama: EyeFox\nToken: {}\nAktif: {}\nTidak Aktif: -".format(REF, AKTIF))

def sign():
    apks = [f for f in os.listdir('.') if f.endswith('.apk')]
    if not apks:
        msgbox("Tidak ada file APK di folder ini."); return
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

def build_from_url():
    url = inputbox("Masukkan URL situs:")
    if not url:
        return
    folder = url.split("//")[-1].split("/")[0]
    tempdir = os.path.join("temp", folder)
    shutil.rmtree(tempdir, ignore_errors=True)
    os.makedirs(tempdir, exist_ok=True)
    msgbox("Mengunduh situs…\n{}".format(url))
    subprocess.run(["wget","-r","-np","-nH","--cut-dirs=1","-P",tempdir,url])
    if os.path.isdir(tempdir):
        shutil.rmtree("www", ignore_errors=True)           # <-- BARIS BARU
        os.symlink(os.path.abspath(tempdir), "www", target_is_directory=True)
        subprocess.run([sys.executable, "setup.py"])
        apk_path = "android/app/build/outputs/apk/debug/app-debug.apk"
        if os.path.isfile(apk_path):
            show_qr(apk_path)

def show_qr(apk_path):
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=2)
    qr.add_data("file://" + os.path.abspath(apk_path))
    qr.make(fit=True)
    qr.print_ascii()
    msgbox("QR-Code untuk APK (file lokal) sudah ditampilkan di terminal!")

if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__) or '.')
    banner()
    menu()
    
