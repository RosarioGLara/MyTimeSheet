import tkinter as tk
from datetime import datetime, timedelta
from PIL import Image, ImageTk
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
root.configure(bg="#fddefd")

# Create a label to display the current time
time_label = tk.Label(root, text="Current Time: ")
time_label.pack(pady=20)

timer_label = tk.Label(root, text="Session: 00:00:00")
timer_label.pack(pady=10)

# create a frame for buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=20)


#img for start
img_start = Image.open("start.png")
img_start = img_start.resize((50,50)) 
start_button = ImageTk.PhotoImage(img_start) # Reduces width and height by a factor of 2
#img for ending 
img_end = tk.PhotoImage(file= "stop.png")
img_end = img_end.zoom(3,3)
#img for saving
img_save = tk.PhotoImage(file="save.png")
img_save = img_save.zoom(3,3)

button_start = tk.Button(
    button_frame,
    image=start_button,
    bg="#fddefd",  # Match background
    activebackground="#fddefd",
    bd=0,
    highlightthickness=0,
    relief='flat',
    command=start_timer
)
button_start.image = img_start
button_start.pack(side=tk.LEFT, padx=10)
button_start.image = img_start  # Prevent garbage collection
button_start.pack(side=tk.LEFT, padx=10)


button_end = tk.Button(
    button_frame,
    image=img_end,
    bg="#fddefd",
    activebackground="#fddefd",
    bd=0,
    highlightthickness=0,
    relief='flat',
    command=end_timer
)
button_end.image = img_end
button_end.pack(side=tk.RIGHT, padx=5)
button_end.image = img_end
button_end.pack(side=tk.RIGHT, padx=5)

button2_frame = tk.Frame(root)
button2_frame.pack(pady=5)

button_save = tk.Button(
    button2_frame,
    image=img_save,
    bg="#fddefd",
    activebackground="#fddefd",
    bd=0,
    highlightthickness=0,
    relief='flat',
    command=save_session
)
button_save.image = img_save
button_save.pack(side=tk.TOP, padx=5)
button_save.pack(side=tk.TOP, padx=5)


session_list_label = tk.Label(root,text="Today's working hours:")
session_list_label.pack(pady=10)

show_time()
root.mainloop()
