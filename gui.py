import tkinter as tk
import time


window_width  = 700
window_height = 500

canvas_width  = 600
canvas_height = 400

# co: circle_object
co = {
    "x": 150,
    "y": 350,
    "dx": 10,
    "dy": 10,
    "r": 20
}

def create_circle(canvas, x, y, r, **kwargs):
    return canvas.create_oval(x-r, y-r, x+r, y+r, **kwargs)

def main():
    window = tk.Tk()
    window.geometry("%dx%d" % (window_width, window_height))

    # Windowのタイトル
    window.title("GUI")

    label = tk.Label(window, text="bonjour!")
    label.place(x=0, y=0)
    
    canvas = tk.Canvas(window, width=canvas_width, height=canvas_height, bg="white")
    canvas.place(x=(window_width-canvas_width)/2, y=(window_height-canvas_height)/2)

    circle = create_circle(canvas, co["x"], co["y"], co["r"], fill="orange")

    window.mainloop()

if __name__ == "__main__":
    main()