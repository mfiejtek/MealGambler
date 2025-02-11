import sqlite3
import os

# Database path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Dir with file
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
        ingredients TEXT
    )
    """)
    
    conn.commit()
    conn.close()

#Add meal to database
def addMeal(name, category, ingredients):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO meals (name, category, ingredients) VALUES (?, ?, ?)", 
                   (name, category, ingredients))
    
    conn.commit()
    conn.close()

#Delete meal from database
def deleteMeal(mealId):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM meals WHERE id = ?", (mealId,))
    
    conn.commit()
    conn.close()

def updateMeal(mealId, newName, newCategory, newIngredients):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("UPDATE meals SET name = ?, category = ?, ingredients = ? WHERE id = ?", (newName, newCategory, newIngredients, mealId))

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
