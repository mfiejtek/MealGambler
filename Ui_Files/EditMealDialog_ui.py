# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EditMealDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QFormLayout, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPlainTextEdit, QSizePolicy,
    QSpinBox, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.nameLabel = QLabel(Dialog)
        self.nameLabel.setObjectName(u"nameLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.nameLabel)

        self.nameLineEdit = QLineEdit(Dialog)
        self.nameLineEdit.setObjectName(u"nameLineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.nameLineEdit)

        self.categoryLabel = QLabel(Dialog)
        self.categoryLabel.setObjectName(u"categoryLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.categoryLabel)

        self.categoryComboBox = QComboBox(Dialog)
        self.categoryComboBox.addItem("")
        self.categoryComboBox.addItem("")
        self.categoryComboBox.addItem("")
        self.categoryComboBox.addItem("")
        self.categoryComboBox.addItem("")
        self.categoryComboBox.setObjectName(u"categoryComboBox")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.categoryComboBox)

        self.caloriesLabel = QLabel(Dialog)
        self.caloriesLabel.setObjectName(u"caloriesLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.caloriesLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.caloriesSpinBox = QSpinBox(Dialog)
        self.caloriesSpinBox.setObjectName(u"caloriesSpinBox")

        self.horizontalLayout.addWidget(self.caloriesSpinBox)

        self.kcalLabel = QLabel(Dialog)
        self.kcalLabel.setObjectName(u"kcalLabel")

        self.horizontalLayout.addWidget(self.kcalLabel)


        self.formLayout.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout)

        self.ingredientsLabel = QLabel(Dialog)
        self.ingredientsLabel.setObjectName(u"ingredientsLabel")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.ingredientsLabel)

        self.ingredientsPlainTextEdit = QPlainTextEdit(Dialog)
        self.ingredientsPlainTextEdit.setObjectName(u"ingredientsPlainTextEdit")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.ingredientsPlainTextEdit)


        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.nameLabel.setText(QCoreApplication.translate("Dialog", u"Name", None))
        self.categoryLabel.setText(QCoreApplication.translate("Dialog", u"Category", None))
        self.categoryComboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Other", None))
        self.categoryComboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Breakfast", None))
        self.categoryComboBox.setItemText(2, QCoreApplication.translate("Dialog", u"Dinner", None))
        self.categoryComboBox.setItemText(3, QCoreApplication.translate("Dialog", u"Supper", None))
        self.categoryComboBox.setItemText(4, QCoreApplication.translate("Dialog", u"Snack", None))

        self.caloriesLabel.setText(QCoreApplication.translate("Dialog", u"Calories", None))
        self.kcalLabel.setText(QCoreApplication.translate("Dialog", u"kcal", None))
        self.ingredientsLabel.setText(QCoreApplication.translate("Dialog", u"Ingredients", None))
    # retranslateUi

