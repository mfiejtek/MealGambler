from PyQt6.QtWidgets import QDialog

from Ui_Files.Ui_SettingsDialog import Ui_Dialog

class SettingsDialog(QDialog, Ui_Dialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)