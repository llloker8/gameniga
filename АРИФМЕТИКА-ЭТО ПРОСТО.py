import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow,  QMessageBox
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
        self.kak.clicked.connect(self.INFO)
        self.kak1.clicked.connect(self.INFO1)
        self.point = 0 #правельные ответы
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
        self.sumPoint = 0 # общее кол. правильных и неправельных ответов
        
        self.statusBar()
        
        self.name_input.setFont(QtGui.QFont('Cambria Math', 40)) #размер и шрифт
        
        self.otvet.clicked.connect(self.Otvet)
        self.badPoint = 0  # неправельные ответы
        self.badPoints = QLCDNumber(self)
        self.badPoints.move(0,590)
        QToolTip.setFont(QFont('Cambria Math', 10))
        self.Easy.setToolTip('Ничего замысловатого, это просто <b>таблица умножения</b>. Отлично подойдёт для начальных классов')
        self.Normal.setToolTip('Уже поинтереснее. Этот режим отлично подойдёт для <b>5-8 классов</b>')
        self.Hard.setToolTip('Давольно сложный уровень. Сделан для <b>9-11 классов</b>. Настоятельно рекомендую перед ним пройти другие уровни сложности ')
    
    ##Всплывающее окно при попытке закрыть программу
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Сообщение', "Вы точно хотите выйти?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            reply = QMessageBox.question(self, 'Сообщение', "Вы точно-точно хотите выйти?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()
        else:
            event.ignore()  
     
    ##Лёгкий уровень
    def easyRun(self):
        self.H = 0
        self.N = 0
        self.E += 1
        self.point = 0
        self.points.display(self.point)
        self.badPoint = 0
        self.badPoints.display(self.point)
        self.sumPoint = 0
        self.Num_1 = random.randint(1, 9)
        self.Num_2 = random.randint(1, 9)
        self.mul = self.Num_1 * self.Num_2
        self.Number_1.display(self.Num_1)
        self.Number_2.display(self.Num_2)
        
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' уровень')
        
    ##Средний уровень   
    def normalRun(self):
        self.E = 0
        self.H = 0
        self.N += 1
        self.point = 0
        self.points.display(self.point)
        self.badPoint = 0
        self.badPoints.display(self.point)
        self.sumPoint = 0
        self.Num_1 = random.randint(10, 99)
        self.Num_2 = random.randint(10, 99)
        self.mul = self.Num_1 * self.Num_2
        self.Number_1.display(self.Num_1)
        self.Number_2.display(self.Num_2)
        
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' уровень')
        
    ##Сложный уровень    
    def hardRun(self):
        self.E = 0
        self.N = 0
        self.H += 1
        self.point = 0
        self.points.display(self.point)
        self.badPoint = 0
        self.badPoints.display(self.point)
        self.sumPoint = 0
        self.Num_1 = random.randint(10, 999)
        self.Num_2 = random.randint(10, 999)
        self.mul = self.Num_1 * self.Num_2
        self.Number_1.display(self.Num_1)
        self.Number_2.display(self.Num_2)
        
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' уровень')
        
    ## выбор цвета для лёгкого    
    def Color_1(self):
        colorEasy = QColorDialog.getColor()
        if colorEasy.isValid():
            self.Easy.setStyleSheet(
                "background-color: {}".format(colorEasy.name())
            )
    ##среднего       
    def Color_2(self):
        colorNormal = QColorDialog.getColor()
        if colorNormal.isValid():
            self.Normal.setStyleSheet(
                "background-color: {}".format(colorNormal.name())
            )
    ##сложного    
    def Color_3(self):
        colorHard = QColorDialog.getColor()
        if colorHard.isValid():
            self.Hard.setStyleSheet(
                "background-color: {}".format(colorHard.name())
            )
    ## отдых(правый верхний угол)        
    def relax(self):
        self.count += 1
        self.LCD_count.display(self.count)
    ##Вопросительный знак для среднего    
    def INFO(self):
        self.kak = QMessageBox()
        self.kak.about(self, 'Быстрый способ умножения двузначных чисел', 'пример:'\
'умножим 95 на 88. В уме эти числа необходимо разложить на составляющие от 100.'\
'(100-5)*(100-12)'\
'Первые две цифры ответа-это первый множитель минус остаток второго разложенного или наоборот второй множитель минус первый остаток,кому как проще'\
'(95-12)=83 или (88-5)=83'\
'вторые две цифры ответа-нужно просто перемножить остатки от ста'\
'(5*12)=60'\
'итого 95*88=8360'\
'При минимальной тренировке вы научитесь быстро считать.Актуальны числа близкие к ста.')
     ##для сложного   
    def INFO1(self):
        self.kak1 = QMessageBox()
        self.kak1.about(self, 'способ умножения трёхзначных чисел', '986 · 997 = (986 - 3) · 1000 + 3 · 14 = 983 000 + 42 = 983 042'\
'Что мы сделали: из тысячи мы вычли недостаток до тысячи первого числа'\
'(14) и недостаток до тысячи второго числа (3), затем умножили на 1000,'\
'а после прибавли произведение недостатков (14 · 3). Все просто.'\
'Вместо тысячи может быть 100, 200 итд - принцип один и тот же.')
    ##кнопка 'ответить'
    def Otvet(self):
        name = self.name_input.text()
        if self.E >= 1:
            if name == str(self.mul):
                self.point += 1
                self.sumPoint += 1
                self.points.display(self.point)
                self.Num_1 = random.randint(1, 9)
                self.Num_2 = random.randint(1, 9)
                self.mul = self.Num_1 * self.Num_2
                self.Number_1.display(self.Num_1)
                self.Number_2.display(self.Num_2)
                if self.sumPoint == 20:
                    if self.point == 20:
                        self.label.setText('Можешь переходить на следующий уровень! <b>5+</b>')
                        self.point = 0
                        self.badPoint = 0
                    elif self.point == 19 or self.badPoint == 18:
                        self.label.setText('Так деражать! <b>4</b>')
                        self.point = 0
                        self.badPoint = 0
                    elif self.point == 17 or self.point == 16 or self.point == 15:
                        self.label.setText('Удовлетворительно. Порешай ещё. <b>3</b>')
                        self.point = 0
                        self.badPoint = 0
                    elif self.point >= 6 and self.point <= 19:
                        self.label.setText('Учи таблицу умножения! <b>2</b>')
                        self.point = 0
                        self.badPoint = 0
                    elif self.point == 20:
                        self.label.setText('Можешь переходить на следующий уровень! <b>5+</b>')
                        self.point = 0
                        self.badPoint = 0
                    
                
                
            
            elif name != str(self.mul):
                self.badPoint += 1
                self.sumPoint += 1
                self.badPoints.display(self.badPoint)
                self.Num_1 = random.randint(1, 9)
                self.Num_2 = random.randint(1, 9)
                self.mul = self.Num_1 * self.Num_2
                self.Number_1.display(self.Num_1)
                self.Number_2.display(self.Num_2)
                if self.sumPoint == 20:
                    if self.badPoint == 0:
                        self.label.setText('Можешь переходить на следующий уровень! <b>5+</b>')
                        self.point = 0
                        self.badPoint = 0
                    if self.badPoint == 1 or self.badPoint == 2:
                        self.label.setText('Так деражать! <b>4</b>')
                        self.point = 0
                        self.badPoint = 0
                    if self.badPoint == 3:
                        self.label.setText('Удовлетворительно. Порешай ещё. <b>3</b>')
                        self.point = 0
                        self.badPoint = 0
                    if self.badPoint == 4:
                        self.label.setText('Удовлетворительно. Порешай ещё. <b>3</b>')
                        self.point = 0
                        self.badPoint = 0
                    if self.badPoint == 5:
                        self.label.setText('Удовлетворительно. Порешай ещё. <b>3</b>')
                        self.point = 0
                        self.badPoint = 0
                    if self.badPoint >= 6 and self.badPoint <= 19:
                        self.label.setText('Учи таблицу умножения! <b>2</b>')
                        self.point = 0
                        self.badPoint = 0
                    if self.badPoint == 20:
                        self.label.setText('КАК? <b>1</b>')
                        self.point = 0
                        self.badPoint = 0
                
             
        
        
        elif self.N >= 1:
            if name == str(self.mul):
                self.point += 1
                self.sumPoint += 1
                self.points.display(self.point)
                self.Num_1 = random.randint(1, 9)
                self.Num_2 = random.randint(1, 9)
                self.mul = self.Num_1 * self.Num_2
                self.Number_1.display(self.Num_1)
                self.Number_2.display(self.Num_2)
                if self.sumPoint == 20:
                    if self.point == 20:
                        self.label.setText('Можешь переходить на следующий уровень! <b>5+</b>')
                        self.point = 0
                        self.badPoint = 0
                    elif self.point == 19 or self.badPoint == 18:
                        self.label.setText('Так деражать! <b>4</b>')
                        self.point = 0
                        self.badPoint = 0
                    elif self.point == 17 or self.point == 16 or self.point == 15:
                        self.label.setText('Удовлетворительно. Порешай ещё. <b>3</b>')
                        self.point = 0
                        self.badPoint = 0
                    elif self.point >= 6 and self.point <= 19:
                        self.label.setText('Учи таблицу умножения! <b>2</b>')
                        self.point = 0
                        self.badPoint = 0
                    elif self.point == 20:
                        self.label.setText('Можешь переходить на следующий уровень! <b>5+</b>')
                        self.point = 0
                        self.badPoint = 0
            
            elif name != str(self.mul):
                self.badPoint += 1
                self.sumPoint += 1
                self.badPoints.display(self.badPoint)
                self.Num_1 = random.randint(10, 99)
                self.Num_2 = random.randint(10, 99)
                self.mul = self.Num_1 * self.Num_2
                self.Number_1.display(self.Num_1)
                self.Number_2.display(self.Num_2)
                if self.sumPoint == 20:
                    if self.badPoint == 0:
                        self.label.setText('Можешь переходить на следующий уровень! <b>5+</b>')
                        self.point = 0
                        self.badPoint = 0
                    if self.badPoint == 1 or self.badPoint == 2:
                        self.label.setText('Так деражать! <b>4</b>')
                        self.point = 0
                        self.badPoint = 0
                    if self.badPoint == 3:
                        self.label.setText('Удовлетворительно. Порешай ещё. <b>3</b>')
                        self.point = 0
                        self.badPoint = 0
                    if self.badPoint == 4:
                        self.label.setText('Удовлетворительно. Порешай ещё. <b>3</b>')
                        self.point = 0
                        self.badPoint = 0
                    if self.badPoint == 5:
                        self.label.setText('Удовлетворительно. Порешай ещё. <b>3</b>')   
                        self.point = 0
                        self.badPoint = 0
                    if self.badPoint >= 6 and self.badPoint <= 19:
                        self.label.setText('Учи таблицу умножения! <b>2</b>')
                        self.point = 0
                        self.badPoint = 0
                    if self.badPoint == 20:
                        self.label.setText('КАК? <b>1</b>')
                        self.point = 0
                        self.badPoint = 0
        
        elif self.H >= 1:
            if name == str(self.mul):
                self.point += 1
                self.sumPoint += 1
                self.points.display(self.point)
                self.Num_1 = random.randint(1, 9)
                self.Num_2 = random.randint(1, 9)
                self.mul = self.Num_1 * self.Num_2
                self.Number_1.display(self.Num_1)
                self.Number_2.display(self.Num_2)
                if self.sumPoint == 20:
                    if self.point == 20:
                        self.label.setText('Можешь переходить на следующий уровень! <b>5+</b>')
                        self.point = 0
                        self.badPoint = 0
                    elif self.point == 19 or self.badPoint == 18:
                        self.label.setText('Так деражать! <b>4</b>')
                        self.point = 0
                        self.badPoint = 0
                    elif self.point == 17 or self.point == 16 or self.point == 15:
                        self.label.setText('Удовлетворительно. Порешай ещё. <b>3</b>')
                        self.point = 0
                        self.badPoint = 0
                    elif self.point >= 6 and self.point <= 19:
                        self.label.setText('Учи таблицу умножения! <b>2</b>')
                        self.point = 0
                        self.badPoint = 0
                    elif self.point == 20:
                        self.label.setText('Можешь переходить на следующий уровень! <b>5+</b>')
                        self.point = 0
                        self.badPoint = 0
            
            elif name != str(self.mul):
                self.badPoint += 1
                self.sumPoint += 1
                self.badPoints.display(self.badPoint)
                self.Num_1 = random.randint(30, 999)
                self.Num_2 = random.randint(30, 999)
                self.mul = self.Num_1 * self.Num_2
                self.Number_1.display(self.Num_1)
                self.Number_2.display(self.Num_2)
                if self.sumPoint == 20:
                    if self.badPoint == 0:
                        self.label.setText('Можешь переходить на следующий уровень! <b>5+</b>')
                        self.point = 0
                        self.badPoint = 0
                    if self.badPoint == 1 or self.badPoint == 2:
                        self.label.setText('Так деражать! <b>4</b>')
                        self.point = 0
                        self.badPoint = 0
                    if self.badPoint == 3:
                        self.label.setText('Удовлетворительно. Порешай ещё. <b>3</b>')
                        self.point = 0
                        self.badPoint = 0
                    if self.badPoint == 4:
                        self.label.setText('Удовлетворительно. Порешай ещё. <b>3</b>')
                        self.point = 0
                        self.badPoint = 0
                    if self.badPoint == 5:
                        self.label.setText('Удовлетворительно. Порешай ещё. <b>3</b>')    
                        self.point = 0
                        self.badPoint = 0
                    if self.badPoint >= 6 and self.badPoint <= 19:
                        self.label.setText('Учи таблицу умножения! <b>2</b>')
                        self.point = 0
                        self.badPoint = 0
                    if self.badPoint == 20:
                        self.label.setText('КАК? <b>1</b>')
                        self.point = 0
                        self.badPoint = 0

                                                                                     
app = QApplication(sys.argv)
ex = Math()
ex.show()
sys.exit(app.exec_())