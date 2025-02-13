from PyQt6.QtWidgets import  QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QFrame, QGridLayout, QDialog, QSizePolicy
from PyQt6.QtGui import QFont
from ChooseMealDialog import ChooseMealDialog
from Meals_Database.meals_database_func import getMealsFromCategory
import random

DEFAULT_DAILY_MEALS = ("Breakfast", "Dinner", "Supper", "Snack")
DEFAULT_DAYS_NUMBER = 7

class DailyMeals(QWidget):
    def __init__(self, userDailyMeals, parent = None):
        super().__init__(parent)
        self.userDailyMeals = userDailyMeals

        self.frame = QFrame(self)
        self.frame.setFrameShape(QFrame.Shape.Box)
        self.frame.setLineWidth(1)
                               
        self.dailyMealsLayout = QVBoxLayout()
        self.dailyMealsLayout.setContentsMargins(0, 0, 0, 0)
        self.dailyMealsLayout.setSpacing(0)
        self.dailyMealsButtons = []

        self.buttonsIni()


        self.frame.setLayout(self.dailyMealsLayout)

        self.mainLayout = QGridLayout()
        self.mainLayout.addWidget(self.frame)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.setSpacing(0)

        self.setLayout(self.mainLayout)

    def buttonsIni(self):
        buttonsFont = QFont()
        buttonsFont.setItalic(True)
        
        for meal in self.userDailyMeals:
            mealButton = QPushButton(meal)
            mealButton.setFont(buttonsFont)
            mealButton.setAutoDefault(False)

            sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            mealButton.setSizePolicy(sizePolicy)

            self.dailyMealsButtons.append(mealButton)
            mealButton.clicked.connect(lambda checked, currentMeal = meal, button = mealButton: self.onMealButtonClicked(currentMeal, button))
            self.dailyMealsLayout.addWidget(mealButton)
        

    def onMealButtonClicked(self, meal, button):
        chooseMealDialog = ChooseMealDialog(meal, self)
        if chooseMealDialog.exec() == QDialog.DialogCode.Accepted:
            newButtonLabel = chooseMealDialog.getMeal()
            if newButtonLabel:
                button.setText(newButtonLabel)

     
class MealsView(QWidget):
    def __init__(self, userDaysNumber = DEFAULT_DAYS_NUMBER, userDailyMeals = DEFAULT_DAILY_MEALS, parent = None):
        super().__init__()

        self.mealsViewLayout = QHBoxLayout()
        self.userDaysNumber = userDaysNumber
        self.userDailyMeals = userDailyMeals
        
        for _ in range(self.userDaysNumber):
            self.mealsViewLayout.addWidget(DailyMeals(self.userDailyMeals))
        
        self.setLayout(self.mealsViewLayout)

    def clearMeals(self):
        for i in range(self.mealsViewLayout.count()):
            layoutItem = self.mealsViewLayout.itemAt(i)
            widget = layoutItem.widget()
            buttonCounter = 0
            for button in widget.dailyMealsButtons:
                button.setText(self.userDailyMeals[buttonCounter])
                buttonCounter+=1

    def randomizeMeals(self):
        for i in range(self.mealsViewLayout.count()):
            layoutItem = self.mealsViewLayout.itemAt(i)
            widget = layoutItem.widget()

            for buttonIndex, button in enumerate(widget.dailyMealsButtons):
                mealCategory = self.userDailyMeals[buttonIndex]
                meals = getMealsFromCategory(mealCategory)
                
                if meals:
                    randomMeal = random.choice(meals)
                    button.setText(randomMeal[1])

