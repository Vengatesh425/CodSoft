import tkinter as tk
import random

class RockPaperScissorsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")

        self.choices = ["Rock", "Paper", "Scissors"]
        self.uscore = 0
        self.cscore = 0

        self.Label=tk.Label(root,text=" Welcome to RockPaperScissors Game\n\n\nChoose Rock, Paper, or Scissors:").pack(pady=15)
        
        for choice in self.choices:
            tk.Button(root, text=choice, width=20, command=lambda c=choice: self.play(c)).pack(pady=5)

        self.result_label = tk.Label(root, text="", pady=20)
        self.result_label.pack()

        self.score_label = tk.Label(root, text=f"   Score Board : \n\n You: {self.uscore} \n Computer: {self.cscore}")
        self.score_label.pack(pady=10)

        tk.Button(root, text="Play Again", command=self.reset_game).pack(pady=10)

    def play(self, uchoice):
        self.uchoice, self.cchoice = uchoice, random.choice(self.choices)
        result = self.determine_winner(self.uchoice, self.cchoice)
        self.result_label.config(text=f"Your Choice : {self.uchoice}\n Computer's Choice : {self.cchoice}\n{result}")
        self.score_label.config(text=f"   Score Board : \n\n You: {self.uscore} \n Computer: {self.cscore}")

    def determine_winner(self, uchoice, cchoice):
        if uchoice == cchoice:
            return "Tie!"
        elif (uchoice == "Rock" and cchoice == "Scissors") or \
             (uchoice == "Paper" and cchoice == "Rock") or \
             (uchoice == "Scissors" and cchoice == "Paper"):
            self.uscore += 1
            return "You Win!"
        else:
            self.cscore += 1
            return "Computer Wins!"

    def reset_game(self):
        self.uscore = self.cscore = 0
        self.result_label.config(text="")
        self.score_label.config(text=f"   Score Board : \n\n You: {self.uscore} \n Computer: {self.cscore}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsApp(root)
    root.mainloop()
    
    
    
    
