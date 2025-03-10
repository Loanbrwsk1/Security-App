"""
@auhtor : Loan BOROWSKI
"""

#? Imports
from PIL import Image
import customtkinter as ctk
import random as rd
import hashlib

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

#? Functions
def return_button():
    global input_rpg
    if return_login == True:
        login()
    elif return_modify_pwd == True:
        modify_pwd()

def switch_languages():
    global state_switch_language
    if switch_language.get() == 0:
        change_switch_color(switch_language)
        state_switch_language = False
        
        #? Login
        switch_language.configure(text = "English")
        label_input.configure(text = "Input your password")
        label_actual_pwd.configure(text = "Actual password")
        label_new_pwd_1.configure(text = "Enter your new password")
        label_new_pwd_2.configure(text = "Confirm your password")
        label_pwd_change_ok.configure(text = "Password changed successfully !")
        label_error_login.configure(text = "Wrong password !")
        label_error_actual_pwd_wrong.configure(text = "The actual password is wrong !")
        label_error_space.configure(text = "Password must not contain spaces !")
        label_error_new_pwd_diff.configure(text = "The passwords are not the same !")
        label_error_empty_pwd.configure(text = "The new password must not be empty !")
        button_login.configure(text = "Login")
        button_new_pwd.configure(text = "Modify your password")
        button_back.configure(text = "Back")
        button_modify.configure(text = "Modify your password")
        button_crypt_decrypt.configure(text = "Crypt / Decrypt Software")
        button_pwd_gen.configure(text = "Random Password Generator")
        button_manage.configure(text = "Manage your passwords")
        button_login_page.configure(text = "Lock the session")
        palet_name = option_menu_palet.get()
        option_menu_palet.configure(values=values)
        option_menu_palet.set(values[values_fr.index(palet_name)])
        #? Crypt Decrypt
        label_input_crypt_decrypt.configure(text = "Input")
        label_output.configure(text = "Output")
        label_enter_key.configure(text = "Put a key here")
        button_crypt.configure(text = "Crypt")
        button_decrypt.configure(text = "Decrypt")
        
        #? Random Password Generator
        label_error_space_rpg.configure(text = "Password must not contain space !")
        label_pin_strong.configure(text = "PIN strong !")
        label_pin_weak.configure(text = "PIN weak !")
        label_pin_vulnerable.configure(text = "PIN vulnerable !")
        label_pwd_strong.configure(text = "Password strong !")
        label_pwd_weak.configure(text = "Password weak !")
        label_pwd_vulnerable.configure(text = "Password vulnerable !")
        label_input_rpg.configure(text = "Input the lenght of your password", font = ("Trebuchet MS", 20))
        button_gen.configure(text = "Generate a\npassword")
        button_try_pwd.configure(text = "Test the effectiveness\nof your password")
        if switch.get() == 0:
            switch.configure(text = "Pwd")
    else:
        change_switch_color(switch_language)
        state_switch_language = True
        
        #? Login
        switch_language.configure(text = "Français")
        label_input.configure(text = "Entrer votre mot de passe")
        label_actual_pwd.configure(text = "Mot de passe actuel")
        label_new_pwd_1.configure(text = "Entrer votre nouveau mot de passe")
        label_new_pwd_2.configure(text = "Confirmer votre mot de passe")
        label_pwd_change_ok.configure(text = "Mot de passe changé avec succès !")
        label_error_login.configure(text = "Mauvais mot de passe !")
        label_error_actual_pwd_wrong.configure(text = "Le mot de passe actuel est faux !")
        label_error_space.configure(text = "Le mot de passe ne doit pas contenir d'espaces !")
        label_error_new_pwd_diff.configure(text = "Les mots de passe ne sont pas les mêmes !")
        label_error_empty_pwd.configure(text = "Le nouveau mot de passe ne doit pas être vide !")
        button_login.configure(text = "Se connecter")
        button_new_pwd.configure(text = "Modifier votre mot de\npasse")
        button_back.configure(text = "Retour")
        button_modify.configure(text = "Modifier votre mot de passe")
        button_crypt_decrypt.configure(text = "Logiciel de Cryptage / Décrytpage")
        button_pwd_gen.configure(text = "Générateur de mot de passe Aléatoire")
        button_manage.configure(text = "Gérer vos mots de passe")
        button_login_page.configure(text = "Verrouiller la session")
        palet_name = option_menu_palet.get()
        option_menu_palet.configure(values=values_fr)
        option_menu_palet.set(values_fr[values.index(palet_name)])
        
        #? Crypt Decrypt
        label_input_crypt_decrypt.configure(text = "Entrée")
        label_output.configure(text = "Sortie")
        label_enter_key.configure(text = "Entrer une clé ici")
        button_crypt.configure(text = "Crypter")
        button_decrypt.configure(text = "Décrypter")
        
        #? Random Password Generator
        label_error_space_rpg.configure(text = "Le mot de passe ne doit\npas contenir d'espace !")
        label_pin_strong.configure(text = "PIN fort !")
        label_pin_weak.configure(text = "PIN faible !")
        label_pin_vulnerable.configure(text = "PIN vulnérable !")
        label_pwd_strong.configure(text = "Mot de passe fort !")
        label_pwd_weak.configure(text = "Mot de passe faible !")
        label_pwd_vulnerable.configure(text = "Mot de passe vulnérable !")
        label_input_rpg.configure(text = "Entrer la longueur de votre mot de passe", font = ("Trebuchet MS", 17))
        button_gen.configure(text = "Générer un\nmot de passe")
        button_try_pwd.configure(text = "Tester l'efficacité de\nvotre mot de passe")
        if switch.get() == 0:
            switch.configure(text = "Mdp")

