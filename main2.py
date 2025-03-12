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
        self.label_input = ctk.CTkLabel(window, text=widgets_text[0][0], font=("Trebuchet MS", 25), text_color=text_color)
        self.label_error_login = ctk.CTkLabel(window, text=widgets_text[0][1], text_color="red", font=("Trebuchet MS", 25))
        self.entry_input = ctk.CTkEntry(window, width=600, height=100, corner_radius=30, font=("Trebuchet MS", 25), border_width=1, border_color=text_color, fg_color = primary_color_hover, text_color = text_color, show="✱")
        self.button_login = ctk.CTkButton(window, width = 258, height = 60, corner_radius = 30,text = widgets_text[0][2], font = ("Trebuchet MS", 25), border_width = 1, command=self.login, border_color = text_color, hover_color = secondary_color_hover, fg_color = secondary_color, text_color = text_color)
        self.button_new_pwd = ctk.CTkButton( window, width = 50, height = 60, corner_radius = 30,text = widgets_text[0][3], font = ("Trebuchet MS", 25), command=self.to_modify_pwd, border_width = 1, border_color = text_color, hover_color = secondary_color_hover, fg_color = secondary_color, text_color = text_color) 
        self.switch_language = ctk.CTkSwitch(window, switch_height = 30, switch_width = 60, text=widgets_text[0][4], corner_radius = 20, font = ("Trebuchet MS", 20), command=switch_language, progress_color = text_color, button_hover_color = text_color_hover, fg_color = secondary_color)
        self.option_menu_palet = ctk.CTkOptionMenu(window, width=70, height=30, corner_radius=20, values=values_palet, font=("Trebuchet MS", 25), dropdown_font=("Trebuchet MS", 15), command=change_palet, fg_color=primary_color_hover, bg_color=primary_color, button_color=secondary_color, button_hover_color=secondary_color_hover, dropdown_fg_color=primary_color_hover, dropdown_hover_color=secondary_color, dropdown_text_color=text_color, text_color=text_color)

    def init(self):
        global locate
        window.geometry("800x400")
        window.title("Login")
        window.iconbitmap("./icons/icon Login.ico")
        locate = "login_page"
        modify_pwd_page.label_error_empty_pwd.place_forget()
        modify_pwd_page.label_actual_pwd.place_forget()
        modify_pwd_page.entry_actual_pwd.place_forget()
        modify_pwd_page.label_new_pwd_1.place_forget()
        modify_pwd_page.entry_new_pwd_1.place_forget()
        modify_pwd_page.label_new_pwd_2.place_forget()
        modify_pwd_page.entry_new_pwd_2.place_forget()
        modify_pwd_page.button_back.place_forget()
        modify_pwd_page.button_modify.place_forget()
        modify_pwd_page.entry_new_pwd_1.delete(0, 'end')
        modify_pwd_page.entry_new_pwd_2.delete(0, 'end')
        menu_page.button_login_page.place_forget()
        menu_page.button_pwd_gen.place_forget()
        menu_page.button_crypt_decrypt.place_forget()
        menu_page.button_manage.place_forget()
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
            self.to_menu()
            self.entry_input.delete(0, "end")
        else:
            self.entry_input.delete(0, "end")
            self.label_error_login.place(x = 290, y = 210)

    def to_modify_pwd(self):
        modify_pwd_page.init()

    def to_menu(self):
        menu_page.init()


