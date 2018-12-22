import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtWidgets import QPushButton, QColorDialog
from PyQt5.QtWidgets import QLCDNumber, QToolTip
from PyQt5.QtWidgets import QLabel, QLineEdit
from PyQt5.QtGui import QFont
from PyQt5 import QtGui
import random
 
 
class Math(QMainWindow):
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
        self.points.move(0, 500)
        self.LCD_count = QLCDNumber(self)
        self.LCD_count.move(1000, 10)
        self.count = 0
        self.Number_1 = QLCDNumber(self)
        self.Number_1.setGeometry(300, 450, 200, 100)
        self.Number_2 = QLCDNumber(self)
        self.Number_2.setGeometry(550, 450, 200, 100)
        self.name_input = QLineEdit(self)
        self.name_input.setGeometry(800, 450, 200, 100)
        self.E = 0
        self.N = 0
        self.H = 0
        
        self.statusBar()
        
        self.name_input.setFont(QtGui.QFont('Cambria Math', 40))
        
        self.otvet.clicked.connect(self.Otvet)
        self.badPoint = 0
        self.badPoints = QLCDNumber(self)
        self.badPoints.move(0,590)
        QToolTip.setFont(QFont('SansSerif', 10))
        self.Easy.setToolTip('Ничего замысловатого, это просто <b>таблица умножения</b>. Отлично подойдёт для начальных классов')
        self.Normal.setToolTip('Уже поинтереснее. Этот режим отлично подойдёт для <b>5-8 классов</b>')
        self.Hard.setToolTip('Давольно сложный уровень. Сделан для <b>9-11 классов</b>. Настоятельно рекомендую перед ним пройти другие уровни сложности ')
     
    
    def easyRun(self):
        self.H = 0
        self.N = 0
        self.E += 1
        self.point = 0
        self.points.display(self.point)
        self.badPoint = 0
        self.badPoints.display(self.point)
        self.Num_1 = random.randint(1, 9)
        self.Num_2 = random.randint(1, 9)
        self.mul = self.Num_1 * self.Num_2
        self.Number_1.display(self.Num_1)
        self.Number_2.display(self.Num_2)
        
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
       
    def normalRun(self):
        self.E = 0
        self.H = 0
        self.N += 1
        self.point = 0
        self.points.display(self.point)
        self.Num_1 = random.randint(10, 99)
        self.Num_2 = random.randint(10, 99)
        self.mul = self.Num_1 * self.Num_2
        self.Number_1.display(self.Num_1)
        self.Number_2.display(self.Num_2)
        
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        
        
    def hardRun(self):
        self.E = 0
        self.N = 0
        self.H += 1
        self.point = 0
        self.points.display(self.point)
        self.Num_1 = random.randint(10, 999)
        self.Num_2 = random.randint(10, 999)
        self.mul = self.Num_1 * self.Num_2
        self.Number_1.display(self.Num_1)
        self.Number_2.display(self.Num_2)
        
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        
        
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
        if self.E >= 1:
            if name == str(self.mul):
                self.point += 1
                self.points.display(self.point)
                self.Num_1 = random.randint(1, 9)
                self.Num_2 = random.randint(1, 9)
                self.mul = self.Num_1 * self.Num_2
                self.Number_1.display(self.Num_1)
                self.Number_2.display(self.Num_2)
            
            elif name != str(self.mul):
                self.badPoint += 1
                self.badPoint += 1
                self.badPoints.display(self.point)
                self.Num_1 = random.randint(1, 9)
                self.Num_2 = random.randint(1, 9)
                self.mul = self.Num_1 * self.Num_2
                self.Number_1.display(self.Num_1)
                self.Number_2.display(self.Num_2)
                if self.badPoint < 2:
                    self.label.setText("Молодец! Продолжай в том же духе!")
        
        elif self.N >= 1:
            if name == str(self.mul):
                self.point += 1
                self.points.display(self.point)
                self.Num_1 = random.randint(10, 99)
                self.Num_2 = random.randint(10, 99)
                self.mul = self.Num_1 * self.Num_2
                self.Number_1.display(self.Num_1)
                self.Number_2.display(self.Num_2)
            
            elif name != str(self.mul):
                self.badPoint += 1
                self.badPoint += 1
                self.badPoints.display(self.point)
                self.Num_1 = random.randint(1, 9)
                self.Num_2 = random.randint(1, 9)
                self.mul = self.Num_1 * self.Num_2
                self.Number_1.display(self.Num_1)
                self.Number_2.display(self.Num_2)
                if self.badPoint < 2:
                    self.label.setText("Молодец! Продолжай в том же духе!")
        
        elif self.H >= 1:
            if name == str(self.mul):
                self.point += 1
                self.points.display(self.point)
                self.Num_1 = random.randint(1, 9)
                self.Num_2 = random.randint(1, 9)
                self.mul = self.Num_1 * self.Num_2
                self.Number_1.display(self.Num_1)
                self.Number_2.display(self.Num_2)
            
            elif name != str(self.mul):
                self.badPoint += 1
                self.badPoint += 1
                self.badPoints.display(self.point)
                self.Num_1 = random.randint(1, 9)
                self.Num_2 = random.randint(1, 9)
                self.mul = self.Num_1 * self.Num_2
                self.Number_1.display(self.Num_1)
                self.Number_2.display(self.Num_2)
                if self.badPoint < 2:
                    self.label.setText("Молодец! Продолжай в том же духе!")
                    
        

 
app = QApplication(sys.argv)
ex = Math()
ex.show()
sys.exit(app.exec_())