def login():
    global password
    input = entry_input.get()
    if hashlib.md5(input.encode()).hexdigest() == password:
        label_input.place_forget()
        entry_input.place_forget()
        button_new_pwd.place_forget()
        button_login.place_forget()
        label_error_login.place_forget()
        menu()
    else:
        entry_input.delete(0, "end")
        label_error_login.place(x = 290, y = 210)

def new_pwd():
    global return_modify_pwd, return_login
    window.geometry("800x550")
    return_modify_pwd, return_login = True, False
    option_menu_palet.place_forget()

    #?Login
    label_input.place_forget()
    entry_input.place_forget()
    button_new_pwd.place_forget()
    button_login.place_forget()
    label_error_login.place_forget()
    label_error_empty_pwd.place_forget()
    label_error_space.place_forget()
    
    #? Modify Password
    label_actual_pwd.place(x = 110, y = 10)
    entry_actual_pwd.place(relx = 0.5, anchor = "n", y = 55)
    label_new_pwd_1.place(x = 110, y = 140)
    entry_new_pwd_1.place(relx = 0.5, anchor = "n", y = 185)
    label_new_pwd_2.place(x = 110, y = 270)
    entry_new_pwd_2.place(relx = 0.5, anchor = "n", y = 315)
    button_back.place(x = 100, y = 440)
    button_modify.place(x = 700, anchor = "ne", y = 440)

def login_page():
    global return_modify_pwd, return_login
    window.geometry("800x400")
    window.iconbitmap("./icons/icon Login.ico")
    return_modify_pwd, return_login = False, True
    if state_switch_language == False:
        window.title("Login")
    else:
        window.title("Se connecter")
    
    #? Modify Password
    label_actual_pwd.place_forget()
    entry_actual_pwd.place_forget()
    label_new_pwd_1.place_forget()
    entry_new_pwd_1.place_forget()
    label_new_pwd_2.place_forget()
    entry_new_pwd_2.place_forget()
    button_back.place_forget()
    button_modify.place_forget()
    entry_input.delete(0, "end")
    entry_actual_pwd.delete(0, "end")
    entry_new_pwd_1.delete(0, "end")
    entry_new_pwd_2.delete(0, "end")
    
    #? Errors
    label_pwd_change_ok.place_forget()
    label_error_login.place_forget()
    label_error_actual_pwd_wrong.place_forget()
    label_error_new_pwd_diff.place_forget()
    label_error_empty_pwd.place_forget()
    label_error_space.place_forget()
    
    #? Menu
    button_crypt_decrypt.place_forget()
    button_pwd_gen.place_forget()
    button_login_page.place_forget()
    button_manage.place_forget()
    
    #? Login
    label_input.place(relx = 0.5, anchor = "n", y = 40)
    entry_input.place(relx = 0.5, anchor = "n", y = 100)
    button_new_pwd.place(x = 100, y = 260)
    button_login.place(x = 440, y = 260)
    switch_language.place(x = 650, y = 10)
    switch_language.configure(switch_height = 30, switch_width = 60)
    option_menu_palet.place(x=10, y=10)

def modify_pwd():
    global password
    actual = entry_actual_pwd.get()
    new_pwd_1 = entry_new_pwd_1.get()
    new_pwd_2 = entry_new_pwd_2.get()
    
    if hashlib.md5(actual.encode()).hexdigest() == password:
        
        if hashlib.md5(new_pwd_1.encode()).hexdigest() == hashlib.md5(new_pwd_2.encode()).hexdigest():
            if new_pwd_1 != "":
                password = hashlib.md5(new_pwd_2.encode()).hexdigest()
                label_error_actual_pwd_wrong.place_forget()
                label_error_new_pwd_diff.place_forget()
                label_error_empty_pwd.place_forget()
                label_error_login.place_forget()
                label_error_space.place_forget()
                label_pwd_change_ok.place(relx = 0.5, anchor = "n", y = 395)
                entry_actual_pwd.delete(0, "end")
                write_pwd(password)
            else:
                label_error_empty_pwd.place(relx = 0.5, anchor = "n", y = 395)
            
        else:
            label_pwd_change_ok.place_forget()
            label_error_actual_pwd_wrong.place_forget()
            label_error_empty_pwd.place_forget()
            label_error_login.place_forget()
            label_error_space.place_forget()
            label_error_new_pwd_diff.place(relx = 0.5, anchor = "n", y = 395)
    else:
        label_pwd_change_ok.place_forget()
        label_error_new_pwd_diff.place_forget()
        label_error_empty_pwd.place_forget()
        label_error_login.place_forget()
        label_error_space.place_forget()
        label_error_actual_pwd_wrong.place(relx = 0.5, anchor = "n", y = 395)

def write_pwd(pwd:str):
    file_rewrite = open("password.txt", "w")
    file_rewrite.write(pwd)
    file_rewrite.close()