class ModifyPwdPage:
    def __init__(self):
        self.label_actual_pwd = ctk.CTkLabel(window, text = widgets_text[1][0], font = ("Trebuchet MS", 20), text_color = text_color)
        self.label_new_pwd_1 = ctk.CTkLabel(window, text = widgets_text[1][1], font = ("Trebuchet MS", 20), text_color = text_color)
        self.label_new_pwd_2 = ctk.CTkLabel(window, text = widgets_text[1][2], font = ("Trebuchet MS", 20), text_color = text_color)
        self.label_pwd_change_ok = ctk.CTkLabel(window, text = widgets_text[1][3], text_color = "green", font = ("Trebuchet MS", 20))
        self.label_error_actual_pwd_wrong = ctk.CTkLabel(window, text = widgets_text[1][4], text_color = "red", font = ("Trebuchet MS", 20))
        self.label_error_new_pwd_diff = ctk.CTkLabel(window, text = widgets_text[1][5], text_color = "red", font = ("Trebuchet MS", 20))
        self.label_error_empty_pwd = ctk.CTkLabel(window, text = widgets_text[1][6], text_color = "red", font = ("Trebuchet MS", 20))
        self.entry_actual_pwd = ctk.CTkEntry(window, width = 600, height = 75, corner_radius = 20,font = ("Trebuchet MS", 20), border_width = 1, border_color = text_color, fg_color = primary_color_hover, text_color = text_color, show="✱")
        self.entry_new_pwd_1 = ctk.CTkEntry(window, width = 600, height = 75, corner_radius = 20,font = ("Trebuchet MS", 20), border_width = 1, border_color = text_color, fg_color = primary_color_hover, text_color = text_color, show="✱")
        self.entry_new_pwd_2 = ctk.CTkEntry(window, width = 600, height = 75, corner_radius = 20,font = ("Trebuchet MS", 20), border_width = 1, border_color =text_color, fg_color = primary_color_hover, text_color = text_color, show="✱")
        self.button_back = ctk.CTkButton(window, width = 200, height = 50, corner_radius = 30,text = widgets_text[1][7], font = ("Trebuchet MS", 20), command=self.to_login_page, border_width = 1, border_color = text_color, hover_color = secondary_color_hover, fg_color = secondary_color, text_color = text_color)
        self.button_modify = ctk.CTkButton(window, width = 50, height = 50, corner_radius = 30,text = widgets_text[1][8], font = ("Trebuchet MS", 20), command=self.modify_pwd, border_width = 1, border_color = text_color, hover_color = secondary_color_hover, fg_color = secondary_color, text_color = text_color)

    def init(self):
        global locate
        window.geometry("800x550")
        locate = "modify_pwd_page"
        login_page.option_menu_palet.place_forget()
        login_page.label_input.place_forget()
        login_page.entry_input.place_forget()
        login_page.button_new_pwd.place_forget()
        login_page.button_login.place_forget()
        login_page.label_error_login.place_forget()
        self.label_error_empty_pwd.place_forget()
        self.label_pwd_change_ok.place_forget()
        self.label_error_actual_pwd_wrong.place_forget()
        self.label_error_new_pwd_diff.place_forget()
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
        self.button_login_page = ctk.CTkButton(window, width = 80, height = 50, corner_radius = 30, command = self.to_login_page, text = widgets_text[2][0], font = ("Trebuchet MS", 25), border_width = 1, border_color = text_color, hover_color = secondary_color_hover, fg_color = secondary_color, text_color = text_color)
        self.button_crypt_decrypt = ctk.CTkButton(window, width = 370, height = 40, corner_radius = 30, command = self.to_crypt_decrypt_software, text = widgets_text[2][1], font = ("Trebuchet MS", 25), border_width = 1, border_color = text_color, hover_color = secondary_color_hover, fg_color = secondary_color, text_color = text_color, image = img_crypt)
        self.button_pwd_gen = ctk.CTkButton(window, width = 370, height = 40, corner_radius = 30, command = self.to_pwd_gen, text = widgets_text[2][2], font = ("Trebuchet MS", 25), border_width = 1, border_color = text_color, hover_color = secondary_color_hover, fg_color = secondary_color, text_color = text_color, image = img_pwd_gen)
        self.button_manage = ctk.CTkButton(window, width = 370, height = 40, corner_radius = 30, command = self.to_manage_pwd, text = widgets_text[2][3], font = ("Trebuchet MS", 25), border_width = 1, border_color = text_color, hover_color = secondary_color_hover, fg_color = secondary_color, text_color = text_color, image = img_manage)
        
    def init(self):
        global locate
        window.geometry("800x400")
        window.title("Menu")
        window.iconbitmap("./icons/icon Menu.ico")
        locate = "menu_page"
        self.button_crypt_decrypt.place(relx = 0.5, anchor = "n", y = 60)
        self.button_pwd_gen.place(relx = 0.5, anchor = "n", y = 140)
        self.button_manage.place(relx = 0.5, anchor = "n", y = 220)
        self.button_login_page.place(relx = 0.5, anchor = "n", y = 320)
        login_page.switch_language.place(x = 650, y = 10)
        login_page.option_menu_palet.place(x=10, y=10)
        crypt_decrypt_page.label_input_crypt_decrypt.place_forget()
        crypt_decrypt_page.label_output.place_forget()
        crypt_decrypt_page.label_enter_key.place_forget()
        crypt_decrypt_page.button_crypt.place_forget()
        crypt_decrypt_page.button_decrypt.place_forget()
        crypt_decrypt_page.entry_key_crypt.place_forget()
        crypt_decrypt_page.textbox_input_crypt_decrypt.place_forget()
        crypt_decrypt_page.textbox_output_crypt_decrypt.place_forget()
        crypt_decrypt_page.button_menu.place_forget()
        crypt_decrypt_page.entry_key_crypt.delete(0, 'end')
        crypt_decrypt_page.textbox_input_crypt_decrypt.delete("0.0", 'end')
        crypt_decrypt_page.textbox_output_crypt_decrypt.delete("0.0", 'end')
        random_password_generator_page.label_input_rpg.place_forget()
        random_password_generator_page.label_val_slide.place_forget()
        random_password_generator_page.label_pwd_vulnerable.place_forget()
        random_password_generator_page.label_pwd_weak.place_forget()
        random_password_generator_page.label_pwd_strong.place_forget()
        random_password_generator_page.button_gen.place_forget()
        random_password_generator_page.button_try_pwd.place_forget()
        random_password_generator_page.textbox.place_forget()
        random_password_generator_page.slider_rpg.place_forget()
        random_password_generator_page.button_menu.place_forget()
        passwords_manager_page.textbox_manage.place_forget()
        passwords_manager_page.button_menu.place_forget()

    def to_login_page(self):
        login_page.init()

    def to_crypt_decrypt_software(self):
        crypt_decrypt_page.init()

    def to_pwd_gen(self):
        random_password_generator_page.init()

    def to_manage_pwd(self):
        passwords_manager_page.init()


