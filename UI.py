import tkinter as tk

# Create custom input dialog using tkinter
def animate_entry(entry, index):
    colors = ["#ffc107", "#4caf50", "#f44336", "#00bcd4", "#9c27b0"]
    entry.configure(fg=colors[index])
    entry.after(1000, animate_entry, entry, (index + 1) % len(colors))

def get_province_input():
    root = tk.Tk()
    root.withdraw()
    global province
    province = ""
    
    # Create a custom input dialog using tkinter
    dialog = tk.Toplevel(root)
    dialog.title("VietNam Quiz game")
    dialog.geometry("300x150")
    dialog.configure(bg="#f5f5f5")
    dialog.resizable(False, False)
    dialog.attributes("-alpha", 0.95)
    dialog.attributes("-topmost", True)
    dialog.bind("<Escape>", lambda event: dialog.destroy())
    
    label = tk.Label(dialog, text="Enter a province:", font=("Arial", 12), bg="#f5f5f5")
    label.pack(pady=10)
    
    entry = tk.Entry(dialog, font=("Arial", 12), bg="#fff", relief=tk.FLAT, borderwidth=2, highlightcolor="#00bcd4", highlightthickness=2)
    entry.pack(pady=10)
    entry.focus_set()
    
    def ok_command():
        global province
        province = entry.get()
        dialog.destroy()
            
        
    button_frame = tk.Frame(dialog, bg="#f5f5f5")
    button_frame.pack(pady=10)
    
    ok_button = tk.Button(button_frame, text="OK", font=("Arial", 12), bg="#00bcd4", fg="#fff", activebackground="#018786", activeforeground="#fff", borderwidth=0, padx=20, pady=5, command=ok_command)
    ok_button.pack(side=tk.LEFT, padx=5)
    
    
    
    # Bind the Enter key to the OK button
    entry.bind("<Return>", lambda event: ok_button.invoke())
    
    # Animate the dialog if it loses focus
    def animate(event=None):
        x, y = dialog.winfo_x(), dialog.winfo_y()
        dialog.attributes("-alpha", 1.0)
        dialog.geometry("+{}+{}".format(x + 5, y + 5))
        dialog.after(20, lambda: dialog.geometry("+{}+{}".format(x - 5, y - 5)))
        dialog.after(40, lambda: dialog.geometry("+{}+{}".format(x + 5, y - 5)))
        dialog.after(60, lambda: dialog.geometry("+{}+{}".format(x - 5, y + 5)))
        dialog.after(80, lambda: dialog.geometry("+{}+{}".format(x, y)))
        dialog.after(100, lambda: dialog.attributes("-alpha", 0.95))
    
    dialog.bind("<FocusOut>", animate)
    
    # Wait for the dialog to be closed
    dialog.wait_window()
    
    root.destroy()
    return province