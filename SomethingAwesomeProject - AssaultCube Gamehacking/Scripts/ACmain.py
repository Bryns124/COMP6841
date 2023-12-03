import customtkinter
import tkinter
from ACinfinitehealthammo import infinitehealthammo
from ACbhop import bhop
from ACnorecoil import norecoil
from ACrapidfire import rapidfire
from ACtriggerbot import triggerbot
import threading

# threading for responsiveness
def start_infinitehealthammo():
    threading.Thread(target=infinitehealthammo).start()

def start_bhop():
    threading.Thread(target=bhop).start()

def start_norecoil():
    threading.Thread(target=norecoil).start()

def start_rapidfire():
    threading.Thread(target=rapidfire).start()

def start_triggerbot():
    threading.Thread(target=triggerbot).start()

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

menu = customtkinter.CTk()
menu.geometry("500x350")

frame = customtkinter.CTkFrame(master=menu)
frame.pack(fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="AssaultCube HAX", font=("Roboto", 24))
label.pack(pady=20, padx=60)

infinitebutton = customtkinter.CTkButton(master=frame, text="Infinite", command=start_infinitehealthammo, width=400, height=40)
infinitebutton.pack(pady=6, padx=8)

bhopbutton = customtkinter.CTkButton(master=frame, text="Bhop", command=start_bhop, width=400, height=40)
bhopbutton.pack(pady=6, padx=8)

norecoilbutton = customtkinter.CTkButton(master=frame, text="No Recoil", command=start_norecoil, width=400, height=40)
norecoilbutton.pack(pady=6, padx=8)

rapidfirebutton = customtkinter.CTkButton(master=frame, text="Rapid Fire", command=start_rapidfire, width=400, height=40)
rapidfirebutton.pack(pady=6, padx=8)

triggerbotbutton = customtkinter.CTkButton(master=frame, text="Trigger Bot", command=start_triggerbot, width=400, height=40)
triggerbotbutton.pack(pady=6, padx=8)

menu.mainloop()
