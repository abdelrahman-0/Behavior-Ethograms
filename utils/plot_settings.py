import numpy as np
import utils.button_event_functions as EVENTS
import pandas as pd
import random
import datetime as dt
import matplotlib
matplotlib.use("Qt5Agg")
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from PyQt5 import QtCore, QtWidgets, QtGui
from utils.warning_functions import DuplicateItemWarning

DEFAULT_CMAP = plt.get_cmap('tab10')

class SubjectsDialog():
    def setupUi(self, Dialog: QtWidgets.QDialog, dataframe):
        Dialog.setObjectName("Dialog")
        Dialog.setModal(True)
        Dialog.resize(250, 270)

        self.label_subjects = QtWidgets.QLabel(Dialog)
        self.label_subjects.setGeometry(QtCore.QRect(30, 10, 200, 16))
        self.label_subjects.setObjectName("label_subjects")

        # Add dynamic checkmarks
        subjects = np.unique(dataframe['Subject'])
        self.checkboxes = []
        self.table = QtWidgets.QTableWidget(len(subjects), 1, Dialog)
        self.table.setFixedSize(200,200)
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setVisible(False)
        self.table.move(self.label_subjects.x(), 35)
        for row, subject in enumerate(subjects):
            qwidget = QtWidgets.QWidget()
            checkbox = QtWidgets.QCheckBox(subject)
            checkbox.setChecked(True)
            qhboxlayout = QtWidgets.QHBoxLayout(qwidget)
            qhboxlayout.addWidget(checkbox)
            qhboxlayout.setContentsMargins(0, 0, 0, 0)
            self.table.setCellWidget(row, 0, qwidget)
            self.table.setItem(row, 1, QtWidgets.QTableWidgetItem(''))
            self.checkboxes += [checkbox]
        self.table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(self.table.x()+127, self.table.y()+200, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda : EVENTS.openBehaviorGroupsDialog(Dialog, dataframe, self.checkboxes))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Behavior-Ethograms Plotter"))
        self.pushButton.setText(_translate("Dialog", "Next"))
        self.label_subjects.setText(_translate("Dialog", "Choose subjects to include in the plot:"))


