import os
import random
import sys

from PyQt5 import QtCore, QtGui, QtNetwork, QtWidgets

import res_rc
from dialog import Ui_Dialog
from helper import *
from home import Ui_Home
from plotter import *

config['pi'] = 'alex@pi'

pi = config['pi']
arduino = config['arduino']


def SetNewIcon():
    i = QtGui.QIcon()
    i.addPixmap(QtGui.QPixmap(':/main/icons/alert round.png'))
    home.btnLEDOff.setIcon(i)


def LED(cmd):
    """
    Control LED lights
    """
    res=Ssh(pi, '%s %s' % (arduino, cmd))
    config['led_state'] = cmd
    log = Log('fucking')
    log.Console('gugdsg')


def Plot():
    """
    Plot something
    """
    fig = plt.figure(FigureClass=MyFigure)
    #fig.suptitle('Main window title')
    ax = fig.subplots(1, 1)
    ax.set_title('X vs Y')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    plot_histograms(ax, data)


if __name__ == '__main__':
    # Setup main window
    Qapp = QtWidgets.QApplication(sys.argv)
    Qhome = QtWidgets.QMainWindow()
    home = Ui_Home()
    home.setupUi(Qhome)

    Qdialog = QtWidgets.QDialog()
    dialog = Ui_Dialog()
    dialog.setupUi(Qdialog)

    # Widget stuff
    home.btnLEDOn.clicked.connect(lambda: LED('on'))
    home.btnLEDOff.clicked.connect(lambda: LED('off'))
    home.actionQuit.triggered.connect(Qapp.exit)
    home.actionAbout.triggered.connect(Qdialog.show)
    home.actionOpen.triggered.connect(SetNewIcon)
    home.actionSave.triggered.connect(Plot)

    # Load main window
    Qhome.setWindowTitle('Learning some Qt')
    Qhome.show()
    Qapp.exec_()
    config.save(sort_keys=False)
