from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
#TODO:
# turn the list of buttons into a list of lists so that we can check for draws
# Class for the ticktacktoe board
class TicTacToeBoard(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 3
        self.rows = 3
        self.spacing = 10
        self.padding = 10

        # Create a list of buttons for the grid
        self.buttons = []
        for i in range(9):
            button = Button(text="", font_size=40)
            button.bind(on_press=self.on_button_press)
            self.add_widget(button)
            self.buttons.append(button)

        # Set the current player to X
        self.current_player = "X"

    def on_button_press(self, button):
        # Update the button text and disable it
        button.text = self.current_player
        button.disabled = True

        # Check for a win
        if self.parent.check_for_win():
            self.parent.status_label.text = f"Player {self.current_player} wins!"
            self.parent.reset_game_button.disabled = False
            return

        # Switch players
        self.current_player = "O" if self.current_player == "X" else "X"
        self.parent.status_label.text = f"Player {self.current_player}'s turn"

        # Check for a draw
        if self.parent.check_for_win() == False:
            if self.parent.check_for_draw():
                self.parent.status_label.text = f"It's a draw!"
                self.parent.reset_game_button.disabled = False
                return

# Class for the ticktacktoe game
class TicTacToeGame(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 1
        self.spacing = 10
        self.padding = 10

        # Create the ticktacktoe board
        self.board = TicTacToeBoard()
        self.add_widget(self.board)

        # Create a label for displaying the game status
        self.status_label = Label(text="Player X's turn", font_size=20)
        self.add_widget(self.status_label)

        # Create a reset button
        self.reset_game_button = Button(text="Reset game", font_size=20, disabled=True)
        self.reset_game_button.bind(on_press=self.reset_game)
        self.add_widget(self.reset_game_button)

    def check_for_win(self):
        # Check if either player has won the game
        buttons = self.board.buttons
        # Check rows
        for i in range(3):
            if buttons[i * 3].text == buttons[i * 3 + 1].text == buttons[i * 3 + 2].text and buttons[i * 3].text != "":
                return True
        # Check columns
        for i in range(3):
            if buttons[i].text == buttons[i + 3].text == buttons[i + 6].text and buttons[i].text != "":
                return True
        # Check diagonals
        if buttons[0].text == buttons[4].text == buttons[8].text and buttons[0].text != "":
            return True
        if buttons[2].text == buttons[4].text == buttons[6].text and buttons[2].text != "":
            return True

        return False

    def check_for_draw(self):
        # Check if the game is a draw
        buttons = self.board.buttons
        for i in range(9):
            if buttons[i].text == "":
                return False
            return True

        return False

    def reset_game(self, button):
        # Reset the game board and enable the reset button
        for btn in self.board.buttons:
            btn.text = ""
            btn.disabled = False
        self.board.current_player = "X"
        self.status_label.text = "Player X's turn"
        button.disabled = True

# Main Kivy app
class TicTacToeApp(App):
    def build(self):
        game = TicTacToeGame()
        return game

if __name__ == "__main__":
    app = TicTacToeApp()
    app.run()