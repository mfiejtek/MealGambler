# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EditMealsDialog.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDialog,
    QFormLayout, QGridLayout, QHBoxLayout, QLabel,
    QListView, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(446, 300)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.categoryLabel = QLabel(Dialog)
        self.categoryLabel.setObjectName(u"categoryLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.categoryLabel)

        self.categoryComboBox = QComboBox(Dialog)
        self.categoryComboBox.addItem("")
        self.categoryComboBox.addItem("")
        self.categoryComboBox.addItem("")
        self.categoryComboBox.addItem("")
        self.categoryComboBox.addItem("")
        self.categoryComboBox.addItem("")
        self.categoryComboBox.setObjectName(u"categoryComboBox")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.categoryComboBox)


        self.horizontalLayout_2.addLayout(self.formLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.listView = QListView(Dialog)
        self.listView.setObjectName(u"listView")
        self.listView.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.horizontalLayout.addWidget(self.listView)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.editButton = QPushButton(Dialog)
        self.editButton.setObjectName(u"editButton")
        self.editButton.setAutoDefault(False)

        self.verticalLayout.addWidget(self.editButton)

        self.addButton = QPushButton(Dialog)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setAutoDefault(False)

        self.verticalLayout.addWidget(self.addButton)

        self.deleteButton = QPushButton(Dialog)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setAutoDefault(False)

        self.verticalLayout.addWidget(self.deleteButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.closeButton = QPushButton(Dialog)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setAutoDefault(False)

        self.verticalLayout.addWidget(self.closeButton)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        QWidget.setTabOrder(self.editButton, self.addButton)
        QWidget.setTabOrder(self.addButton, self.deleteButton)
        QWidget.setTabOrder(self.deleteButton, self.closeButton)
        QWidget.setTabOrder(self.closeButton, self.listView)

        self.retranslateUi(Dialog)
        self.closeButton.clicked.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.categoryLabel.setText(QCoreApplication.translate("Dialog", u"Category", None))
        self.categoryComboBox.setItemText(0, QCoreApplication.translate("Dialog", u"All", None))
        self.categoryComboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Breakfast", None))
        self.categoryComboBox.setItemText(2, QCoreApplication.translate("Dialog", u"Dinner", None))
        self.categoryComboBox.setItemText(3, QCoreApplication.translate("Dialog", u"Supper", None))
        self.categoryComboBox.setItemText(4, QCoreApplication.translate("Dialog", u"Snack", None))
        self.categoryComboBox.setItemText(5, QCoreApplication.translate("Dialog", u"Other", None))

        self.editButton.setText(QCoreApplication.translate("Dialog", u"&Edit", None))
        self.addButton.setText(QCoreApplication.translate("Dialog", u"&Add", None))
        self.deleteButton.setText(QCoreApplication.translate("Dialog", u"&Delete", None))
        self.closeButton.setText(QCoreApplication.translate("Dialog", u"&Close", None))
    # retranslateUi

