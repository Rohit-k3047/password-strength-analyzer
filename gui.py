import tkinter as tk
from tkinter import ttk, messagebox
import threading

from analyzer import analyze_password
from generator import generate_password
from breach_checker import check_password_breach


# -----------------------------
# Main window
# -----------------------------
window = tk.Tk()

window.title("Password Strength Analyzer")
window.geometry("700x850")
window.resizable(False, False)

# -----------------------------
# Theme
# -----------------------------

BG = "#101820"
CARD = "#18232D"
TEXT = "#FFFFFF"
MUTED = "#AAB4BE"
ENTRY_BG = "#253442"

GREEN = "#2ECC71"
YELLOW = "#F1C40F"
ORANGE = "#E67E22"
RED = "#E74C3C"

window.configure(bg=BG)


# -----------------------------
# Functions
# -----------------------------
def check_breach_background(password):

    result = check_password_breach(password)

    window.after(
        0,
        lambda: update_breach_result(result)
    )

def update_breach_result(result):

    if result["compromised"] is True:

        breach_label.config(
            text=f"⚠ COMPROMISED — Seen {result['count']} times",
            fg=RED
        )

    elif result["compromised"] is False:

        breach_label.config(
            text="✓ NOT FOUND IN BREACH DATABASE",
            fg=GREEN
        )

    else:

        breach_label.config(
            text="? BREACH CHECK FAILED",
            fg=YELLOW
        )

def analyze():

    password = password_entry.get()

    if not password:

        strength_label.config(
            text="Strength: --",
            fg=TEXT
        )

        score_label.config(text="Score: --")
        risk_label.config(text="Risk: --")
        entropy_label.config(text="Entropy: --")

        breach_label.config(
            text="Breach Status: --",
            fg=TEXT
        )

        strength_bar["value"] = 0

        return

    # --------------------------------
    # Local password analysis
    # --------------------------------

    result = analyze_password(password)

    # --------------------------------
    # Strength color
    # --------------------------------

    if result["strength"] == "VERY STRONG":

        strength_color = GREEN

    elif result["strength"] == "STRONG":

        strength_color = GREEN

    elif result["strength"] == "MEDIUM":

        strength_color = YELLOW

    elif result["strength"] == "WEAK":

        strength_color = ORANGE

    else:

        strength_color = RED

    # --------------------------------
    # Display strength
    # --------------------------------

    strength_label.config(
        text=f"Strength: {result['strength']}",
        fg=strength_color
    )

    # --------------------------------
    # Score
    # --------------------------------

    score_label.config(
        text=f"Score: {result['score']} / 7"
    )

    # --------------------------------
    # Risk
    # --------------------------------

    risk_label.config(
        text=f"Risk: {result['risk_level']}"
    )

    # --------------------------------
    # Entropy
    # --------------------------------

    entropy_label.config(
        text=f"Effective Entropy: "
             f"{result['effective_entropy']} bits"
    )

    # --------------------------------
    # Strength meter
    # --------------------------------

    strength_bar["value"] = result["score"]

    # --------------------------------
    # Start breach check
    # --------------------------------

    breach_label.config(
        text="Checking breach database...",
        fg=YELLOW
    )

    thread = threading.Thread(
        target=check_breach_background,
        args=(password,),
        daemon=True
    )

    thread.start()

    # --------------------------------
    # Security checks
    # --------------------------------

    common_label.config(
        text=f"Common Password: {result['is_common']}"
    )

    sequence_label.config(
        text=f"Sequential Pattern: {result['has_sequence']}"
    )

    keyboard_label.config(
        text=f"Keyboard Pattern: {result['has_keyboard']}"
    )

    repetition_label.config(
        text=f"Repeated Characters: {result['has_repetition']}"
    )

    # --------------------------------
    # Suggestions
    # --------------------------------

    suggestions_text.delete(
        "1.0",
        tk.END
    )

    if result["suggestions"]:

        for suggestion in result["suggestions"]:

            suggestions_text.insert(
                tk.END,
                "• " + suggestion + "\n"
            )

    else:

        suggestions_text.insert(
            tk.END,
            "No basic improvements needed."
        )

def toggle_password():

    if password_entry.cget("show") == "*":

        password_entry.config(show="")
        show_button.config(text="Hide")

    else:

        password_entry.config(show="*")
        show_button.config(text="Show")


def generate():

    try:

        length = int(length_var.get())

        generated = generate_password(length)

        generated_entry.config(show="")

        generated_entry.delete(0, tk.END)

        generated_entry.insert(
            0,
            generated
        )

    except ValueError:

        messagebox.showerror(
            "Invalid Length",
            "Password length must be a number."
        )


def copy_password():

    password = generated_entry.get()

    if not password:

        messagebox.showwarning(
            "Nothing to Copy",
            "Generate a password first."
        )

        return

    window.clipboard_clear()
    window.clipboard_append(password)

    messagebox.showinfo(
        "Copied",
        "Password copied to clipboard.\n"
        "Clipboard will be cleared in 30 seconds."
    )

    window.after(
        30000,
        clear_clipboard
    )

def clear_clipboard():

    try:
        window.clipboard_clear()
        window.update()

    except tk.TclError:
        pass

# -----------------------------
# Title
# -----------------------------

title_label = tk.Label(
    window,
    text="PASSWORD STRENGTH ANALYZER",
    font=("Arial", 22, "bold"),
    bg=BG,
    fg=TEXT
)

title_label.pack(pady=(20, 5))

subtitle_label = tk.Label(
    window,
    text="Cybersecurity Password Assessment Tool",
    font=("Arial", 11),
    bg=BG,
    fg=MUTED
)

