from Ui_Files.Ui_GenerateMealsDialog import Ui_Dialog
from PyQt6.QtWidgets import QDialog

from SettingsDialog import SettingsDialog

class GenerateMealsDialog(QDialog, Ui_Dialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Generate meals")

        self.clearButton.clicked.connect(self.onClearButtonClick)
        self.randGenerateButton.clicked.connect(self.onRandomButtonClick)
        self.settingsButton.clicked.connect(self.onSettingButtonClick)


    def onSettingButtonClick(self):
        self.settingsDialog = SettingsDialog(self)
        self.settingsDialog.exec()
    
    def onClearButtonClick(self):
        self.mealsViewWidget.clearMeals()
    
    def onRandomButtonClick(self):
        self.mealsViewWidget.randomizeMeals()
