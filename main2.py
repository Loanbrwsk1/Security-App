"""
@author : Loan Borowski
"""

#? Imports
from PIL import Image
import customtkinter as ctk
import random
import hashlib

#? Class
class LoginPage:
    def __init__(self):
        self.values = ["By default", "Black", "White", "Black and Red", "Grey and Red", "Blue and Brown", "Blue and Orange", "Black and Blue", "Green and Orange", "White and Blue", "Blue and Yellow", "Burgundy and Black"]
        self.values_fr = ["Par défault", "Noir", "Blanc", "Noir et Rouge", "Gris et Rouge", "Bleu et Marron", "Bleu et Orange", "Noir et Bleu", "Vert et Orange", "Blanc et Bleu", "Bleu et Jaune", "Bordeaux et Noir"]
        self.label_input = ctk.CTkLabel(window, text="Input your password", font=("Trebuchet MS", 25), text_color=text_color)
        self.label_error_login = ctk.CTkLabel(window, text="Wrong password !", text_color="red", font=("Trebuchet MS", 25))
        self.entry_input = ctk.CTkEntry(window, width=600, height=100, corner_radius=30, font=("Trebuchet MS", 25), border_width=1, border_color=text_color, fg_color = primary_color_hover, text_color = text_color, show="✱")
        self.button_login = ctk.CTkButton(window, width = 258, height = 60, corner_radius = 30,text = "Login", font = ("Trebuchet MS", 25), border_width = 1, command=self.login, border_color = text_color, hover_color = secondary_color_hover, fg_color = secondary_color, text_color = text_color)
        self.button_new_pwd = ctk.CTkButton( window, width = 50, height = 60, corner_radius = 30,text = "Modify your password", font = ("Trebuchet MS", 25), command=self.to_modify_pwd, border_width = 1, border_color = text_color, hover_color = secondary_color_hover, fg_color = secondary_color, text_color = text_color) 
        self.switch_language = ctk.CTkSwitch(window, switch_height = 30, switch_width = 60, text = "English", corner_radius = 20, font = ("Trebuchet MS", 20), progress_color = text_color, button_hover_color = text_color_hover, fg_color = secondary_color)
        self.option_menu_palet = ctk.CTkOptionMenu(window, width=70, height=30, corner_radius=20, values=self.values, font=("Trebuchet MS", 25), dropdown_font=("Trebuchet MS", 15), command=change_palet, fg_color=primary_color_hover, bg_color=primary_color, button_color=secondary_color, button_hover_color=secondary_color_hover, dropdown_fg_color=primary_color_hover, dropdown_hover_color=secondary_color, dropdown_text_color=text_color, text_color=text_color)

    def init(self):
        window.geometry("800x400")
        modify_pwd_page.label_error_empty_pwd.place_forget()
        modify_pwd_page.label_actual_pwd.place_forget()
        modify_pwd_page.entry_actual_pwd.place_forget()
        modify_pwd_page.label_new_pwd_1.place_forget()
        modify_pwd_page.entry_new_pwd_1.place_forget()
        modify_pwd_page.label_new_pwd_2.place_forget()
        modify_pwd_page.entry_new_pwd_2.place_forget()
        modify_pwd_page.button_back.place_forget()
        modify_pwd_page.button_modify.place_forget()
        self.label_input.place(relx = 0.5, anchor = "n", y = 40)
        self.entry_input.place(relx = 0.5, anchor = "n", y = 100)
        self.button_new_pwd.place(x = 100, y = 260)
        self.button_login.place(x = 440, y = 260)
        self.switch_language.place(x = 650, y = 10)
        self.option_menu_palet.place(x=10, y=10)

    def login(self):
        input = self.entry_input.get()
        if hashlib.md5(input.encode()).hexdigest() == password:
            self.label_input.place_forget()
            self.entry_input.place_forget()
            self.button_new_pwd.place_forget()
            self.button_login.place_forget()
            self.label_error_login.place_forget()
            # menu = Menu()
            # menu.init()
        else:
            self.entry_input.delete(0, "end")
            self.label_error_login.place(x = 290, y = 210)

    def to_modify_pwd(self):
        modify_pwd_page.init()