subtitle_label.pack(pady=(0, 20))


# -----------------------------
# Password section
# -----------------------------
password_frame = tk.LabelFrame(
    window,
    text=" Password ",
    padx=15,
    pady=15,
    bg=CARD,
    fg=TEXT,
    font=("Arial", 11, "bold")
)

password_frame.pack(
    fill="x",
    padx=40
)


password_entry = tk.Entry(
    password_frame,
    width=45,
    font=("Arial", 14),
    show="*",
    bg=ENTRY_BG,
    fg=TEXT,
    insertbackground=TEXT,
    relief="flat"
)

password_entry.grid(
    row=0,
    column=0,
    padx=5,
    pady=5
)

show_button = tk.Button(
    password_frame,
    text="Show",
    command=toggle_password,
    bg=ENTRY_BG,
    fg=TEXT,
    activebackground=ENTRY_BG,
    activeforeground=TEXT,
    relief="flat",
    padx=10
)

show_button.grid(
    row=0,
    column=1,
    padx=5
)


analyze_button = tk.Button(
    password_frame,
    text="ANALYZE PASSWORD",
    command=analyze,
    width=20,
    bg=GREEN,
    fg="black",
    activebackground=GREEN,
    relief="flat",
    font=("Arial", 10, "bold"),
    pady=6
)

analyze_button.grid(
    row=1,
    column=0,
    columnspan=2,
    pady=10
)


# -----------------------------
# Strength section
# -----------------------------

strength_frame = tk.LabelFrame(
    window,
    text=" Security Assessment ",
    padx=15,
    pady=15,
    bg=CARD,
    fg=TEXT,
    font=("Arial", 11, "bold")
)

strength_frame.pack(
    fill="x",
    padx=40,
    pady=15
)


strength_label = tk.Label(
    strength_frame,
    text="Strength: --",
    font=("Arial", 17, "bold"),
    bg=CARD,
    fg=TEXT
)

strength_label.pack()


strength_bar = ttk.Progressbar(
    strength_frame,
    orient="horizontal",
    length=500,
    mode="determinate",
    maximum=7
)

strength_bar.pack(
    pady=10
)


score_label = tk.Label(
    strength_frame,
    text="Score: --",
    font=("Arial", 12),
    bg=CARD,
    fg=TEXT
)

score_label.pack()


risk_label = tk.Label(
    strength_frame,
    text="Risk: --",
    font=("Arial", 12),
    bg=CARD,
    fg=TEXT
)

risk_label.pack()


entropy_label = tk.Label(
    strength_frame,
    text="Entropy: --",
    font=("Arial", 12),
    bg=CARD,
    fg=TEXT
)

entropy_label.pack()


breach_label = tk.Label(
    strength_frame,
    text="Breach Status: --",
    font=("Arial", 12),
    bg=CARD,
    fg=TEXT
)

breach_label.pack(
    pady=(5, 0)
)


# -----------------------------
# Security checks
# -----------------------------

checks_frame = tk.LabelFrame(
    window,
    text="Security Checks",
    padx=15,
    pady=10
)

checks_frame.pack(
    fill="x",
    padx=40
)


common_label = tk.Label(
    checks_frame,
    text="Common Password: --",
    anchor="w",
    bg=CARD,
    fg=TEXT
)

common_label.pack(
    fill="x"
)


sequence_label = tk.Label(
    checks_frame,
    text="Sequential Pattern: --",
    anchor="w",
    bg=CARD,
    fg=TEXT
)

sequence_label.pack(
    fill="x"
)


keyboard_label = tk.Label(
    checks_frame,
    text="Keyboard Pattern: --",
    anchor="w",
    bg=CARD,
    fg=TEXT
)

keyboard_label.pack(
    fill="x"
)


repetition_label = tk.Label(
    checks_frame,
    text="Repeated Characters: --",
    anchor="w",
    bg=CARD,
    fg=TEXT
)

repetition_label.pack(
    fill="x"
)


# -----------------------------
# Generator
# -----------------------------

generator_frame = tk.LabelFrame(
    window,
    text="Secure Password Generator",
    padx=15,
    pady=10
)

generator_frame.pack(
    fill="x",
    padx=40,
    pady=15
)


tk.Label(
    generator_frame,
    text="Length:"
).grid(
    row=0,
    column=0,
    padx=5
)


length_var = tk.StringVar(
    value="16"
)


length_box = ttk.Combobox(
    generator_frame,
    textvariable=length_var,
    values=["8", "12", "16", "20", "24", "32"],
    width=8,
    state="readonly"
)

length_box.grid(
    row=0,
    column=1,
    padx=5
)


generate_button = tk.Button(
    generator_frame,
    text="Generate",
    command=generate
)

generate_button.grid(
    row=0,
    column=2,
    padx=5
)


generated_entry = tk.Entry(
    generator_frame,
    width=35,
    font=("Arial", 12)
)

generated_entry.grid(
    row=1,
    column=0,
    columnspan=2,
    pady=10
)


copy_button = tk.Button(
    generator_frame,
    text="Copy",
    command=copy_password
)

copy_button.grid(
    row=1,
    column=2,
    padx=5
)


# -----------------------------
# Suggestions
# -----------------------------

suggestions_frame = tk.LabelFrame(
    window,
    text="Recommendations",
    padx=10,
    pady=10
)

suggestions_frame.pack(
    fill="both",
    expand=True,
    padx=40
)


suggestions_text = tk.Text(
    suggestions_frame,
    height=5,
    width=70
)

suggestions_text.pack(
    fill="both",
    expand=True
)


# -----------------------------
# Start application
# -----------------------------

window.mainloop()