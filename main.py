import wmi

c = wmi.WMI()

for os in c.Win32_OperatingSystem():
    print(f"Operating System: {os.Caption}")