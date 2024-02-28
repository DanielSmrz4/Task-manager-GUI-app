from tkinter import *
from tkinter import ttk
from customtkinter import *

# Appereance
set_appearance_mode("Dark")
set_default_color_theme("blue")

# Main window
window = CTk()
window.geometry("400x400+800+400")
window.title("Taskman")
window.resizable(False, False)


# FUNCTIONS -------------------------------------/
def add_task():
    task_text = entry_task.get()
    reward_text = entry_reward.get()
    entry_task.delete(0, END)
    entry_reward.delete(0, END)
    # Frame for one entry to a list
    one_entry_frame = CTkFrame(frame_task_list)
    one_entry_frame.pack(fill=BOTH, padx=10)

    label_task = CTkLabel(one_entry_frame, text=task_text, font=("Helvetica", 13))
    label_task.grid(row=0, column=0)

    button_task = CTkButton(one_entry_frame, text="Done", font=("Helvetica", 10, "bold"), width=50, corner_radius=40, height=20)
    button_task.grid(row=0, column=1, padx=(220, 0))

    label_reward = CTkLabel(one_entry_frame, text=reward_text, font=("Helvetica", 13,))
    label_reward.grid(row=1, column=0)

    button_reward = CTkButton(one_entry_frame, text="Claim", font=("Helvetica", 10, "bold"), width=50, corner_radius=40,height=20)
    button_reward.grid(row=1, column=1, padx=(220, 0))
    # Underline after each entry
    label_line = CTkFrame(frame_task_list, bg_color="white", height=2, corner_radius=20)
    label_line.pack(fill="x", padx=6)


# WIDGETS ---------------------------------------/

# Frame header
frame_header = CTkFrame(window, corner_radius=15, height=40, fg_color="transparent")
frame_header.pack(fill=BOTH, padx=10)

# Entry Task input
entry_task = CTkEntry(window, placeholder_text="Task", font=("Helvetica", 13, "bold"), width=380, height=25, corner_radius=15)
entry_task.pack(pady=(10, 0))

# Entry Reward input
entry_reward = CTkEntry(window, placeholder_text="Reward", font=("Helvetica", 13, "bold"), width=380, height=25, corner_radius=15)
entry_reward.pack(pady=(5, 0))

# Add button
button_add = CTkButton(window, text="Add", font=("Helvetica", 12, "bold"), width=50, corner_radius=40, height=20, command=add_task)
button_add.pack(pady=10)

# Frame task list
frame_task_list = CTkScrollableFrame(master=window, corner_radius=15, height=150)
frame_task_list.pack(side="bottom", fill=BOTH, padx=10, pady=(0, 10), expand=True)

# Text variable for messages for completing tasks and claiming rewards
var_task_list = StringVar()
var_task_list.set("My list")
# Label for Text variable
label_message = CTkLabel(frame_task_list, textvariable=var_task_list, font=("Helvetica", 12, "bold"))
label_message.pack()

# Completed button
button_completed = CTkButton(frame_task_list, text="Completed", font=("Helvetica", 12, "bold"), corner_radius=20, width=50, height=20)
# button_completed.pack(side="bottom", anchor="se", pady=10)


window.mainloop()
