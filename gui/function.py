# -*- coding: utf-8 -*-
"""
@author: msh, yk
"""

from logging import getLogger

from PyQt5 import QtWidgets, QtGui


class Files:
    def __init__(self, frame, logger=None):
        self.frame = frame
        self.logger = logger or getLogger("dummy")

    def get_files(self, file_type=None):

        if file_type is not None:
            ftype = file_type
        else:
            ftype = "fits, fit, fts (*.fits *.fit *.fts)"

        files = QtWidgets.QFileDialog.getOpenFileNames(self.frame, "Images...", '', (ftype),
                                                       None, QtWidgets.QFileDialog.DontUseNativeDialog)
        return files[0]

    def get_file(self, file_type=None):

        if file_type is not None:
            ftype = file_type
        else:
            ftype = "fits, fit, fts (*.fits *.fit *.fts)"

        file = QtWidgets.QFileDialog.getOpenFileName(self.frame, "File...", "", (ftype),
                                                     None, QtWidgets.QFileDialog.DontUseNativeDialog)

        return file[0]

    def save_file(self, file_type=None, name=None):
        if file_type is None:
            tp = "fits (*.fits)"
        else:
            tp = file_type

        if name is None:
            nm = ""
        else:
            nm = name

        file = QtWidgets.QFileDialog.getSaveFileName(self.frame, "Output file", nm, (tp),
                                                     None, QtWidgets.QFileDialog.DontUseNativeDialog)

        return file[0]

    def save_directory(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(self.frame, 'Select directory',
                                                               None, QtWidgets.QFileDialog.DontUseNativeDialog)
        return directory


class Devices:
    def __init__(self, frame, logger=None):
        self.frame = frame
        self.logger = logger or getLogger("dummy")

    def list_of_selected(self, flist):
        ret = []
        for x in flist.selectedItems():
            ret.append(x.text())
        return ret

    def c_replace_list_con(self, fcomb, lst):
        self.rm_all(fcomb)
        self.c_add(fcomb, lst)

    def replace_list_con(self, flist, lst):
        self.rm_all(flist)
        self.add(flist, lst)

    def rm_all(self, flist):
        flist.clear()

    def add(self, flist, the_list):
        it = flist.count() - 1
        for x in the_list:
            it = it + 1
            item = QtWidgets.QListWidgetItem()
            flist.addItem(item)
            item = flist.item(it)
            item.setText(QtWidgets.QApplication.translate("Form", x, None))

    def clear_table(self, device):
        for i in reversed(range(device.rowCount())):
            device.removeRow(i)

    def add_table(self, device, list):
        for line in list:
            rowPosition = device.rowCount()
            device.insertRow(rowPosition)
            for it, value in enumerate(line):
                device.setItem(rowPosition, it, QtWidgets.QTableWidgetItem(str(value)))
                # device.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(str(line[1])))

    def list_of_table(self, device):
        number_of_rows = device.rowCount()
        number_of_columns = device.columnCount()
        ret = []
        if number_of_rows > 0 and number_of_columns > 0:
            for i in range(number_of_rows):
                row = []
                for j in range(number_of_columns):
                    row.append(device.item(i, j).text())

                ret.append(row)

            return ret

    def list_of_selected_table(self, device):
        rows = []
        for row in device.selectionModel().selectedRows():
            rows.append(row.row())

        return rows

    def remove_from_table(self, device):
        unwanted_rows = self.list_of_selected_table(device)

        for unwanted_row in sorted(unwanted_rows, reverse=True):
            device.removeRow(unwanted_row)

    def colorify_table(self, device):
        number_of_rows = device.rowCount()
        number_of_columns = device.columnCount()
        if number_of_rows > 0 and number_of_columns > 0:
            for i in range(number_of_rows):
                vd = float(device.item(i, 6).text())
                for j in range(number_of_columns):
                    if vd < 70:
                        device.item(i, j).setBackground(QtGui.QColor('red'))
                        device.item(i, j).setForeground(QtGui.QColor('white'))
                    elif vd < 80:
                        device.item(i, j).setBackground(QtGui.QColor('yellow'))
                        device.item(i, j).setForeground(QtGui.QColor('black'))
                    else:
                        device.item(i, j).setBackground(QtGui.QColor('green'))
                        device.item(i, j).setForeground(QtGui.QColor('white'))



    def replace_table(self, device, list):
        self.clear_table(device)
        self.add_table(device, list)

    def c_add(self, fcomb, the_list):
        for i in the_list:
            fcomb.addItem(str(i))

    def rm(self, flist):
        for x in flist.selectedItems():
            flist.takeItem(flist.row(x))

    def list_of_list(self, flist):
        ret = []
        for x in range(flist.count()):
            ret.append(flist.item(x).text())

        return ret

    def c_list_pf_list(self, fcomb):
        return [fcomb.itemText(i) for i in range(fcomb.count())]

    def ask(self, question):
        answ = QtWidgets.QMessageBox.question(self.frame, "MYRaf", question,
                                              QtWidgets.QMessageBox.Yes |
                                              QtWidgets.QMessageBox.No,
                                              QtWidgets.QMessageBox.No)

        return answ == QtWidgets.QMessageBox.Yes

    def ask_calcel(self, question):
        answ = QtWidgets.QMessageBox.question(self.frame, "MYRaf", question,
                                              QtWidgets.QMessageBox.Yes |
                                              QtWidgets.QMessageBox.No |
                                              QtWidgets.QMessageBox.Cancel,
                                              QtWidgets.QMessageBox.Cancel)
        if answ == QtWidgets.QMessageBox.Yes:
            return "yes"
        elif answ == QtWidgets.QMessageBox.No:
            return "no"

        return "cancel"
