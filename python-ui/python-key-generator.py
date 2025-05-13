import tkinter as tk
from tkinter import ttk 

#Important things
padding = 5

#Window et al
window = tk.Tk()
window.columnconfigure(0, weight=1, minsize=20)
window.rowconfigure(1, weight=1, minsize=20)


#Individual step
frm_step = tk.Frame(master=window, width=500, height=100, bg="yellow")
frm_step.columnconfigure([0, 1, 2, 3], weight=1, minsize=20)
frm_step.rowconfigure([0, 1], weight=1, minsize=20)
frm_step.grid(column=0, row=0, sticky="nwe", padx=padding, pady=padding)

listbox_movement = ttk.Combobox(
    master=frm_step,
    width=10,
    textvariable = tk.StringVar()
)

listbox_movement['values'] = (
    'Fowards',
    'Backwards',
    'Left',
    'Right'
)

listbox_movement.grid(column=0, row=0, sticky="news", padx=padding, pady=padding)

#Speed
frm_speed = tk.Frame(master=frm_step, width=40, height=30, bg="brown")
frm_speed.columnconfigure(1, weight=1, minsize=20)
frm_speed.rowconfigure([0], weight=1, minsize=20)
frm_speed.grid(column=1, row=0, sticky="nwe", padx=padding, pady=padding)
lbl_speed = tk.Label(
    master=frm_speed,
    text='Speed:'
)
lbl_speed.grid(column=0, row=0, sticky="new", padx=padding, pady=padding)
ent_speed = tk.Entry(
    master=frm_speed,
    width=10
)
ent_speed.grid(column=1, row=0, sticky="new", padx=padding, pady=padding)

#Time
frm_time = tk.Frame(master=frm_step, width=40, height=30, bg="brown")
frm_time.columnconfigure(1, weight=1, minsize=20)
frm_time.rowconfigure([0], weight=1, minsize=20)
frm_time.grid(column=2, row=0, sticky="nwe", padx=padding, pady=padding)
lbl_time = tk.Label(
    master=frm_time,
    text='Time:'
)
lbl_time.grid(column=0, row=0, sticky="new", padx=padding, pady=padding)
ent_time = tk.Entry(
    master=frm_time,
    width=10
)
ent_time.grid(column=1, row=0, sticky="new", padx=padding, pady=padding)

#Angle
frm_angle = tk.Frame(master=frm_step, width=40, height=30, bg="brown")
frm_angle.columnconfigure(1, weight=1, minsize=20)
frm_angle.rowconfigure([0], weight=1, minsize=20)
frm_angle.grid(column=3, row=0, sticky="nwe", padx=padding, pady=padding)
lbl_angle = tk.Label(
    master=frm_angle,
    text='Angle:'
)
lbl_angle.grid(column=0, row=0, sticky="new", padx=padding, pady=padding)
ent_angle = tk.Entry(
    master=frm_angle,
    width=10
)
ent_angle.grid(column=1, row=0, sticky="new", padx=padding, pady=padding)

frm_action = tk.Frame(master=frm_step, width=40, height=30, bg="brown")
frm_action.columnconfigure([0, 1], weight=1, minsize=20)
frm_action.rowconfigure([0], weight=1, minsize=20)
frm_action.grid(column=0, row=1, sticky="swe", padx=padding, pady=padding)



#Instruction info
frm_step_hold = tk.Frame(master=window, width=1080, height=720, bg="red")
frm_step_hold.columnconfigure([0], weight=1, minsize=200)
frm_step_hold.rowconfigure([0], weight=1, minsize=200)

frm_step_hold.grid(column=0, row=1, sticky="nsew", padx=padding, pady=padding)

#Verify and add frame
frm_solve = tk.Frame(master=window, width=200, height=50, bg="blue")
frm_solve.columnconfigure([0, 1], weight=1, minsize=20)
frm_solve.grid(column=0, row=2, sticky="nsew", padx=padding, pady=padding)

btn_add = tk.Button(
    master=frm_solve,
    text="+",
    width=1,
    height=1,
    bg="green",
    fg="black",
)
btn_add.grid(column=0, row=0, sticky="e", padx=padding, pady=padding)
btn_compute = tk.Button(
    master=frm_solve,
    text="/",
    width=1,
    height=1,
    bg="green",
    fg="black",
)
btn_compute.grid(column=1, row=0, sticky="w", padx=padding, pady=padding)

#Output frame
frm_solve = tk.Frame(master=window, width=200, height=50, bg="cyan")
frm_solve.grid(column=0, row=3, sticky="nsew", padx=padding, pady=padding)

window.mainloop()