def menu():
    global in_manage_pwd
    window.geometry("800x400")
    window.title("Menu")
    window.iconbitmap("./icons/icon Menu.ico")
    label_input.place_forget()
    button_menu.place_forget()
    option_menu_palet.place(x=10, y=10)
    
    #? Crypt Decrypt
    label_input_crypt_decrypt.place_forget()
    text_box_input_crypt_decrypt.place_forget()
    button_crypt.place_forget()
    entry_key_crypt.place_forget()
    button_decrypt.place_forget()
    label_output.place_forget()
    text_box_output_crypt_decrypt.place_forget()
    
    #? Random Password Generator
    label_input_rpg.place_forget()
    slider_rpg.place_forget()
    label_val_slide.place_forget()
    button_gen.place_forget()
    text_box_output_rpg.place_forget()
    text_box_input_rpg.place_forget()
    button_menu.place_forget()
    switch.place_forget()
    label_enter_key.place_forget()
    button_try_pwd.place_forget()
    label_pwd_vulnerable.place_forget()
    label_pwd_weak.place_forget()
    label_pwd_strong.place_forget()
    label_pin_vulnerable.place_forget()
    label_pin_weak.place_forget()
    label_pin_strong.place_forget()
    
    #? Manage Password
    text_box_input_manage.place_forget()
    in_manage_pwd = False
    
    #? Menu
    button_crypt_decrypt.place(relx = 0.5, anchor = "n", y = 60)
    button_pwd_gen.place(relx = 0.5, anchor = "n", y = 140)
    button_manage.place(relx = 0.5, anchor = "n", y = 220)
    button_login_page.place(relx = 0.5, anchor = "n", y = 320)
    switch_language.place(x = 680, y = 10)
    switch_language.configure(switch_height = 20, switch_width = 40)

def to_crypt_decrypt_software():
    window.geometry("950x460")
    window.iconbitmap("./Icons/icon Crypt Decrypt.ico")
    if state_switch_language == False:
        window.title("Encrypting / Decrypting")
    else:
        window.title("Cryptage / Decryptage")
    
    #? Menu
    button_crypt_decrypt.place_forget()
    button_pwd_gen.place_forget()
    button_login_page.place_forget()
    button_manage.place_forget()
    switch_language.place_forget()
    option_menu_palet.place_forget()
    
    #? Crypt Decrypt
    label_input_crypt_decrypt.place(x = 102, y = 10)
    text_box_input_crypt_decrypt.place(x = 10, y = 50)
    button_crypt.place(relx = 0.5, anchor = "n", y = 50)
    label_enter_key.place(relx = 0.5, anchor = "n", y = 180)
    entry_key_crypt.place(relx = 0.5, anchor = "n", y = 215)
    button_decrypt.place(relx = 0.5, anchor = "n", y = 345)
    label_output.place(x = 738, y = 10)
    text_box_output_crypt_decrypt.place(x = 640, y = 50)
    button_menu.place(x = 10, y = 10)

def crypt():
    global alph
    result = ""
    key = entry_key_crypt.get()
    message = text_box_input_crypt_decrypt.get("0.0", "end")
    
    rd.seed(key)
    alphabet_shuffle = alph.copy()
    rd.shuffle(alphabet_shuffle)
    
    for i in message:
        for j in range(len(alph)):
            if i == alph[j]:
                result += alphabet_shuffle[j]
        text_box_output_crypt_decrypt.delete("0.0", "end")
        text_box_output_crypt_decrypt.insert("0.0", result)

def decrypt():
    global alph
    result = ""
    key = entry_key_crypt.get()
    message = text_box_input_crypt_decrypt.get("0.0", "end")
    
    rd.seed(key)
    alphabet_shuffle = alph.copy()
    rd.shuffle(alphabet_shuffle)
    
    for i in message:
        for j in range(len(alph)):
            if i == alphabet_shuffle[j]:
                result += alph[j]
        text_box_output_crypt_decrypt.delete("0.0", "end")
        text_box_output_crypt_decrypt.insert("0.0", result)

def to_pwd_gen():
    global return_modify_pwd, return_login, button_to_try_pwd, mdp
    window.iconbitmap("./icons/icon-pwd-gen.ico")
    window.geometry("328x310")
    return_modify_pwd, return_login = False, False
    if state_switch_language == False:
        window.title("Random Password Generator")
    else:
        window.title("Générateur de mots de passe")
    
    #? Menu
    button_crypt_decrypt.place_forget()
    button_pwd_gen.place_forget()
    button_manage.place_forget()
    button_login_page.place_forget()
    button_menu.place(x = 10, y = 10)
    option_menu_palet.place_forget()
    
    #? Random Password Generate
    switch.place(x = 255, y = 10)
    label_input_rpg.place(relx = 0.5, anchor = "n", y = 40)
    slider_rpg.place(relx = 0.5, anchor = "n", y = 100)
    label_val_slide.place(relx = 0.5, anchor = "n", y = 123)
    button_gen.place(x = 5, y = 153)
    text_box_output_rpg.place(relx = 0.5, anchor = "n", y = 210)
    button_try_pwd.place(x = 150, y = 153)
    text_box_input_rpg.place_forget()
    label_pin_strong.place_forget()
    label_pin_weak.place_forget()
    label_pin_vulnerable.place_forget()
    label_pwd_strong.place_forget()
    label_pwd_vulnerable.place_forget()
    label_pwd_weak.place_forget()
    label_error_space_rpg.place_forget()
    button_gen.configure(state = "disabled")
    button_to_try_pwd = False

