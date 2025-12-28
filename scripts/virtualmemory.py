import psutil
import os

swap = psutil.swap_memory()
def get_vmem():
    info = {
        "status": swap.used > 0,
        "total": swap.total,
        "used": swap.used,
        "free": swap.free,
        "usage": swap.percent
    }
    return info

def check_vmem(info):
    if swap.used == 0:
        choice = input("Do you want to turn on the paging file 1 (yes)/ 0 (no): ")
        if choice == "1":
            os.system("SystemPropertiesAdvanced")
            info["action"] = "opened_settings"
        elif choice == "0":
            print("Thanks so much for checking this out")
            info["action"] = "declined"
        else:
            print("Invalid number")
            info["action"] = "invalid"
    else:
        print("Your paging file is working fine")
        info["action"] = "active"  #

    return info



# print("\n=== Swap / Paging File ===")
# print(f"Total: {swap.total / 1024**3:.2f} GB")
# print(f"Used: {swap.used / 1024**3:.2f} GB")
# print(f"Free: {swap.free / 1024**3:.2f} GB")
# print(f"Usage: {swap.percent}%")
#option to turn

