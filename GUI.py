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

# Modern Color Palette - Define colors once, use everywhere
COLORS = {
    "primary": "#3b82f6",           # Main blue color
    "primary_hover": "#2563eb",     # Darker blue for hover
    "primary_dark": "#1d4ed8",      # Even darker blue
    "secondary": "#8b5cf6",         # Purple accent
    "success": "#10b981",           # Green for success
    "warning": "#f59e0b",           # Orange for warnings
    "danger": "#ef4444",            # Red for errors
    "dark": "#1a1a1a",              # Dark background
    "darker": "#0f0f0f",            # Darker background
    "card": "gray20",               # Card background
    "card_hover": "gray25",         # Card hover
    "text_primary": "white",        # Main text color
    "text_secondary": "gray70"      # Dimmed text
}

# Consistent spacing throughout the app
PADDING = 20


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Configure window
        self.title("Windows Optimizer")
        self.geometry("800x650")



        # Step 2: Create TabView (ONLY ONCE!)
        self.tab_view = customtkinter.CTkTabview(
            master=self,
            corner_radius=15,
            segmented_button_fg_color="gray15",
            segmented_button_selected_color=COLORS["primary"],
            segmented_button_unselected_color="gray20",
            text_color=COLORS["text_primary"],
            segmented_button_unselected_hover_color="gray25"
        )
        self.tab_view.pack(padx=20, pady=(0, 20), fill="both", expand=True)

        # Step 3: Add all the tabs
        self.tab_view.add("💻 Computer Information")
        self.tab_view.add("✨ Visual FX")
        self.tab_view.add("💾 Virtual Memory")
        self.tab_view.add("🚀 Startup Apps")
        self.tab_view.add("🖱️Mouse")
        self.tab_view.add("☀️ Windows Brightness")





        # ---- Tab 1: Computer Information ----
        self.textbox = customtkinter.CTkTextbox(
            master=self.tab_view.tab("💻 Computer Information"),
            height=200
        )
        self.textbox.pack(padx=25, pady=15, fill="both", expand=True)

        self.button_1 = customtkinter.CTkButton(
            master=self.tab_view.tab("💻 Computer Information"),
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
            master=self.tab_view.tab("✨ Visual FX"),
            text="Virtual FX Settings",
            font=("Segoe UI", 14, "bold")

        )
        self.fx_label.pack(padx=20, pady=(20, 5), anchor="w")

        self.fx_button = customtkinter.CTkSegmentedButton(
            master=self.tab_view.tab("✨ Visual FX"),
            values=["Let Windows decide", "Best appearance", "Best performance", "Custom"],
            command=self.apply_virtual_fx,

        )

        self.fx_button.pack(padx=20, pady=20, fill="x")

        # Status label
        self.fx_status = customtkinter.CTkLabel(
            master=self.tab_view.tab("✨ Visual FX"),
            text="",
            text_color="gray"
        )
        self.fx_status.pack(padx=20, pady=(5, 10), anchor="w")

        # ---- Tab 3: Virtual Memory ----
        self.label_3 = customtkinter.CTkLabel(
            master=self.tab_view.tab("💾 Virtual Memory"),
            text="Content for Tab 3",
            wraplength=240,
            justify="left"
        )
        self.label_3.pack(padx=20, pady=10, fill="x")

        # ---- Tab 4: Startup Apps ----
        self.button = customtkinter.CTkButton(
            master=self.tab_view.tab("🚀 Startup Apps"),
            text="Open Task Manager",
            command=self.open_startup_app
        )
        self.button.pack(padx=20, pady=10, fill="x")

        # ---- Tab 5: Mouse ----
        # Label
        self.mouse_label = customtkinter.CTkLabel(
            master=self.tab_view.tab("🖱️Mouse"),
            text="Mouse Acceleration Mode",
            font=("Segoe UI", 14, "bold")
        )
        self.mouse_label.pack(padx=20, pady=(20, 5), anchor="w")

        # Option menu
        self.mouse_option = customtkinter.CTkOptionMenu(
            master=self.tab_view.tab("🖱️Mouse"),
            values=["Disabled Enhanced Pointer Precision", "Legacy Acceleration", "Enable Enhanced Pointer Precision"],
            command=self.on_mouse_option
        )
        self.mouse_option.set("Legacy Acceleration")
        self.mouse_option.pack(padx=20, pady=5, fill="x")

        # Status label
        self.mouse_status = customtkinter.CTkLabel(
            master=self.tab_view.tab("🖱️Mouse"),
            text="",
            text_color="gray"
        )
        self.mouse_status.pack(padx=20, pady=(5, 10), anchor="w")

        # ---- Tab 6: Windows Brightness ----
        self.brightness_label = customtkinter.CTkLabel(
            master=self.tab_view.tab("☀️ Windows Brightness"),
            text="Brightness: 0%",
            font=("Segoe UI", 14, "bold")
        )
        self.brightness_label.pack(padx=20, pady=(20, 10), anchor="w")

        self.brightness_slider = customtkinter.CTkSlider(
            master=self.tab_view.tab("☀️ Windows Brightness"),
            from_=0,
            to=100,
            command=self.brightness_slider_change
        )
        self.brightness_slider.pack(padx=20, pady=10, fill="x")

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
        lines = scripts.virtualmemory.get_vmem()
        self.textbox.delete("1.0", "11.0")
        for line in lines:
            self.textbox.insert("end", line + "\n")

    def brightness_slider_change(self, value):
        value = int(value)
        scripts.brightness.set_brightness(value)
        self.brightness_label.configure(text=f"{value}%")
        current = scripts.brightness.get_brightness()[0]
        self.brightness_slider.set(current)
        self.brightness_label.configure(text=f"Brightness: {current}%")







if __name__ == "__main__":
    app = App()
    app.mainloop()