class CryptDecryptPage:
    def __init__(self):
        self.label_input_crypt_decrypt = ctk.CTkLabel(window, width = 100, height = 25, corner_radius = 20, text = widgets_text[3][0], font = ("Trebuchet MS", 25), text_color = text_color)
        self.label_output = ctk.CTkLabel(window, width = 100, height = 25, corner_radius = 20, text = widgets_text[3][1], font = ("Trebuchet MS", 25), text_color = text_color)
        self.label_enter_key = ctk.CTkLabel(window, text = widgets_text[3][2], font = ("Trebuchet MS", 25), text_color = text_color)
        self.button_crypt = ctk.CTkButton(window, width = 200, height = 100, corner_radius = 20, text = widgets_text[3][3], command = self.crypt, font = ("Trebuchet MS", 25), border_width = 1, border_color = text_color, hover_color = secondary_color_hover, fg_color = secondary_color, text_color = text_color)
        self.button_decrypt = ctk.CTkButton(window, width = 200, height = 100, corner_radius = 20, text = widgets_text[3][4], command = self.decrypt, font = ("Trebuchet MS", 25), border_width = 1, border_color = text_color, hover_color = secondary_color_hover, fg_color = secondary_color, text_color = text_color)
        self.entry_key_crypt = ctk.CTkEntry(window, width = 300, height = 80, corner_radius = 20, font = ("Arila", 25),border_width = 1, border_color = text_color, fg_color = primary_color_hover, text_color=text_color)
        self.textbox_input_crypt_decrypt = ctk.CTkTextbox(window, width = 300, height = 400, corner_radius = 20, font = ("Trebuchet MS", 25), fg_color = primary_color_hover, border_color = text_color, border_width = 1, text_color = text_color)
        self.textbox_output_crypt_decrypt = ctk.CTkTextbox(window, width = 300, height = 400, corner_radius = 20, font = ("Trebuchet MS", 25), fg_color = primary_color_hover, border_color = text_color, border_width = 1, text_color = text_color)
        self.button_menu = ctk.CTkButton(window, width = 10, corner_radius = 20, command = self.to_menu_page, text = "Menu", font = ("Trebuchet MS", 20), border_width = 1, border_color = text_color, hover_color = secondary_color_hover, fg_color = secondary_color, text_color = text_color)

    def init(self):
        global locate
        window.geometry("950x460")
        window.title("Crypt / Decrypt")
        window.iconbitmap("./Icons/icon Crypt Decrypt.ico")
        locate = "crypt_decrypt_page"
        menu_page.button_login_page.place_forget()
        menu_page.button_crypt_decrypt.place_forget()
        menu_page.button_pwd_gen.place_forget()
        menu_page.button_manage.place_forget()
        login_page.switch_language.place_forget()
        login_page.option_menu_palet.place_forget()
        self.label_input_crypt_decrypt.place(x = 102, y = 10)
        self.textbox_input_crypt_decrypt.place(x = 10, y = 50)
        self.button_crypt.place(relx = 0.5, anchor = "n", y = 50)
        self.label_enter_key.place(relx = 0.5, anchor = "n", y = 180)
        self.entry_key_crypt.place(relx = 0.5, anchor = "n", y = 215)
        self.button_decrypt.place(relx = 0.5, anchor = "n", y = 345)
        self.label_output.place(x = 738, y = 10)
        self.textbox_output_crypt_decrypt.place(x = 640, y = 50)
        self.button_menu.place(x = 10, y = 10)
        
    def crypt(self):
        global alph
        result = ""
        key = self.entry_key_crypt.get()
        message = self.textbox_input_crypt_decrypt.get("0.0", "end")
        random.seed(key)
        alphabet_shuffle = alph.copy()
        random.shuffle(alphabet_shuffle)
        for i in message:
            for j in range(len(alph)):
                if i == alph[j]:
                    result += alphabet_shuffle[j]
            self.textbox_output_crypt_decrypt.delete("0.0", "end")
            self.textbox_output_crypt_decrypt.insert("0.0", result)

    def decrypt(self):
        global alph
        result = ""
        key = self.entry_key_crypt.get()
        message = self.textbox_input_crypt_decrypt.get("0.0", "end")
        random.seed(key)
        alphabet_shuffle = alph.copy()
        random.shuffle(alphabet_shuffle)
        for i in message:
            for j in range(len(alph)):
                if i == alphabet_shuffle[j]:
                    result += alph[j]
            self.textbox_output_crypt_decrypt.delete("0.0", "end")
            self.textbox_output_crypt_decrypt.insert("0.0", result)

    def to_menu_page(self):
        menu_page.init()


