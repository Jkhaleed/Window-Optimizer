import psutil

ram = psutil.virtual_memory()
swap = psutil.swap_memory()

print("=== RAM ===")
print(f"Total: {ram.total / 1024**3:.2f} GB")
print(f"Available: {ram.available / 1024**3:.2f} GB")
print(f"Used: {ram.used / 1024**3:.2f} GB")
print(f"Usage: {ram.percent}%")

print("\n=== Swap / Paging File ===")
print(f"Total: {swap.total / 1024**3:.2f} GB")
print(f"Used: {swap.used / 1024**3:.2f} GB")
print(f"Free: {swap.free / 1024**3:.2f} GB")
print(f"Usage: {swap.percent}%")
