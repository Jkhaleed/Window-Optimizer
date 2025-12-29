import webbrowser, subprocess, os
import time
from enum import Enum

# Repository for all the links for Settings, Control Panel, etc. for ease-of-access

class WinSettings:
    """Container for Windows Settings URIs."""

    class _Base(Enum):
        def open(self):
            print(f"Opening {self.value}")
            webbrowser.open(self.value)

    class System(_Base):
        DISPLAY = "ms-settings:display"
        SOUND = "ms-settings:sound"
        NOTIFICATIONS = "ms-settings:notifications"
        POWER_SLEEP = "ms-settings:powersleep"
        BATTERY = "ms-settings:batterysaver"
        STORAGE = "ms-settings:storagesense"
        MULTITASKING = "ms-settings:multitasking"
        ACTIVATION = "ms-settings:activation"
        ABOUT = "ms-settings:about"
        CLIPBOARD = "ms-settings:clipboard"
        REMOTE_DESKTOP = "ms-settings:remotedesktop"

    class Devices(_Base):
        BLUETOOTH = "ms-settings:bluetooth"
        PRINTERS = "ms-settings:printers"
        MOUSE = "ms-settings:mousetouchpad"
        TYPING = "ms-settings:typing"
        USB = "ms-settings:usb"

    class Network(_Base):
        STATUS = "ms-settings:network-status"
        WIFI = "ms-settings:network-wifi"
        ETHERNET = "ms-settings:network-ethernet"
        VPN = "ms-settings:network-vpn"
        PROXY = "ms-settings:network-proxy"
        AIRPLANE_MODE = "ms-settings:network-airplanemode"

    class Personalization(_Base):
        BACKGROUND = "ms-settings:personalization-background"
        COLORS = "ms-settings:colors"
        LOCKSCREEN = "ms-settings:lockscreen"
        THEMES = "ms-settings:themes"
        FONTS = "ms-settings:fonts"
        START = "ms-settings:personalization-start"
        TASKBAR = "ms-settings:taskbar"

    class Apps(_Base):
        FEATURES = "ms-settings:appsfeatures"
        DEFAULT_APPS = "ms-settings:defaultapps"
        OFFLINE_MAPS = "ms-settings:maps"
        VIDEO_PLAYBACK = "ms-settings:videoplayback"
        STARTUP = "ms-settings:startupapps"

    class Accounts(_Base):
        INFO = "ms-settings:yourinfo"
        EMAIL = "ms-settings:emailandaccounts"
        SIGNIN = "ms-settings:signinoptions"
        FAMILY = "ms-settings:otherusers"

    class TimeLanguage(_Base):
        DATE_TIME = "ms-settings:dateandtime"
        REGION = "ms-settings:regionformatting"
        LANGUAGE = "ms-settings:keyboard"
        SPEECH = "ms-settings:speech"

    class Gaming(_Base):
        GAME_BAR = "ms-settings:gaming-gamebar"
        GAME_MODE = "ms-settings:gaming-gamemode"

    class Privacy(_Base):
        GENERAL = "ms-settings:privacy"
        LOCATION = "ms-settings:privacy-location"
        CAMERA = "ms-settings:privacy-webcam"
        MICROPHONE = "ms-settings:privacy-microphone"
        NOTIFICATIONS = "ms-settings:privacy-notifications"
        ACCOUNT_INFO = "ms-settings:privacy-accountinfo"

    class Update(_Base):
        WINDOWS_UPDATE = "ms-settings:windowsupdate"
        BACKUP = "ms-settings:backup"
        RECOVERY = "ms-settings:recovery"
        TROUBLESHOOT = "ms-settings:troubleshoot"
        SECURITY = "ms-settings:windowsdefender"
        DELIVERY_OPTIMIZATION = "ms-settings:delivery-optimization"


