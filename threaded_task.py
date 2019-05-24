from tkinter import messagebox
import threading


class ThreadedTask(threading.Thread):
    def __init__(self, queue, controller):
        threading.Thread.__init__(self)
        self.queue = queue
        self.controller = controller

    def update_status(self, text):
        self.controller.controller.controller.statusbar.set_status_label(text)

    def run(self):
        try:
            message = 'Completed'

        except Exception as e:
            message = 'Unexpected error: ' + str(e)

        self.queue.put(message)

        if message == 'Completed':
            messagebox.showinfo('Information', message)
        else:
            messagebox.showerror('Error', message)

        self.update_status(message)
        self.controller.progress_bar.destroy()
        self.controller.log_modify_button['state'] = 'normal'
