import subprocess, os

def _dialog(args):
    cmd = ["dialog", "--stdout", "--backtitle", "EyeFox Dashboard"] + args
    res = subprocess.run(cmd, capture_output=True, text=True)
    return res

def radiolist(title, items):
    n = len(items)
    menu = []
    for idx, text in enumerate(items, 1):
        menu += [str(idx), text, "OFF"]
    res = _dialog(["--radiolist", title, str(n+7), "60", str(n)] + menu)
    if res.returncode != 0 or not res.stdout.strip():
        return None
    try:
        return int(res.stdout.strip()) - 1
    except ValueError:
        return None

def checklist(title, items):
    n = len(items)
    menu = []
    for idx, text in enumerate(items, 1):
        menu += [str(idx), text, "OFF"]
    res = _dialog(["--checklist", title, str(n+7), "70", str(n)] + menu)
    if res.returncode != 0 or not res.stdout.strip():
        return []
    return [items[int(x)-1] for x in res.stdout.split()]

def filepicker(title, files):
    res = radiolist(title, files)
    return files[res] if res is not None else None

def msgbox(text):
    _dialog(["--msgbox", text, "10", "60"])

def inputbox(title, default=""):
    res = _dialog(["--inputbox", title, "8", "60", default])
    return res.stdout.strip() if res.returncode == 0 else default
    
