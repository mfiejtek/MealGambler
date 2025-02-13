from Ui_Files.Ui_GenerateMealsDialog import Ui_Dialog
from PyQt6.QtWidgets import QDialog, QWidget, QVBoxLayout, QPushButton

DEFAULT_DAILY_MEALS = ("Breakfast", "Dinner", "Supper")

class DailyMeals(QWidget):
    def __init__(self, userDailyMeals = DEFAULT_DAILY_MEALS):
        super().__init__()

        self.layout = QVBoxLayout()
        
        for meal in userDailyMeals:
            mealButton = QPushButton(meal)
            self.layout.addWid

        
        self.setLayout(self.layout)


class GenerateMealsDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
