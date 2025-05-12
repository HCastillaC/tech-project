import tkinter as tk

window = tk.Tk()

frame_control = tk.Frame()
button_foward = tk.Button(
    master=frame_control,
    text='F'
)
button_backward = tk.Button(
    master=frame_control,
    text='B'
)
button_left = tk.Button(
    master=frame_control,
    text='L'
)
button_right = tk.Button(
    master=frame_control,
    text='R'
)

button_foward.grid(row=0,column=1)
button_backward.grid(row=1,column=1)
button_left.grid(row=1,column=0)
button_right.grid(row=1,column=2)
frame_control.pack()

frame_input_output = tk.Frame()
entry_input = tk.Entry(
    master=frame_input_output
)
entry_output = tk.Label(
    master=frame_input_output,
    text="Fuck y'all"
)
entry_input.grid(row=0,column=0)
entry_output.grid(row=1,column=0)
frame_input_output.pack()

window.mainloop()