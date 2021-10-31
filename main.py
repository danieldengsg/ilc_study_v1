# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import sys

from PyQt5 import QtWidgets, QtCore
from ui_figure import Ui_MainWindow
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import numpy as np
import scipy.signal as sg


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


class mymplcanvas(FigureCanvas):
    def __init__(self, parent=None, row=1, col=1, width=50, height=50, dpi=100):
        self.fig, self.axes = plt.subplots(row, col)

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        # NavigationToolbar(FigureCanvas, parent)


class mainwindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(mainwindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButtonOK.clicked.connect(self.btn_ok)
        self.pushButtonClose.clicked.connect(self.btn_close)

    def btn_ok(self):
        qwidget = QtWidgets.QWidget()
        mycanvas = mymplcanvas(qwidget, 1, 1)
        self.verticalLayout.addWidget(qwidget)
        x = np.linspace(0, 100, 100)
        y = np.sin(x * 2 * np.pi)
        mycanvas.axes.plot(x, y)
        mycanvas.axes.grid()
        qwidget2 = QtWidgets.QWidget()
        toolbar = NavigationToolbar(mycanvas, qwidget2)
        self.verticalLayout.addWidget(qwidget2)

    def btn_close(self):
        self.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = mainwindow()
    main_window.show()
    sys.exit(app.exec_())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
