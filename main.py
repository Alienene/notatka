from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, 
                             QListWidget, QLineEdit, QVBoxLayout)

app = QApplication([])
window = QWidget()

line = QLineEdit()
list1 = QListWidget()

b1 = QPushButton('добавити')
b2 = QPushButton('видалити')
b3 = QPushButton('зберегти')

v1 = QVBoxLayout()
v1.addWidget(line)
v1.addWidget(b1)
v1.addWidget(list1)
v1.addWidget(b2)
v1.addWidget(b3)
window.setLayout(v1)

tasks = []
def add():
    t = line.text() #витягуємо текст з поля для введення
    if t:
        tasks.append(t)
        list1.addItem(t)
        line.clear()
b1.clicked.connect(add)


def delete():
    t = list1.currentRow()
    if t>=0:
        del tasks[t]
        list1.takeItem(t)
b2.clicked.connect(delete)

def save():
    with open('tasks.txt','w') as f:
        for t in tasks:
            f.write(t+'\n')
b3.clicked.connect(save)


window.show()
app.exec()