class RandomPasswordGeneratorPage:
    def __init__(self):
        self.label_input_rpg = ctk.CTkLabel(window, width = 10, height = 30, text = widgets_text[4][0], font = ("Trebuchet MS", 20), text_color = text_color)
        self.label_val_slide = ctk.CTkLabel(window, width = 50, height = 25, corner_radius = 20, text = "20", font = ("Trebuchet MS", 20), text_color = text_color)
        self.label_pwd_vulnerable = ctk.CTkLabel(window, text = widgets_text[4][1], text_color = "red", font = ("Trebuchet MS", 20))
        self.label_pwd_weak = ctk.CTkLabel(window, text = widgets_text[4][2], text_color = "orange", font = ("Trebuchet MS", 20))
        self.label_pwd_strong = ctk.CTkLabel(window, text = widgets_text[4][3], text_color = "green", font = ("Trebuchet MS", 20))
        self.button_gen = ctk.CTkButton(window, height = 40, corner_radius = 30, text = widgets_text[4][4], command = self.action_gen_button, font = ("Trebuchet MS", 13), hover_color = secondary_color_hover, border_width = 1, border_color = text_color, fg_color = secondary_color, text_color = text_color)
        self.button_try_pwd = ctk.CTkButton(window, height = 40, corner_radius = 30, text = widgets_text[4][5], command = self.action_test_button, font = ("Trebuchet MS", 13), hover_color = secondary_color_hover, border_width = 1, border_color = text_color, fg_color = secondary_color, text_color = text_color)
        self.textbox = ctk.CTkTextbox(window, width = 300, height = 93, corner_radius = 20, font = ("Trebuchet MS", 20), border_width = 1, border_color = text_color, fg_color = primary_color_hover, text_color = text_color)
        self.slider_rpg = ctk.CTkSlider(window, width = 300, from_ = 1, to = 40, command = self.slider_event_rpg, button_hover_color = secondary_color_hover, fg_color = secondary_color, button_color = secondary_color)
        self.button_menu = ctk.CTkButton(window, width = 10, corner_radius = 20, text = "Menu", command = self.to_menu_page, font = ("Trebuchet MS", 13), hover_color = secondary_color_hover, border_width = 1, border_color = text_color, fg_color = secondary_color, text_color = text_color)

    def init(self):
        global locate
        window.iconbitmap("./icons/icon-pwd-gen.ico")
        window.geometry("330x350")
        locate = "pwd_gen_page"
        menu_page.button_crypt_decrypt.place_forget()
        menu_page.button_pwd_gen.place_forget()
        menu_page.button_manage.place_forget()
        menu_page.button_login_page.place_forget()
        login_page.option_menu_palet.place_forget()
        self.button_menu.place(x = 10, y = 10)
        self.label_input_rpg.place(relx = 0.5, anchor = "n", y = 40)
        self.slider_rpg.place(relx = 0.5, anchor = "n", y = 120)
        self.label_val_slide.place(relx = 0.5, anchor = "n", y = 143)
        self.button_gen.place(x = 15, y = 173)
        self.textbox.place(relx = 0.5, anchor = "n", y = 235)
        self.button_try_pwd.place(x = 160, y = 173)
        self.label_pwd_strong.place_forget()
        self.label_pwd_vulnerable.place_forget()
        self.label_pwd_weak.place_forget()

    def action_gen_button(self):
        pwd = self.gen(int(self.slider_rpg.get()))
        self.textbox.delete("0.0", "end")
        self.textbox.insert("0.0", pwd)

    def action_test_button(self):
        pwd = self.textbox.get("0.0", "end")
        self.try_pwd(pwd.replace("\n", ""))

    def try_pwd(self, pwd):
        pwd_score = 0
        dico = {}
        for char in all:
            if char in min or char in maj:
                dico[char] = 1
            elif char in num:
                dico[char] = 2
            elif char in symbols:
                dico[char] = 3
        for char in pwd:
            pwd_score += dico[char]
        if pwd_score <= 10 or len(pwd) < 15:
            self.label_pwd_strong.place_forget()
            self.label_pwd_weak.place_forget()
            self.label_pwd_vulnerable.place(relx = 0.5, anchor = "n", y = 90)
        elif 10 > pwd_score <= 20 or 15 >= len(pwd) < 20:
            self.label_pwd_strong.place_forget()
            self.label_pwd_vulnerable.place_forget()
            self.label_pwd_weak.place(relx = 0.5, anchor = "n", y = 90)
        elif pwd_score > 20 or len(pwd) >= 20:
            self.label_pwd_vulnerable.place_forget()
            self.label_pwd_weak.place_forget()
            self.label_pwd_strong.place(relx = 0.5, anchor = "n", y = 90)

    def gen(self, lenght:int) -> str:
        pwd = ""
        for _ in range(lenght):
            pwd += all[random.randint(0, len(all) - 1)]
        self.try_pwd(pwd)
        return pwd

    def slider_event_rpg(self, value=20):
        self.label_val_slide.configure(text=int(value))
        self.textbox.delete("0.0", "end")
        self.textbox.insert("0.0", self.gen(int(value)))

    def to_menu_page(self):
        menu_page.init()


