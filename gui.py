import tkinter as tk
import time

window_width  = 400
window_height = 400

def main():
    window = tk.Tk()
    window.geometry("%dx%d" % (window_width, window_height))

    # Windowのタイトル
    window.title("GUI_change")

    label = tk.Label(window, text="bonjour!")
    label.place(x=0, y=0)

    window.mainloop()

if __name__ == "__main__":
    main()