import winreg
import os
import ctypes, ctypes.wintypes
from settings import WinSettings, WinControlPanel, WinSystemTools

# It is not appropriate to set visual effects solely through an API, nor through editing a single registry key.
# It is potential that any changes to a single visual effect rely on editing multiple registry keys and making API calls.
# Some settings have no proper API call (e.g. "Enable (Aero) peek") or may even be unused (e.g. "Enable taskbar animations") as of Windows 11 25H2.
# For the user to change visual effects, they should to be redirected to Windows proprietary settings apps.

# SystemParametersInfoW GET constants
SPI_GETANIMATION = 0x0048
SPI_GETCOMBOBOXANIMATION = 0x1004
SPI_GETCURSORSHADOW = 0x101A
SPI_GETDRAGFULLWINDOWS = 0x0026
SPI_GETDROPSHADOW = 0x1024
SPI_GETFONTSMOOTHING = 0x004A
SPI_GETGRADIENTCAPTIONS = 0x1008
SPI_GETLISTBOXSMOOTHSCROLLING = 0x1006
SPI_GETMENUANIMATION = 0x1002
SPI_GETSELECTIONFADE = 0x1014
SPI_GETTOOLTIPANIMATION = 0x1016
SPI_GETTOOLTIPFADE = 0x1018
SPI_GETUIEFFECTS = 0x103E


PATH = r"Software\Microsoft\Windows\CurrentVersion\Explorer\VisualEffects"
NAME = "VisualFXSetting"

def getall_visual_fx():
    preset_desc = "Error"
    preset = get_vfx_preset()
    if preset == 0:
        preset_desc = "Let Windows decide"
    elif preset == 1:
        preset_desc = "Optimize for appearance"
    elif preset == 2:
        preset_desc = "Optimize for performance"
    elif preset == 3:
        preset_desc = "Custom"

    return {
        "Visual effects preset": preset_desc,
        "Window minimize/maximize animations": get_visual_fx(SPI_GETANIMATION),
        "Combo box animations": get_visual_fx(SPI_GETCOMBOBOXANIMATION),
        "Cursor shadow": get_visual_fx(SPI_GETCURSORSHADOW),
        "Show window contents while dragging": get_visual_fx(SPI_GETDRAGFULLWINDOWS),
        "Window drop shadows": get_visual_fx(SPI_GETDROPSHADOW),
        "Font smoothing": get_visual_fx(SPI_GETFONTSMOOTHING),
        "Gradient title bars": get_visual_fx(SPI_GETGRADIENTCAPTIONS),
        "Smooth-scroll list boxes": get_visual_fx(SPI_GETLISTBOXSMOOTHSCROLLING),
        "Menu animations (fade/slide)": get_visual_fx(SPI_GETMENUANIMATION),
        "Selection fade": get_visual_fx(SPI_GETSELECTIONFADE),
        "Tooltip animations": get_visual_fx(SPI_GETTOOLTIPANIMATION),
        "General UI effects": get_visual_fx(SPI_GETUIEFFECTS),
    }

def get_vfx_preset():
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, PATH, 0, winreg.KEY_READ) as key:
            value, _ = winreg.QueryValueEx(key, NAME)
            return value
    except FileNotFoundError:
        return None
    except OSError:
        return None


class ANIMATIONINFO(ctypes.Structure):
    _fields_ = [
        ("cbSize", ctypes.wintypes.UINT),
        ("iMinAnimate", ctypes.c_int)
    ]


# Gets 
def get_visual_fx(spi_constant):
    if (spi_constant == SPI_GETANIMATION):
        anim_info = ANIMATIONINFO()
        anim_info.cbSize = ctypes.sizeof(ANIMATIONINFO)
        success = ctypes.windll.user32.SystemParametersInfoW(
            spi_constant, anim_info.cbSize, ctypes.byref(anim_info), 0
        )
        if not success:
            return "Error retrieving"
        return True if anim_info.iMinAnimate else False

    status = ctypes.c_bool()
    # uiAction, uiParam, pvParam, fWinIni
    success = ctypes.windll.user32.SystemParametersInfoW(
        spi_constant, 0, ctypes.byref(status), 0
    )
    if not success:
        return "Error retrieving"
    return status.value

# Should there be an automatic way to find settings for vfx and other related settings?
def getlinks_vfx():
    return [
        WinSettings.EaseOfAccess.VISUAL_EFFECTS, 
        WinControlPanel.Accessibility.EASIER_TO_SEE,
        WinSystemTools.Dialogs.PERFORMANCE_OPTIONS,
    ]

