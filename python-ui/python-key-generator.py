import tkinter as tk

#Important things
padding = 5

window = tk.Tk()

frame_control = tk.Frame(master=window, width=200, height=100, bg="red")
button_fwd = tk.Button(
    master=frame_control,
    text='F',
    bg='white'
)
button_bwd = tk.Button(
    master=frame_control,
    text='B',
    bg='white'
)
button_left = tk.Button(
    master=frame_control,
    text='L',
    bg='white'
)
button_right = tk.Button(
    master=frame_control,
    text='R',
    bg='white'
)
frame_control.columnconfigure([0, 1, 2], weight=1, minsize=20)
frame_control.rowconfigure([0, 1], weight=1, minsize=20)


button_fwd.grid(column=1, row=0, sticky="nsew", padx=padding, pady=padding)
button_bwd.grid(column=1, row=1, sticky="nsew", padx=padding, pady=padding)
button_left.grid(column=0, row=1, sticky="nsew", padx=padding, pady=padding)
button_right.grid(column=2, row=1, sticky="nsew", padx=padding, pady=padding)

frame_control.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

frame_io = tk.Frame(master=window, width=100, height=100, bg="yellow")
frame_input = tk.Frame(master=frame_io, width=100, height=50, bg="green")
label_input = tk.Label(
    master=frame_input,
    text='Enter speed/turn radius here:'
)
entry_input = tk.Entry(
    master=frame_input,
)
label_output = tk.Label(
    master=frame_io,
    text='Fucking hell'
)
frame_io.columnconfigure(0, weight=1, minsize=20)
frame_io.rowconfigure([0, 1], weight=1, minsize=20)
frame_input.columnconfigure(1, weight=1, minsize=20)
frame_input.rowconfigure(0, weight=1, minsize=20)
label_input.grid(column=0, row=0, sticky="nsew", padx=padding, pady=padding)
entry_input.grid(column=1, row=0, sticky="nsew", padx=padding, pady=padding)
frame_input.grid(column=0, row=0, sticky="nsew", padx=padding, pady=padding)
label_output.grid(column=0, row=1, sticky="nsew", padx=padding, pady=padding)
frame_io.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

window.mainloop()