class PasswordsManagerPage:
    def __init__(self):
        self.textbox_manage = ctk.CTkTextbox(window, width = 780, height = 350, font = ("Trebuchet MS", 20), border_width = 1, border_color = text_color, fg_color = primary_color_hover, text_color = text_color)
        self.button_menu = ctk.CTkButton(window, width = 10, corner_radius = 20, text = "Menu", command = self.to_menu_page, font = ("Trebuchet MS", 13), hover_color = secondary_color_hover, border_width = 1, border_color = text_color, fg_color = secondary_color, text_color = text_color)

    def init(self):
        global locate
        window.title("Passwords Manager")
        window.iconbitmap("./icons/icon-manage.ico")
        locate = "passwords_manager_page"
        menu_page.button_crypt_decrypt.place_forget()
        menu_page.button_pwd_gen.place_forget()
        menu_page.button_manage.place_forget()
        menu_page.button_login_page.place_forget()
        login_page.switch_language.place_forget()
        login_page.option_menu_palet.place_forget()
        self.textbox_manage.place(x = 10, y = 40)
        self.button_menu.place(x = 10, y = 5)
        content = open("manage.txt", "r")
        self.textbox_manage.delete(0.0, "end")
        self.textbox_manage.insert(0.0, content.read())
        self.save()

    def save(self):
        manage_text = open("manage.txt", "w")
        manage_text.write(self.textbox_manage.get(0.0, "end"))
        if locate == "passwords_manager_page":
            window.after(1000, self.save)

    def to_menu_page(self):
        menu_page.init()


