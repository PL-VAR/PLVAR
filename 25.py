from PyQt5 import QtCore , QtGui , QtWidgets
from PyQt5.QtGui import QPixmap , QIcon
#################################################################
from PyQt5 import *
#################################################################
import sys

########
app = QtWidgets.QApplication(sys.argv)      # creating application
window = QtWidgets.QWidget()                # creating our window
#window.resize(400,500)                      # resize window size as we like
#window.move(600,100)                        # move window to the postion that we need
########


########
window.setGeometry(600,100 , 400,500)       # Geometry (x,y , width,hight)
window.setWindowTitle("PL-VAR")             # set the name of the window
########


########################## Tabs ###########################
label = QtWidgets.QLabel('<b>Fonts</b>',window)
label.move(10,20)

def Fonts():
    font = QtWidgets.QFontDialog.getFont()

button = QtWidgets.QPushButton('Select Font',window)
label.move(8,20)
button.clicked.connect(Fonts)
###########################################################

window.show()                               # showing our window
app.exec_()                                 # to still apperance