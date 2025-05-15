import tkinter as tk
import math as mt
from tkinter import ttk 

#Important things
padding = 5
iterator = int(0)
lenght_rear = 0.095 #calculate
lenght_front = 0.9 #calculate
time_step = 0.01

def add_new_step():
    global iterator
    
    frm_step_hold.rowconfigure(iterator, weight=1, minsize=110)
    frm_substep = tk.Frame(master=frm_step_hold, width=500, height=100, bg="orange")
    frm_substep.columnconfigure([0, 1, 2, 3], weight=10, minsize=50)
    frm_substep.rowconfigure([0, 1], weight=1, minsize=50)
    frm_substep.grid(column=0, row=iterator, sticky="nwe", padx=padding, pady=padding)
    iterator+=1
    
    lbl_index = tk.Label(
        master=frm_substep,
        text=str(iterator)+':'
    )
    lbl_index.grid(column=0, row=0, sticky="nse", padx=padding, pady=padding)
    
    #Speed
    frm_sub_speed = tk.Frame(master=frm_substep, width=50, height=50, bg="brown")
    frm_sub_speed.columnconfigure(1, weight=1, minsize=20)
    frm_sub_speed.rowconfigure([0], weight=1, minsize=20)
    frm_sub_speed.grid(column=1, row=0, sticky="nwse", padx=padding, pady=padding)
    lbl_sub_speed = tk.Label(
        master=frm_sub_speed,
        text='Speed:'
    )
    lbl_sub_speed.grid(column=0, row=0, sticky="nwse", padx=padding, pady=padding)
    ent_sub_speed = tk.Label(
        master=frm_sub_speed,
        text=ent_speed.get()
    )
    ent_sub_speed.grid(column=1, row=0, sticky="nwse", padx=padding, pady=padding)
    
    #time
    frm_sub_time = tk.Frame(master=frm_substep, width=50, height=50, bg="brown")
    frm_sub_time.columnconfigure(1, weight=1, minsize=20)
    frm_sub_time.rowconfigure([0], weight=1, minsize=20)
    frm_sub_time.grid(column=2, row=0, sticky="nwse", padx=padding, pady=padding)
    lbl_sub_time = tk.Label(
        master=frm_sub_time,
        text='Time:'
    )
    lbl_sub_time.grid(column=0, row=0, sticky="nwse", padx=padding, pady=padding)
    ent_sub_time = tk.Label(
        master=frm_sub_time,
        text=ent_time.get()
    )
    ent_sub_time.grid(column=1, row=0, sticky="nwse", padx=padding, pady=padding)
    
    #angle
    frm_sub_angle = tk.Frame(master=frm_substep, width=50, height=50, bg="brown")
    frm_sub_angle.columnconfigure(1, weight=1, minsize=20)
    frm_sub_angle.rowconfigure([0], weight=1, minsize=20)
    frm_sub_angle.grid(column=3, row=0, sticky="nwse", padx=padding, pady=padding)
    lbl_sub_angle = tk.Label(
        master=frm_sub_angle,
        text='Angle:'
    )
    lbl_sub_angle.grid(column=0, row=0, sticky="nwse", padx=padding, pady=padding)
    ent_sub_angle = tk.Label(
        master=frm_sub_angle,
        text=ent_angle.get()
    )
    ent_sub_angle.grid(column=1, row=0, sticky="nwse", padx=padding, pady=padding)
    
    #instruction
    frm_sub_instruction = tk.Frame(master=frm_substep, width=50, height=50, bg="brown")
    frm_sub_instruction.columnconfigure(1, weight=1, minsize=20)
    frm_sub_instruction.rowconfigure([0], weight=1, minsize=20)
    frm_sub_instruction.grid(column=0, row=1, sticky="nwse", padx=padding, pady=padding)
    ent_sub_instruction = tk.Label(
        master=frm_sub_instruction,
        text=current_instruction.get()
    )
    ent_sub_instruction.grid(column=1, row=0, sticky="nwse", padx=padding, pady=padding)
    
    listbox_movement.current()
    
    #target_angle
    frm_sub_target_angle = tk.Frame(master=frm_substep, width=50, height=50, bg="brown")
    frm_sub_target_angle.columnconfigure(1, weight=1, minsize=20)
    frm_sub_target_angle.rowconfigure([0], weight=1, minsize=20)
    frm_sub_target_angle.grid(column=1, row=1, sticky="nwse", padx=padding, pady=padding)
    lbl_sub_target_angle = tk.Label(
        master=frm_sub_target_angle,
        text='Target angle:'
    )
    lbl_sub_target_angle.grid(column=0, row=0, sticky="nwse", padx=padding, pady=padding)
    ent_sub_target_angle = tk.Label(
        master=frm_sub_target_angle,
        text=ent_target_angle.get()
    )
    ent_sub_target_angle.grid(column=1, row=0, sticky="nwse", padx=padding, pady=padding)
    
    #frontal_movement
    frm_sub_frontal_movement = tk.Frame(master=frm_substep, width=50, height=50, bg="brown")
    frm_sub_frontal_movement.columnconfigure(1, weight=1, minsize=20)
    frm_sub_frontal_movement.rowconfigure([0], weight=1, minsize=20)
    frm_sub_frontal_movement.grid(column=2, row=1, sticky="nwse", padx=padding, pady=padding)
    lbl_sub_frontal_movement = tk.Label(
        master=frm_sub_frontal_movement,
        text='Frontal movement:'
    )
    lbl_sub_frontal_movement.grid(column=0, row=0, sticky="nwse", padx=padding, pady=padding)
    ent_sub_frontal_movement = tk.Label(
        master=frm_sub_frontal_movement,
        text=ent_frontal_movement.get()
    )
    ent_sub_frontal_movement.grid(column=1, row=0, sticky="nwse", padx=padding, pady=padding)
    
    #lateral_movement
    frm_sub_lateral_movement = tk.Frame(master=frm_substep, width=50, height=50, bg="brown")
    frm_sub_lateral_movement.columnconfigure(1, weight=1, minsize=20)
    frm_sub_lateral_movement.rowconfigure([0], weight=1, minsize=20)
    frm_sub_lateral_movement.grid(column=3, row=1, sticky="nwse", padx=padding, pady=padding)
    lbl_sub_lateral_movement = tk.Label(
        master=frm_sub_lateral_movement,
        text='Lateral movement:'
    )
    lbl_sub_lateral_movement.grid(column=0, row=0, sticky="nwse", padx=padding, pady=padding)
    ent_sub_lateral_movement = tk.Label(
        master=frm_sub_lateral_movement,
        text=ent_lateral_movement.get()
    )
    ent_sub_lateral_movement.grid(column=1, row=0, sticky="nwse", padx=padding, pady=padding)