def gen(lenght:int) -> str:
    global all
    min = "abcdefghijklmnopqrstuvwxyz"
    maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = "0123456789"
    symbols = "{}()[]/|.!?,;:+-*%^=€$£_&#@"
    all = min + maj + num + symbols
    mdp = ""
    if switch.get() == 0:
        for _ in range(lenght):
            mdp += all[rd.randint(0, len(all) - 1)]
    else:
        for _ in range(lenght):
            mdp += num[rd.randint(0, len(num) - 1)]
    return mdp

def try_pwd():
    global button_to_try_pwd
    if button_to_try_pwd == True:
        pwd_get = text_box_input_rpg.get(0.0, "end")
        try:
            pwd_get_test = int(pwd_get)
            if len(pwd_get) > 1 and len(pwd_get) < 10:
                label_pwd_vulnerable.place_forget()
                label_pwd_weak.place_forget()
                label_pwd_strong.place_forget()
                label_pin_weak.place_forget()
                label_pin_strong.place_forget()
                label_error_space_rpg.place_forget()
                label_pin_vulnerable.place(relx = 0.5, anchor = "n", y = 70)
            elif len(pwd_get) >= 10 and len(pwd_get) < 15:
                label_pwd_vulnerable.place_forget()
                label_pwd_weak.place_forget()
                label_pwd_strong.place_forget()
                label_pin_vulnerable.place_forget()
                label_pin_strong.place_forget()
                label_error_space_rpg.place_forget()
                label_pin_weak.place(relx = 0.5, anchor = "n", y = 70)
            else:
                label_pwd_vulnerable.place_forget()
                label_pwd_weak.place_forget()
                label_pwd_strong.place_forget()
                label_pin_vulnerable.place_forget()
                label_pin_weak.place_forget()
                label_error_space_rpg.place_forget()
                label_pin_strong.place(relx = 0.5, anchor = "n", y = 70)
            for i in range(len(pwd_get)):
                if pwd_get[i] == " ":
                    label_pwd_vulnerable.place_forget()
                    label_pwd_weak.place_forget()
                    label_pwd_strong.place_forget()
                    label_pin_weak.place_forget()
                    label_pin_strong.place_forget()
                    label_pin_vulnerable.place_forget()
                    label_error_space_rpg.place(relx = 0.5, anchor = "n", y = 70)
        except:
            if len(pwd_get) > 1 and len(pwd_get) < 10:
                label_pin_vulnerable.place_forget()
                label_pin_weak.place_forget()
                label_pin_strong.place_forget()
                label_pwd_weak.place_forget()
                label_pwd_strong.place_forget()
                label_error_space_rpg.place_forget()
                label_pwd_vulnerable.place(relx = 0.5, anchor = "n", y = 70)
            elif len(pwd_get) >= 10 and len(pwd_get) < 15:
                label_pin_vulnerable.place_forget()
                label_pin_weak.place_forget()
                label_pin_strong.place_forget()
                label_pwd_vulnerable.place_forget()
                label_pwd_strong.place_forget()
                label_error_space_rpg.place_forget()
                label_pwd_weak.place(relx = 0.5, anchor = "n", y = 70)
            else:
                label_pin_vulnerable.place_forget()
                label_pin_weak.place_forget()
                label_pin_strong.place_forget()
                label_pwd_vulnerable.place_forget()
                label_pwd_weak.place_forget()
                label_error_space_rpg.place_forget()
                label_pwd_strong.place(relx = 0.5, anchor = "n", y = 70)
            for i in range(len(pwd_get)):
                if pwd_get[i] == " ":
                    label_pwd_vulnerable.place_forget()
                    label_pwd_weak.place_forget()
                    label_pwd_strong.place_forget()
                    label_pin_weak.place_forget()
                    label_pin_strong.place_forget()
                    label_pin_vulnerable.place_forget()
                    label_error_space_rpg.place(relx = 0.5, anchor = "n", y = 70)
            if pwd_get == "\n":
                label_pwd_vulnerable.place_forget()
                label_pwd_weak.place_forget()
                label_pwd_strong.place_forget()
                label_pin_weak.place_forget()
                label_pin_strong.place_forget()
                label_pin_vulnerable.place_forget()
                label_error_space_rpg.place_forget()
    
    else:
        pwd_get = text_box_output_rpg.get("0.0", "end")
        if switch.get() == 0:
            if len(pwd_get) > 1 and len(pwd_get) < 10:
                label_pin_vulnerable.place_forget()
                label_pin_weak.place_forget()
                label_pin_strong.place_forget()
                label_pwd_weak.place_forget()
                label_pwd_strong.place_forget()
                label_error_space_rpg.place_forget()
                label_pwd_vulnerable.place(relx = 0.5, anchor = "n", y = 70)
            elif len(pwd_get) >= 10 and len(pwd_get) < 15:
                label_pin_vulnerable.place_forget()
                label_pin_weak.place_forget()
                label_pin_strong.place_forget()
                label_pwd_vulnerable.place_forget()
                label_pwd_strong.place_forget()
                label_error_space_rpg.place_forget()
                label_pwd_weak.place(relx = 0.5, anchor = "n", y = 70)
            else:
                label_pin_vulnerable.place_forget()
                label_pin_weak.place_forget()
                label_pin_strong.place_forget()
                label_pwd_vulnerable.place_forget()
                label_pwd_weak.place_forget()
                label_error_space_rpg.place_forget()
                label_pwd_strong.place(relx = 0.5, anchor = "n", y = 70)
        else:
            if len(pwd_get) > 1 and len(pwd_get) < 4:
                label_pwd_vulnerable.place_forget()
                label_pwd_weak.place_forget()
                label_pwd_strong.place_forget()
                label_pin_weak.place_forget()
                label_pin_strong.place_forget()
                label_error_space_rpg.place_forget()
                label_pin_vulnerable.place(relx = 0.5, anchor = "n", y = 70)
            elif len(pwd_get) >= 4 and len(pwd_get) < 8:
                label_pwd_vulnerable.place_forget()
                label_pwd_weak.place_forget()
                label_pwd_strong.place_forget()
                label_pin_vulnerable.place_forget()
                label_pin_strong.place_forget()
                label_error_space_rpg.place_forget()
                label_pin_weak.place(relx = 0.5, anchor = "n", y = 70)
            else:
                label_pwd_vulnerable.place_forget()
                label_pwd_weak.place_forget()
                label_pwd_strong.place_forget()
                label_pin_vulnerable.place_forget()
                label_pin_weak.place_forget()
                label_error_space_rpg.place_forget()
                label_pin_strong.place(relx = 0.5, anchor = "n", y = 70)

