from PyQt6.QtWidgets import  QApplication , QWidget, QLabel, QPushButton, QLineEdit
on = False
x = 0
y = 0
sum = 0
belgi = ""
hisob = ""
myproject = QApplication([])
oyna = QWidget()

oyna.setWindowTitle("MY PROJECT")
oyna.setFixedSize(500, 400)
oyna.setStyleSheet("background-color:blue")

lbl = QLabel("",oyna)
lbl.setGeometry(20, 20, 460, 50)
lbl.setStyleSheet("background-color:black;color:red")



edit = QLineEdit("OFF",oyna)
edit.setGeometry(35, 25, 430, 40)
edit.setStyleSheet("background-color:white;color:black")

# ======================================================
def hisobla():
    global y
    global x
    global belgi
    global sum
    global hisob
    if belgi =="+":
        print(x,y)
        sum = x + y
    elif belgi =="-":
        print(x, y)
        sum = x - y
    elif belgi =="*":
        print(x,y)
        sum = x * y
    elif belgi =="/":
        print(x,y)
        sum = x//y

    hisob= str(sum)
    print(hisob)
    edit.setText(hisob)
def teng():
    global y
    y = int(edit.text())
    edit.setText("")
    hisobla()
def bol():
    global belgi
    global x
    global on
    if on:
        belgi = "/"
        x = int(edit.text())
        edit.setText("")


def kopay():
    global belgi
    global x
    global on
    if on:
        belgi = "*"
        x = int(edit.text())
        edit.setText("")
def minus():
    global on
    global belgi
    global x
    if on:
        x= int(edit.text())
        edit.setText("")
        belgi = "-"
def plus():
    global x
    global belgi
    global on
    if on:
        x = int(edit.text())
        edit.setText("")
        belgi = "+"
def onn():
    global on
    if on == False:
        on = True
        edit.setText("")
    else:
        on = False
        lbl.setText("")





bt1 = QPushButton("ON/OFF",oyna)
bt1.setGeometry(400, 80, 80, 80)
bt1.setStyleSheet("background-color:black;color:white;font-size: 20px")
bt1.clicked.connect(onn)

bt2 = QPushButton("+",oyna)
bt2.setGeometry(400, 180, 80, 80)
bt2.setStyleSheet("background-color:orange;color:white;font-size: 30px")
bt2.clicked.connect(plus)

bt3 = QPushButton("-",oyna)
bt3.setGeometry(270, 180, 80, 80)
bt3.setStyleSheet("background-color:orange;color:white;font-size: 30px")
bt3.clicked.connect(minus)

bt4 = QPushButton("=",oyna)
bt4.setGeometry(20, 290, 460, 100)
bt4.setStyleSheet("background-color:black;color:white;font-size: 90px")
bt4.clicked.connect(teng)

bt5 = QPushButton("x",oyna)
bt5.setGeometry(150, 180, 80, 80)
bt5.setStyleSheet("background-color:orange;color:white;font-size: 30px")
bt5.clicked.connect(kopay)

bt6 = QPushButton("/",oyna)
bt6.setGeometry(20, 180, 80, 80)
bt6.setStyleSheet("background-color:orange;color:white; font-size: 30px")
bt6.clicked.connect(bol)

oyna.show()
myproject.exec()

