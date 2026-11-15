# py-tictactoe

Play tic-tac-toe against the computer in your terminal. The computer uses the minimax algorithm, so it never loses: the best you can do is draw.

Requires Python 3 and has no dependencies.

## Usage

```sh
python tic.py
```

You play `O` and move first. The computer plays `X`. Empty cells are shown as `0`.

Enter a move as `row column`, both counted from 0:

```
Enter Move : 1 1

0 0 0
0 O 0
0 0 0

0 0 0
0 O 0
0 0 X
```

The top-left cell is `0 0` and the bottom-right is `2 2`. Entering an occupied cell asks again.

## How it works

`getMaxMove` and `getMinMove` search the full game tree. The computer picks the move with the best guaranteed outcome, with a win scored 1, a draw 0 and a loss -1. The 3x3 board is small enough to search exhaustively, so there is no depth limit or pruning.

At the end the game prints `Player 1` if the computer (`X`) wins, `Player 2` if you (`O`) win, or `Draw`.

## License

MIT. See [LICENSE](LICENSE).
