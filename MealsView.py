from PyQt6.QtWidgets import  QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QFrame, QGridLayout
from PyQt6.QtGui import QFont
from ChooseMealDialog import ChooseMealDialog

DEFAULT_DAILY_MEALS = ("Breakfast", "Dinner", "Supper")
DEFAULT_DAYS_NUMBER = 7

class DailyMeals(QWidget):
    def __init__(self, userDailyMeals = DEFAULT_DAILY_MEALS, parent = None):
        super().__init__(parent)

        self.frame = QFrame(self)
        self.frame.setFrameShape(QFrame.Shape.Box)
        self.frame.setLineWidth(1)
                               

        self.dailyMealsLayout = QVBoxLayout()
        self.dailyMealsButtons = []
        

        buttonsFont = QFont()
        buttonsFont.setItalic(True)
        
        for meal in userDailyMeals:
            mealButton = QPushButton(meal)
            mealButton.setFont(buttonsFont)
            mealButton.clicked.connect(lambda checked, currentMeal = meal: self.onMealButtonClicked(currentMeal))
            self.dailyMealsLayout.addWidget(mealButton)

        self.frame.setLayout(self.dailyMealsLayout)

        self.mainLayout = QGridLayout()
        self.mainLayout.addWidget(self.frame)

        self.setLayout(self.mainLayout)

    def onMealButtonClicked(self, meal):
        self.chooseMealDialog = ChooseMealDialog(meal, self)
        self.chooseMealDialog.show()

class MealsView(QWidget):
    def __init__(self, userDaysNumber = DEFAULT_DAYS_NUMBER, parent = None):
        super().__init__()

        self.mealsViewLayout = QHBoxLayout()
        

        for _ in range(userDaysNumber):
            self.mealsViewLayout.addWidget(DailyMeals())
        
        self.setLayout(self.mealsViewLayout)

