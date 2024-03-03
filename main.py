import tkinter as tk

class DrawingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Polygon Drawer")

        self.canvas = tk.Canvas(master, width=1920, height=1080, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.vertices = []
        self.polygon = None

        self.canvas.bind("<Button-1>", self.add_vertex)
        self.canvas.bind("<Button-3>", self.draw_polygon)

    def add_vertex(self, event):
        x, y = event.x, event.y
        self.vertices.append((x, y))
        self.canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill="black")
        if len(self.vertices) > 1:
            last_x, last_y = self.vertices[-2]
            self.canvas.create_line(last_x, last_y, x, y, fill="black")
        #display coordinates
        self.canvas.create_text(x + 10, y, text=f"({x}, {y})", anchor=tk.W)
    def draw_polygon(self, event):
        if len(self.vertices) > 2:
            self.canvas.create_polygon(self.vertices, outline="black", fill="")
            self.vertices = []

def main():
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
