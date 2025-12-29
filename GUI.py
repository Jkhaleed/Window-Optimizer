import subprocess
import customtkinter
import tkinter.messagebox as messagebox  # for popups

import scripts.compinfo
import scripts.mouse
import scripts.brightness
import scripts.startup
import scripts.virtualmemory
import scripts.visualfx

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
customtkinter.deactivate_automatic_dpi_awareness()

COLORS = {
    "primary": "#3b82f6",
    "primary_hover": "#2563eb",
    "primary_dark": "#1d4ed8",
    "secondary": "#8b5cf6",
    "success": "#10b981",
    "warning": "#f59e0b",
    "danger": "#ef4444",
    "dark": "#1a1a1a",
    "darker": "#0f0f0f",
    "card": "gray20",
    "card_hover": "gray25",
    "text_primary": "white",
    "text_secondary": "gray70"
}

PADDING = 20


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Windows Optimizer")
        self.geometry("800x650")

        self.brightness_text = customtkinter.StringVar()

        # ---- TabView ----
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

        self.tab_view.add("💻 Computer Information")
        self.tab_view.add("✨ Visual FX")
        self.tab_view.add("💾 Virtual Memory")
        self.tab_view.add("🚀 Startup Apps")
        self.tab_view.add("🖱️Mouse")
        self.tab_view.add("☀️ Windows Brightness")

        # ---- Tabs ----
        self.setup_computer_info_tab()
        self.setup_visual_fx_tab()
        self.setup_virtual_memory_tab()
        self.setup_startup_tab()
        self.setup_mouse_tab()
        self.setup_brightness_tab()

    # ---------------- TAB SETUP ----------------
    def setup_computer_info_tab(self):
        tab = self.tab_view.tab("💻 Computer Information")
        self.textbox = customtkinter.CTkTextbox(tab, height=200)
        self.textbox.pack(padx=25, pady=15, fill="both", expand=True)

        self.button_1 = customtkinter.CTkButton(
            tab,
            text="Click me computer info",
            command=self.show_computer_info
        )
        self.button_1.pack(pady=10)

    def setup_visual_fx_tab(self):
        tab = self.tab_view.tab("✨ Visual FX")
        self.fx_label = customtkinter.CTkLabel(
            tab,
            text="Visual FX Settings",
            font=("Segoe UI", 14, "bold")
        )
        self.fx_label.pack(padx=20, pady=(20, 5), anchor="w")

        self.fx_button = customtkinter.CTkSegmentedButton(
            tab,
            values=["Let Windows decide", "Best appearance", "Best performance", "Custom"],
            command=self.apply_virtual_fx
        )
        self.fx_button.pack(padx=20, pady=20, fill="x")

    def setup_virtual_memory_tab(self):
        tab = self.tab_view.tab("💾 Virtual Memory")

        info_frame = customtkinter.CTkFrame(tab, corner_radius=10)
        info_frame.pack(padx=PADDING, pady=PADDING, fill="x")

        info_label = customtkinter.CTkLabel(
            info_frame,
            text="💿 Check your virtual memory (page file) settings",
            text_color=COLORS["text_secondary"]
        )
        info_label.pack(padx=15, pady=12, anchor="w")

        self.memory_textbox = customtkinter.CTkTextbox(tab, height=300)
        self.memory_textbox.pack(padx=PADDING, pady=10, fill="both", expand=True)

        # Button to check virtual memory
        self.button_vmem = customtkinter.CTkButton(
            tab,
            text="🔍 Check Virtual Memory",
            command=self.show_memory_info
        )
        self.button_vmem.pack(pady=10)

    def setup_startup_tab(self):
        tab = self.tab_view.tab("🚀 Startup Apps")
        self.button_startup = customtkinter.CTkButton(
            tab,
            text="Open Task Manager",
            command=self.open_startup_app
        )
        self.button_startup.pack(padx=20, pady=10, fill="x")

    def setup_mouse_tab(self):
        tab = self.tab_view.tab("🖱️Mouse")
        self.mouse_label = customtkinter.CTkLabel(
            tab,
            text="Mouse Acceleration Mode",
            font=("Segoe UI", 14, "bold")
        )
        self.mouse_label.pack(padx=20, pady=(20, 5), anchor="w")

        self.mouse_option = customtkinter.CTkOptionMenu(
            tab,
            values=[
                "Disabled Enhanced Pointer Precision",
                "Legacy Acceleration",
                "Enable Enhanced Pointer Precision"
            ],
            command=self.on_mouse_option
        )
        self.mouse_option.set("Legacy Acceleration")
        self.mouse_option.pack(padx=20, pady=5, fill="x")

    def setup_brightness_tab(self):
        tab = self.tab_view.tab("☀️ Windows Brightness")
        self.brightness_label = customtkinter.CTkLabel(
            tab,
            textvariable=self.brightness_text,
            font=("Segoe UI", 14, "bold")
        )
        self.brightness_label.pack(padx=20, pady=(20, 10), anchor="w")

        self.brightness_slider = customtkinter.CTkSlider(
            tab,
            from_=0,
            to=100
        )
        self.brightness_slider.pack(padx=20, pady=10, fill="x")
        self.show_brightness()

    # ---------------- METHODS ----------------
    def show_computer_info(self):
        self.textbox.delete("1.0", "end")
        for line in scripts.compinfo.get_computer_info():
            self.textbox.insert("end", line + "\n")

    def apply_virtual_fx(self, choice):
        mapping = {
            "Let Windows decide": 0,
            "Best appearance": 1,
            "Best performance": 2,
            "Custom": 3
        }
        scripts.visualfx.select_visual_fx(mapping[choice], open_customizer=(choice == "Custom"))
        self.fx_label.configure(text=f"Visual FX set to: {choice}")

    def on_mouse_option(self, choice):
        mapping = {
            "Disabled Enhanced Pointer Precision": 0,
            "Legacy Acceleration": 1,
            "Enable Enhanced Pointer Precision": 2
        }
        scripts.mouse.update_mouse_acceleration(mapping[choice])

    def show_memory_info(self):
        self.memory_textbox.delete("1.0", "end")
        info = scripts.virtualmemory.get_vmem()

        # Display all info
        for k, v in info.items():
            if k != "needs_attention":
                self.memory_textbox.insert("end", f"{k}: {v}\n")

        # Prompt if virtual memory usage is zero
        if info.get("needs_attention"):
            response = messagebox.askyesno(
                title="Paging file",
                message="Paging file usage is 0. Do you want to open virtual memory settings?"
            )
            if response:
                scripts.virtualmemory.open_virtual_memory_settings()

    def open_startup_app(self):
        scripts.startup.open_task_manager_startup()

    def show_brightness(self):
        value = scripts.brightness.get_brightness()
        self.brightness_text.set(f"Brightness: {value}%")


if __name__ == "__main__":
    app = App()
    app.mainloop()
