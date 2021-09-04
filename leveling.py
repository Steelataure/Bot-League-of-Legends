import win32api, win32con
import pyautogui
import time
from tkinter import *
import tkinter.font as font
import sys


# Pour que le programme fonctionne, il faut avoir la même résolution d'écran (24 pouce)
# et que la taille du client soit de 1280x720

# Champion qui sera choisi en priorité (Modifiable)


interface = Tk()
interface.title("LeagueBot")
# interface.iconbitmap("botleague2.ico")
interface.resizable(width=False, height=False)

window_width = 650
window_height = 270

screen_width = interface.winfo_screenwidth()
screen_height = interface.winfo_screenheight()
x_cordinate = int((screen_width / 2) - (window_width / 2))  # Permet de mettre la fenêtre au milieu
y_cordinate = int((screen_height / 2) - (window_height / 2))

interface.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

background = PhotoImage(file='data/degrad.png')
label1 = Label(interface, image=background)
label1.place(x=-2, y=0)

f = font.Font(size=20)
f2 = font.Font(size=15, weight='bold', family='ArialBlack')

vide = Frame(None)
vide.pack(pady=25)
Champion_prioritaire = Entry(width=30, font='ArialBlack', borderwidth=4, bg='#C829DD')
Champion_prioritaire.pack(padx=20, pady=40)
Champion_prioritaire['font'] = f
Champion_prioritaire.focus()

champion_prioritaire = ["Caitlyn"]


def Champion_saisi():
    champion_prioritaire.append(Champion_prioritaire.get())

    if champion_prioritaire[1]:
        loop()

    elif not champion_prioritaire[1]:
        sys.exit()


Go = Button(text="Utiliser le Bot", width=16, borderwidth=5, command=Champion_saisi,
            bg='#268BE1')
Go['font'] = f2
Go.pack()


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


def right_click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, x, y, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, x, y, 0, 0)


def loop():
    def debut():
        time.sleep(5)
        click(400, 200)  # JOUER HAUT  # 300 100
        time.sleep(1.2)  # + 150 + 120
        click(460, 260)  # IA # 700, 730
        time.sleep(1.2)

    debut()

    def champ_select():
        click(850, 850)  # LANCER
        time.sleep(4)
        click(850, 850)  # LANCER
        time.sleep(4)

        # EN CAS DE DODGE / LEAVE BUSTER
        # time.sleep(TEMPS DE PENALITE EN SECONDE)

        click(900, 720)  # ACCEPTER
        time.sleep(15)
        click(900, 720)  # ACCEPTER
        time.sleep(2)
        click(1020, 320)  # CHOISIR PERSO # 740, 200
        time.sleep(1)

        click(1100, 260)
        time.sleep(1)
        pyautogui.write(champion_prioritaire[-1])
        time.sleep(1)
        click(740, 320)

        click(950, 780)  # LOCK A CHECK # 800, 660
        time.sleep(60)

    def ingame():
        for i in range(85):
            right_click(800, 635)
            click(1000, 500)
            time.sleep(15)

        for i in range(15):
            click(900, 850)  # LANCER
            right_click(800, 600)
            click(900, 850)  # LANCER
            time.sleep(1)
            click(900, 500)
            time.sleep(5)
            click(900, 720)  # ACCEPTER
            time.sleep(5)
            click(900, 720)  # ACCEPTER
            time.sleep(2)
            click(1020, 320)  # CHOISIR PERSO # 740, 200
            time.sleep(1)

            click(1100, 260)
            time.sleep(1)
            pyautogui.write(champion_prioritaire)
            time.sleep(1)
            click(740, 320)
            time.sleep(1)

            click(950, 780)  # LOCK A CHECK # 800, 660
            right_click(950, 800)
            click(1000, 500)
            time.sleep(30)

    def after_game():
        click(1160, 260)  # Compte non vérifié (1010, 140)
        time.sleep(5)
        click(850, 620)  # Honor quelqu'un (700, 500)
        time.sleep(6)
        click(950, 850)  # Honor quelqu'un (700, 500)
        time.sleep(6)
        click(850, 850)  # REJOUER         (700,730)

    while True:
        champ_select()
        time.sleep(30)
        ingame()
        time.sleep(15)


interface.mainloop()
