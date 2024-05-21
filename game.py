import tkinter as tk
import random

class CatchGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Catch the Falling Objects")
        self.canvas = tk.Canvas(self.root, width=400, height=600, bg="white")
        self.canvas.pack()

        self.basket = self.canvas.create_rectangle(175, 550, 225, 575, fill="blue")
        self.objects = []
        self.score = 0

        self.score_text = self.canvas.create_text(50, 20, text=f"Score: {self.score}", font=("Arial", 14))

        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)

        self.create_object()
        self.update_game()

    def move_left(self, event):
        self.canvas.move(self.basket, -20, 0)

    def move_right(self, event):
        self.canvas.move(self.basket, 20, 0)

    def create_object(self):
        x = random.randint(10, 390)
        obj = self.canvas.create_oval(x, 0, x+20, 20, fill="red")
        self.objects.append(obj)
        self.root.after(2000, self.create_object)

    def update_game(self):
        for obj in self.objects:
            self.canvas.move(obj, 0, 5)
            if self.check_collision(obj):
                self.objects.remove(obj)
                self.canvas.delete(obj)
                self.score += 10
                self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")
            elif self.canvas.coords(obj)[1] > 600:
                self.game_over()
                return
        self.root.after(50, self.update_game)

    def check_collision(self, obj):
        obj_coords = self.canvas.coords(obj)
        basket_coords = self.canvas.coords(self.basket)
        if obj_coords[2] >= basket_coords[0] and obj_coords[0] <= basket_coords[2]:
            if obj_coords[3] >= basket_coords[1] and obj_coords[1] <= basket_coords[3]:
                return True
        return False

    def game_over(self):
        self.canvas.create_text(200, 300, text="Game Over", font=("Arial", 24), fill="red")

if __name__ == "__main__":
    root = tk.Tk()
    game = CatchGame(root)
    root.mainloop()
