import customtkinter
import Computerinformation

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Configure window
        self.title("CustomTkinter Tabs Example")
        self.geometry("300x400")

        # Create the TabView widget
        self.tab_view = customtkinter.CTkTabview(master=self)
        self.tab_view.pack(padx=20, pady=20, fill="both", expand=True)

        # Add tabs
        self.tab_view.add("Computer Information")
        self.tab_view.add("Virtual Effect")
        self.tab_view.set("Computer Information")

        # ---- Tab 1 ----
        self.textbox = customtkinter.CTkTextbox(
            master=self.tab_view.tab("Computer Information"),
            width=400,
            height=200
        )
        self.textbox.pack(padx=20, pady=10)

        self.button_1 = customtkinter.CTkButton(
            master=self.tab_view.tab("Computer Information"),
            text="Click me computer info",
            command=self.show_computer_info   #
        )
        self.button_1.pack(padx=20, pady=10)

        # ---- Tab 2 ----
        self.label_2 = customtkinter.CTkLabel(
            master=self.tab_view.tab("Virtual Effect"),
            text="Content for Tab 2"
        )
        self.label_2.pack(padx=20, pady=10)

    def show_computer_info(self):
        lines = Computerinformation.get_computer_info()

        self.textbox.delete("1.0", "end")

        for line in lines:
            self.textbox.insert("end", line + "\n")


if __name__ == "__main__":
    app = App()
    app.mainloop()
