import psutil
import os

swap = psutil.swap_memory()

def get_vmem():
    return {
        "status": swap.used == 0,
        "total": swap.total,
        "used": swap.used,
        "free": swap.free,
        "usage": swap.percent
	}

print("\n=== Swap / Paging File ===")
print(f"Total: {swap.total / 1024**3:.2f} GB")
print(f"Used: {swap.used / 1024**3:.2f} GB")
print(f"Free: {swap.free / 1024**3:.2f} GB")
print(f"Usage: {swap.percent}%")
#option to turn
if swap.used == 0:
    choice = input("Do you want to turn on the paging file 1 (yes)/ 0 (no): ")
    if choice == "1":
        os.system("SystemPropertiesAdvanced")
    elif choice == "0":
        print("Thanks so much for checking this out")
    else:
        print("Invalid number")
else:
    print("Your paging file is working fine")
