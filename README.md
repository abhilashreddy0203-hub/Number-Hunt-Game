# 🎯 Number Hunt Game

A fun, interactive, console-based number guessing game built with
**Python**. Choose a difficulty level, follow the hints, and try to find
the secret number using as few attempts as possible.

## 🚀 Features

-   Four difficulty levels: Easy, Classic, Hard, and Insane
-   Random secret number generation
-   Helpful higher/lower hints after each guess
-   Limited attempts based on difficulty
-   Displays the narrowed range of possible numbers
-   Prevents duplicate guesses
-   Validates user input and number ranges
-   Replay option
-   Best-score tracking for each difficulty using JSON

## 🕹️ Difficulty Levels

  Difficulty     Number Range   Attempts
  ------------ -------------- ----------
  Easy                  1--50          8
  Classic              1--100          7
  Hard                 1--500          9
  Insane              1--1000         10

## 🛠️ Built With

-   Python 3
-   `random` --- generates the secret number
-   `json` --- stores best scores
-   `os` --- handles the score-file path

## 📁 Project Structure

``` text
Number-Hunt-Game/
├── number_hunt.py
├── number_hunt_best.json   # Created automatically when a best score is saved
└── README.md
```

You do not need to create `number_hunt_best.json` manually. The game
creates it when it saves a new best score.

## ⚙️ Getting Started

### 1. Clone the repository

``` bash
git clone https://github.com/abhilashreddy0203-hub/Number-Hunt-Game.git
```

### 2. Open the project folder

``` bash
cd Number-Hunt-Game
```

### 3. Run the game

Make sure Python 3 is installed, then run:

``` bash
python number_hunt.py
```

On some Windows systems, use:

``` bash
py number_hunt.py
```

## 🎮 How to Play

1.  Run the program.
2.  Choose a difficulty by entering a number from `1` to `4`.
3.  Enter a whole-number guess within the displayed range.
4.  Use the hints:
    -   **Too low** --- guess a higher number.
    -   **Too high** --- guess a lower number.
    -   **Correct** --- you found the secret number!
5.  Try to win in as few attempts as possible.
6.  Choose whether to play another round.

## 🏆 Best Scores

The game stores the best number of attempts for each difficulty in
`number_hunt_best.json`. A lower number of attempts is a better score.
This file is generated automatically when a new best score is recorded.

## 👨‍💻 Author

**Abhilash Reddy**

-   GitHub:
    [@abhilashreddy0203-hub](https://github.com/abhilashreddy0203-hub)
-   Repository: [Number Hunt
    Game](https://github.com/abhilashreddy0203-hub/Number-Hunt-Game)

## 📜 License

This project is available for educational and personal learning
purposes.
