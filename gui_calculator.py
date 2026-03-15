import tkinter as tk
from tkinter import messagebox

# Calculator logic

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error"
    return a / b

# GUI setup
class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Python Calculator")
        self.geometry("320x570")
        self.resizable(False, False)
        self.expression = ""
        # ...existing code...
        self.create_widgets()

    def create_widgets(self):
        # Color scheme
        display_bg = "#222831"
        display_fg = "#eeeeee"
        display_font = ("Arial", 28, "bold")
        button_bg = "#393e46"
        button_fg = "#00adb5"
        button_font = ("Arial", 20, "bold")
        special_bg = "#00adb5"
        special_fg = "#222831"
        operator_bg = "#ff5722"
        operator_fg = "#fff"
        pad = 8

        # Improved display box
        self.display = tk.Entry(self, font=display_font, borderwidth=4, relief="groove", justify="right",
                               bg=display_bg, fg=display_fg)
        self.display.pack(fill="x", padx=pad, pady=(pad, pad//2))

        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
            ["C"],
            ["Restart", "Close"]
        ]

        for row in buttons:
            frame = tk.Frame(self, bg="", pady=pad//2)
            frame.pack(expand=True, fill="both", padx=pad)
            for btn in row:
                # Custom button style
                if btn == "Close":
                    bg = "#d7263d"
                    fg = "#fff"
                    b = tk.Button(frame, text=btn, font=button_font, command=self.destroy,
                                 bg=bg, fg=fg, activebackground="#fff", activeforeground=bg,
                                 relief="flat", borderwidth=0, highlightthickness=0)
                elif btn == "Restart":
                    bg = "#f7b32b"
                    fg = "#222831"
                    b = tk.Button(frame, text=btn, font=button_font, command=self.restart_calculator,
                                 bg=bg, fg=fg, activebackground="#fff", activeforeground=bg,
                                 relief="flat", borderwidth=0, highlightthickness=0)
                elif btn in ["=", "C"]:
                    bg = special_bg
                    fg = special_fg
                    b = tk.Button(frame, text=btn, font=button_font, command=lambda x=btn: self.on_button_click(x),
                                 bg=bg, fg=fg, activebackground=button_bg, activeforeground=button_fg,
                                 relief="flat", borderwidth=0, highlightthickness=0)
                elif btn in ["/", "*", "-", "+"]:
                    bg = operator_bg
                    fg = operator_fg
                    b = tk.Button(frame, text=btn, font=button_font, command=lambda x=btn: self.on_button_click(x),
                                 bg=bg, fg=fg, activebackground="#fff", activeforeground=bg,
                                 relief="flat", borderwidth=0, highlightthickness=0)
                else:
                    bg = button_bg
                    fg = button_fg
                    b = tk.Button(frame, text=btn, font=button_font, command=lambda x=btn: self.on_button_click(x),
                                 bg=bg, fg=fg, activebackground=special_bg, activeforeground=special_fg,
                                 relief="flat", borderwidth=0, highlightthickness=0)
                b.configure(width=4, height=2)
                b.pack(side="left", expand=True, fill="both", padx=(pad//2), pady=(pad//2))
                def on_enter(e, btn=b, bg=bg, fg=fg):
                    btn.configure(bg=fg, fg=bg)
                def on_leave(e, btn=b, bg=bg, fg=fg):
                    btn.configure(bg=bg, fg=fg)
                b.bind("<Enter>", lambda e, btn=b, bg=bg, fg=fg: on_enter(e, btn, bg, fg))
                b.bind("<Leave>", lambda e, btn=b, bg=bg, fg=fg: on_leave(e, btn, bg, fg))

        # Add product label at the bottom
        product_label = tk.Label(self, text="Product built by Turei Milner", font=("Arial", 10, "italic"), fg="#888", bg="#222831")
        product_label.pack(side="bottom", fill="x", pady=(4, 8))
    def restart_calculator(self):
        self.expression = ""
        self.display.delete(0, tk.END)

    def on_button_click(self, char):
        if char == "C":
            self.expression = ""
            self.display.delete(0, tk.END)
        elif char == "=":
            try:
                result = eval(self.expression)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
                self.expression = str(result)
            except Exception:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
                self.expression = ""
        else:
            self.expression += str(char)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expression)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
