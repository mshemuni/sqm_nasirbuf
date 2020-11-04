# -*- coding: utf-8 -*-
"""
@author: msniaei
"""

try:
    from sys import argv
    from os.path import isfile

    from PyQt5 import QtWidgets
    from PyQt5 import QtCore
    from PyQt5.QtGui import QPixmap, QPen, QColor, QBrush
    from PyQt5.QtWidgets import QGraphicsScene

    from json import dump, loads

    from gui import ds
    from gui import function
    from logging import getLogger, basicConfig

    import argparse

    import numpy as np

    from sqm import data
except Exception as e:
    print(e)
    exit(0)


class MainWindow(QtWidgets.QMainWindow, ds.Ui_MainWindow):
    def __init__(self, parent=None, logger_level=40, log_file=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.flags = QtCore.Qt.Window
        self.setWindowFlags(self.flags)

        self.fFile = function.Files(self)
        self.fDevice = function.Devices(self)

        self.log_file = log_file

        self.tabWidget.setTabEnabled(0, False)
        self.tabWidget.setTabEnabled(1, False)

        LOG_FORMAT = "[%(asctime)s, %(levelname)s], [%(filename)s, %(funcName)s, %(lineno)s]: %(message)s"
        basicConfig(filename=self.log_file, level=logger_level, format=LOG_FORMAT)
        self.my_logger = getLogger()

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.live_view)
        self.tabWidget.currentChanged.connect(self.timer_starter)
        self.interval.valueChanged.connect(self.timer_starter)

        self.connect2dev.clicked.connect(lambda: self.connect_me())
        self.read.clicked.connect(lambda: self.read_stat())
        self.remove_record.clicked.connect(lambda: self.del_record())
        self.export_records.clicked.connect(lambda: self.export())

        header = self.records.horizontalHeader()
        for i in range(6):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(7, QtWidgets.QHeaderView.Stretch)

        self.dh = None
        self.update_log()

    def export(self):
        data = self.fDevice.list_of_table(self.records)
        if data is not None:
            file = self.fFile.save_file("CVS (*.cvs)")
            with open(file, "w") as f2w:
                f2w.write("#JD,Raw Mag, New Mag, Temperature, Flux, Valid Data, Comment\n")
                for line in data:
                    f2w.write(f"{','.join(line)}\n")
        else:
            QtWidgets.QMessageBox.warning(self, "DAG SQM Warning", "Nothing to export")

    def del_record(self):
        self.fDevice.remove_from_table(self.records)

    def read_stat(self):

        nos = self.sample_number.value()
        jd = mag_r = temperature = mag_n = flux = 0
        vd = 0
        comm = self.comment.text()
        canceled = False

        progress = QtWidgets.QProgressDialog("Reading...", "Abort", 0, nos, self)
        progress.setWindowModality(QtCore.Qt.WindowModal)
        progress.setWindowTitle('DAG SQM: Please Wait')
        progress.setAutoClose(True)

        for _ in range(nos):
            try:
                the_data = self.dh.__read__()
                if the_data is not None:
                    progress.setLabelText("Reading")
                    if progress.wasCanceled():
                        progress.setLabelText("ABORT!")
                        canceled = True
                        break

                    # [jd, raw_mag, tempe, new_mag, flux]
                    jd += the_data[0]
                    mag_r += the_data[1]
                    temperature += the_data[2]
                    mag_n += the_data[3]
                    flux += the_data[4]
                    vd += 1
                    progress.setValue(vd)

            except Exception as e:
                self.my_logger.error(e)

        progress.close()
        if not canceled:
            self.fDevice.add_table(self.records,
                                   [map(str, [jd / vd, mag_r / vd, mag_n / vd,
                                              temperature / vd, flux, nos, 100 * vd / nos, comm])])

        self.fDevice.colorify_table(self.records)

    def update_log(self):
        if self.log_file is not None:
            with open(self.log_file, "r") as lfile:
                d = []
                for line in lfile:
                    d.append(line.strip())

                self.fDevice.replace_list_con(self.logs, d)
                self.logs.scrollToBottom()

    def timer_starter(self):
        tab = self.tabWidget.currentIndex()
        if tab == 0:
            self.timer.start(self.interval.value() * 1000)
        else:
            self.timer.stop()
            if tab == 2:
                self.update_log()

    def live_view(self):
        try:
            data = self.dh.__read__()
            self.temperature.display(data[2])
            self.brightness_raw.display(data[1])
            self.brightness_new.display(data[3])
            self.flux.display(data[4])
        except Exception as e:
            self.my_logger.error(e)

    def connect_me(self):
        if self.connect2dev.text() == "Connect":
            port = self.port.text()
            self.dh = data.Handle(port, logger=self.my_logger)
            self.dh.connect()
            if self.dh.con is not None:
                self.tabWidget.setTabEnabled(0, True)
                self.tabWidget.setTabEnabled(1, True)
                self.connect2dev.setText("Disconnect")
            else:
                QtWidgets.QMessageBox.critical(self, "DAG SQM Error", "Can't connect")
        else:
            self.dh.close()
            self.tabWidget.setTabEnabled(0, False)
            self.tabWidget.setTabEnabled(1, False)
            self.tabWidget.setVisible(2)
            self.connect2dev.setText("Connect")
            self.fDevice.clear_table(self.records)


def read_once(my_logger):
    dh = data.Handle("/dev/ttyUSB0", logger=my_logger)
    sample = dh.read()
    try:
        print(", ".join(list(map(str, list(map(float, sample))))))
    except Exception as e:
        my_logger.error(e)


def read_sample(my_logger, nos=50):
    dh = data.Handle("/dev/ttyUSB0", logger=my_logger)
    jd = mag_r = temperature = mag_n = flux = 0
    vd = 0
    dh.connect()
    for i in range(nos):
        the_data = dh.__read__()
        if the_data is not None:
            jd += the_data[0]
            mag_r += the_data[1]
            temperature += the_data[2]
            mag_n += the_data[3]
            flux += the_data[4]
            vd += 1
    try:
        lst = [jd / vd, mag_r / vd, temperature / vd, mag_n / vd, flux / vd, nos, 100 * vd / nos]
        print(", ".join(list(map(str, list(map(float, lst))))))
    except Exception as e:
        my_logger.error(e)


def main():
    parser = argparse.ArgumentParser(description='DAG SQM')
    parser.add_argument("-l", "--logger", default=40, type=int,
                        help="Logger level: CRITICAL=50, ERROR=40, WARNING=30, INFO=20, DEBUG=10, NOTSET=0")
    parser.add_argument("-f", "--logfile", default=None, type=str, help="Path to log file")
    parser.add_argument("-g", "--gui", default=False, help="Open GUI", action='store_true')
    parser.add_argument("-n", "--numberOfSamples", default=1, type=int, help="Number of samples")
    args = parser.parse_args()

    if args.gui:
        app = QtWidgets.QApplication(argv)
        window = MainWindow(logger_level=args.logger, log_file=args.logfile)
        window.show()
        app.exec()
    else:
        LOG_FORMAT = "[%(asctime)s, %(levelname)s], [%(filename)s, %(funcName)s, %(lineno)s]: %(message)s"
        basicConfig(filename=args.logfile, level=args.logger, format=LOG_FORMAT)
        my_logger = getLogger()

        if args.numberOfSamples == 1:
            read_once(my_logger)
        else:
            read_sample(my_logger, args.numberOfSamples)


if __name__ == "__main__":
    main()
