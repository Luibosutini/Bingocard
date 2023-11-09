import tkinter as tk
import random

class BingoCardGenerator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Bingo Card Generator")
        self.card = self.generate_bingo_card()
        self.buttons = [[None for _ in range(5)] for _ in range(5)]

        for i in range(5):
            for j in range(5):
                if i == 2 and j == 2:  # Center square is Free
                    label = tk.Label(self.root, text="Free", font=('Helvetica', 16, 'bold'))
                else:
                    label = tk.Label(self.root, text=str(self.card[i][j]), font=('Helvetica', 16))

                label.grid(row=i, column=j, padx=10, pady=10)
                label.bind('<Button-1>', lambda event, row=i, col=j: self.mark_square(row, col))

        self.root.mainloop()

    def generate_bingo_card(self):
        # Generate a list of 24 unique numbers for the Bingo card
        numbers = random.sample(range(1, 76), 24)

        # Split the numbers into 5 rows of 5, excluding the center square
        card = [numbers[i:i+5] for i in range(0, 24, 5)]

        # Insert a Free space in the center
        card[2][2] = "Free"

        return card

    def mark_square(self, row, col):
        if self.buttons[row][col] is None:
            self.buttons[row][col] = tk.Label(self.root, text="X", font=('Helvetica', 16, 'bold'))
            self.buttons[row][col].grid(row=row, column=col, padx=10, pady=10)
        else:
            self.buttons[row][col].destroy()
            self.buttons[row][col] = None

if __name__ == "__main__":
    BingoCardGenerator()
