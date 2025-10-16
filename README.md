# Snake Game

Welcome to the **Snake Game**! This is a fun and interactive game where you control a snake to eat food and grow longer. The game features random colors and dynamic gameplay to keep you entertained.

## How to Play
1. Use the arrow keys to control the snake:
   - **Up Arrow**: Move up
   - **Down Arrow**: Move down
   - **Left Arrow**: Move left
   - **Right Arrow**: Move right
2. Eat the food to grow your snake.
3. Avoid colliding with the walls or yourself, or the game will end.

## Features
- Dynamic gameplay with increasing difficulty.
- Randomly generated food with numbers.
- Random background colors for a vibrant experience.

## Warning
**This game is not recommended for individuals with epilepsy or sensitivity to flashing lights and colors.** The game features rapidly changing random colors that may trigger seizures or discomfort.

## Requirements
- Python 3.10 or higher
- Required Python modules:
  - `turtle`
  - `random`

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/MonJarvis/Snake_game.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Snake_game
   ```
3. Install the required dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```

## Running the Game
1. Activate your Python environment (if applicable).
2. Run the game:
   ```bash
   python main.py
   ```

## Creating an Executable (Optional)
To create a standalone executable for the game, use PyInstaller:
```bash
pip install pyinstaller
pyinstaller --onefile --windowed main.py
```
The executable will be located in the `dist` folder.

## License
This project is licensed under the MIT License. Feel free to use and modify it as you like.

## Acknowledgments
- Built with Python's `turtle` module.
- Inspired by the classic Snake game.

Enjoy the game and have fun!
