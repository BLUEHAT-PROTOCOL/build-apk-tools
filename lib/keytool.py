import os, subprocess, getpass

def make_keystore():
    if os.path.exists("release.keystore"):
        return
    pw = getpass.getpass("Masukkan password keystore: ")
    dname = "CN=EyeFox, OU=Mobile, O=Android, L=Jakarta, C=ID"
    subprocess.run([
        "keytool", "-genkey", "-v", "-keystore", "release.keystore", "-alias", "release",
        "-keyalg", "RSA", "-keysize", "2048", "-validity", "10000",
        "-dname", dname, "-storepass", pw, "-keypass", pw
    ])
    
