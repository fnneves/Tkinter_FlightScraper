# -*- coding: utf-8 -*-

import tkinter as tk
from flight_scraper_bot import Flight_Bot

def close_app():
    window.destroy()

def run_app():
    print('getting user inputs')
    user_city_from = str(from_city_entry.get())
    user_city_to = str(to_city_entry.get())
    user_date_depart = str(departure_date_entry.get())
    user_date_return = str(return_date_entry.get())
    
    print('starting Chrome')
    bot = Flight_Bot()
    bot.start_kayak(user_city_from, user_city_to, user_date_depart, user_date_return)

def caps_to(event):
    
    """Forces the input TO to be upper case and less than 4 characters"""
    
    to_city1.set(to_city1.get().upper())
    if len(to_city1.get()) > 3: to_city1.set(to_city1.get()[:3])

def caps_from(event):
    
    """Forces the input FROM to be upper case and less than 4 characters"""
    
    from_city1.set(from_city1.get().upper())
    if len(from_city1.get()) > 3: from_city1.set(from_city1.get()[:3])    

window = tk.Tk()

window.title("Flight_Scraper")
frame_header = tk.Frame(master = window, borderwidth=2, pady=2)
center_frame = tk.Frame(window, borderwidth=2, pady=5)
bottom_frame = tk.Frame(window, borderwidth=2, pady=5)
frame_header.grid(row=0, column=0)
center_frame.grid(row=1, column=0)
bottom_frame.grid(row=2, column=0)

header = tk.Label(frame_header, text = "FLIGHT SCRAPER TOOL", bg='grey', fg='black', height='3', width='50', font=("Helvetica 16 bold"))
header.grid(row=0, column=0)

frame_main_1 = tk.Frame(center_frame, borderwidth=2, relief='sunken')
frame_main_2 = tk.Frame(center_frame, borderwidth=2, relief='sunken')

from_city = tk.Label(frame_main_1, text = "FROM: ")
to_city = tk.Label(frame_main_2, text = "TO:      ")
departure_date = tk.Label(frame_main_1, text = "    DEPARTURE DATE:")
return_date = tk.Label(frame_main_2, text = "     RETURN DATE:")

from_city1 = tk.StringVar()
to_city1 = tk.StringVar()
departure_date1 = tk.StringVar()
return_date1 = tk.StringVar()

from_city_entry = tk.Entry(frame_main_1, textvariable = from_city1, width=4)
to_city_entry = tk.Entry(frame_main_2, textvariable = to_city1, width=4)

departure_date_entry = tk.Entry(frame_main_1, textvariable = departure_date1, width=12)
from_city_entry.bind("<KeyRelease>", caps_from)
return_date_entry = tk.Entry(frame_main_2, textvariable = return_date1, width=12)
to_city_entry.bind("<KeyRelease>", caps_to)

button_run = tk.Button(bottom_frame, text="Start", command=run_app, bg='dark green', fg='white', relief='raised', width=10, font=('Helvetica 9 bold'))
button_run.grid(column=0, row=0, sticky='w', padx=100, pady=2)

button_close = tk.Button(bottom_frame, text="Exit", command=close_app, bg='dark red', fg='white', relief='raised', width=10, font=('Helvetica 9'))
button_close.grid(column=1, row=0, sticky='e', padx=100, pady=2)

frame_main_1.pack(fill='x', pady=2)
frame_main_2.pack(fill='x',pady=2)
from_city.pack(side="left")
from_city_entry.pack(side='left', padx=1)
departure_date.pack(side='left', padx=5)
departure_date_entry.pack(side='left')
to_city.pack(side='left')
to_city_entry.pack(side='left', padx=1)
return_date_entry.pack(side='right')
return_date.pack(side='right', padx=5)


window.mainloop()