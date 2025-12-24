import subprocess



def open_task_manager_startup():
    """
    Opens the Windows Task Manager and navigates to the Startup tab.
    This uses a run command which works on modern Windows versions.
    """
    try:
        # The command to open the Task Manager to the Startup tab
        command = "cmd.exe /c start taskmgr"
        subprocess.run(command, shell=True)
        print("Task Manager opened successfully.")

    except FileNotFoundError:
        print("Error: taskmgr.exe or cmd.exe not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    open_task_manager_startup()
