import tkinter as tk

window = tk.Tk()
window.title("Tic - Tac - Toe")

fr_label = tk.Frame(master=window, relief=tk.SUNKEN, borderwidth=5)
fr_label.pack(fill=tk.X)
lbl_title = tk.Label(master=fr_label, text="Tic - Tac - Toe")
lbl_title.pack()

fr_content = tk.Frame(master=window)
fr_content.pack()

for r in range(3):
    window.columnconfigure(r, weight=1, minsize=75)
    window.rowconfigure(r, weight=1, minsize=50)
    for c in range(3):
        frame = tk.Frame(master=fr_content, relief=tk.RAISED, borderwidth=1)
        frame.grid(row=r, column=c, sticky="snew")
        label = tk.Label(master=frame, text=f"Row {r}\nColumn {c}")
        label.pack(padx=5, pady=5)

window.mainloop()
