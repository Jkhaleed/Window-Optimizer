import subprocess

output = subprocess.check_output("systeminfo", text=True)
for line in output.splitlines():
    print(line)
