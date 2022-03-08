import os
import pandas as pd
from PyQt5 import QtWidgets
from utils.plot_settings import AddGroupDialog, SubjectsDialog, BehaviorGroupsDialog, BehaviorsDialog
from utils.warning_functions import InvalidPathWarning, InvalidCSVFileWarning, ZeroSubjectsWarning, ZeroBehaviorGroupsWarning

def plot_function(textEdit: QtWidgets.QTextEdit):
    path = textEdit.toPlainText().strip()
    if os.path.splitext(path)[-1] == '.csv' and os.path.exists(path):
        valid_csv, dataframe = checkCSV(path)
        if valid_csv:
            openSubjectsDialog(dataframe)
        else:
            InvalidCSVFileWarning()
    else:
        InvalidPathWarning()

def openSubjectsDialog(dataframe):
    Dialog = QtWidgets.QDialog()
    ui = SubjectsDialog()
    ui.setupUi(Dialog, dataframe)
    Dialog.exec_()

def checkCSV(path: str):
    valid_csv = False
    try:
        df = pd.read_csv(path, index_col=False)
    except Exception as e:
        print('_' * 20)
        print('The following error occured while reading the csv file:')
        print(e)
        print('_' * 20)
        return valid_csv, None
    if set(['Start (s)', 'Stop (s)', 'Subject', 'Behavior']) <= set(df.columns) and df.shape[0] >= 1:
        valid_csv = True
    return valid_csv, df


def getOpenFilesAndDirs(textEdit: QtWidgets.QTextEdit, parent=None, caption='', directory='', 
                        filter='', initialFilter='', options=None):
    def updateText():
        selected = []
        for index in view.selectionModel().selectedRows():
            selected.append('"{}"'.format(index.data()))
        lineEdit.setText(' '.join(selected))
    dialog = QtWidgets.QFileDialog(parent, windowTitle=caption)
    dialog.setFileMode(dialog.ExistingFiles)
    if options:
        dialog.setOptions(options)
    dialog.setOption(dialog.DontUseNativeDialog, True)
    if directory:
        dialog.setDirectory(directory)
    if filter:
        dialog.setNameFilter(filter)
        if initialFilter:
            dialog.selectNameFilter(initialFilter)
    dialog.accept = lambda: QtWidgets.QDialog.accept(dialog)
    stackedWidget = dialog.findChild(QtWidgets.QStackedWidget)
    view = stackedWidget.findChild(QtWidgets.QListView)
    view.selectionModel().selectionChanged.connect(updateText)
    lineEdit = dialog.findChild(QtWidgets.QLineEdit)
    dialog.directoryEntered.connect(lambda: lineEdit.setText(''))
    dialog.exec_()
    selected_files = dialog.selectedFiles()
    if len(selected_files) == 0:
        return
    if len(selected_files) > 1:
        print('Multiple files selected. Will only consider the first one.')
    file = dialog.selectedFiles()[0]
    textEdit.setText(file)

def openBehaviorGroupsDialog(dialogOld: QtWidgets.QDialog, dataframe: pd.DataFrame, checkboxes: list[QtWidgets.QCheckBox]):
    selected_subjects = []
    for checkbox in checkboxes:
        if checkbox.isChecked():
            selected_subjects += [checkbox.text()]
    if len(selected_subjects) > 0:
        dialogOld.hide()
        Dialog = QtWidgets.QDialog()
        ui = BehaviorGroupsDialog()
        ui.setupUi(Dialog, dialogOld, dataframe[dataframe['Subject'].apply(lambda x : x in selected_subjects)], selected_subjects)
        Dialog.exec_()
    else:
        ZeroSubjectsWarning()

def closeBehaviorGroupsDialog(dialogOld: QtWidgets.QDialog, Dialog: QtWidgets.QDialog):
    dialogOld.show()
    Dialog.close()

def openBehaviorsDialog(Dialog: QtWidgets.QDialog, listWidget: QtWidgets.QListWidget, dataframe: pd.DataFrame, selected_subjects: list):
    behaviorGroupsList =  [str(listWidget.item(i).text()) for i in range(listWidget.count())]
    if behaviorGroupsList:
        Dialog.hide()
        newDialog = QtWidgets.QDialog()
        ui = BehaviorsDialog()
        ui.setupUi(newDialog, Dialog, dataframe, selected_subjects, behaviorGroupsList)
        newDialog.exec_()
    else:
        ZeroBehaviorGroupsWarning()

def closeBehaviorsDialog(dialogOld: QtWidgets.QDialog, Dialog: QtWidgets.QDialog):
    dialogOld.show()
    Dialog.close()

def upButton(listWidget: QtWidgets.QListWidget):
    currentIndex = listWidget.currentRow()
    currentItem = listWidget.takeItem(currentIndex)
    listWidget.insertItem(currentIndex - 1, currentItem)
    listWidget.setCurrentRow(currentIndex - 1)

def downButton(listWidget: QtWidgets.QListWidget):
    currentIndex = listWidget.currentRow()
    currentItem = listWidget.takeItem(currentIndex)
    listWidget.insertItem(currentIndex + 1, currentItem)
    listWidget.setCurrentRow(currentIndex + 1)

def addButton(listWidget: QtWidgets.QListWidget):
    Dialog = QtWidgets.QDialog()
    ui = AddGroupDialog()
    ui.setupUi(Dialog, listWidget)
    Dialog.exec_()

def removeButton(listWidget: QtWidgets.QListWidget):
    currentIndex = listWidget.currentRow()
    listWidget.takeItem(currentIndex)