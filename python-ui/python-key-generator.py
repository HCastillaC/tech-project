import tkinter as tk
import math as mt
from tkinter import ttk

#Important things
padding = 5
iterator = int(0)
lenght_rear = 0.095 #calculate 0.095
lenght_front = 0.09 #calculate 0.09
time_step = 0.01
instruction = ''
max_speed = 5

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
        text="{:.4f}".format(float(ent_speed.get()))
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
        text="{:.4f}".format(float(ent_time.get()))
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
        text="{:.4f}".format(float(ent_angle.get()))
    )
    ent_sub_angle.grid(column=1, row=0, sticky="nwse", padx=padding, pady=padding)
    
    #instruction
    frm_sub_instruction = tk.Frame(master=frm_substep, width=50, height=50, bg="brown")
    frm_sub_instruction.columnconfigure(1, weight=1, minsize=100)
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
    frm_sub_target_angle.columnconfigure(1, weight=1, minsize=100)
    frm_sub_target_angle.rowconfigure([0], weight=1, minsize=20)
    frm_sub_target_angle.grid(column=1, row=1, sticky="nwse", padx=padding, pady=padding)
    lbl_sub_target_angle = tk.Label(
        master=frm_sub_target_angle,
        text='Target angle:'
    )
    lbl_sub_target_angle.grid(column=0, row=0, sticky="nwse", padx=padding, pady=padding)
    ent_sub_target_angle = tk.Label(
        master=frm_sub_target_angle,
        text="{:.4f}".format(float(ent_target_angle.get()))
    )
    ent_sub_target_angle.grid(column=1, row=0, sticky="nwse", padx=padding, pady=padding)
    
    #frontal_movement
    frm_sub_frontal_movement = tk.Frame(master=frm_substep, width=50, height=50, bg="brown")
    frm_sub_frontal_movement.columnconfigure(1, weight=1, minsize=100)
    frm_sub_frontal_movement.rowconfigure([0], weight=1, minsize=20)
    frm_sub_frontal_movement.grid(column=2, row=1, sticky="nwse", padx=padding, pady=padding)
    lbl_sub_frontal_movement = tk.Label(
        master=frm_sub_frontal_movement,
        text='Frontal movement:'
    )
    lbl_sub_frontal_movement.grid(column=0, row=0, sticky="nwse", padx=padding, pady=padding)
    ent_sub_frontal_movement = tk.Label(
        master=frm_sub_frontal_movement,
        text="{:.4f}".format(float(ent_frontal_movement.get()))
    )
    ent_sub_frontal_movement.grid(column=1, row=0, sticky="nwse", padx=padding, pady=padding)
    
    #lateral_movement
    frm_sub_lateral_movement = tk.Frame(master=frm_substep, width=50, height=50, bg="brown")
    frm_sub_lateral_movement.columnconfigure(1, weight=1, minsize=100)
    frm_sub_lateral_movement.rowconfigure([0], weight=1, minsize=20)
    frm_sub_lateral_movement.grid(column=3, row=1, sticky="nwse", padx=padding, pady=padding)
    lbl_sub_lateral_movement = tk.Label(
        master=frm_sub_lateral_movement,
        text='Lateral movement:'
    )
    lbl_sub_lateral_movement.grid(column=0, row=0, sticky="nwse", padx=padding, pady=padding)
    ent_sub_lateral_movement = tk.Label(
        master=frm_sub_lateral_movement,
        text="{:.4f}".format(float(ent_lateral_movement.get()))
    )
    ent_sub_lateral_movement.grid(column=1, row=0, sticky="nwse", padx=padding, pady=padding)
    
    global instruction
    instruction += listbox_movement.get()[0] + ','
    #speed handling
    actual_speed = float(ent_speed.get())
    speed_output = (255 / max_speed) * actual_speed
    instruction += str(int(speed_output)) + ','
    instruction += "{:.0f}".format(float(ent_angle.get())) + ','
    instruction += "{:.4f}".format(float(ent_time.get())) + '/'
    
    ent_output.insert(tk.END, instruction)
    instruction = ''
    
        