class ModifyPwdPage:
    def __init__(self):
        self.label_actual_pwd = ctk.CTkLabel(window, text = "Actual password", font = ("Trebuchet MS", 20), text_color = text_color)
        self.label_new_pwd_1 = ctk.CTkLabel(window, text = "Enter your new password", font = ("Trebuchet MS", 20), text_color = text_color)
        self.label_new_pwd_2 = ctk.CTkLabel(window, text = "Confirm your password", font = ("Trebuchet MS", 20), text_color = text_color)
        self.label_pwd_change_ok = ctk.CTkLabel(window, text = "Password changed successfully !", text_color = "green", font = ("Trebuchet MS", 20))
        self.label_error_actual_pwd_wrong = ctk.CTkLabel(window, text = "The actual password is wrong !", text_color = "red", font = ("Trebuchet MS", 20))
        self.label_error_new_pwd_diff = ctk.CTkLabel(window, text = "The passwords are not the same !",text_color = "red", font = ("Trebuchet MS", 20))
        self.label_error_empty_pwd = ctk.CTkLabel(window, text = "The new password must not be empty !", text_color = "red", font = ("Trebuchet MS", 20))
        self.entry_actual_pwd = ctk.CTkEntry(window, width = 600, height = 75, corner_radius = 20,font = ("Trebuchet MS", 20), border_width = 1, border_color = text_color, fg_color = primary_color_hover, text_color = text_color, show="✱")
        self.entry_new_pwd_1 = ctk.CTkEntry(window, width = 600, height = 75, corner_radius = 20,font = ("Trebuchet MS", 20), border_width = 1, border_color = text_color, fg_color = primary_color_hover, text_color = text_color, show="✱")
        self.entry_new_pwd_2 = ctk.CTkEntry(window, width = 600, height = 75, corner_radius = 20,font = ("Trebuchet MS", 20), border_width = 1, border_color =text_color, fg_color = primary_color_hover, text_color = text_color, show="✱")
        self.button_back = ctk.CTkButton(window, width = 200, height = 50, corner_radius = 30,text = "Back", font = ("Trebuchet MS", 20), command=self.to_login_page, border_width = 1, border_color = text_color, hover_color = secondary_color_hover, fg_color = secondary_color, text_color = text_color)
        self.button_modify = ctk.CTkButton(window, width = 50, height = 50, corner_radius = 30,text = "Modify your password", font = ("Trebuchet MS", 20), command=self.modify_pwd, border_width = 1, border_color = text_color, hover_color = secondary_color_hover, fg_color = secondary_color, text_color = text_color)

    def init(self):
        window.geometry("800x550")
        login_page.option_menu_palet.place_forget()
        login_page.label_input.place_forget()
        login_page.entry_input.place_forget()
        login_page.button_new_pwd.place_forget()
        login_page.button_login.place_forget()
        login_page.label_error_login.place_forget()
        self.label_error_empty_pwd.place_forget()
        self.label_actual_pwd.place(x = 110, y = 10)
        self.entry_actual_pwd.place(relx = 0.5, anchor = "n", y = 55)
        self.label_new_pwd_1.place(x = 110, y = 140)
        self.entry_new_pwd_1.place(relx = 0.5, anchor = "n", y = 185)
        self.label_new_pwd_2.place(x = 110, y = 270)
        self.entry_new_pwd_2.place(relx = 0.5, anchor = "n", y = 315)
        self.button_back.place(x = 100, y = 440)
        self.button_modify.place(x = 700, anchor = "ne", y = 440)

    def modify_pwd(self):
        global password
        actual = self.entry_actual_pwd.get()
        new_pwd_1 = self.entry_new_pwd_1.get()
        new_pwd_2 = self.entry_new_pwd_2.get()
        if hashlib.md5(actual.encode()).hexdigest() == password:
            if hashlib.md5(new_pwd_1.encode()).hexdigest() == hashlib.md5(new_pwd_2.encode()).hexdigest():
                if new_pwd_1 != "":
                    password = hashlib.md5(new_pwd_2.encode()).hexdigest()
                    self.label_error_actual_pwd_wrong.place_forget()
                    self.label_error_new_pwd_diff.place_forget()
                    self.label_error_empty_pwd.place_forget()
                    login_page.label_error_login.place_forget()
                    self.label_pwd_change_ok.place(relx = 0.5, anchor = "n", y = 395)
                    self.entry_actual_pwd.delete(0, "end")
                    self.write_pwd(password)
                else:
                    self.label_error_empty_pwd.place(relx = 0.5, anchor = "n", y = 395)
            else:
                self.label_pwd_change_ok.place_forget()
                self.label_error_actual_pwd_wrong.place_forget()
                self.label_error_empty_pwd.place_forget()
                login_page.label_error_login.place_forget()
                self.label_error_new_pwd_diff.place(relx = 0.5, anchor = "n", y = 395)
        else:
            self.label_pwd_change_ok.place_forget()
            self.label_error_new_pwd_diff.place_forget()
            self.label_error_empty_pwd.place_forget()
            login_page.label_error_login.place_forget()
            self.label_error_actual_pwd_wrong.place(relx = 0.5, anchor = "n", y = 395)

    def write_pwd(self, pwd):
        file_rewrite = open("password.txt", "w")
        file_rewrite.write(pwd)
        file_rewrite.close()

    def to_login_page(self):
        login_page.init()