def pwd(input:int):
    global mdp
    mdp = gen(input)
    text_box_output_rpg.delete("0.0", "end")
    text_box_output_rpg.insert("0.0", mdp)
    try_pwd()

def pin(input:int):
    global mdp
    mdp = gen(int(input))
    text_box_output_rpg.delete("0.0", "end")
    text_box_output_rpg.insert("0.0", mdp)
    try_pwd()

def slider_event_rpg(value = 20):
    global input_rpg
    label_val_slide.configure(text = int(value))
    input_rpg = int(value)
    if switch.get() == 0:
        pwd(input_rpg)
    else:
        pin(input_rpg)

def pwd_to_pin():
    global input_rpg
    if switch.get() == 0:
        if state_switch_language == True:
            switch.configure(progress_color = text_color, button_color = text_color, button_hover_color = text_color_hover, fg_color = secondary_color, text = "Mdp")
            pwd(input_rpg)
        else:
            switch.configure(progress_color = text_color, button_color = text_color, button_hover_color = text_color_hover, fg_color = secondary_color, text = "Pwd")
            pwd(input_rpg)
    else:
        switch.configure(progress_color = text_color, button_color = secondary_color, button_hover_color = secondary_color_hover, fg_color = secondary_color, text = "PIN")
        pin(input_rpg)

def to_try_pwd():
    global button_to_try_pwd
    if button_to_try_pwd == False:
        label_pin_strong.place_forget()
        label_pin_weak.place_forget()
        label_pin_vulnerable.place_forget()
        label_pwd_strong.place_forget()
        label_pwd_vulnerable.place_forget()
        label_pwd_weak.place_forget()
        slider_rpg.place_forget()
        label_val_slide.place_forget()
        label_input_rpg.place_forget()
        switch.place_forget()
        text_box_output_rpg.place_forget()
        option_menu_palet.place_forget()
        text_box_input_rpg.place(relx = 0.5, anchor = "n", y = 210)
        button_gen.configure(state = "normal")
        button_to_try_pwd = True
    else:
        try_pwd()

