'''Create a Countdown timer in python'''
# Import the time module
import time
from tkinter import *
import multiprocessing
from tkinter import ttk, messagebox
from playsound import playsound
from threading import *

# Hour list
hour_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 
15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

# Minute List
min_sec_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 
15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 
30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44,
45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 
]

class CountDown:
    def __init__(self, root):
        self.window = root
        self.window.geometry("480x320+0+0")
        self.window.title('Timer')
        # Tkinter window background color
        self.window.configure(bg='gray35')
        # Fixing the Window length constant
        self.window.resizable(width = False, height = False)

        # Tkinter Label
        time_label = Label(self.window, text="Set Time", font=("times new roman",20, "bold"), bg='gray35', fg='yellow')
        time_label.place(x=180, y=30)

        hour_label = Label(self.window, text="Hour", font=("times new roman",15), bg='gray35', fg='white')
        hour_label.place(x=50, y=70)

        minute_label = Label(self.window, text="Minute", font=("times new roman",15), bg='gray35', fg='white')
        minute_label.place(x=200, y=70)

        second_label = Label(self.window, text="Second", font=("times new roman",15), bg='gray35', fg='white')
        second_label.place(x=350, y=70)
        # ===========================================

        # Tkinter Combobox
        self.hour = StringVar()
        self.hour_combobox = ttk.Combobox(self.window, width=8, height=10, textvariable=self.hour, font=("times new roman",15))
        self.hour_combobox['values'] = hour_list
        self.hour_combobox.current(0)
        self.hour_combobox.place(x=50,y=110)

        # Combobox for minutes
        self.minute = StringVar()
        self.minute_combobox = ttk.Combobox(self.window, width=8, height=10, textvariable=self.minute, font=("times new roman",15))
        self.minute_combobox['values'] = min_sec_list
        self.minute_combobox.current(0)
        self.minute_combobox.place(x=200,y=110)

        # Combobox for seconds
        self.second = StringVar()
        self.second_combobox = ttk.Combobox(self.window, width=8, height=10, textvariable=self.second, font=("times new roman",15))
        self.second_combobox['values'] = min_sec_list
        self.second_combobox.current(0)
        self.second_combobox.place(x=350,y=110)
        # ===========================================

        # Tkinter Button
        # calcel button
        cancel_button = Button(self.window, text='Cancel', font=('Helvetica',12), bg="white", fg="black", command=self.Cancel)
        cancel_button.place(x=140, y=150)

        # Done Button
        done_button = Button(self.window, text='Done', font=('Helvetica',12), bg="green", fg="white", command=self.Threding)
        done_button.place(x=250, y=150)

    # Creating a thread to run the show_time function
    def Threding(self):
        # Killing a thread through "daemon=True" isn't a good idea
        self.x = Thread(target=self.show_time, daemon=True)
        self.x.start()

    def Cancel(self):
        self.window.destroy()

    # When the done button will be pressed then,
    # this "show_time" function will get called.
    def show_time(self):
        # For avoiding any error
        try:
            time_display = Label(self.window, 
            font=('Helvetica', 20 , "bold"), 
            bg = 'gray35', fg = 'yellow')
            time_display.place(x=130, y=190)

            # Total amount of time in seconds
            h = (int(self.hour_combobox.get())*3600)
            m = (int(self.minute_combobox.get())*60)
            s = (int(self.second_combobox.get()))
            time_left = h + m + s

            while time_left > 0:
                # mins secs divmod:
                # mins, secs = divmod(time_left/60, time_left%60)
                # time_left = sec 60
                mins, secs = divmod(time_left, 60)

                hours = 0
                if mins > 60:
                    # hour minute
                    hours, mins = divmod(mins, 60)

                time_display.config(text=f"Time Left: {hours}: {mins}: {secs}")
                time_display.update()
                # sleep function: for 1 second
                time.sleep(1)
                time_left = time_left -1
            
            process = multiprocessing.Process(target=playsound, args=('Ringtones/romantic.mp3',))
            process.start()
            messagebox.showinfo('Time Over', 'Please ENTER to stop playing')
            process.terminate()
        # If an error occurs then an error message will show
        except Exception as es:
            # Tkinter Messagebox
            messagebox.showerror('Error!', f'Error due to {es}')

if __name__ == "__main__":
    root = Tk()
    obj = CountDown(root)
    root.mainloop()