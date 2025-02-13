from PyQt6.QtWidgets import  QWidget, QVBoxLayout, QPushButton, QHBoxLayout
from PyQt6.QtGui import QFont

DEFAULT_DAILY_MEALS = ("Breakfast", "Dinner", "Supper")
DEFAULT_DAYS_NUMBER = 7

class DailyMeals(QWidget):
    def __init__(self, userDailyMeals = DEFAULT_DAILY_MEALS, parent = None):
        super().__init__(parent)

        self.dailyMealsLayout = QVBoxLayout()
        self.dailyMealsButtons = []

        buttonsFont = QFont()
        buttonsFont.setItalic(True)
        
        for meal in userDailyMeals:
            mealButton = QPushButton(meal)
            mealButton.setFont(buttonsFont)
            mealButton.clicked.connect(lambda checked, currentMeal = meal: self.onMealButtonClicked(currentMeal))
            self.dailyMealsLayout.addWidget(mealButton)

        self.setLayout(self.dailyMealsLayout)

    def onMealButtonClicked(slef, meal):
        print(f"Clicked {meal}")

class MealsView(QWidget):
    def __init__(self, userDaysNumber = DEFAULT_DAYS_NUMBER, parent = None):
        super().__init__()

        self.mealsViewLayout = QHBoxLayout()

        for _ in range(userDaysNumber):
            self.mealsViewLayout.addWidget(DailyMeals())
        
        self.setLayout(self.mealsViewLayout)

