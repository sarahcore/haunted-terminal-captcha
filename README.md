# 👁️ HAUNTED TERMINAL: CAPTCHA

> **prove you're human. if you can.**

Haunted Terminal: CAPTCHA is a short psychological horror game developed in Python and played entirely through a terminal.

What begins as a simple human verification process gradually becomes something more unsettling.

The system asks questions. It evaluates your answers. It watches for inconsistencies.

But can you trust the results?

## 💻 About the Project

Haunted Terminal: CAPTCHA is a small terminal-based horror game inspired by CAPTCHA verification systems and unsettling interactions with technology.

The project was created as a way to **reinforce basic programming logic in Python** by developing a simple, interactive game.

The goal was to practice familiar concepts, such as variables, conditional statements, loops, functions and user input, while experimenting with psychological horror through text and terminal interactions.

The game was intentionally designed to remain simple, without graphical interfaces, external libraries or complex mechanics.

This is a playable version, but it may not be the final one. The project may receive improvements and changes over time.

## ✨ Features

- 15 interactive verification tests
- Terminal-based gameplay
- Retro green-on-black terminal aesthetic
- Typewriter-style text animations
- Timed messages and unexpected system behavior
- Hidden humanity score
- Three possible endings
- Randomized verification elements
- No external dependencies

## 🛠️ Technologies

- Python 3
- Python standard library (`random`, `sys`, `time`)
- ANSI escape sequences for terminal colors and effects

No external Python libraries or frameworks were used.

## 📁 Project Structure

```text
haunted-terminal-captcha/
├── captcha.py
└── README.md
```

## ▶️ How to Run

1. Download or clone this repository.
2. Make sure Python 3 is installed.
3. Open a terminal in the project folder.
4. Run one of the following commands:

**Option 1 — Python Launcher (Windows)**

```powershell
py captcha.py
```

**Option 2 — Python**

```powershell
python captcha.py
```

Alternatively, on Windows, you may be able to launch the game by double-clicking `captcha.py` if Python is properly installed and associated with `.py` files.

For the intended visual experience, running the game through Windows Terminal or another terminal with ANSI escape sequence support is recommended.

No additional dependencies are required.

## ⚙️ How It Works

The game presents a sequence of verification tests that require the player to enter answers through the terminal.

Python processes the responses using conditional statements and updates a hidden humanity score based on certain answers.

The experience also includes:

- Delays controlled by `time.sleep()`
- Character-by-character text animations
- Randomized system responses
- Terminal color formatting
- Conditional ending selection

The final classification depends on the player's accumulated score, including a randomized adjustment.

## 🧠 What I Practiced

Through this project, I reinforced:

- Basic programming logic
- Python variables and data types
- User input with `input()`
- Terminal output with `print()`
- Conditional statements (`if`, `elif`, `else`)
- Comparison operators
- Lists and membership checks
- Functions and parameters
- `for` loops
- Importing and using standard library modules
- Random number generation
- Controlling execution timing
- Working with terminal output

## 💡 What I Learned

Haunted Terminal: CAPTCHA was an opportunity to reinforce my understanding of Python fundamentals through a creative project.

Rather than focusing on learning entirely new concepts, I wanted to practice applying programming logic to a complete, interactive experience.

The project also allowed me to experiment with how timing, text presentation and simple terminal effects can influence the atmosphere of a game.

It was an exercise in combining programming practice with creativity while keeping the implementation straightforward.

## 🖤 Design Decisions

The game was intentionally kept simple to focus on reinforcing basic programming logic.

Some of the main design decisions were:

- Using a real terminal instead of a graphical interface
- Choosing green text on a black background to create a retro computer aesthetic
- Building tension through text rather than images
- Keeping the player's humanity score hidden
- Using timed messages to control the pacing
- Including multiple endings to make player responses meaningful
- Avoiding external libraries and unnecessary complexity

## 🚀 Future Improvements

The current version is playable, but it is not necessarily the final version.

As I continue developing my programming skills, I may revisit the project to improve the code, refine existing mechanics or experiment with new ideas.

I'm open to feedback, suggestions and constructive criticism, particularly regarding programming logic, code organization and potential improvements.

## 👁️ Haunted Terminal

Haunted Terminal is a concept for a future collection of experimental horror projects exploring unsettling interactions between humans and computers.

The collection is still in its early planning stages, and its ideas, projects and overall direction may change during development.

CAPTCHA is one of the first experiments connected to this concept.

