# Security App

## [Français](#security-app-1)

## [English](#security-app-2)

## **Security App**

### **Description**

Cette application est sécurisée par un mot de passe (par défaut "_password_") et vous pouvez le modifier.
De plus, votre mot de passe est chiffré avec bcrypt.
Dans cette appli, vous pouvez chiffrer et déchiffrer un message avec une clé en utilisant un chiffrement symétrique AES.
Aussi, vous pouvez générer des mots de passe sécurisés et tester les vôtres.
Enfin, vous pouvez sauvegarder ce que vous voulez dans le gestionnaire de mots de passe qui est aussi chiffré avec comme clé votre mot de passe en clair.

### **Bibliothèques utilisées**

- pillow
- pycryptodome
- tkinter
- customtkinter
- random
- hashlib
- bcrypt
- base64
- string
- json
- os

### **Lancer le script**

Sur Windows, après avoir installé les bibliothèques demandées, une simple exécution via VSCode devrait fonctionner. Sinon passez par le terminal et exécutez avec ```python main.py``` une fois dans le dossier.

Sur Linux, vous aurez peut-être besoin de créer un environnement :

- ```python3 -m venv venv``` dans le dossier
- ```source venv/bin/activate```
- ```python3 main.py```

Et tout devrait fonctionner normalement.

### **Customisation**

Vous pouvez customiser l'application en changeant la palette dans le coin haut gauche et le language (Français ou Anglais) dans le coin haut droit.
Tous ces paramètres et données sont sauvegardées dans le fichier user_data.json.

### **Problème d'affichage**

Si la fenêtre semble ne pas être normale, vérifiez que votre écran n'est pas zoomé. Il faut que l'échelle soit à 100%.

## **Security App**

### **Decription**

This app is secured by a password (by default "password") and you can modify it.  
Also, your password is encrypted with bcrypt.
In this app, you can crypt and decrypt a message with a key using a symmetric encryption.
Also, you can generate secured passwords and test yours.  
Finally, you can save whatever you want in the passwords manager which is also encrypted with your plaintext password as a key.

### **Libraries used**

- pillow
- pycryptodome
- tkinter
- customtkinter
- random
- hashlib
- bcrypt
- base64
- string
- json
- os

### **Launch the script**

On Windows, after installing the requested libraries, a simple execution via VSCode should work. Otherwise, go through the terminal and run it with ``python main.py`` once in the folder.

On Linux, you may need to create an environment:

- ```python3 -m venv venv`` in the folder
- ``source venv/bin/activate``
- ```python3 main.py```

And everything should work normally.

### **Customization**

You can customize the app by changing the palet in the top left and the language (English or French) in the top right.
All this settings and datas will be saved in the user_data.json file.

### **Display issue**

If the window seems not to be correctly displayed, plaease check if your display is zoomed. The scale must be at 100%.