def solve_time():
    global time_step
    
    solve_target_angle = 0
    solve_speed = float(ent_speed.get())
    solve_delta = float(ent_angle.get())
    solve_beta = mt.atan((lenght_rear / (lenght_rear + lenght_front)) * mt.tan(solve_delta * mt.pi / 180)) * 180 / mt.pi
    solve_frontal_movement = 0
    solve_lateral_movement = 0
    solve_time = 0
    while mt.fabs(solve_target_angle) < mt.fabs(float(ent_target_angle.get())):
        solve_frontal_movement += solve_speed * mt.cos((solve_target_angle + solve_beta) * mt.pi / 180) * time_step
        solve_lateral_movement += solve_speed * mt.sin((solve_target_angle + solve_beta) * mt.pi / 180) * time_step
        solve_target_angle += (solve_speed / (lenght_rear + lenght_front)) * mt.cos(solve_beta * mt.pi / 180) * mt.tan(solve_delta * mt.pi / 180) * time_step
        solve_time+=time_step
        print(mt.cos(solve_beta * mt.pi / 180))
    
    ent_time.delete(0, tk.END)
    ent_time.insert(0, str(solve_time))
    ent_frontal_movement.delete(0, tk.END)
    ent_frontal_movement.insert(0, str(solve_frontal_movement))
    ent_lateral_movement.delete(0, tk.END)
    ent_lateral_movement.insert(0, str(solve_lateral_movement))

