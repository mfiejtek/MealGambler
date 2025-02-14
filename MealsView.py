from PyQt6.QtWidgets import  QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QFrame, QGridLayout, QDialog, QSizePolicy
from PyQt6.QtGui import QFont
from ChooseMealDialog import ChooseMealDialog
from Meals_Database.meals_database_func import getMealsFromCategory
from Meals_Database.user_settings_func import load_settings
import random

DEFAULT_DAILY_MEALS = ("Breakfast", "Dinner", "Supper", "Snack")
DEFAULT_DAYS_NUMBER = 7

class DailyMeals(QWidget):
    def __init__(self, userDailyMeals, userDay, parent = None):
        super().__init__(parent)
        self.userDailyMeals = userDailyMeals
        self.userDays = userDay

        self.frame = QFrame(self)
        self.frame.setFrameShape(QFrame.Shape.Box)
        self.frame.setLineWidth(1)
                               
        self.dailyMealsLayout = QVBoxLayout()
        self.dailyMealsLayout.setContentsMargins(0, 0, 0, 0)
        self.dailyMealsLayout.setSpacing(0)
        self.dailyMealsButtons = []

        self.buttonsIni()


        self.frame.setLayout(self.dailyMealsLayout)

        self.mainLayout = QHBoxLayout()
        self.mainLayout.addWidget(self.frame)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.setSpacing(0)

        self.setLayout(self.mainLayout)

    def buttonsIni(self):
        for meal in self.userDailyMeals:
            mealButton = QPushButton(meal)
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
    def __init__(self,parent = None):
        super().__init__()

        self.mealsViewLayout = QHBoxLayout()
        self.refreshView()
        self.setLayout(self.mealsViewLayout)

    def clearView(self):
        while self.mealsViewLayout.count():
            item = self.mealsViewLayout.takeAt(0)
            widget = item.widget()
            widget.deleteLater()

    def refreshView(self):
        self.clearView()
        settings = load_settings()
        self.userDays = settings.get("days", [])
        self.userDailyMeals = settings.get("meals", [])

        for day in self.userDays:
            self.mealsViewLayout.addWidget(DailyMeals(self.userDailyMeals, day))

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