def main():
    # 1. Map constants to readable labels for the report
    vfx_labels = {
        SPI_GETANIMATION: "Window Minimize/Maximize Animations",
        SPI_GETCOMBOBOXANIMATION: "Combo Box Animations",
        SPI_GETCURSORSHADOW: "Cursor Shadow",
        SPI_GETDRAGFULLWINDOWS: "Show Window Contents While Dragging",
        SPI_GETDROPSHADOW: "Drop Shadows (Windows)",
        SPI_GETFONTSMOOTHING: "Font Smoothing (ClearType)",
        SPI_GETGRADIENTCAPTIONS: "Gradient Title Bars",
        SPI_GETLISTBOXSMOOTHSCROLLING: "Smooth-scroll List Boxes",
        SPI_GETMENUANIMATION: "Menu Animations (Fade/Slide)",
        SPI_GETSELECTIONFADE: "Selection Fade",
        SPI_GETTOOLTIPANIMATION: "Tooltip Animations",
        SPI_GETUIEFFECTS: "General UI Effects"
    }

    print("="*50)
    print(" Windows Visual Effects Configuration ")
    print("="*50)

    # vfx_preset = "[ ERROR ]"
    # if get_vfx_preset() == 0:
    #     vfx_preset = "[ LET WINDOWS DECIDE ]"
    # elif get_vfx_preset() == 1:
    #     vfx_preset = "[ BEST APPEARANCE ]"
    # elif get_vfx_preset() == 2:
    #     vfx_preset = "[ BEST PERFORMANCE ]"
    # elif get_vfx_preset() == 3:
    #     vfx_preset = "[ CUSTOM ]"

    # print(f"{"PRESET":<40} {vfx_preset}")

    # # 2. Print Current Statuses
    # for constant, label in vfx_labels.items():
    #     status = get_visual_fx(constant)
    #     status_str = "[ ENABLED ]" if status is True else "[ DISABLED ]"
    #     if status == "Error retrieving":
    #         status_str = "[ ERROR ]"
        
    #     print(f"{label:<40} {status_str}")

    print(getall_visual_fx())

    print("Note: not all visual effects shown.")
    print("\n" + "="*50)
    print(" Redirect to Settings ")
    print("="*50)
    print("Manual changes are required for Visual Effects.")
    
    # 3. Get the links from your helper function
    links = getlinks_vfx()
    
    for i, link in enumerate(links, 1):
        # link.name gives the Enum key, link.value gives the URI/Command
        print(f"{i}. Open {link.__class__.__name__}: {link.name}")

    print("0. Exit")
    
    # 4. Interactive Choice
    try:
        choice = int(input("\nSelect a menu to open (0-3): "))
        if 1 <= choice <= len(links):
            selected_link = links[choice-1]
            # print(f"\nProceeding: {selected_link.open()}")
        else:
            print("Exiting.")
    except ValueError:
        print("Invalid input, exiting.")

if __name__ == "__main__":
    main()


# import winreg
# import os
# import ctypes, ctypes.wintypes

# PATH = r"Software\Microsoft\Windows\CurrentVersion\Explorer\VisualEffects"
# NAME = "VisualFXSetting"

# # Setting change broadcast constants
# HWND_BROADCAST = 0xFFFF
# WM_SETTINGCHANGE = 0x001A
# SMTO_ABORTIFHUNG = 0x0002

# def refresh_windows():
#     print("Broadcasting change to Windows")
#     word = ctypes.wintypes.DWORD()
#     # Refresh shell
#     status = ctypes.windll.user32.SendMessageTimeoutW(
#         HWND_BROADCAST, 
#         WM_SETTINGCHANGE, 
#         0, 
#         "Environment", 
#         SMTO_ABORTIFHUNG, 
#         5000, 
#         ctypes.byref(word)
#     )
#     # Refresh desktop/taskbar
#     status = ctypes.windll.user32.SendMessageTimeoutW(
#         HWND_BROADCAST, 
#         WM_SETTINGCHANGE, 
#         0, 
#         "UserPreferencesMask", 
#         SMTO_ABORTIFHUNG, 
#         5000, 
#         ctypes.byref(word)
#     )

#     if status == 0:
#         print("Timeout: Windows not refreshed")


# def get_visual_fx():
#     try:
#         with winreg.OpenKey(winreg.HKEY_CURRENT_USER, PATH, 0, winreg.KEY_READ) as key:
#             value, _ = winreg.QueryValueEx(key, NAME)
#             return value
#     except FileNotFoundError:
#         return None
#     except OSError:
#         return None

# def set_visual_fx(value: int):
#     with winreg.CreateKey(winreg.HKEY_CURRENT_USER, PATH) as key:
#         winreg.SetValueEx(key, NAME, 0, winreg.REG_DWORD, value)
    
#     refresh_windows()


# def main():
#     print("Visual effects are currently set to: ", end="")
#     match get_visual_fx():
#         case 0:
#             print("(0) Let Windows decide")
#         case 1:
#             print("(1) Best appearance")
#         case 2:
#             print("(2) Best performance")
#         case 3:
#             print("(3) Custom")

#     while True:
#         print(
#               "\nChoose an option to set to:\n"
#               "(0) Let Windows choose what's best for my computer\n"
#               "(1) Adjust for best appearance\n"
#               "(2) Adjust for best performance\n"
#               "(3) Custom\n"
#               "(4) Exit"
#               )

#         choice = input()

#         if choice == '0':
#             set_visual_fx(0)
#             break
#         elif choice == '1':
#             set_visual_fx(1)
#             break
#         elif choice == '2':
#             set_visual_fx(2)
#             break
#         elif choice == '3':
#             set_visual_fx(3)
#             output = input("Do you want to open the effects customizer? 0 (no)/ 1 (yes): ")
#             if output == "0":
#                 break
#             elif output == '1':
#                 print("loading...")
#                 try:
#                     os.system("SystemPropertiesPerformance")
#                 except Exception as e:
#                     print(f"ERROR: {e}")
#             else:
#                 print("Invalid number")
#             break
#         elif choice == '4':
#             print('Exiting the program, Goodbye!')
#             break
#         else:
#             print("Invalid number")


# def select_visual_fx(value: int, open_customizer: bool = False):
#     if value not in (0, 1, 2, 3):
#         raise ValueError("Visual FX value must be 0-3")

#     set_visual_fx(value)
#     if value == 3 and open_customizer:
#         try:
#             os.system("SystemPropertiesPerformance")
#         except Exception as e:
#             print(f"Failed to open customizer: {e}")
#     return value

# if __name__ == "__main__":
#     main()
