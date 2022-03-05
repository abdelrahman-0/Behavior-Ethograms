from PyQt5.QtWidgets import QMessageBox

def InvalidCSVFileWarning():
    msg = QMessageBox()
    msg.setWindowTitle("Invalid CSV File")
    msg.setText('CSV file not in the correct format.')
    msg.setInformativeText('File needs to have at least 1 row and contain the following columns:\n\'Subject\'\n\'Behavior\'\n\'Start (s)\'\n\'Stop (s)\'')
    msg.exec_()

def InvalidPathWarning():
    msg = QMessageBox()
    msg.setWindowTitle("Invalid Path Error")
    msg.setText('Please make sure to pass a valid .csv file in the required format.\n')
    msg.exec_()

def ZeroSubjectsWarning():
    msg = QMessageBox()
    msg.setWindowTitle("Zero Subjects Warning")
    msg.setText('Please select at least one subject.\n')
    msg.exec_()

def ZeroBehaviorGroupsWarning():
    msg = QMessageBox()
    msg.setWindowTitle("Zero Behavior-Groups Warning")
    msg.setText('Please add at least one behavior-group.\n')
    msg.exec_()

def DuplicateItemWarning():
    msg = QMessageBox()
    msg.setWindowTitle("Duplicate Group Warning")
    msg.setText('Behavior-Group already in list.\n')
    msg.exec_()