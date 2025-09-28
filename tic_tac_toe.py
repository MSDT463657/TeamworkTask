"""Simple console Tic Tac Toe game for two human players.

Run the module directly to play a game. Players take turns entering
positions 1-9 that map to the board as follows:

1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9

The first player is X and the second player is O. The first player to
align three marks horizontally, vertically, or diagonally wins. If the
board fills without a winner, the game is a draw.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class GameState:
    """Represents the current state of a Tic Tac Toe game."""

    board: List[str]
    current_player: str = "X"

    def switch_player(self) -> None:
        """Switch to the other player's turn."""
        self.current_player = "O" if self.current_player == "X" else "X"


WINNING_COMBINATIONS = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
)


def create_game() -> GameState:
    """Return a fresh game with an empty board."""
    return GameState(board=[" "] * 9)


def format_board(board: List[str]) -> str:
    """Return a string representation of the board."""
    rows = [" | ".join(board[i : i + 3]) for i in range(0, 9, 3)]
    separator = "\n---------\n"
    return separator.join(rows)


def print_board(board: List[str]) -> None:
    """Pretty-print the board to stdout."""
    print(format_board(board))


def winner(board: List[str]) -> Optional[str]:
    """Return the winning player symbol if there is a winner."""
    for a, b, c in WINNING_COMBINATIONS:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    return None


def is_draw(board: List[str]) -> bool:
    """Return True if the board is full with no winner."""
    return all(square != " " for square in board)


def take_turn(game: GameState) -> None:
    """Handle the current player's move, prompting until a valid move is made."""
    while True:
        try:
            choice = input(
                f"Player {game.current_player}, choose a square (1-9): "
            ).strip()
            position = int(choice) - 1
            if position not in range(9):
                raise ValueError
        except ValueError:
            print("Please enter a number from 1 to 9.")
            continue

        if game.board[position] != " ":
            print("That square is already taken. Try again.")
            continue

        game.board[position] = game.current_player
        break


def play_game() -> None:
    """Play a full game of Tic Tac Toe via the console."""
    game = create_game()
    print("Welcome to Tic Tac Toe! Player X goes first.\n")

    while True:
        print_board(game.board)
        take_turn(game)

        win = winner(game.board)
        if win:
            print_board(game.board)
            print(f"\nPlayer {win} wins! Congratulations!")
            break

        if is_draw(game.board):
            print_board(game.board)
            print("\nIt's a draw!")
            break

        game.switch_player()


if __name__ == "__main__":
    play_game()
