# Notakto Problem Solver

Welcome to the Notakto Problem Solver repository! This project is designed to solve the "Notakto" game, also known as "To Win the Game," a combinatorial game where two players take turns removing markers from a grid of cells. The goal of the game is to force your opponent to remove the last marker.

## What is Notakto?

Notakto is a variation of Tic-Tac-Toe where the goal is to create a losing position for your opponent. The game is played on a grid of cells, and two players take turns marking cells. The catch is that a player must choose an entire group of cells (usually in a straight line) to mark, and they cannot choose cells that are already marked. The player who marks the last group of cells wins the game, but with Notakto, the player who is forced to mark the last group loses.

## How Does This Solver Work?

This repository contains a Python implementation of a Notakto problem solver. It uses combinatorial game theory principles to determine the optimal moves for a given position. The solver can help you analyze Notakto positions and find the best moves to win or force your opponent into a losing position.

## Getting Started

To use the Notakto Problem Solver, follow these steps:

1. Clone this repository to your local machine:

```bash
git clone https://github.com/abelxmendoza/Notakto-Problem.git
```

2. Install the required Python libraries if you haven't already. You can do this using pip:

```bash
pip install
```

3. Run the solver with a Notakto position as input. You can either input the position manually or load it from a file. For example:

```bash
python3 notaktoDepth.py
	or
python3 notaktoDepth2.py
	or
python3 notaktoMinimax.py
```

You will be prompted to enter the position, and the solver will provide the optimal move and analysis.



## Contributing

Contributions to this project are welcome! Whether you want to improve the solver, add new features, or fix bugs, please feel free to fork this repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](https://chat.openai.com/c/LICENSE) file for details.

## Acknowledgments

* Thanks to the community for contributions and feedback.
* Notakto image by [Wikipedia](https://en.wikipedia.org/wiki/Notakto).

Have fun playing and analyzing Notakto with this solver! If you have any questions or encounter issues, please don't hesitate to open an issue or reach out to the project maintainers.


## Documentation:

[https://docs.google.com/document/d/1t0bS8v3cPHdEAquWiqjxTLejev2GLJY5WfG0WhinLMc/edit?usp=sharing](https://docs.google.com/document/d/1t0bS8v3cPHdEAquWiqjxTLejev2GLJY5WfG0WhinLMc/edit?usp=sharing)
