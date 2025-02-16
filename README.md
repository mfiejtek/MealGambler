# MealGambler

MealGambler is a PyQt6-based application that helps users randomly select meals and create a weekly meal plan. It allows users to add, view, and delete meals stored in an SQLite database.

## Features
- Randomly generate meals for a weekly meal plan
- Add new meals with categories and ingredients
- Edit and delete meals
- Store meals in an SQLite database
- Save and load user settings in a JSON file

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/MealGambler.git
   cd MealGambler
   ```

2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Running the Application

Execute the following command:
```sh
python MainWindow.py
```

## Building an Executable (Windows)

To generate an `.exe` file, use PyInstaller:
```sh
pyinstaller MealGambler.spec
```
The executable will be found in the `dist` folder.

## File Structure
```
MealGambler/
│-- Meals_Database/
│   │-- meals.db (SQLite database)
│   │-- settings.json (User settings)
│-- Ui_Files/
│   │-- Ui_MainWindow.py
│-- MainWindow.py
│-- requirements.txt
```

## Notes
- The application will create a `meals.db` file in the executable's directory if it does not exist.
- User settings are stored in `settings.json`.

## License
This project is open-source. You are free to use and modify it.