#Window et al
window = tk.Tk()
window.columnconfigure(0, weight=1, minsize=20)
window.rowconfigure(1, weight=1, minsize=20)

#Individual step
frm_step = tk.Frame(master=window, width=500, height=100, bg="yellow")
frm_step.columnconfigure([0, 1, 2, 3], weight=1, minsize=50)
frm_step.rowconfigure([0, 1], weight=1, minsize=50)
frm_step.grid(column=0, row=0, sticky="nwe", padx=padding, pady=padding)


current_instruction = tk.StringVar()
listbox_movement = ttk.Combobox(
    master=frm_step,
    width=10,
    textvariable = current_instruction,
)

listbox_movement['values'] = (
    'Fowards',
    'Backwards',
    'Left',
    'Right'
)

listbox_movement.grid(column=0, row=0, sticky="news", padx=padding, pady=padding)

#Speed
frm_speed = tk.Frame(master=frm_step, width=70, height=70, bg="brown")
frm_speed.columnconfigure(1, weight=1, minsize=20)
frm_speed.rowconfigure([0], weight=1, minsize=20)
frm_speed.grid(column=1, row=0, sticky="nwse", padx=padding, pady=padding)
lbl_speed = tk.Label(
    master=frm_speed,
    text='Speed:'
)
lbl_speed.grid(column=0, row=0, sticky="nwse", padx=padding, pady=padding)
ent_speed = tk.Entry(
    master=frm_speed,
    width=10
)
ent_speed.grid(column=1, row=0, sticky="nwse", padx=padding, pady=padding)

#Time
frm_time = tk.Frame(master=frm_step, width=70, height=70, bg="brown")
frm_time.columnconfigure(1, weight=1, minsize=20)
frm_time.rowconfigure([0], weight=1, minsize=20)
frm_time.grid(column=2, row=0, sticky="nwse", padx=padding, pady=padding)
lbl_time = tk.Label(
    master=frm_time,
    text='Time(s):'
)
lbl_time.grid(column=0, row=0, sticky="nwse", padx=padding, pady=padding)
ent_time = tk.Entry(
    master=frm_time,
    width=10
)
ent_time.grid(column=1, row=0, sticky="nwse", padx=padding, pady=padding)

#Angle
frm_angle = tk.Frame(master=frm_step, width=70, height=70, bg="brown")
frm_angle.columnconfigure(1, weight=1, minsize=20)
frm_angle.rowconfigure([0], weight=1, minsize=20)
frm_angle.grid(column=3, row=0, sticky="nwse", padx=padding, pady=padding)
lbl_angle = tk.Label(
    master=frm_angle,
    text='Angle(°):'
)
lbl_angle.grid(column=0, row=0, sticky="nwse", padx=padding, pady=padding)
ent_angle = tk.Entry(
    master=frm_angle,
    width=10
)
ent_angle.grid(column=1, row=0, sticky="nwse", padx=padding, pady=padding)

#Tools
frm_action = tk.Frame(master=frm_step, width=70, height=70, bg="brown")
frm_action.columnconfigure([0, 1, 2, 3], weight=1)
frm_action.grid(column=0, row=1, sticky="nwse", padx=padding, pady=padding)
btn_add = tk.Button(
    master=frm_action,
    text="+",
    width=3,
    height=1,
    bg="green",
    fg="black",
    command=add_new_step
)
btn_add.grid(column=0, row=0, sticky="nwse", padx=padding, pady=padding)
btn_solve_time = tk.Button(
    master=frm_action,
    text="t",
    width=3,
    height=1,
    bg="green",
    fg="black",
    command=solve_time
)
btn_solve_time.grid(column=1, row=0, sticky="nwse", padx=padding, pady=padding)
btn_solve_target = tk.Button(
    master=frm_action,
    text="T",
    width=3,
    height=1,
    bg="green",
    fg="black",
)
btn_solve_target.grid(column=2, row=0, sticky="nwse", padx=padding, pady=padding)
btn_solve_angle = tk.Button(
    master=frm_action,
    text="a",
    width=3,
    height=1,
    bg="green",
    fg="black",
)
btn_solve_angle.grid(column=3, row=0, sticky="nwse", padx=padding, pady=padding)


