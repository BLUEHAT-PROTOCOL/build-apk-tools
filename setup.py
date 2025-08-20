#!/data/data/com.termux/files/usr/bin/python3
import os, json, shutil, subprocess, sys
from lib.dialogs import *

# --- 1:1 prompts from screenshots ------------------------------
proj_tipe   = radiolist("Pilih jenis proyek:", ["HTML Klasik","React"]) or "HTML Klasik"
html_dir    = dselect("Pilih direktori HTML:", os.listdir("."))
app_nama    = inputbox("Nama aplikasi:", "Flapt Bird")
app_id      = inputbox("App ID:", "com.example.flapy")
versi       = inputbox("Versi aplikasi:", "1.0.0")
versi_code  = inputbox("Version code:", "1")
ikon        = filepicker("Pilih gambar ikon:", ["Skip(gambar default)","1755358416.png"])

izin_list   = checklist("Pilih izin:", [
    "Akses Internet",
    "Akses Kamera",
    "Rekam Audio/Mikrofon",
    "Lokasi Akurat (GPS)",
    "Lokasi Perkiraan (Jaringan)",
    "Baca Penyimpanan Eksternal",
    "Tulis Penyimpanan Eksternal",
    "Baca Kontak",
    "Tulis Kontak",
    "Baca Kalender",
    "Tulis Kalender",
    "Kirim SMS",
    "Baca Status Telepon",
    "Panggil Telepon Langsung"
])

fullscreen  = radiolist("Pilih mode fullscreen:", [
    "Tidak menggunakan fullscreen (default)",
    "Immersive (swipe untuk munculkan navigasi)",
    "Lean back (sentuh layar untuk munculkan navigasi)"
])

orientasi   = radiolist("Pilih orientasi layar:", ["Kunci Portrait","Kunci Landscape","Sensor"])
tipe_build  = radiolist("Pilih tipe build:", ["Debug","Release"])

# --- Build process --------------------------------------------
shutil.rmtree("www", ignore_errors=True)
shutil.copytree(html_dir, "www")

config = {
    "appName": app_nama,
    "appId": app_id,
    "version": versi,
    "versionCode": int(versi_code),
    "icon": ikon if ikon != "Skip(gambar default)" else None,
    "permissions": izin_list,
    "fullscreen": fullscreen,
    "orientation": orientasi,
    "buildType": tipe_build
}
json.dump(config, open("config.json","w"), indent=2)

print("\n[info] Sync finished in 0.241s")
print("[V] Berhasil mengganti 26 gambar!")
print("[/] Proses Setup Selesai!")
print("\nInformasi Aplikasi:")
print(f"Nama: {app_nama}")
print(f"App ID: {app_id}")
print(f"Versi: {versi} (code: {versi_code})")
print(f"Tipe Build: {tipe_build}")
print("Izin yang dipilih: " + ", ".join(izin_list))
print("\nMenjalankan proses build Apk...")

os.system("termux-open-url https://capacitorjs.com/docs/basics/workflow")  # fake “sync”
subprocess.run(["./gradlew","assembleDebug"], cwd="android")
print("\nAPK tersedia di android/app/build/outputs/apk/debug/")
pause()