class MenuPage:
    def __init__(self):
        pass


class CryptDecryptPage:
    def __init__(self):
        pass


class RandomPasswordGeneratorPage:
    def __init__(self):
        pass


class PasswordsManagerPage:
    def __init__(self):
        pass


def change_palet(choice):
    global primary_color, primary_color_hover, secondary_color, secondary_color_hover, text_color, text_color_hover
    if choice == "Black" or choice == "Noir":
        primary_color = "#000000"
        primary_color_hover = "#1a1a1a"
        secondary_color = "#2b2b2b"
        secondary_color_hover = "#3a3a3a"
        text_color = "#ffffff"
        text_color_hover = "#e8e8e8"
    elif choice == "White" or choice == "Blanc":
        primary_color = "#FFFFFF"
        primary_color_hover = "#EDECEC"
        secondary_color = "#DBDBDB"
        secondary_color_hover = "#D3D3D3"
        text_color="#000000"
        text_color_hover="#4C4C4C"
    elif choice == "By default" or choice == "Par défault":
        primary_color = "#33365c"
        primary_color_hover = "#242642"
        secondary_color = "#b3193d"
        secondary_color_hover = "#941835"
        text_color = "#e7ffee"
        text_color_hover = "#cccfcd"
    elif choice == "Black and Red" or choice == "Noir et Rouge":
        primary_color = "#1c1626"
        primary_color_hover = "#38343e"
        secondary_color = "#ff2961"
        secondary_color_hover = "#db2252"
        text_color = "#fefffb"
        text_color_hover = "#e1e1e1"
    elif choice == "Grey and Red" or choice == "Gris et Rouge":
        primary_color = "#afbfd2"
        primary_color_hover = "#9da8b6"
        secondary_color = "#9e2835"
        secondary_color_hover = "#bd3140"
        text_color = "#ffffff"
        text_color_hover = "#e8e8e8"
    elif choice == "Blue and Brown" or choice == "Bleu et Marron":
        primary_color = "#4396bf"
        primary_color_hover = "#62acd0"
        secondary_color = "#663733"
        secondary_color_hover = "#7f4c48"
        text_color = "#212133"
        text_color_hover = "#424253"
    elif choice == "Blue and Orange" or choice == "Bleu et Orange":
        primary_color = "#272946"
        primary_color_hover = "#404375"
        secondary_color = "#eda031"
        secondary_color_hover = "#d58f2b"
        text_color = "#e7ffee"
        text_color_hover = "#d5ecdc"
    elif choice == "Black and Blue" or choice == "Noir et Bleu":
        primary_color = "#08001f"
        primary_color_hover = "#1a0066"
        secondary_color = "#444d84"
        secondary_color_hover = "#6570b3"
        text_color = "#b2d5d1"
        text_color_hover = "#9fbdba"
    elif choice == "Green and Orange" or choice == "Vert et Orange":
        primary_color = "#314e52"
        primary_color_hover = "#446c71"
        secondary_color = "#f2a154"
        secondary_color_hover = "#d8904b"
        text_color = "#d3d3d3"
        text_color_hover = "#c0c0c0"
    elif choice == "White and Blue" or choice == "Blanc et Bleu":
        primary_color = "#fefff2"
        primary_color_hover = "#edeee4"
        secondary_color = "#8e9ce9"
        secondary_color_hover = "#adb7ec"
        text_color = "#10121c"
        text_color_hover = "#3a3c47"
    elif choice == "Blue and Yellow" or choice == "Bleu et Jaune":
        primary_color = "#174977"
        primary_color_hover = "#113455"
        secondary_color = "#ddab4f"
        secondary_color_hover = "#c59640"
        text_color = "#e9d5ba"
        text_color_hover = "#c6b59d"
    elif choice == "Burgundy and Black" or choice == "Bordeaux et Noir":
        primary_color = "#6f0b3e"
        primary_color_hover = "#4b082a"
        secondary_color = "#232323"
        secondary_color_hover = "#303030"
        text_color = "#e5e5e5"
        text_color_hover = "#d1d1d1"
    apply_changes()

