from PyQt6.QtWidgets import QDialog, QMessageBox
from Meals_Database.user_settings_func import load_settings, save_settings


from Ui_Files.Ui_SettingsDialog import Ui_Dialog

class SettingsDialog(QDialog, Ui_Dialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.initializeCheckBoxes()
        self.buttonBox.accepted.connect(self.onSaveButtonclick)
        
    def initializeCheckBoxes(self):
        settings = load_settings()
        mealsSettings = settings.get("meals", [])
        daysSettings = settings.get("days", [])

        self.mondayCheckBox.setChecked(self.mondayCheckBox.text() in daysSettings)
        self.tuesdayCheckBox.setChecked(self.tuesdayCheckBox.text() in daysSettings)
        self.wednesdayCheckBox.setChecked(self.wednesdayCheckBox.text() in daysSettings)
        self.thursdayCheckBox.setChecked(self.thursdayCheckBox.text()in daysSettings)
        self.fridayCheckBox.setChecked(self.fridayCheckBox.text() in daysSettings)
        self.saturdayCheckBox.setChecked(self.saturdayCheckBox.text() in daysSettings)
        self.sundayCheckBox.setChecked(self.sundayCheckBox.text() in daysSettings)

        self.breakfastCheckBox.setChecked(self.breakfastCheckBox.text() in mealsSettings)
        self.dinnerCheckBox.setChecked(self.dinnerCheckBox.text() in mealsSettings)
        self.supperCheckBox.setChecked(self.supperCheckBox.text() in mealsSettings)
        self.snackCheckBox.setChecked(self.snackCheckBox.text() in mealsSettings)
        self.otherCheckBox.setChecked(self.otherCheckBox.text() in mealsSettings)




    def onSaveButtonclick(self):
        selectedMeals = []
        if self.breakfastCheckBox.isChecked():
            selectedMeals.append("Breakfast")
        if self.dinnerCheckBox.isChecked():
            selectedMeals.append("Dinner")
        if self.supperCheckBox.isChecked():
            selectedMeals.append("Supper")
        if self.snackCheckBox.isChecked():
            selectedMeals.append("Snack")
        if self.otherCheckBox.isChecked():
            selectedMeals.append("Other")

        selectedDays = []
        if self.mondayCheckBox.isChecked():
            selectedDays.append("Monday")
        if self.tuesdayCheckBox.isChecked():
            selectedDays.append("Tuesday")
        if self.wednesdayCheckBox.isChecked():
            selectedDays.append("Wednesday")
        if self.thursdayCheckBox.isChecked():
            selectedDays.append("Thursday")
        if self.fridayCheckBox.isChecked():
            selectedDays.append("Friday")
        if self.saturdayCheckBox.isChecked():
            selectedDays.append("Saturday")
        if self.sundayCheckBox.isChecked():
            selectedDays.append("Sunday")

        settings = {
            "meals": selectedMeals,
            "days": selectedDays
        }

        self.done(QDialog.DialogCode.Accepted)
        QMessageBox.information(self, "Success", "Settings saved.")
        save_settings(settings)
        

        

       


