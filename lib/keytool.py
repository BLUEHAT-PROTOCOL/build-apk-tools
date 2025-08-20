import os, subprocess, getpass

def make_keystore():
    alias = "release"
    ks = "release.keystore"
    if os.path.exists(ks):
        return
    pw = getpass.getpass("Masukkan password keystore: ")
    dname = "CN=EyeFox, OU=Mobile, O=Android, L=Jakarta, C=ID"
    subprocess.run([
        "keytool","-genkey","-v","-keystore",ks,"-alias",alias,
        "-keyalg","RSA","-keysize","2048","-validity","10000",
        "-dname",dname,"-storepass",pw,"-keypass",pw
    ])