def solve_time():
    theta_f_deg = float(ent_target_angle.get())
    delta_deg = float(ent_angle.get())
    v = float(ent_speed.get())
    L = lenght_front + lenght_rear
    L_r = lenght_rear

    theta_f = mt.radians(theta_f_deg)
    delta = mt.radians(delta_deg)

    if abs(delta) < 1e-6:  # Handle angle ≈ 0
        if abs(theta_f) < 1e-6:
            t = theta_f / v if v != 0 else 0
            dx = v * t
            dy = 0
        else:
            t = 0
            dx = 0
            dy = 0
    else:
        beta = mt.atan((L_r / L) * mt.tan(delta))
        omega = (v / L) * mt.cos(beta) * mt.tan(delta)
        t = theta_f / omega if omega != 0 else 0
        theta_f = omega * t
        dx = (v / omega) * mt.sin(theta_f) if omega != 0 else v * t
        dy = (v / omega) * (1 - mt.cos(theta_f)) if omega != 0 else 0

    ent_time.delete(0, tk.END)
    ent_time.insert(0, str(t))
    ent_frontal_movement.delete(0, tk.END)
    ent_frontal_movement.insert(0, str(dx))
    ent_lateral_movement.delete(0, tk.END)
    ent_lateral_movement.insert(0, str(dy))

    
def solve_target_angle():
    t = float(ent_time.get())
    delta_deg = float(ent_angle.get())
    v = float(ent_speed.get())
    L = lenght_front + lenght_rear
    L_r = lenght_rear

    delta = mt.radians(delta_deg)

    if abs(delta) < 1e-6:
        theta_f_deg = 0
        dx = v * t
        dy = 0
    else:
        beta = mt.atan((L_r / L) * mt.tan(delta))
        omega = (v / L) * mt.cos(beta) * mt.tan(delta)
        theta_f = omega * t
        theta_f_deg = mt.degrees(theta_f)
        dx = (v / omega) * mt.sin(theta_f) if omega != 0 else v * t
        dy = (v / omega) * (1 - mt.cos(theta_f)) if omega != 0 else 0

    ent_target_angle.delete(0, tk.END)
    ent_target_angle.insert(0, str(theta_f_deg))
    ent_frontal_movement.delete(0, tk.END)
    ent_frontal_movement.insert(0, str(dx))
    ent_lateral_movement.delete(0, tk.END)
    ent_lateral_movement.insert(0, str(dy))

    
def solve_angle():
    # Known values
    theta_f_deg = float(ent_target_angle.get())  # desired heading change (degrees)
    t = float(ent_time.get())                    # time in seconds
    v = float(ent_speed.get())                   # velocity (m/s)
    L = float(lenght_front + lenght_rear)        # wheelbase (m)
    L_r = lenght_rear                            # distance from rear axle to CoM (L/2)

    # Convert final heading to radians
    theta_f = mt.radians(theta_f_deg)
    if abs(theta_f) < 1e-6:
        ent_angle.delete(0, tk.END)
        ent_angle.insert(0, "0.0")
        ent_frontal_movement.delete(0, tk.END)
        ent_frontal_movement.insert(0, str(v * t))
        ent_lateral_movement.delete(0, tk.END)
        ent_lateral_movement.insert(0, "0.0")
        return
    
    # Function to evaluate heading error for a given δ (in radians)
    def heading_error(delta):
        try:
            beta = mt.atan((L_r / L) * mt.tan(delta))
            omega = (v / L) * mt.cos(beta) * mt.tan(delta)
            return omega * t - theta_f
        except:
            return float('inf')  # in case of division by zero or tan blowing up

    # Bisection method parameters
    delta_min = mt.radians(-45)  # lower bound in radians
    delta_max = mt.radians(45)   # upper bound in radians
    tolerance = 1e-6
    max_iterations = 100

    # Bisection loop
    for _ in range(max_iterations):
        delta_mid = (delta_min + delta_max) / 2
        f_mid = heading_error(delta_mid)
        f_min = heading_error(delta_min)

        if abs(f_mid) < tolerance:
            break

        if f_min * f_mid < 0:
            delta_max = delta_mid
        else:
            delta_min = delta_mid

    # Convert result to degrees
    delta_solution_deg = mt.degrees(delta_mid)
    
    # Compute yaw rate ω
    beta = mt.atan((L_r / L) * mt.tan(delta_mid))
    omega = (v / L) * mt.cos(beta) * mt.tan(delta_mid)

    # Compute final heading angle
    theta_f = omega * t

    # Compute displacement in global frame
    dx = (v / omega) * (mt.sin(theta_f))         # since sin(θ₀) = 0
    dy = (v / omega) * (1 - mt.cos(theta_f))     # since cos(θ₀) = 1

    # Frontal = dx, Lateral = dy when θ₀ = 0
    frontal = dx
    lateral = dy

    ent_angle.delete(0, tk.END)
    ent_angle.insert(0, str(delta_solution_deg))
    ent_frontal_movement.delete(0, tk.END)
    ent_frontal_movement.insert(0, str(frontal))
    ent_lateral_movement.delete(0, tk.END)
    ent_lateral_movement.insert(0, str(lateral))