def to_manage_pwd():
    global return_modify_pwd, return_login, in_manage_pwd
    return_modify_pwd, return_login, in_manage_pwd = False, False, True
    window.iconbitmap("./icons/icon-manage.ico")
    if state_switch_language == False:
        window.title("Passwords Manager")
    else:
        window.title("Manager de mots de passe")
    
    #? Menu
    button_crypt_decrypt.place_forget()
    button_pwd_gen.place_forget()
    button_manage.place_forget()
    button_login_page.place_forget()
    switch_language.place_forget()
    option_menu_palet.place_forget()
    
    text_box_input_manage.place(x = 10, y = 40)
    button_menu.place(x = 10, y = 5)
    input_manage = open("manage.txt", "r")
    text_box_input_manage.delete(0.0, "end")
    text_box_input_manage.insert(0.0, input_manage.read())
    save()

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
    label_input.configure(text_color=text_color)
    label_actual_pwd.configure(text_color=text_color)
    label_new_pwd_1.configure(text_color=text_color)
    label_new_pwd_2.configure(text_color=text_color)
    label_input_crypt_decrypt.configure(text_color=text_color)
    label_output.configure(text_color=text_color)
    label_enter_key.configure(text_color=text_color)
    label_input_rpg.configure(text_color=text_color)
    label_val_slide.configure(text_color=text_color)
    entry_actual_pwd.configure(border_color=text_color, fg_color=primary_color_hover, text_color=text_color)
    entry_new_pwd_1.configure(border_color=text_color, fg_color=primary_color_hover, text_color=text_color)
    entry_new_pwd_2.configure(border_color=text_color, fg_color=primary_color_hover, text_color=text_color)
    entry_input.configure(border_color=text_color, fg_color=primary_color_hover, text_color=text_color)
    entry_key_crypt.configure(border_color=text_color, fg_color=primary_color_hover, text_color=text_color)
    button_login.configure(border_color=text_color, hover_color=secondary_color_hover, fg_color=secondary_color, text_color=text_color)
    button_new_pwd.configure(border_color=text_color, hover_color=secondary_color_hover, fg_color=secondary_color, text_color=text_color)
    button_back.configure(border_color=text_color, hover_color=secondary_color_hover, fg_color=secondary_color, text_color=text_color)
    button_modify.configure(border_color=text_color, hover_color=secondary_color_hover, fg_color=secondary_color, text_color=text_color)
    button_crypt.configure(border_color=text_color, hover_color=secondary_color_hover, fg_color=secondary_color, text_color=text_color)
    button_decrypt.configure(border_color=text_color, hover_color=secondary_color_hover, fg_color=secondary_color, text_color=text_color)
    button_gen.configure(border_color=text_color, hover_color=secondary_color_hover, fg_color=secondary_color, text_color=text_color)
    button_try_pwd.configure(border_color=text_color, hover_color=secondary_color_hover, fg_color=secondary_color, text_color=text_color)
    button_menu.configure(border_color=text_color, hover_color=secondary_color_hover, fg_color=secondary_color, text_color=text_color)
    button_pwd_gen.configure(border_color=text_color, hover_color=secondary_color_hover, fg_color=secondary_color, text_color=text_color)
    button_crypt_decrypt.configure(border_color=text_color, hover_color=secondary_color_hover, fg_color=secondary_color, text_color=text_color)
    button_manage.configure(border_color=text_color, hover_color=secondary_color_hover, fg_color=secondary_color, text_color=text_color)
    button_login_page.configure(border_color=text_color, hover_color=secondary_color_hover, fg_color=secondary_color, text_color=text_color)
    option_menu_palet.configure(fg_color=primary_color_hover, bg_color=primary_color, button_color=secondary_color, button_hover_color=secondary_color_hover, dropdown_fg_color=primary_color_hover, dropdown_hover_color=secondary_color, dropdown_text_color=text_color, text_color=text_color)
    text_box_input_crypt_decrypt.configure(fg_color=primary_color_hover, border_color=text_color, text_color=text_color)
    text_box_output_crypt_decrypt.configure(fg_color=primary_color_hover, border_color=text_color, text_color=text_color)
    text_box_input_manage.configure(fg_color=primary_color_hover, border_color=text_color, text_color=text_color)
    text_box_input_rpg.configure(fg_color=primary_color_hover, border_color=text_color, text_color=text_color)
    text_box_output_rpg.configure(fg_color=primary_color_hover, border_color=text_color, text_color=text_color)
    slider_rpg.configure(fg_color=primary_color_hover, button_color=text_color, button_hover_color=text_color_hover, progress_color=secondary_color)
    switch.configure(progress_color=text_color, button_hover_color=text_color_hover, fg_color=secondary_color, button_color=text_color, text_color=text_color)
    switch_language.configure(progress_color=text_color, button_hover_color=text_color_hover, fg_color=secondary_color, button_color=text_color, text_color=text_color)
    for switch_name in switchs:
        change_switch_color(switch_name)

def change_switch_color(switch_name):
    if switch_name.get() == 0:
        switch_name.configure(button_color=text_color, button_hover_color=text_color_hover)
    else:
        switch_name.configure(button_color=secondary_color, button_hover_color=secondary_color_hover)

def save():
    manage_text = open("manage.txt", "w")
    manage_text.write(text_box_input_manage.get(0.0, "end"))
    if in_manage_pwd:
        window.after(1000, save)

def destroy():
    window.destroy()

#? Vars
values = ["By default", "Black", "White", "Black and Red", "Grey and Red", "Blue and Brown", "Blue and Orange", "Black and Blue", "Green and Orange", "White and Blue", "Blue and Yellow", "Burgundy and Black"]
values_fr = ["Par défault", "Noir", "Blanc", "Noir et Rouge", "Gris et Rouge", "Bleu et Marron", "Bleu et Orange", "Noir et Bleu", "Vert et Orange", "Blanc et Bleu", "Bleu et Jaune", "Bordeaux et Noir"]
    
    #? Return Button
return_login = True
return_modify_pwd = False

    #? Login
file_read = open("password.txt", "r")
password = file_read.read()
file_read.close()
state_switch_language = False

    #? Random Password Generator
input_rpg = 20
button_to_try_pwd = False

    #? Crypt Decrypt Software
alph = []
for i in range(32, 127):
    alph.append(chr(i))
carac_accent = ["€", "é", "è", "ê", "ë", "à", "â", "ù", "û", "ü", "ô", "î", "ç"]
alph.extend(carac_accent)

    #? Manage Passwords
in_manage_pwd = False

#? Login
    #? Labels
label_input = ctk.CTkLabel(window, text = "Input your password", font = ("Trebuchet MS", 25), text_color = text_color)
label_actual_pwd = ctk.CTkLabel(window, text = "Actual password", font = ("Trebuchet MS", 20), text_color = text_color)
label_new_pwd_1 = ctk.CTkLabel(window, text = "Enter your new password", font = ("Trebuchet MS", 20), text_color = text_color)
label_new_pwd_2 = ctk.CTkLabel(window, text = "Confirm your password", font = ("Trebuchet MS", 20), text_color = text_color)
label_error_login = ctk.CTkLabel(window, text = "Wrong password !", text_color = "red", font = ("Trebuchet MS", 25))
label_pwd_change_ok = ctk.CTkLabel(window, text = "Password changed successfully !", text_color = "green", font = ("Trebuchet MS", 20))
label_error_actual_pwd_wrong = ctk.CTkLabel(window, text = "The actual password is wrong !", text_color = "red", font = ("Trebuchet MS", 20))
label_error_space = ctk.CTkLabel(window, text = "Password must not contain spaces !", text_color = "red", font = ("Trebuchet MS", 20))
label_error_new_pwd_diff = ctk.CTkLabel(window, text = "The passwords are not the same !",text_color = "red", font = ("Trebuchet MS", 20))
label_error_empty_pwd = ctk.CTkLabel(window, text = "The new password must not be empty !", text_color = "red", font = ("Trebuchet MS", 20))

    #? Entry
