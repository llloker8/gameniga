import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtWidgets import QPushButton, QColorDialog
from PyQt5.QtWidgets import QLCDNumber
from PyQt5.QtWidgets import QLabel, QLineEdit
import random
 
 
class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui',self)
        self.Easy.clicked.connect(self.easyRun)
        self.Normal.clicked.connect(self.normalRun)
        self.Hard.clicked.connect(self.hardRun)
        self.KLIK.clicked.connect(self.relax)
        self.colorEasy.clicked.connect(self.Color_1)
        self.colorNormal.clicked.connect(self.Color_2)
        self.colorHard.clicked.connect(self.Color_3)
        self.point = 0
        self.points = QLCDNumber(self)
        self.points.move(1000, 50)
        self.LCD_count = QLCDNumber(self)
        self.LCD_count.move(1000, 10)
        self.count = 0
        self.Number_1 = QLCDNumber(self)
        self.Number_1.move(500, 450)
        self.Number_2 = QLCDNumber(self)
        self.Number_2.move(620, 450)
        self.name_input = QLineEdit(self)
        self.name_input.move(730, 360)
        self.otvet.clicked.connect(self.Otvet)
        
 
    def easyRun(self):
        self.Num_1 = random.randint(1, 9)
        self.Num_2 = random.randint(1, 9)
        self.mul = self.Num_1 * self.Num_2
        self.Number_1.display(self.Num_1)
        self.Number_2.display(self.Num_2)
        name = self.name_input.text()
        if name == self.mul:
            self.points += 1
            self.points.display(self.point)
    def normalRun(self):
        self.Num_1 = random.randint(10, 99)
        self.Num_2 = random.randint(10, 99)
        self.mul = self.Num_1 * self.Num_2
        self.Number_1.display(self.Num_1)
        self.Number_2.display(self.Num_2)
        
        
    def hardRun(self):
        self.Num_1 = random.randint(10, 999)
        self.Num_2 = random.randint(10, 999)
        self.mul = self.Num_1 * self.Num_2
        self.Number_1.display(self.Num_1)
        self.Number_2.display(self.Num_2)
        
        
    def Color_1(self):
        colorEasy = QColorDialog.getColor()
        if colorEasy.isValid():
            self.Easy.setStyleSheet(
                "background-color: {}".format(colorEasy.name())
            )
            
    def Color_2(self):
        colorNormal = QColorDialog.getColor()
        if colorNormal.isValid():
            self.Normal.setStyleSheet(
                "background-color: {}".format(colorNormal.name())
            )
        
    def Color_3(self):
        colorHard = QColorDialog.getColor()
        if colorHard.isValid():
            self.Hard.setStyleSheet(
                "background-color: {}".format(colorHard.name())
            )
            
    def relax(self):
        self.count += 1
        self.LCD_count.display(self.count)
        
    def Otvet(self):
        name = self.name_input.text()
        if name == self.mul:
            self.points += 1
            self.points.display(self.point)
 
app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())