#? Functions
def return_button():
    if locate == "login_page":
        login_page.login()
    elif locate == "modify_pwd_page":
        modify_pwd_page.modify_pwd()

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
    menu_page.button_login_page.configure(border_color=text_color, hover_color=secondary_color_hover, fg_color=secondary_color, text_color=text_color)
    menu_page.button_pwd_gen.configure(border_color=text_color, hover_color=secondary_color_hover, fg_color=secondary_color, text_color=text_color)
    menu_page.button_crypt_decrypt.configure(border_color=text_color, hover_color=secondary_color_hover, fg_color=secondary_color, text_color=text_color)
    menu_page.button_manage.configure(border_color=text_color, hover_color=secondary_color_hover, fg_color=secondary_color, text_color=text_color)
    crypt_decrypt_page.label_input_crypt_decrypt.configure(text_color=text_color)
    crypt_decrypt_page.label_output.configure(text_color=text_color)
    crypt_decrypt_page.label_enter_key.configure(text_color=text_color)
    crypt_decrypt_page.button_crypt.configure(border_color=text_color, hover_color=secondary_color_hover, fg_color=secondary_color, text_color=text_color)
    crypt_decrypt_page.button_decrypt.configure(border_color=text_color, hover_color=secondary_color_hover, fg_color=secondary_color, text_color=text_color)
    crypt_decrypt_page.button_menu.configure(border_color=text_color, hover_color=secondary_color_hover, fg_color=secondary_color, text_color=text_color)
    crypt_decrypt_page.entry_key_crypt .configure(border_color=text_color, fg_color=primary_color_hover, text_color=text_color)
    crypt_decrypt_page.textbox_input_crypt_decrypt.configure(fg_color=primary_color_hover, border_color=text_color, text_color=text_color)
    crypt_decrypt_page.textbox_output_crypt_decrypt.configure(fg_color=primary_color_hover, border_color=text_color, text_color=text_color)
    random_password_generator_page.label_input_rpg.configure(text_color=text_color)
    random_password_generator_page.label_val_slide.configure(text_color=text_color)
    random_password_generator_page.button_gen.configure(border_color=text_color, hover_color=secondary_color_hover, fg_color=secondary_color, text_color=text_color)
    random_password_generator_page.button_try_pwd.configure(border_color=text_color, hover_color=secondary_color_hover, fg_color=secondary_color, text_color=text_color)
    random_password_generator_page.textbox.configure(fg_color=primary_color_hover, border_color=text_color, text_color=text_color)
    random_password_generator_page.slider_rpg.configure(fg_color=primary_color_hover, button_color=text_color, button_hover_color=text_color_hover, progress_color=secondary_color)
    random_password_generator_page.button_menu.configure(border_color=text_color, hover_color=secondary_color_hover, fg_color=secondary_color, text_color=text_color)
    passwords_manager_page.textbox_manage.configure(fg_color=primary_color_hover, border_color=text_color, text_color=text_color)
    passwords_manager_page.button_menu.configure(border_color=text_color, hover_color=secondary_color_hover, fg_color=secondary_color, text_color=text_color)

