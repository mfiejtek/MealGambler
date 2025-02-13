from PyQt6.QtWidgets import QDialog, QListView, QMessageBox
from PyQt6.QtGui import QStandardItem, QStandardItemModel
from PyQt6.QtCore import Qt, QModelIndex


from Meals_Database.meals_database_func import getMealsFromCategory
from Ui_Files.Ui_ChooseMealDialog import Ui_Dialog

class ChooseMealDialog(QDialog, Ui_Dialog):
    def __init__(self, category, parent = None):
        super().__init__(parent)
        self.category = category
        self.setupUi(self)
        self.setWindowTitle("Choose meals")
        
        self.listView.setSelectionMode(QListView.SelectionMode.SingleSelection)
        self.mealsModel = QStandardItemModel()
        self.listView.setModel(self.mealsModel)
        self.listView.doubleClicked.connect(self.getMeal)
        self.loadMeals()
        self.listView.setCurrentIndex(QModelIndex())

        self.buttonBox.accepted.connect(self.accept)

    def loadMeals(self):
        self.mealsModel.clear()
        meals = getMealsFromCategory(self.category)

        for meal in meals:
            mealItem = QStandardItem(meal[1])                           # Name
            mealItem.setData(meal[0], Qt.ItemDataRole.UserRole)         # Id
            mealItem.setData(meal[2], Qt.ItemDataRole.UserRole + 1)     # Category
            mealItem.setData(meal[3], Qt.ItemDataRole.UserRole + 2)     # Calories
            mealItem.setData(meal[4], Qt.ItemDataRole.UserRole + 3)     # Ingredients
            self.mealsModel.appendRow(mealItem)
    

    def getMeal(self):
        selectedIndex = self.listView.selectedIndexes()
        if not selectedIndex: 
            QMessageBox.warning(self, "Error", "Please select a meal.")
            return 
        index = selectedIndex[0]
        mealName = index.data(Qt.ItemDataRole.DisplayRole)
        self.done(QDialog.DialogCode.Accepted)
        return mealName
        