#target_angle
frm_target_angle = tk.Frame(master=frm_step, width=70, height=70, bg="brown")
frm_target_angle.columnconfigure(1, weight=1, minsize=20)
frm_target_angle.rowconfigure([0], weight=1, minsize=20)
frm_target_angle.grid(column=1, row=1, sticky="nwse", padx=padding, pady=padding)
lbl_target_angle = tk.Label(
    master=frm_target_angle,
    text='Target angle(°):'
)
lbl_target_angle.grid(column=0, row=0, sticky="nwse", padx=padding, pady=padding)
ent_target_angle = tk.Entry(
    master=frm_target_angle,
    width=10
)
ent_target_angle.grid(column=1, row=0, sticky="nwse", padx=padding, pady=padding)


#frontal_movement
frm_frontal_movement = tk.Frame(master=frm_step, width=70, height=70, bg="brown")
frm_frontal_movement.columnconfigure(1, weight=1, minsize=20)
frm_frontal_movement.rowconfigure([0], weight=1, minsize=20)
frm_frontal_movement.grid(column=2, row=1, sticky="nwse", padx=padding, pady=padding)
lbl_frontal_movement = tk.Label(
    master=frm_frontal_movement,
    text='Frontal movement:'
)
lbl_frontal_movement.grid(column=0, row=0, sticky="nwse", padx=padding, pady=padding)
ent_frontal_movement = tk.Entry(
    master=frm_frontal_movement,
    width=10
)
ent_frontal_movement.grid(column=1, row=0, sticky="nwse", padx=padding, pady=padding)


#lateral_movement
frm_lateral_movement = tk.Frame(master=frm_step, width=70, height=70, bg="brown")
frm_lateral_movement.columnconfigure(1, weight=1, minsize=20)
frm_lateral_movement.rowconfigure([0], weight=1, minsize=20)
frm_lateral_movement.grid(column=3, row=1, sticky="nwse", padx=padding, pady=padding)
lbl_lateral_movement = tk.Label(
    master=frm_lateral_movement,
    text='Lateral movement:'
)
lbl_lateral_movement.grid(column=0, row=0, sticky="nwse", padx=padding, pady=padding)
ent_lateral_movement = tk.Entry(
    master=frm_lateral_movement,
    width=10
)
ent_lateral_movement.grid(column=1, row=0, sticky="nwse", padx=padding, pady=padding)

#Instruction info
frm_step_hold = tk.Frame(master=window, width=1080, height=720, bg="red")
frm_step_hold.columnconfigure([0], weight=1, minsize=200)
frm_step_hold.grid(column=0, row=1, sticky="nsew", padx=padding, pady=padding)

#Verify and add frame
frm_solve = tk.Frame(master=window, width=200, height=50, bg="blue")
frm_solve.columnconfigure([0], weight=1, minsize=20)
frm_solve.grid(column=0, row=2, sticky="nsew", padx=padding, pady=padding)

btn_compute = tk.Button(
    master=frm_solve,
    text="Compute!",
    width=10,
    height=1,
    bg="green",
    fg="black",
)
btn_compute.grid(column=0, row=0, sticky="", padx=padding, pady=padding)

#Output frame
frm_solve = tk.Frame(master=window, width=200, height=50, bg="cyan")
frm_solve.grid(column=0, row=3, sticky="nsew", padx=padding, pady=padding)

window.mainloop()
