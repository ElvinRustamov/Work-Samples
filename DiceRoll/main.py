class DiceRoll:
    import tkinter
    import random
    from tkinter import messagebox
    MIN = 1
    MAX = 6

    def __init__(self):
        self.root = self.tkinter.Tk()
        self.screen()

    def screen(self):
        self.user_input = self.tkinter.Entry(self.root)
        self.user_input.pack()
        button = self.tkinter.Button(self.root, text='Submit', command=self.get_user_entry)
        button.pack()
        self.root.title('Dice Roll Generator')
        self.root.mainloop()


    def get_user_entry(self):
        try:
            self.user_entry = int(self.user_input.get())
            self.calculating_point()
        except:
            self.messagebox.showerror('Python Error', f'Only Numbers Allowed. "{self.user_input.get()}" is not a number.')

    def calculating_point(self):
        total = 0
        for number in range(self.user_entry):
            dice_value = self.random.randint(self.MIN, self.MAX)
            total += dice_value
            print(f"Dice {number + 1} value is: {dice_value}")
        self.messagebox.showinfo("Total Point", f"Total Point: {total}")
        label = self.tkinter.Label(self.root, text=f'Total Point: {total}')
        label.pack()
        self.play_again()

    def play_again(self):
        msg_box = self.messagebox.askquestion('Exit Application', 'Play Again?')
        if msg_box == 'no':
            self.root.destroy()

if __name__ == '__main__':
    DiceRoll()
