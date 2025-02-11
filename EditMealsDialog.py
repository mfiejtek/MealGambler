from PyQt6.QtWidgets import QDialog
from PyQt6.QtGui import QStandardItem, QStandardItemModel
from Ui_Files.Ui_EditMealsDialog import Ui_Dialog
from Meals_Database.meals_database_func import getAllMeals


class EditMealsDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Edit meals")  
        #List view ini  
        self.listView.setModel(self.initializeListView())


    def initializeListView(self):
        meals = getAllMeals()
        model = QStandardItemModel()

        for meal in meals:
            name, category, ingredients = meal[1], meal[2], meal[3]
            meal_item = QStandardItem(f"{name}")
            model.appendRow(meal_item)
        
        return model

        