import tkinter as tk
import time
import pyautogui

class AutoWriterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Auto Writer")

        self.text_label = tk.Label(root, text="Enter text:")
        self.text_label.pack()

        self.text_entry = tk.Text(root, height=5, width=50)
        self.text_entry.pack()

        self.speed_label = tk.Label(root, text="Words per minute:")
        self.speed_label.pack()

        self.speed_slider = tk.Scale(root, from_=0, to=120, orient=tk.HORIZONTAL) # Change from 120 for higher speeds.
        self.speed_slider.pack()

        self.start_button = tk.Button(root, text="Start Writing", command=self.start_writing)
        self.start_button.pack()

        self.stop_button = tk.Button(root, text="Stop Writing", command=self.stop_writing)
        self.stop_button.pack()

        self.is_writing = False 

    def start_writing(self):
        if not self.is_writing:
            self.is_writing = True
            speed = self.speed_slider.get()
            text_to_write = self.text_entry.get("1.0", tk.END)

            words = text_to_write.split()
            delay = 60 / speed  

            for word in words:
                if not self.is_writing:
                    break  
                if word.strip():  
                    pyautogui.write(word)
                    pyautogui.press('space')
                    time.sleep(delay)

            self.is_writing = False  

    def stop_writing(self):
        self.is_writing = False

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoWriterApp(root)
    root.mainloop()