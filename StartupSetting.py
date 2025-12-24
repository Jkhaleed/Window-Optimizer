import winreg

base = r"Software\Microsoft\Windows\CurrentVersion\Explorer\VisualEffects"

with winreg.OpenKey(winreg.HKEY_CURRENT_USER, base) as key:
    i = 0
    while True:
        try:
            subkey = winreg.EnumKey(key, i)
            print(subkey)
            i += 1
        except OSError:
            break


