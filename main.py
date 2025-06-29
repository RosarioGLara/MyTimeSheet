import tkinter as tk
from datetime import datetime, timedelta

# shows the current time in the label
def show_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    time_label.config(text=f"Current Time: {current_time}")
    root.after(1000, show_time) # update every second

# Start and end timer functions
def start_timer():
    #used global variables to keep track of the timer state
    global start_time, running 
    if not running:
        start_time = datetime.now()
        running = True
        update_timer()

def end_timer():
    global running, elapsed
    if running:
        running = False
        elapsed += datetime.now() - start_time # calculates how long the timer was running
        timer_label.config(text=f"Session: {str(elapsed)}")

def update_timer():
    if running:
        delta = datetime.now() - start_time + elapsed
        timer_label.config(text=f"Session: {str(delta).split('.')[0]}")
        root.after(1000, update_timer) # update every second

def save_session():
    global elapsed
    if elapsed.total_seconds() > 0: #only save if there is elapsed time
        today = datetime.now().strftime("%Y-%m-%d") # get today's date in YYYY-MM-DD format
        sessions[today] = sessions.get(today, timedelta()) + elapsed # adds the elapsed time to today's session
        session_list_label.config(
            text="Today's Total: " + str(sessions[today]).split('.')[0]
        )
        reset_timer()

def reset_timer():
    global start_time, running, elapsed # reset the timer variables
    start_time = None
    running = False
    elapsed = timedelta()
    timer_label.config(text="Session: 00:00:00")

#global variables
start_time = None
running = False
elapsed = timedelta()
sessions = {}

# Initialize the main window
root = tk.Tk()
root.title('MyTimeTracker')
root.geometry('400x350')

# Create a label to display the current time
time_label = tk.Label(root, text="Current Time: ")
time_label.pack(pady=20)

timer_label = tk.Label(root, text="Session: 00:00:00")
timer_label.pack(pady=10)

# create a frame for buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

button_start = tk.Button(button_frame, text="Start", command=start_timer)
button_start.pack(side=tk.LEFT, padx=10)

button_end = tk.Button(button_frame, text="End", command=end_timer)
button_end.pack(side=tk.RIGHT, padx=10)

button2_frame = tk.Frame(root)
button2_frame.pack(pady=20)
button_save = tk.Button(button2_frame, text="Save", command=save_session)
button_save.pack(side=tk.TOP, padx=10)

session_list_label = tk.Label(root,text="Today's working hours:")
session_list_label.pack(pady=10)

show_time()
root.mainloop()
