import customtkinter as ctk

window = ctk.CTk()
window.title("Will you be my valentine")
window.geometry("640x400")

yheight, ywidth = 100, 40

def yes_click():
    popup = ctk.CTkToplevel(window)
    popup.title("THANK YOU CUTIE")
    popup.geometry("400x240")
    label = ctk.CTkLabel(popup, text="YAAYYY UR THE BEST CUTIE :DDDD", font=("Times New Roman", 20))
    label.pack(pady=50)

def no_click():
    global yheight, ywidth
    yheight += 25
    ywidth += 25
    yes_button.configure(width=ywidth, height=yheight)

main_label = ctk.CTkLabel(window, text="will you be my valentine?????(PWEASE)", font=("Times New Roman", 20))
main_label.pack(pady=20)

button_frame = ctk.CTkFrame(window)
button_frame.pack(pady=10)

yes_button = ctk.CTkButton(button_frame, text="YES", font=("Times New Roman", 14), command=yes_click, width=ywidth, height=yheight, fg_color="green")
no_button = ctk.CTkButton(button_frame, text="NO", font=("Times New Roman", 14), command=no_click, width=40, height=100, fg_color="red", hover_color="darkred")

yes_button.pack(side="left", padx=10)
no_button.pack(side="left", padx=10)

window.mainloop()