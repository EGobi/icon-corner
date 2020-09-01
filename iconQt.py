import sys, signal
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt

class Application(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowFlags(Qt.CustomizeWindowHint | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
		self.setGeometry(1366, 694, 253, 350)
		self.create_image()
        
	def create_image(self):
		label = QLabel(self)
		pixmap = QPixmap('/home/neko/Pictures/.Mãe de Deus.png').scaled(253, 350, Qt.KeepAspectRatio)
		label.setPixmap(pixmap)
		label.mousePressEvent = self.on_click
		self.show()
		self.pos = 1
        
	def on_click(self, event = None):
		if self.pos == 1:
			self.setGeometry(3033, 694, 253, 350)
			self.pos = 2
		elif self.pos == 2:
			self.setGeometry(0, 1082, 253, 350)
			self.pos = 3
		else:
			self.setGeometry(1366, 694, 253, 350)
			self.pos = 1

signal.signal(signal.SIGINT, signal.SIG_DFL)
root = QApplication(sys.argv)
app = Application()
sys.exit(root.exec_())