def change_switch_color(switch_name):
    if switch_name.get() == 0:
        switch_name.configure(button_color=text_color, button_hover_color=text_color_hover)
    else:
        switch_name.configure(button_color=secondary_color, button_hover_color=secondary_color_hover)

def switch_language():
    global values_palet, index, widgets_text
    if login_page.switch_language.get() == 0:
        index = values_palet.index(login_page.option_menu_palet.get())
        values_palet = ["By default", "Black", "White", "Black and Red", "Grey and Red", "Blue and Brown", "Blue and Orange", "Black and Blue", "Green and Orange", "White and Blue", "Blue and Yellow", "Burgundy and Black"]
        widgets_text = [["Input your password", "Wrong password !", "Login", "Modify your password", "English"], 
                        ["Actual password", "Enter your new password", "Confirm your password", "Password changed successfully !", "The actual password is wrong !", "The passwords are not the same !", "The new password must not be empty !", "Back", "Modify your password"], 
                        ["Lock the session", "Crypt / Decrytp Software", "Random Password Generator", "Passwords Manager"],
                        ["Input", "Output", "Put a key here", "Crypt", "Decrypt"],
                        ["Input the lenght of your password", "Password vulnerable !", "Password weak !", "Password strong !", "Generate a\npassword", "Test the efficiency\nof your password"]]
    elif login_page.switch_language.get() == 1:
        index = values_palet.index(login_page.option_menu_palet.get())
        values_palet = ["Par défault", "Noir", "Blanc", "Noir et Rouge", "Gris et Rouge", "Bleu et Marron", "Bleu et Orange", "Noir et Bleu", "Vert et Orange", "Blanc et Bleu", "Bleu et Jaune", "Bordeaux et Noir"]
        widgets_text = [["Entrez votre mot de passe", "Mauvais mot de passe", "Se connecter", "Modifier votre mot de\npasse", "Français"], 
                        ["Mot de passe actuel", "Entrez votre nouveau mot de passe", "Confirmez votre mot de passe", "Mot de passe modifié avec succès !", "Le mot de passe actuel est incorrect !", "Les mots de passe ne sont pas les mêmes !", "Le nouveau mot de passe ne doit pas être vide !", "Retour", "Modifier votre mot de passe"],
                        ["Verrouiller la session", "Application de Chiffrage / Déchiffrage", "Générateur de Mots de Passe Aléatoire", "Gestionnaire de Mot de Passe"],
                        ["Entrée", "Sortie", "Entrez une clé ici", "Chiffrer", "Déchiffrer"],
                        ["Entrez la longueur de votre mot de\npasse", "Mot de passe vulnérable !", "Mot de passe faible !", "Mot de passe fort !", "Générer un\nmot de passe", "Tester l'efficacité de\nvotre mot de passe"]]
    apply_changes_language()
    change_switch_color(login_page.switch_language)

def apply_changes_language():
    login_page.option_menu_palet.configure(values=values_palet)
    login_page.option_menu_palet.set(values_palet[index])
    login_page.label_input.configure(text=widgets_text[0][0])
    login_page.label_error_login.configure(text=widgets_text[0][1])
    login_page.button_login.configure(text=widgets_text[0][2])
    login_page.button_new_pwd.configure(text=widgets_text[0][3])
    login_page.switch_language.configure(text=widgets_text[0][4])
    modify_pwd_page.label_actual_pwd.configure(text=widgets_text[1][0])
    modify_pwd_page.label_new_pwd_1.configure(text=widgets_text[1][1])
    modify_pwd_page.label_new_pwd_2.configure(text=widgets_text[1][2])
    modify_pwd_page.label_pwd_change_ok.configure(text=widgets_text[1][3])
    modify_pwd_page.label_error_actual_pwd_wrong.configure(text=widgets_text[1][4])
    modify_pwd_page.label_error_new_pwd_diff.configure(text=widgets_text[1][5])
    modify_pwd_page.label_error_empty_pwd.configure(text=widgets_text[1][6]) 
    modify_pwd_page.button_back.configure(text=widgets_text[1][7])
    modify_pwd_page.button_modify.configure(text=widgets_text[1][8])
    menu_page.button_login_page.configure(text=widgets_text[2][0])
    menu_page.button_crypt_decrypt.configure(text=widgets_text[2][1])
    menu_page.button_pwd_gen.configure(text=widgets_text[2][2])
    menu_page.button_manage.configure(text=widgets_text[2][3])
    crypt_decrypt_page.label_input_crypt_decrypt.configure(text=widgets_text[3][0])
    crypt_decrypt_page.label_output.configure(text=widgets_text[3][1])
    crypt_decrypt_page.label_enter_key.configure(text=widgets_text[3][2])
    crypt_decrypt_page.button_crypt.configure(text=widgets_text[3][3])
    crypt_decrypt_page.button_decrypt.configure(text=widgets_text[3][4])
    random_password_generator_page.label_input_rpg.configure(text=widgets_text[4][0])
    random_password_generator_page.label_pwd_vulnerable.configure(text=widgets_text[4][1])
    random_password_generator_page.label_pwd_weak.configure(text=widgets_text[4][2])
    random_password_generator_page.label_pwd_strong.configure(text=widgets_text[4][3]) 
    random_password_generator_page.button_gen.configure(text=widgets_text[4][4])
    random_password_generator_page.button_try_pwd.configure(text=widgets_text[4][5])

