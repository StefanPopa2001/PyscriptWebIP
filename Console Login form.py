import bcrypt
import sqlite3
import webbrowser

con = sqlite3.connect("login.db")
cur = con.cursor()

cur.execute("drop table user")
cur.execute("CREATE TABLE IF NOT EXISTS user(username, password)")
cur.execute("""INSERT INTO user(username, password) VALUES ('root', '$2b$04$fVxqMEA9vggmDELauM.e5.klNl.oWKYyMNL6LYzbbE3ypjNhE1k26')""")

def afficherMenu():
    print("Entrez votre nom d'utilisateur pour continuer...")
    usernameEntre=input()
    while(usernameEntre.replace(" ", "")==""):
        usernameEntre=input()
    print("Vous essayez de vous connecter en tant que ",usernameEntre)
    print("Veuillez entrer votre mot de passe...")
    cur.execute("select password from user where username like ?",(usernameEntre,))
    mdpVerifHash = cur.fetchone()
    mdpVerifHash = mdpVerifHash[0]
    mdpVerifHash = mdpVerifHash.encode('utf-8')
    utiliserMDP(mdpVerifHash)

def utiliserMDP(mdp):
    mdpEntre=input()
    mdpEntre=mdpEntre.encode('utf-8')
    if(bcrypt.checkpw(mdpEntre,mdp)):
        print("Mot de passe corest, renvoi vers l'application...")
        webbrowser.open('https://projetsysrso.web.app/index.html') 
    else:
        print("Mot de passe incorrect, veuillez réesayer...")
        utiliserMDP(mdp)

afficherMenu()
