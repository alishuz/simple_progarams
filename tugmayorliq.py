import tkinter as tk
root = tk.Tk()
root.geometry("400x250")
root.title("Welcome to My App")
text_var = tk.StringVar()
text_var.set("Salom")
label = tk.Label(root,
                 textvariable=text_var,
                 anchor=tk.CENTER,
                 bg="lightblue",
                 height=3,
                 width=30,
                 bd=3,
                 font=("Arial", 16, "bold"),
                 cursor="hand2",
                 fg="red",
                 padx=15,
                 pady=15,
                 justify=tk.CENTER,
                 relief=tk.RAISED,
                 underline=0,
                 wraplength=250
                )
label.pack(pady=20)
root.mainloop()