class WinControlPanel:
    """Container for legacy Windows Control Panel elements."""

    class _Base(Enum):
        def open(self):
            """Executes the control panel command for the canonical name."""
            # Use subprocess to call 'control /name Microsoft.Name'
            subprocess.Popen(['control', '/name', self.value])
            return f"Opening Control Panel item: {self.name}..."

    class System(_Base):
        SYSTEM_INFO = "Microsoft.System"
        POWER_OPTIONS = "Microsoft.PowerOptions"
        FIREWALL = "Microsoft.WindowsFirewall"
        SECURITY_MAINTENANCE = "Microsoft.ActionCenter"
        BITLOCKER = "Microsoft.BitLockerDriveEncryption"
        STORAGE_SPACES = "Microsoft.StorageSpaces"

    class Network(_Base):
        NETWORK_SHARING = "Microsoft.NetworkAndSharingCenter"
        INTERNET_OPTIONS = "Microsoft.InternetOptions"
        INFRARED = "Microsoft.Infrared"

    class Hardware(_Base):
        DEVICES_PRINTERS = "Microsoft.DevicesAndPrinters"
        SOUND = "Microsoft.Sound"
        MOUSE = "Microsoft.Mouse"
        KEYBOARD = "Microsoft.Keyboard"
        GAME_CONTROLLERS = "Microsoft.GameControllers"
        PHONE_MODEM = "Microsoft.PhoneAndModem"
        COLOR_MANAGEMENT = "Microsoft.ColorManagement"

    class Programs(_Base):
        PROGRAMS_FEATURES = "Microsoft.ProgramsAndFeatures"
        DEFAULT_PROGRAMS = "Microsoft.DefaultPrograms"

    class UserAccounts(_Base):
        USER_ACCOUNTS = "Microsoft.UserAccounts"
        CREDENTIAL_MANAGER = "Microsoft.CredentialManager"
        WORK_FOLDERS = "Microsoft.WorkFolders"

    class Appearance(_Base):
        FONTS = "Microsoft.Fonts"
        EASE_OF_ACCESS = "Microsoft.EaseOfAccessCenter"

    class ClockRegion(_Base):
        DATE_TIME = "Microsoft.DateAndTime"
        REGION = "Microsoft.RegionAndLanguage"

    class Administrative(_Base):
        ADMIN_TOOLS = "Microsoft.AdministrativeTools"
        ODBC_DATA_SOURCES = "Microsoft.DefaultPrograms"
        INDEXING_OPTIONS = "Microsoft.IndexingOptions"


class MMC(Enum):
    """Container for Windows Management Console (.msc) tools."""
    def open(self):
        """Opens the .msc snap-in directly."""
        # .msc files are registered to auto-open with mmc.exe
        print(f"Launching {self.value}")
        os.startfile(self.value)

    DEVICE_MANAGER = "devmgmt.msc"
    DISK_MANAGEMENT = "diskmgmt.msc"
    SERVICES = "services.msc"
    EVENT_VIEWER = "eventvwr.msc"
    TASK_SCHEDULER = "taskschd.msc"
    # GROUP_POLICY = "gpedit.msc"     # Note: Pro/Enterprise editions only
    COMPUTER_MANAGEMENT = "compmgmt.msc"
    SHARED_FOLDERS = "fsmgmt.msc"


class WinSystemTools:
    """Container for essential Windows system executables and shell commands."""

    class _Base(Enum):
        def open(self):
            print(f"Starting {self.value}")
            os.startfile(self.value)

    class Utilities(_Base):
        TASK_MANAGER = "taskmgr.exe"
        REGISTRY_EDITOR = "regedit.exe"
        RESOURCE_MONITOR = "resmon.exe"
        PERFORMANCE_MONITOR = "perfmon.exe"
        SYSTEM_INFORMATION = "msinfo32.exe"
        DIRECTX_DIAGNOSTICS = "dxdiag.exe"
        CHARACTER_MAP = "charmap.exe"
        ON_SCREEN_KEYBOARD = "osk.exe"
        SNIPPING_TOOL = "snippingtool.exe"
        CALCULATOR = "calc.exe"
    
    def get_system_info():
        try:
            result = subprocess.run(['systeminfo'], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f"Error occurred: {e}"
        except FileNotFoundError:
            return "systeminfo.exe not found"


if __name__ == "__main__":
    WinSettings.System.ABOUT.open()
    time.sleep(1)
    WinSettings.Gaming.GAME_BAR.open()
    time.sleep(1)
    WinControlPanel.System.SYSTEM_INFO.open()
    time.sleep(1)
    # WinSettings.Gaming.open() # does not work (no page exists)
    WinControlPanel.System.POWER_OPTIONS.open()
    time.sleep(1)
    WinControlPanel.Hardware.SOUND.open()
    time.sleep(1)
    MMC.DEVICE_MANAGER.open()
    time.sleep(1)
    print(WinSystemTools.get_system_info())