def apply_changes():
    window.configure(fg_color=primary_color)
    login_page.label_input.configure(text_color=text_color)
    login_page.entry_input.configure(border_color=text_color, fg_color=primary_color_hover, text_color=text_color)
    login_page.button_login.configure(border_color=text_color, hover_color=secondary_color_hover, fg_color=secondary_color, text_color=text_color)
    login_page.button_new_pwd.configure(border_color=text_color, hover_color=secondary_color_hover, fg_color=secondary_color, text_color=text_color)
    login_page.switch_language.configure(progress_color=text_color, button_hover_color=text_color_hover, fg_color=secondary_color, button_color=text_color, text_color=text_color)
    login_page.option_menu_palet.configure(fg_color=primary_color_hover, bg_color=primary_color, button_color=secondary_color, button_hover_color=secondary_color_hover, dropdown_fg_color=primary_color_hover, dropdown_hover_color=secondary_color, dropdown_text_color=text_color, text_color=text_color)
    change_switch_color(login_page.switch_language)
    modify_pwd_page.label_actual_pwd.configure(text_color=text_color)
    modify_pwd_page.label_new_pwd_1.configure(text_color=text_color)
    modify_pwd_page.label_new_pwd_2.configure(text_color=text_color)
    modify_pwd_page.entry_actual_pwd.configure(border_color=text_color, fg_color=primary_color_hover, text_color=text_color)
    modify_pwd_page.entry_new_pwd_1.configure(border_color=text_color, fg_color=primary_color_hover, text_color=text_color)
    modify_pwd_page.entry_new_pwd_2.configure(border_color=text_color, fg_color=primary_color_hover, text_color=text_color) 
    modify_pwd_page.button_back.configure(border_color=text_color, hover_color=secondary_color_hover, fg_color=secondary_color, text_color=text_color)
    modify_pwd_page.button_modify.configure(border_color=text_color, hover_color=secondary_color_hover, fg_color=secondary_color, text_color=text_color)

    # label_input_crypt_decrypt.configure(text_color=text_color)
    # label_output.configure(text_color=text_color)
    # label_enter_key.configure(text_color=text_color)
    # label_input_rpg.configure(text_color=text_color)
    # label_val_slide.configure(text_color=text_color)
    # entry_key_crypt.configure(border_color=text_color, fg_color=primary_color_hover, text_color=text_color)
    # button_crypt.configure(border_color=text_color, hover_color=secondary_color_hover, fg_color=secondary_color, text_color=text_color)
    # button_decrypt.configure(border_color=text_color, hover_color=secondary_color_hover, fg_color=secondary_color, text_color=text_color)
    # button_gen.configure(border_color=text_color, hover_color=secondary_color_hover, fg_color=secondary_color, text_color=text_color)
    # button_try_pwd.configure(border_color=text_color, hover_color=secondary_color_hover, fg_color=secondary_color, text_color=text_color)
    # button_menu.configure(border_color=text_color, hover_color=secondary_color_hover, fg_color=secondary_color, text_color=text_color)
    # button_pwd_gen.configure(border_color=text_color, hover_color=secondary_color_hover, fg_color=secondary_color, text_color=text_color)
    # button_crypt_decrypt.configure(border_color=text_color, hover_color=secondary_color_hover, fg_color=secondary_color, text_color=text_color)
    # button_manage.configure(border_color=text_color, hover_color=secondary_color_hover, fg_color=secondary_color, text_color=text_color)
    # button_login_page.configure(border_color=text_color, hover_color=secondary_color_hover, fg_color=secondary_color, text_color=text_color)
    # text_box_input_crypt_decrypt.configure(fg_color=primary_color_hover, border_color=text_color, text_color=text_color)
    # text_box_output_crypt_decrypt.configure(fg_color=primary_color_hover, border_color=text_color, text_color=text_color)
    # text_box_input_manage.configure(fg_color=primary_color_hover, border_color=text_color, text_color=text_color)
    # text_box_input_rpg.configure(fg_color=primary_color_hover, border_color=text_color, text_color=text_color)
    # text_box_output_rpg.configure(fg_color=primary_color_hover, border_color=text_color, text_color=text_color)
    # slider_rpg.configure(fg_color=primary_color_hover, button_color=text_color, button_hover_color=text_color_hover, progress_color=secondary_color)
    # switch.configure(progress_color=text_color, button_hover_color=text_color_hover, fg_color=secondary_color, button_color=text_color, text_color=text_color)