def solve_movement():
    t = float(ent_time.get())
    delta_deg = float(ent_angle.get())
    v = float(ent_speed.get())
    L = lenght_front + lenght_rear
    L_r = lenght_rear

    delta = mt.radians(delta_deg)

    if abs(delta) < 1e-6:
        dx = v * t
        dy = 0
    else:
        beta = mt.atan((L_r / L) * mt.tan(delta))
        omega = (v / L) * mt.cos(beta) * mt.tan(delta)
        theta_f = omega * t
        dx = (v / omega) * mt.sin(theta_f) if omega != 0 else v * t
        dy = (v / omega) * (1 - mt.cos(theta_f)) if omega != 0 else 0

    ent_frontal_movement.delete(0, tk.END)
    ent_frontal_movement.insert(0, str(dx))
    ent_lateral_movement.delete(0, tk.END)
    ent_lateral_movement.insert(0, str(dy))


#Window et al
window = tk.Tk()
window.title('Path Computer')
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
    'Forwards',
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
frm_action.columnconfigure([0, 1, 2, 3, 4], weight=1)
frm_action.grid(column=0, row=1, sticky="nwse", padx=padding, pady=padding)
btn_add = tk.Button(
    master=frm_action,
    text="+",
    width=2,
    height=1,
    bg="green",
    fg="black",
    command=add_new_step
)
btn_add.grid(column=0, row=0, sticky="nwse", padx=padding, pady=padding)
btn_solve_time = tk.Button(
    master=frm_action,
    text="t",
    width=2,
    height=1,
    bg="green",
    fg="black",
    command=solve_time
)
btn_solve_time.grid(column=1, row=0, sticky="nwse", padx=padding, pady=padding)
btn_solve_target = tk.Button(
    master=frm_action,
    text="ψ",
    width=2,
    height=1,
    bg="green",
    fg="black",
    command=solve_target_angle
)
btn_solve_target.grid(column=2, row=0, sticky="nwse", padx=padding, pady=padding)
btn_solve_angle = tk.Button(
    master=frm_action,
    text="δ",
    width=2,
    height=1,
    bg="green",
    fg="black",
    command=solve_angle
)
btn_solve_angle.grid(column=3, row=0, sticky="nwse", padx=padding, pady=padding)
btn_solve_movement = tk.Button(
    master=frm_action,
    text="∆s",
    width=2,
    height=1,
    bg="green",
    fg="black",
    command=solve_movement
)
btn_solve_movement.grid(column=4, row=0, sticky="nwse", padx=padding, pady=padding)


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

#Instruction info# Replace your current frm_step_hold definition with this scrollable setup:

# Create a canvas to hold the scrollable frame
canvas = tk.Canvas(master=window, width=720, height=480, bg="red")
canvas.grid(column=0, row=1, sticky="nsew", padx=padding, pady=padding)

# Add a vertical scrollbar linked to the canvas
scrollbar = ttk.Scrollbar(master=window, orient="vertical", command=canvas.yview)
scrollbar.grid(column=1, row=1, sticky="ns")

canvas.configure(yscrollcommand=scrollbar.set)

# Create the frame that will contain the steps inside the canvas
frm_step_hold = tk.Frame(master=canvas, bg="red")
frm_step_hold.columnconfigure(0, weight=1, minsize=200)

# Create a window inside the canvas to hold frm_step_hold
canvas_frame = canvas.create_window((0, 0), window=frm_step_hold, anchor="nw")

# Update scrollregion when frm_step_hold size changes
def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

frm_step_hold.bind("<Configure>", on_frame_configure)

# Bind mousewheel scrolling to canvas
def _on_mousewheel(event):
    # For Windows and MacOS
    if event.delta:
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    # For Linux (event.num 4 is scroll up, 5 is scroll down)
    elif event.num == 4:
        canvas.yview_scroll(-1, "units")
    elif event.num == 5:
        canvas.yview_scroll(1, "units")

canvas.bind_all("<MouseWheel>", _on_mousewheel)  # Windows and MacOS
canvas.bind_all("<Button-4>", _on_mousewheel)    # Linux scroll up
canvas.bind_all("<Button-5>", _on_mousewheel)    # Linux scroll down

#Output frame
frm_solve = tk.Frame(master=window, width=200, height=50, bg="cyan")
frm_solve.grid(column=0, row=3, sticky="nsew", padx=padding, pady=padding)
frm_solve.columnconfigure([0], weight=1, minsize=20)
frm_solve.rowconfigure([0], weight=1, minsize=20)
ent_output = tk.Entry(
    master=frm_solve,
    text=instruction
)
ent_output.grid(column=0, row=0, sticky="nwse", padx=padding, pady=padding)

window.mainloop()