def destroy():
    window.destroy()


if __name__ == "__main__":

    #? Appearance
    ctk.set_appearance_mode("dark")
    primary_color = "#33365c"
    primary_color_hover = "#242642"
    secondary_color = "#b3193d"
    secondary_color_hover = "#941835"
    text_color = "#e7ffee"
    text_color_hover = "#cccfcd"

    #? Window
    window = ctk.CTk()
    window.title("Login")
    window.iconbitmap("./icons/icon Login.ico")
    window.geometry("800x400+240+80")
    window.configure(background = "black", fg_color = primary_color)
    window.resizable(width = False, height = False)

    #? Vars
    img_pwd_gen = ctk.CTkImage(light_image=Image.open("./icons/icon pwd-gen.png"), size=(30, 30))
    img_crypt = ctk.CTkImage(light_image=Image.open("./icons/icon Crypt Decrypt.ico"), size=(30, 30))
    img_manage = ctk.CTkImage(light_image=Image.open("./icons/icon manage.png"), size=(30, 30))

    values_palet = ["By default", "Black", "White", "Black and Red", "Grey and Red", "Blue and Brown", "Blue and Orange", "Black and Blue", "Green and Orange", "White and Blue", "Blue and Yellow", "Burgundy and Black"]
    locate = "login_page"
    widgets_text = [["Input your password", "Wrong password !", "Login", "Modify your password", "English"], 
                    ["Actual password", "Enter your new password", "Confirm your password", "Password changed successfully !", "The actual password is wrong !", "The passwords are not the same !", "The new password must not be empty !", "Back", "Modify your password"],
                    ["Lock the session", "Crypt / Decrypt Software", "Random Passwords Generator", "Password Manager"],
                    ["Input", "Output", "Put a key here", "Crypt", "Decrypt"],
                    ["Input the lenght of your password", "Password vulnerable !", "Password weak !", "Password strong !", "Generate a\npassword", "Test the efficiency\nof your password"]]
    


    alph = []
    for i in range(32, 127):
        alph.append(chr(i))
    carac_accent = ["€", "é", "è", "ê", "ë", "à", "â", "ù", "û", "ü", "ô", "î", "ç"]
    alph.extend(carac_accent)

    min = "abcdefghijklmnopqrstuvwxyz"
    maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = "0123456789"
    symbols = "{}()[]/|.!?,;:+-*%^=€$£_&#@ "
    all = min + maj + num + symbols

    file_read = open("password.txt", "r")
    password = file_read.read()
    file_read.close()

    login_page = LoginPage()
    modify_pwd_page = ModifyPwdPage()
    menu_page = MenuPage()
    crypt_decrypt_page = CryptDecryptPage()
    random_password_generator_page = RandomPasswordGeneratorPage()
    passwords_manager_page = PasswordsManagerPage()
    login_page.init()

    #? Binds
    window.bind("<Return>", lambda _:return_button())
    window.bind("<Escape>", lambda _: destroy())

    #? Mainloop
    window.mainloop()