def change_switch_color(switch_name):
    if switch_name.get() == 0:
        switch_name.configure(button_color=text_color, button_hover_color=text_color_hover)
    else:
        switch_name.configure(button_color=secondary_color, button_hover_color=secondary_color_hover)

def destroy():
    window.destroy()


if __name__ == "__main__":

    #? Appearance
    primary_color = "#33365c"
    primary_color_hover = "#242642"
    secondary_color = "#b3193d"
    secondary_color_hover = "#941835"
    text_color = "#e7ffee"
    text_color_hover = "#cccfcd"
    ctk.set_appearance_mode("dark")

    #? Window
    window = ctk.CTk()
    window.title("Login")
    window.iconbitmap("./icons/icon Login.ico")
    window.geometry("800x400+240+80")
    window.configure(background = "black", fg_color = primary_color)
    window.resizable(width = False, height = False)

    img_pwd_gen = ctk.CTkImage(light_image = Image.open("./icons/icon pwd-gen.png"), size = (30, 30))
    img_crypt = ctk.CTkImage(light_image = Image.open("./icons/icon Crypt Decrypt.ico"), size = (30, 30))
    img_manage = ctk.CTkImage(light_image = Image.open("./icons/icon manage.png"), size = (30, 30))

    login_page = LoginPage()
    modify_pwd_page = ModifyPwdPage()
    login_page.init()
    file_read = open("password.txt", "r")
    password = file_read.read()
    file_read.close()

    window.bind("<Return>", lambda _:login_page.login())
    window.bind("<Escape>", lambda _: destroy())

    window.mainloop()