entry_input = ctk.CTkEntry(window, width = 600, height = 100, corner_radius = 30, font = ("Trebuchet MS", 25), border_width = 1, border_color = text_color, fg_color = primary_color_hover, text_color = text_color, show="•")
entry_actual_pwd = ctk.CTkEntry(window, width = 600, height = 75, corner_radius = 20,font = ("Trebuchet MS", 20), border_width = 1, border_color = text_color, fg_color = primary_color_hover, text_color = text_color, show="•")
entry_new_pwd_1 = ctk.CTkEntry(window, width = 600, height = 75, corner_radius = 20,font = ("Trebuchet MS", 20), border_width = 1, border_color = text_color, fg_color = primary_color_hover, text_color = text_color, show="•")
entry_new_pwd_2 = ctk.CTkEntry(window, width = 600, height = 75, corner_radius = 20,font = ("Trebuchet MS", 20), border_width = 1, border_color =text_color, fg_color = primary_color_hover, text_color = text_color, show="•")

    #? Buttons
button_login = ctk.CTkButton(window, width = 258, height = 60,command = login, corner_radius = 30,text = "Login", font = ("Trebuchet MS", 25), border_width = 1, border_color = text_color, hover_color = secondary_color_hover, fg_color = secondary_color, text_color = text_color)
button_new_pwd = ctk.CTkButton( window, width = 50, height = 60, command = new_pwd, corner_radius = 30,text = "Modify your password", font = ("Trebuchet MS", 25), border_width = 1, border_color = text_color, hover_color = secondary_color_hover, fg_color = secondary_color, text_color = text_color) 
button_back = ctk.CTkButton(window, width = 200, height = 50, command = login_page, corner_radius = 30,text = "Back", font = ("Trebuchet MS", 20), border_width = 1, border_color = text_color, hover_color = secondary_color_hover, fg_color = secondary_color, text_color = text_color)
button_modify = ctk.CTkButton(window, width = 50, height = 50, command = modify_pwd, corner_radius = 30,text = "Modify your password", font = ("Trebuchet MS", 20), border_width = 1, border_color = text_color, hover_color = secondary_color_hover, fg_color = secondary_color, text_color = text_color)

    #? Switch
switch_language = ctk.CTkSwitch(window, switch_height = 30, switch_width = 60, text = "English", corner_radius = 20, command = switch_languages, font = ("Trebuchet MS", 20), progress_color = text_color, button_hover_color = text_color_hover, fg_color = secondary_color)

    #? Menu
button_menu = ctk.CTkButton(window, width = 10, corner_radius = 20, command = menu, text = "Menu", font = ("Trebuchet MS", 20), border_width = 1, border_color = text_color, hover_color = secondary_color_hover, fg_color = secondary_color, text_color = text_color)
button_pwd_gen = ctk.CTkButton(window, width = 370, height = 40, corner_radius = 30, command = to_pwd_gen, text = "Random Password Generator", font = ("Trebuchet MS", 25), border_width = 1, border_color = text_color, hover_color = secondary_color_hover, fg_color = secondary_color, text_color = text_color, image = img_pwd_gen)
button_crypt_decrypt = ctk.CTkButton(window, width = 370, height = 40, corner_radius = 30, command = to_crypt_decrypt_software, text = "Crypt / Decrytp Software", font = ("Trebuchet MS", 25), border_width = 1, border_color = text_color, hover_color = secondary_color_hover, fg_color = secondary_color, text_color = text_color, image = img_crypt)
button_manage = ctk.CTkButton(window, width = 370, height = 40, corner_radius = 30, command = to_manage_pwd, text = "Passwords Manager", font = ("Trebuchet MS", 25), border_width = 1, border_color = text_color, hover_color = secondary_color_hover, fg_color = secondary_color, text_color = text_color, image = img_manage)
button_login_page = ctk.CTkButton(window, width = 80, height = 50, corner_radius = 30, command = login_page, text = "Lock the session", font = ("Trebuchet MS", 25), border_width = 1, border_color = text_color, hover_color = secondary_color_hover, fg_color = secondary_color, text_color = text_color)
option_menu_palet = ctk.CTkOptionMenu(window, width=70, height=30, corner_radius=20, font=("Trebuchet MS", 25), values=values, dropdown_font=("Trebuchet MS", 15), fg_color=primary_color_hover, bg_color=primary_color, button_color=secondary_color, button_hover_color=secondary_color_hover, dropdown_fg_color=primary_color_hover, dropdown_hover_color=secondary_color, dropdown_text_color=text_color, text_color=text_color, command=change_palet)

#? Crypt Decrypt
    #? Labels
label_input_crypt_decrypt = ctk.CTkLabel(window, width = 100, height = 25, corner_radius = 20, text = "Input", font = ("Trebuchet MS", 25), text_color = text_color)
label_output = ctk.CTkLabel(window, width = 100, height = 25, corner_radius = 20, text = "Output", font = ("Trebuchet MS", 25), text_color = text_color)
label_enter_key = ctk.CTkLabel(window, text = "Put a key here", font = ("Trebuchet MS", 25), text_color = text_color)

    #? Buttons
