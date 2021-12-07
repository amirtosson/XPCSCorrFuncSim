# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
import sys
if int(QtCore.qVersion()[0]) > 4:
    from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
else:
    from matplotlib.backends.backend_qt4agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure


class SiegMainWindow(QtWidgets.QMainWindow):
    main_canvas = FigureCanvas(Figure(figsize=(5, 3)))

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #TODO: Set tooltips
        uic.loadUi("siegmainwindow.ui", self)
        layout = QtWidgets.QVBoxLayout(self.widgetPlot)
        layout.addWidget(self.main_canvas)
        self.startButton.clicked.connect(self.calculate_cor_func)

    def calculate_cor_func(self):
        #beta, gamma, n, delta_t
        colors = ["red", "blue", "black", "green", "yellow"]
        g = []
        for x in range(self.n1spinBox.value()):
            j = math.exp(- self.gamma1SpinBox.value() * self.deltaT1SpinBox.value() * (x + 1))
            g.append(1 + (self.beta1SpinBox.value() * j))

        plt.plot(range(self.n1spinBox.value()), g, color=colors[0], label="data"+"_" + str(self.n1spinBox.value())+"_" + str(self.deltaT1SpinBox.value())+"_" + str(self.beta1SpinBox.value()))


        g = []
        for x in range(self.n2spinBox.value()):
            j = math.exp(- self.gamma2SpinBox.value() * self.deltaT2SpinBox.value() * (x + 1))
            g.append(1 + (self.beta2SpinBox.value() * j))
        plt.plot(range(self.n2spinBox.value()), g, color=colors[1],
                 label="data" + "_" + str(self.n2spinBox.value()) + "_" + str(
                     self.deltaT2SpinBox.value()) + "_" + str(self.beta2SpinBox.value()))


        g = []
        for x in range(self.n3spinBox.value()):
            j = math.exp(- self.gamma3SpinBox.value() * self.deltaT3SpinBox.value() * (x + 1))
            g.append(1 + (self.beta3SpinBox.value() * j))
        plt.plot(range(self.n3spinBox.value()), g, color=colors[2],
                 label="data" + "_" + str(self.n3spinBox.value()) + "_" + str(
                     self.deltaT3SpinBox.value()) + "_" + str(self.beta3SpinBox.value()))


        g = []
        for x in range(self.n4spinBox.value()):
            j = math.exp(- self.gamma4SpinBox.value() * self.deltaT4SpinBox.value() * (x + 1))
            g.append(1 + (self.beta4SpinBox.value() * j))
        plt.plot(range(self.n4spinBox.value()), g, color=colors[3],
                 label="data" + "_" + str(self.n4spinBox.value()) + "_" + str(
                     self.deltaT4SpinBox.value()) + "_" + str(self.beta4SpinBox.value()))
        g = []
        for x in range(self.n5spinBox.value()):
            j = math.exp(- self.gamma5SpinBox.value() * self.deltaT5SpinBox.value() * (x + 1))
            g.append(1 + (self.beta5SpinBox.value() * j))
        plt.plot(range(self.n5spinBox.value()), g, color=colors[4],
                 label="data" + "_" + str(self.n5spinBox.value()) + "_" + str(
                     self.deltaT5SpinBox.value()) + "_" + str(self.beta5SpinBox.value()))

        plt.ylim([0.9, 1.6])
        plt.legend()
        plt.xscale('log')
        plt.show()
"""
        g = []
        for i in range(5):
            g = []
            x = QtWidgets.QWidget()
            obj_name = "beta"+ 1 + "SpinBox"
            x.setObjectName(obj_name)
            print(x.value())
            self.beta1SpinBox.value()

"""


def main():
    app = QtWidgets.QApplication(sys.argv)
    mw = SiegMainWindow()
    mw.show()
    sys.exit(app.exec_())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

"""
    colors = ["red", "blue", "black", "green", "yellow"]

    for i in range(5):
        number_of_doses = 20 * (i+1)
        cor_func_vals = main(0.6, 0.1, number_of_doses, 0.9*(i+0.1))
        plt.plot(range(number_of_doses), cor_func_vals, color=colors[i], label="b"+str(i))
    plt.ylim([0.9, 1.6])
    plt.legend()
    plt.xscale('log')
    plt.show()
"""
