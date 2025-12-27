import winreg
import os

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


def main():
    print("Visual effects are currently set to: ", end="")
    match get_visual_fx():
        case 0:
            print("(0) Let Windows decide")
        case 1:
            print("(1) Best appearance")
        case 2:
            print("(2) Best performance")
        case 3:
            print("(3) Custom")

    while True:
        print(
              "\nChoose an option to set to:\n"
              "(0) Let Windows choose what's best for my computer\n"
              "(1) Adjust for best appearance\n"
              "(2) Adjust for best performance\n"
              "(3) Custom\n"
              "(4) Exit"
              )

        choice = input()

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
            output = input("Do you want to open the effects customizer? 0 (no)/ 1 (yes): ")
            if output == "0":
                break
            elif output == '1':
                print("loading...")
                try:
                    os.system("SystemPropertiesPerformance")
                except Exception as e:
                    print(f"ERROR: {e}")
            else:
                print("Invalid number")
            break
        elif choice == '4':
            print('Exiting the program, Goodbye!')
            break
        else:
            print("Invalid number")


def select_visual_fx(value: int, open_customizer: bool = False):
    if value not in (0, 1, 2, 3):
        raise ValueError("Visual FX value must be 0-3")

    set_visual_fx(value)
    if value == 3 and open_customizer:
        try:
            os.system("SystemPropertiesPerformance")
        except Exception as e:
            print(f"Failed to open customizer: {e}")
    return value

if __name__ == "__main__":
    main()
