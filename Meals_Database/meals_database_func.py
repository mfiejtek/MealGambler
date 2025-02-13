import sqlite3
import os
import sys

# Database path
# Prawidłowa ścieżka do bazy danych w przypadku uruchomienia z pliku .exe
if getattr(sys, 'frozen', False):  # Gdy uruchamiane z pliku exe
    BASE_DIR = os.path.dirname(sys.executable)  # Katalog, w którym znajduje się plik exe
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Katalog w przypadku uruchamiania z pliku .py
DB_PATH = os.path.join(BASE_DIR, "meals.db")  # Full database path


#Ini of meals database
def initializeDatabase():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS meals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT,
        calories INTEGER,
        ingredients TEXT
    )
    """)
    
    conn.commit()
    conn.close()

#Add meal to database
def addMeal(name, category, calories, ingredients):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO meals (name, category, calories, ingredients) VALUES (?, ?, ?, ?)", 
                   (name, category, calories, ingredients))
    
    conn.commit()
    conn.close()

#Delete meal from database
def deleteMeal(mealId):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM meals WHERE id = ?", (mealId,))
    
    conn.commit()
    conn.close()

def updateMeal(mealId, newName, newCategory, newCalories, newIngredients):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""UPDATE meals SET
                    name = ?,
                    category = ?,
                    calories = ?,
                    ingredients = ?
                    WHERE id = ?""", 
                (newName, newCategory, newCalories, newIngredients, mealId))

    conn.commit()
    conn.close()

#Get all meals from database
def getAllMeals():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM meals")
    meals = cursor.fetchall() 

    conn.close()
    return meals