class BehaviorGroupsDialog():
    def setupUi(self, Dialog, dialogOld, dataframe, selected_subjects):
        Dialog.setObjectName("Dialog")
        Dialog.resize(414, 351)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 10, 321, 61))
        self.label.setScaledContents(False)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(250, 80, 41, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 110, 41, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(190, 280, 21, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(220, 280, 21, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(330, 320, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(250, 320, 75, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(30, 80, 211, 191))
        self.listWidget.setObjectName("listWidget")
        for behavior in np.unique(dataframe['Behavior']):
            self.listWidget.addItem(behavior)
        self.updateButtonsStatus()
        self.connectButtons(dialogOld, Dialog, dataframe, selected_subjects)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Behavior-Group Settings"))
        self.label.setText(_translate("Dialog", "Set behavior-groups: Different behaviors can be grouped under one behavior-group in the final ethogram. Single behaviors need to be in a group of their own. The order of the groups in the final ethogram can be controlled by the \'Up\' and \'Down\' keys."))
        self.pushButton.setText(_translate("Dialog", "Up"))
        self.pushButton_2.setText(_translate("Dialog", "Down"))
        self.pushButton_3.setText(_translate("Dialog", "+"))
        self.pushButton_4.setText(_translate("Dialog", "-"))
        self.pushButton_5.setText(_translate("Dialog", "Next"))
        self.pushButton_6.setText(_translate("Dialog", "Back"))

    def updateButtonsStatus(self):
        self.pushButton.setDisabled(self.listWidget.count() == 0 or self.listWidget.currentRow() == 0)
        self.pushButton_2.setDisabled(self.listWidget.count() == 0 or self.listWidget.currentRow() == self.listWidget.count() - 1)
        self.pushButton_4.setDisabled(self.listWidget.count() == 0)

    def connectButtons(self, dialogOld, Dialog, dataframe, selected_subjects):
        self.listWidget.itemSelectionChanged.connect(self.updateButtonsStatus)
        self.pushButton.clicked.connect(lambda : EVENTS.upButton(self.listWidget))
        self.pushButton_2.clicked.connect(lambda : EVENTS.downButton(self.listWidget))
        self.pushButton_3.clicked.connect(lambda : EVENTS.addButton(self.listWidget))
        self.pushButton_4.clicked.connect(lambda : EVENTS.removeButton(self.listWidget))
        self.pushButton_5.clicked.connect(lambda : EVENTS.openBehaviorsDialog(Dialog, self.listWidget, dataframe, selected_subjects))
        self.pushButton_6.clicked.connect(lambda : EVENTS.closeBehaviorGroupsDialog(dialogOld, Dialog))

class AddGroupDialog():
    def setupUi(self, Dialog, listWidget: QtWidgets.QListWidget):
        Dialog.setObjectName("Dialog")
        Dialog.resize(322, 51)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(240, 10, 75, 31))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 221, 31))
        self.textEdit.setObjectName("textEdit")
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textEdit.setFont(font)
        self.connectButtons(Dialog, listWidget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Add Behavior-Group"))
        self.pushButton.setText(_translate("Dialog", "Add Group"))

    def connectButtons(self, Dialog: QtWidgets.QDialog, listWidget: QtWidgets.QListWidget):
        self.pushButton.clicked.connect(lambda : self.addGroupEvent(Dialog, listWidget))

    def addGroupEvent(self, Dialog, listWidget):
        itemList =  [str(listWidget.item(i).text()) for i in range(listWidget.count())]
        text = self.textEdit.toPlainText()
        if text in itemList:
            DuplicateItemWarning()
        else:
            listWidget.addItem(text)
            Dialog.close()

class BehaviorsDialog():
    def setupUi(self, Dialog: QtWidgets.QDialog, oldDialog: QtWidgets.QDialog, dataframe: pd.DataFrame, selected_subjects: list, behaviorGroupsList: list):
        Dialog.setObjectName("Dialog")
        Dialog.resize(581, 335)

        #### TODO
        # Dialog.setModal(False)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 20, 421, 21))
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_color = QtWidgets.QLabel(Dialog)
        self.label_color.setGeometry(QtCore.QRect(360, 70, 31, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_color.setFont(font)
        self.label_color.setObjectName("label_color")
        self.label_behaviorGroup = QtWidgets.QLabel(Dialog)
        self.label_behaviorGroup.setGeometry(QtCore.QRect(200, 70, 91, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_behaviorGroup.setFont(font)
        self.label_behaviorGroup.setAutoFillBackground(False)
        self.label_behaviorGroup.setObjectName("label_behaviorGroup")
        self.label_behavior = QtWidgets.QLabel(Dialog)
        self.label_behavior.setGeometry(QtCore.QRect(70, 70, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_behavior.setFont(font)
        self.label_behavior.setObjectName("label_behavior")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(450, 300, 121, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 270, 121, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(450, 240, 121, 21))
        self.pushButton_3.setObjectName("pushButton_3")


        behaviors = sorted(np.unique(dataframe['Behavior']))
        self.behavior_dicts = []
        for i, behavior in enumerate(behaviors):
            behavior_dict = {}
            y_val = self.label_behavior.y() + 25 + i * 25

            hashtagSign = QtWidgets.QLabel(Dialog)
            hashtagSign.setText('#')
            hashtagSign.move(self.label_color.x() - 13, y_val + 1)

            behaviorGroupComboBox = QtWidgets.QComboBox(Dialog)
            behaviorGroupComboBox.move(self.label_behaviorGroup.x(), y_val)
            for group in behaviorGroupsList:
                behaviorGroupComboBox.addItem(group)
            if behavior in behaviorGroupsList:
                behaviorGroupComboBox.setCurrentIndex(behaviorGroupsList.index(behavior))
            else:
                default = list(set(behaviorGroupsList) - set([behavior]))[0]
                behaviorGroupComboBox.setCurrentIndex(behaviorGroupsList.index(default))
            behavior_dict['behavior_group'] = behaviorGroupComboBox

            colorTextEdit = QtWidgets.QLineEdit(Dialog)
            colorTextEdit.move(self.label_color.x() , y_val)
            colorTextEdit.setMaximumWidth(55)
            colorTextEdit.setText('%02x%02x%02x' % tuple((np.array(DEFAULT_CMAP(i/(len(behaviors)-1))[:3]) * 255).astype(int)))
            behavior_dict['color'] = colorTextEdit

            checkbox = QtWidgets.QCheckBox(Dialog)
            checkbox.setText(behavior)
            checkbox.setChecked(True)
            checkbox.move(self.label_behavior.x(), y_val)
            behavior_dict['behavior_checkbox'] = checkbox

            self.behavior_dicts += [behavior_dict]

        self.connectButtons(dataframe, selected_subjects, behaviorGroupsList)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Match behaviors to behavior-groups"))
        self.label.setText(_translate("Dialog", "Select behaviors to be included in the final ethogram and match them with their group:"))
        self.label_color.setText(_translate("Dialog", "Color"))
        self.label_behaviorGroup.setText(_translate("Dialog", "Behavior-Group"))
        self.label_behavior.setText(_translate("Dialog", "Behavior"))
        self.pushButton.setText(_translate("Dialog", "Plot"))
        self.pushButton_2.setText(_translate("Dialog", "Additional settings"))
        self.pushButton_3.setText(_translate("Dialog", "Back"))

    def connectButtons(self, dataframe: pd.DataFrame, selected_subjects: list, behaviorGroupsList: list):
        self.pushButton.clicked.connect(lambda : self.plotEthogram(dataframe, selected_subjects, behaviorGroupsList))

    def plotEthogram(self, dataframe: pd.DataFrame, selected_subjects: list, behaviorGroupsList: list):
        init = dt.datetime(2017, 1, 1)
        selected_behaviors = {}
        for behavior_dict in self.behavior_dicts:
            if behavior_dict['behavior_checkbox'].isChecked():
                options_dict = {}
                options_dict['color'] = behavior_dict['color'].text()
                options_dict['group'] = behavior_dict['behavior_group'].currentText()
                selected_behaviors[behavior_dict['behavior_checkbox'].text()] = options_dict
        dataframe = dataframe[dataframe['Behavior'].apply(lambda x : x in selected_behaviors.keys())]
        column_indices = {}
        for idx, col in enumerate(dataframe.columns):
            column_indices[col] = idx
        fig, axs = plt.subplots(figsize=(20, len(selected_subjects) * 8), nrows=len(selected_subjects), ncols=1, sharex=True)
        if len(selected_subjects) == 1:
            axs = [axs]
        for subject_idx, subject in enumerate(selected_subjects):
            subject_df = dataframe[dataframe['Subject'] == subject]
            for behavior, options_dict in selected_behaviors.items():
                subject_behavior_df = subject_df[subject_df['Behavior'] == behavior]
                for row in subject_behavior_df.iterrows():
                    start = matplotlib.dates.date2num(init + dt.timedelta(seconds=row[1]['Start (s)']))
                    end = matplotlib.dates.date2num(init + dt.timedelta(seconds=row[1]['Stop (s)']))
                    axs[subject_idx].barh(behaviorGroupsList.index(options_dict['group']) + 1, end - start, left=start, height=0.5, align="center", edgecolor='#'+options_dict['color'], color='#'+options_dict['color'], alpha=1)
            axs[subject_idx].grid(color="g", linestyle=":")
            axs[subject_idx].set_yticks(np.arange(1, len(behaviorGroupsList) + 1))
            axs[subject_idx].set_yticklabels(behaviorGroupsList, fontdict={"fontsize": 10})
            axs[subject_idx].xaxis_date()
            axs[subject_idx].xaxis.set_major_formatter(DateFormatter("%H:%M:%S"))
            axs[subject_idx].set_xlabel("Time (HH:MM:SS)", fontdict={"fontsize": 12})
            axs[subject_idx].invert_yaxis()

        fig.autofmt_xdate()
        plt.tight_layout()
        plt.show()