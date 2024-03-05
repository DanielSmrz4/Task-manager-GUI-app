from tkinter import *
from customtkinter import *
from datetime import datetime
import random


# Appereance
set_appearance_mode("Dark")
set_default_color_theme("blue")

# Main window
window = CTk()
window.geometry("400x450+1800+300")
window.title("Taskman")
window.resizable(False, False)
window.iconbitmap("icon2.ico")


# FUNCTIONS -----------------------------------------------------/
def add_task():
    window.focus()
    var_task_list.set("My list")
    task_text = entry_task.get()
    reward_text = entry_reward.get()
    if reward_text == "":
        reward_text = "Good feeling"
    if task_text == "":
        var_task_list.set("Fill again")
    else:
        entry_task.delete(0, END)
        entry_reward.delete(0, END)
        # Frame for one entry to a list
        one_entry_frame = CTkFrame(frame_task_list, height=80)
        one_entry_frame.pack(fill="x")
        # ------------------------------------ /

        def task_done():
            answears = ["Nice!", "Good job!", "Well done!", "Would you look at that!", "Ez"]
            answear = random.choice(answears)
            label_task.configure(text=answear)
            button_task.destroy()

        label_task = CTkLabel(one_entry_frame, text=task_text, font=("Helvetica", 13), text_color="steel blue2")
        label_task.place(relx=0.02, rely=0.01)
        button_task = CTkButton(one_entry_frame, text="Done", font=("Helvetica", 10, "bold"), width=50, corner_radius=50, height=15, command=task_done)
        button_task.place(relx=0.8, rely=0.01)
        # ------------------------------------ /

        def claim_reward():
            answears = ["Nice!", "Good job!", "Well done!", "Would you look at that!", "Ez", "Enjoy your reward"]
            if label_task.cget("text") in answears:
                var_task_list.set(f"My list")
                one_entry_frame.destroy()
                score.set(score.get() + 1)
                if score.get() >= 4:
                    label_daily_score.configure(text_color="lime green")

            else:
                answears = ["You ain't finished yet budy", "Not so fast cowboy", "Nope", "No room for cheaters here", "You can't fool me", "Nah uh"]
                answear = random.choice(answears)
                var_task_list.set(answear)

        label_reward = CTkLabel(one_entry_frame, text=reward_text, font=("Helvetica", 13,), text_color="lime green")
        label_reward.place(relx=0.02, rely=0.28)
        button_reward = CTkButton(one_entry_frame, text="Claim", font=("Helvetica", 10, "bold"), width=50, corner_radius=50, height=15, command=claim_reward)
        button_reward.place(relx=0.8, rely=0.28)

        # ------------------------------------ /

        label_line = CTkFrame(one_entry_frame, bg_color="gray", height=1, width= 380, corner_radius=20)
        label_line.place(relx=0.01, rely=0.6)


# WIDGETS ---------------------------------------------------------/

# Frame header -------------------------------/
frame_header = CTkFrame(window, corner_radius=15, height=40, fg_color="transparent")
frame_header.pack(fill="x", padx=20, pady=(10, 0))


# Function for updating date and time
def update():
    current_dt = datetime.now()
    date_now = current_dt.strftime("%d.%m.%Y")
    time_now = current_dt.strftime("%H:%M:%S")
    date_time = date_now + "\n" + time_now
    label_date_time.configure(text=date_time)
    label_date_time.after(1000, update)


# Label for displaying date and time
label_date_time = CTkLabel(frame_header, font=("Helvetica", 13), text_color="grey")
label_date_time.place(relx=0.4, rely=0.1)
# Variable and Label for daily score
score = IntVar()
score.set(0)
label_daily_score = CTkLabel(frame_header, textvariable=score, font=("Helvetica", 25, "bold"))
label_daily_score.place(relx=0.9, rely=0.2)
update()
# --------------------------------------------/

# Entry Task input
entry_task = CTkEntry(window, placeholder_text="Task", font=("Helvetica", 13, "bold"), width=380, height=25, corner_radius=15)
entry_task.pack(pady=(10, 0))

# Entry Reward input
entry_reward = CTkEntry(window, placeholder_text="Reward", font=("Helvetica", 13, "bold"), width=380, height=25, corner_radius=15)
entry_reward.pack(pady=(5, 0))

# Add button
button_add = CTkButton(window, text="Add", font=("Helvetica", 13, "bold"), width=70, corner_radius=40, height=20, command=add_task)
button_add.pack(pady=10)

# Frame task list
frame_task_list = CTkScrollableFrame(master=window, corner_radius=15, height=150)
frame_task_list.pack(side="bottom", fill=BOTH, padx=10, pady=(0, 10), expand=True)

# Text variable for messages for completing tasks and claiming rewards
var_task_list = StringVar()
var_task_list.set("My list")
# Label for Text variable
label_message = CTkLabel(frame_task_list, textvariable=var_task_list, font=("Helvetica", 12, "bold"))
label_message.pack(anchor="n")

# Completed button
button_completed = CTkButton(frame_task_list, text="Completed", font=("Helvetica", 12, "bold"), corner_radius=20, width=50, height=20)
# button_completed.pack(side="bottom", anchor="se", pady=10)


window.mainloop()