button_crypt = ctk.CTkButton(window, width = 200, height = 100, corner_radius = 20, text = "Crypt", command = crypt, font = ("Trebuchet MS", 25), border_width = 1, border_color = text_color, hover_color = secondary_color_hover, fg_color = secondary_color, text_color = text_color)
button_decrypt = ctk.CTkButton(window, width = 200, height = 100, corner_radius = 20, text = "Decrypt", command = decrypt, font = ("Trebuchet MS", 25), border_width = 1, border_color = text_color, hover_color = secondary_color_hover, fg_color = secondary_color, text_color = text_color)

    #? Entry
entry_key_crypt = ctk.CTkEntry(window, width = 300, height = 80, corner_radius = 20, font = ("Arila", 25),border_width = 1, border_color = text_color, fg_color = primary_color_hover, text_color=text_color)

    #? Textebox
text_box_input_crypt_decrypt = ctk.CTkTextbox(window, width = 300, height = 400, corner_radius = 20, font = ("Trebuchet MS", 25), fg_color = primary_color_hover, border_color = text_color, border_width = 1, text_color = text_color)
text_box_output_crypt_decrypt = ctk.CTkTextbox(window, width = 300, height = 400, corner_radius = 20, font = ("Trebuchet MS", 25), fg_color = primary_color_hover, border_color = text_color, border_width = 1, text_color = text_color)

#? Random Password Generator
    #? Labels
label_input_rpg = ctk.CTkLabel(window, width = 10, height = 30, text = "Input the lenght of your password", font = ("Trebuchet MS", 20), text_color = text_color)
label_val_slide = ctk.CTkLabel(window, width = 50, height = 25, corner_radius = 20, text = "20", font = ("Trebuchet MS", 20), text_color = text_color)
label_pwd_vulnerable = ctk.CTkLabel(window, text = "Password vulnerable !", text_color = "red", font = ("Trebuchet MS", 20))
label_pwd_weak = ctk.CTkLabel(window, text = "Password weak !", text_color = "orange", font = ("Trebuchet MS", 20))
label_pwd_strong = ctk.CTkLabel(window, text = "Password strong !", text_color = "green", font = ("Trebuchet MS", 20))
label_pin_vulnerable = ctk.CTkLabel(window, text = "PIN vulnerable !", text_color = "red", font = ("Trebuchet MS", 20))
label_pin_weak = ctk.CTkLabel(window, text = "PIN weak !", text_color = "orange", font = ("Trebuchet MS", 20))
label_pin_strong = ctk.CTkLabel(window, text = "PIN strong !", text_color = "green", font = ("Trebuchet MS", 20))
label_error_space_rpg = ctk.CTkLabel(window, text = "Password must not contain space !", text_color = "red", font = ("Trebuchet MS", 20))

    #? Buttons
button_gen = ctk.CTkButton(window, height = 40, corner_radius = 30, text = "Generate a\npassword", command = to_pwd_gen, font = ("Trebuchet MS", 13), state = "disabled", hover_color = secondary_color_hover, border_width = 1, border_color = text_color, fg_color = secondary_color, text_color = text_color)
button_try_pwd = ctk.CTkButton(window, height = 40, corner_radius = 30, text = "Test the effectiveness\nof your password", command = to_try_pwd, font = ("Trebuchet MS", 13), hover_color = secondary_color_hover, border_width = 1, border_color = text_color, fg_color = secondary_color, text_color = text_color)

    #? Textbox
text_box_output_rpg = ctk.CTkTextbox(window, width = 300, height = 93, corner_radius = 20, font = ("Trebuchet MS", 20), border_width = 1, border_color = text_color, fg_color = primary_color_hover, text_color = text_color)
text_box_input_rpg = ctk.CTkTextbox(window, width = 300, height = 93, corner_radius = 20, font = ("Trebuchet MS", 20), border_width = 1, border_color = text_color, fg_color = primary_color_hover, text_color = text_color)

    #? Slider
slider_rpg = ctk.CTkSlider(window, width = 300, from_ = 1, to = 40, command = slider_event_rpg, button_hover_color = secondary_color_hover, fg_color = secondary_color, button_color = secondary_color)

    #? Switch
switch = ctk.CTkSwitch(window, corner_radius = 20, command = pwd_to_pin, font = ("Trebuchet MS", 15), progress_color = text_color, button_hover_color = text_color_hover, fg_color = secondary_color, text = "Pwd")

#? Manage Password
    #? Textbox
text_box_input_manage = ctk.CTkTextbox(window, width = 780, height = 350, font = ("Trebuchet MS", 20), border_width = 1, border_color = text_color, fg_color = primary_color_hover, text_color = text_color)

#? Places
label_input.place(relx = 0.5, anchor = "n", y = 40)
entry_input.place(relx = 0.5, anchor = "n", y = 100)
button_new_pwd.place(x = 100, y = 260)
button_login.place(x = 440, y = 260)
switch_language.place(x = 650, y = 10)
option_menu_palet.place(x=10, y=10)
switchs = [switch, switch_language]

#? Bind
window.bind("<Return>", lambda _:return_button())
window.bind("<Escape>", lambda _: destroy())

#? Mainloop
window.mainloop()