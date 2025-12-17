# Windows Optimizer Settings

## CLI

Create a Command Line Interface that can list and alter settings in Windows, augmenting the performance of the system based on user input. Some settings include (but are not limited to):

- "View advanced system settings" -> "Performance" -> "Visual effects", "Processor scheduling"
- Virtual memory
- Disk usage(?) and temporary files
- Brightness
- Background apps
- App startup settings
- Windows update settings
  - Delivery optimization
- Disk optimization (defragment and optimize drives)
  - Provide SMART data for drive health
- Toggle mouse acceleration

Windows settings can be accessed using the Windows API. This includes the `windows.h` header file in C, and the `pywin32` library in Python. Otherwise, windows settings can be changed using the Windows Management Instrumentation (WMI), such as the `wmi` library in Python.

As a last resort, settings in Windows can be changed from editing the registry. However, this should be avoided as it can cause unintended behaviour.

## GUI

Create a GUI wrapper that is able to display every setting included in the CLI.

*TBD*