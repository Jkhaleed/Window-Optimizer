import customtkinter
import scripts.compinfo
import scripts.mouse
import scripts.brightness
import scripts.startup
import scripts.virtualmemory
import scripts.visualfx

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
customtkinter.deactivate_automatic_dpi_awareness()


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Configure window
        self.title("Window Optimizer")
        self.geometry("700x550")

        # Create the TabView widget
        self.tab_view = customtkinter.CTkTabview(
            master=self,
            corner_radius=10,
            segmented_button_fg_color="gray20",
            segmented_button_selected_color="gray35"
        )
        self.tab_view.pack(padx=20, pady=20, fill="both", expand=True)

        # Add tabs
        self.tab_view.add("Computer Information")
        self.tab_view.add("Virtual FX")
        self.tab_view.add("Virtual Memory")
        self.tab_view.add("Startup Apps")
        self.tab_view.add("Mouse")
        self.tab_view.add("Windows Brightness")
        self.tab_view.set("Computer Information")

        # ---- Tab 1: Computer Information ----
        self.textbox = customtkinter.CTkTextbox(
            master=self.tab_view.tab("Computer Information"),
            height=200
        )
        self.textbox.pack(padx=20, pady=10, fill="both", expand=True)

        self.button_1 = customtkinter.CTkButton(
            master=self.tab_view.tab("Computer Information"),
            text="Click me computer info",
            corner_radius=32,
            fg_color="transparent",
            command=self.show_computer_info,
            hover_color="#4158D0",
            border_color="white",
            border_width=2
        )
        self.button_1.pack(padx=20, pady=10)

        # ---- Tab 2: Virtual FX ----
        self.fx_label = customtkinter.CTkLabel(
            master=self.tab_view.tab("Virtual FX"),
            text="Virtual FX Settings",
            font=("Segoe UI", 14, "bold")
        )
        self.fx_label.pack(padx=20, pady=(20, 5), anchor="w")

        self.fx_button = customtkinter.CTkSegmentedButton(
            master=self.tab_view.tab("Virtual FX"),
            values=["Let Windows decide", "Best appearance", "Best performance", "Custom"],
            command=self.apply_virtual_fx
        )

        self.fx_button.set("Let Windows decide")
        self.fx_button.pack(padx=20, pady=20, fill="x")

        # Status label
        self.fx_status = customtkinter.CTkLabel(
            master=self.tab_view.tab("Virtual FX"),
            text="",
            text_color="gray"
        )
        self.fx_status.pack(padx=20, pady=(5, 10), anchor="w")

        # ---- Tab 3: Virtual Memory ----
        self.label_3 = customtkinter.CTkLabel(
            master=self.tab_view.tab("Virtual Memory"),
            text="Content for Tab 3",
            wraplength=240,
            justify="left"
        )
        self.label_3.pack(padx=20, pady=10, fill="x")

        # ---- Tab 4: Startup Apps ----
        self.button = customtkinter.CTkButton(
            master=self.tab_view.tab("Startup Apps"),
            text="Open Task Manager",
            command=self.open_startup_app
        )
        self.button.pack(padx=20, pady=10, fill="x")

        # ---- Tab 5: Mouse ----
        # Label
        self.mouse_label = customtkinter.CTkLabel(
            master=self.tab_view.tab("Mouse"),
            text="Mouse Acceleration Mode",
            font=("Segoe UI", 14, "bold")
        )
        self.mouse_label.pack(padx=20, pady=(20, 5), anchor="w")

        # Option menu
        self.mouse_option = customtkinter.CTkOptionMenu(
            master=self.tab_view.tab("Mouse"),
            values=["Disabled Enhanced Pointer Precision", "Legacy Acceleration", "Enable Enhanced Pointer Precision"],
            command=self.on_mouse_option
        )
        self.mouse_option.set("Legacy Acceleration")
        self.mouse_option.pack(padx=20, pady=5, fill="x")

        # Status label
        self.mouse_status = customtkinter.CTkLabel(
            master=self.tab_view.tab("Mouse"),
            text="",
            text_color="gray"
        )
        self.mouse_status.pack(padx=20, pady=(5, 10), anchor="w")

        # ---- Tab 6: Windows Brightness ----
        self.label_6 = customtkinter.CTkLabel(
            master=self.tab_view.tab("Windows Brightness"),
            text="Content for Tab 6",
            wraplength=240,
            justify="left"
        )
        self.label_6.pack(padx=20, pady=10, fill="x")

    # ---------------- METHODS ----------------
    def show_computer_info(self):
        lines = scripts.compinfo.get_computer_info()
        self.textbox.delete("1.0", "end")
        for line in lines:
            self.textbox.insert("end", line + "\n")

    def open_startup_app(self):
        scripts.startup.open_task_manager_startup()

    def apply_virtual_fx(self, choice):
        # Map GUI string to integer value
        mapping = {
            "Let Windows decide": 0,
            "Best appearance": 1,
            "Best performance": 2,
            "Custom": 3
        }

        value = mapping.get(choice)  # Convert string -> int

        if value is None:
            print(f"Invalid Visual FX choice: {choice}")
            return

        # Call backend with integer
        scripts.visualfx.select_visual_fx(
            value,
            open_customizer=(value == 3)
        )

        # Update GUI label
        self.fx_label.configure(text=f"Visual FX set to: {choice}")

    def on_mouse_option(self, choice):
        mapping = {
            "Disabled Enhanced Pointer Precision": 0,
            "Legacy Acceleration": 1,
            "Enable Enhanced Pointer Precision": 2
        }
        value = mapping[choice]
        scripts.mouse.update_mouse_acceleration(value)

    def show_memory_info(self):
        lines = scripts.virtualmemory.get_vmem_and_check()
        self.textbox.delete("1.0", "11.0")
        for line in lines:
            self.textbox.insert("end", line + "\n")


if __name__ == "__main__":
    app = App()
    app.mainloop()
