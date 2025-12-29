import psutil
import ctypes

def get_vmem():
    swap = psutil.swap_memory()  # Move inside the function

    info = {
        "status": swap.total > 0,
        "total": f"{swap.total / 1024 ** 3:.2f} GB",
        "used": f"{swap.used / 1024 ** 3:.2f} GB",
        "free": f"{swap.free / 1024 ** 3:.2f} GB",
        "usage": f"{swap.percent} %",
        "needs_attention": swap.total == 0  # simple check for missing pagefile
    }

    return info

def open_virtual_memory_settings():
    ctypes.windll.shell32.ShellExecuteW(
        None,
        "runas",  # forces UAC
        "SystemPropertiesAdvanced",
        None,
        None,
        1
    )
