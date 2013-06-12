#!/usr/bin/env python

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore



class Icon(QtGui.QWidget):
    def __init__(self , parent=None):
	    QtGui.QWidget.__init__(self, parent)
		
	    color = QtGui.QColor(0,0,0)
		
	    self.setGeometry(300,300,250,180)
	    self.resize(300,180)
	    self.setWindowTitle('Color')
	    self.button = QtGui.QPushButton('colors',self)
	    self.button.setFocusPolicy(QtCore.Qt.NoFocus)
	    self.button.move(20,20)
	    self.connect(self.button,QtCore.SIGNAL('clicked()'),self.showDialog)
			self.setFocus
		
			self.widget = QtGui.QWidget(self)
		
			self.lable = QtGui.QLineEdit(self)
			self.lable.move(130,120)
			self.lable.resize(100,20)
			self.widget.setStyleSheet("QWidget {backround-color: black}")
			self.lable.setText(color.name())
			self.widget.setGeometry(130,22,100,100)
		
		def showDialog(self):
	    color = QtGui.QColorDialog.getColor()
		
	    self.widget.setStyleSheet("QWidget {background-color : %s}" % color.name())
	    self.lable.setText(color.name())
		
		
		

		
			

		
		
app = QtGui.QApplication(sys.argv)
icon = Icon()
icon.show()
sys.exit(app.exec_())
