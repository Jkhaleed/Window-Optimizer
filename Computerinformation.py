import subprocess

def get_computer_info():
    output = subprocess.check_output("systeminfo", text=True)
    return output.splitlines()

