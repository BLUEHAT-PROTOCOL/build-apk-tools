# 🚀 HTML-to-APK Termux Buat APK langsung dari HP Android tanpa PC!

# build-apk-tools

Menu Utama	Build APK	Hasil	

![menu](https://placehold.co/200x120/000/fff?text=DASHBOARD)	![build](https://placehold.co/200x120/0a0/fff?text=BUILD+APK)	![apk](https://placehold.co/200x120/007/fff?text=APK+READY)	



⚙️ Fitur

✅ Tidak butuh PC / Android Studio

✅ Pilih folder HTML → APK dalam 1 menit

✅ Prompt lengkap: nama, App ID, versi, izin, fullscreen, orientasi, debug/release

✅ Otomatis buat & tanda-tangan keystore ( release.keystore )

✅ Output APK siap dipasang:
  android/app/build/outputs/apk/debug/ 



📦 Instalasi (Termux)

pkg update && pkg upgrade -y
pkg install python openjdk-17 apksigner whiptail git gradle

git clone https://github.com/YOUR_USERNAME/html-to-apk-termux.git
cd html-to-apk-termux
chmod +x *.py
./mulai.py


🧭 Cara Pakai
1. Jalankan  ./mulai.py
2. Pilih Build APK
3. APK siap di  android/app/build/outputs/apk/debug/



📁 Struktur Folder

build-apk/
├── mulai.py          # Menu utama (DASHBOARD)
├── setup.py          # Mesin build
├── lib/
│   ├── dialogs.py    # Whiptail 1:1 clone
│   └── keytool.py    # Auto keystore
├── templates/        # AndroidManifest & build.gradle
└── README.md         # ini



📜 Lisensi
MIT – bebas modifikasi & redistribusi.



🐛 Laporkan Bug / Fitur Baru
Buka issue di tab “Issues” atau PR langsung.



Happy building! 🛠️📱
Dibuat dengan ❤️ di Termux.



DEV: BLUEHATPROTOCOL 
