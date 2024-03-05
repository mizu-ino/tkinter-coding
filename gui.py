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


def move_circle(x, y, dx, dy):
     # 仮の変数に移動後の値を記録
     _x = x + dx
     _y = y + dy
     # 上左右の壁に当たった？
     if _x < 0 or _x > canvas_width:
         dx *= -1
     if _y < 0 or _y > canvas_height:
         dy *= -1
     # 移動内容を反映
     if 0 <= _x <= canvas_width:
         x = _x
     if 0 <= _y <= canvas_height:
         y = _y

     return _x, _y, dx, dy

def main():
    window = tk.Tk()
    window.geometry("%dx%d" % (window_width, window_height))

    # Windowのタイトル
    window.title("GUI")

    label = tk.Label(window, text="bonjour!")
    label.place(x=0, y=0)
    
    canvas = tk.Canvas(window, width=canvas_width, height=canvas_height, bg="yellow")
    canvas.place(x=(window_width-canvas_width)/2, y=(window_height-canvas_height)/2)

    #---３点指定
    canvas.create_polygon(10, 10,
                      110, 10,
                      60, 100, fill="white")
    
    #---６点指定
    canvas.create_polygon(450, 60,
                      425, 17,
                      375, 17,
                      350, 60,
                      375, 103,
                      425, 103, fill="orange")
    
    while True:
        # Create a circle
        circle = create_circle(canvas, co["x"], co["y"], co["r"], fill="orange")
        co["x"], co["y"], co["dx"], co["dy"] = move_circle(co["x"], co["y"], co["dx"], co["dy"])
        label = tk.Label(window, text="%d, %d" % (co["x"], co["y"]))
        label.place(x=0, y=0)
        label2 = tk.Label(window, text="%d, %d" % (co["dx"], co["dy"]))
        label2.place(x=0, y=20)

        time.sleep(0.02)
        window.update()
        canvas.delete(circle)
        label.destroy()
    
    


    window.mainloop()




if __name__ == "__main__":
    main()