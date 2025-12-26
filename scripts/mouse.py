import winreg

PATH = r"Control Panel\Mouse"
NAME = "MouseSpeed"


def get_acceleration():
    # Read the mouse and return it as a string
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, PATH,0, winreg.KEY_READ) as key:
            value, reg_type = winreg.QueryValueEx(key, NAME)

            if reg_type != winreg.REG_SZ:
                return None  # unexpected type

            return int(value)
    except (FileNotFoundError, OSError, ValueError):
        return None


def set_acceleration(value: int):
    if value not in (0, 1, 2):
        raise ValueError("MouseSpeed must be 0, 1, or 2")

    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, PATH,0,winreg.KEY_SET_VALUE) as key:
        winreg.SetValueEx(key, NAME, 0, winreg.REG_SZ, str(value))


def main():
    #Main Menu
    original = get_acceleration()
    print(f"Original MouseSpeed: {original}")

    print("\nMain menu")
    print("0 - Disable Enhanced Pointer Precision")
    print("1 - Legacy Acceleration")
    print("2 - Enable Enhanced Pointer Precision")
    print("3 - Exit")

    while True:
        choice = input("Enter a choice (0–3): ")

        if choice == "3":
            print("Exiting program.")
            break

        try:
            set_acceleration(int(choice))
            print("MouseSpeed updated successfully.")
            break
        except (ValueError, OSError):
            print("Invalid input. Please enter 0, 1, 2, or 3.")


if __name__ == "__main__":
    main()
