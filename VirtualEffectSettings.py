import winreg

PATH = r"Software\Microsoft\Windows\CurrentVersion\Explorer\VisualEffects"
NAME = "VisualFXSetting"


def get_visual_fx():
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, PATH, 0, winreg.KEY_READ) as key:
            value, _ = winreg.QueryValueEx(key, NAME)
            return value
    except FileNotFoundError:
        return None
    except OSError:
        return None


def set_visual_fx(value: int):
    with winreg.CreateKey(winreg.HKEY_CURRENT_USER, PATH) as key:
        winreg.SetValueEx(key, NAME, 0, winreg.REG_DWORD, value)
# Backup original state
original = get_visual_fx()
print("Original VisualFXSetting:", original)

# Apply Best Performance
def display_menu():
    print(" Main menu ")
    print("0, Let Windows choose what's best for my computer ")
    print("1, Adjust for best appearance")
    print("2, Adjust for best performance")
    print("3, custom")
    print("4, Exit the program")


def main():
    while True:
        display_menu()
        choice = input("Enter a choice (0-4): ")

        if choice == '0':
            set_visual_fx(0)
            break
        elif choice == '1':
            set_visual_fx(1)
            break
        elif choice == '2':
            set_visual_fx(2)
            break
        elif choice == '3':
            set_visual_fx(3)
            output = input("Do you want to customize the virtual effects; (0 (no)/ 1 (yes): ")
            if output == "0":
                break
            elif output == '1':
                print("loading...")
                base = r"Software\Microsoft\Windows\CurrentVersion\Explorer\VisualEffects"
                def getCustomset():
                    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, base) as key:
                        i = 0
                        while True:
                            try:
                                subkey = winreg.EnumKey(key, i)
                                print(subkey)
                                i += 1
                            except OSError:
                                break

                def setCustomerset(value: bool):


            else:
                print("Invalid number")
            break
        elif choice == '4':
            print('Exiting the program, Goodbye!')
            break
        else:
            print("Invalid number")


print("Visual effects set to Best Performance")

if __name__ == "__main__":
    main()
