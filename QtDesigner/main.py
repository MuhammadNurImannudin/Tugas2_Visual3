# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Latihan2(object):
    def __init__(self):
        # Menyimpan data biodata
        self.biodata_list = []
        self.current_index = -1  # Untuk melacak entri yang sedang diedit

    def setupUi(self, Latihan2):
        Latihan2.setObjectName("Latihan2")
        Latihan2.resize(395, 469)
        Latihan2.setStyleSheet("background-color: rgb(64, 67, 255)")
        self.centralwidget = QtWidgets.QWidget(Latihan2)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 70, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.label_2.setObjectName("label_2")
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 130, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.label_3.setObjectName("label_3")
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 160, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.label_4.setObjectName("label_4")
        
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(150, 70, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.lineEdit_3.setObjectName("lineEdit_3")
        
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(150, 100, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.lineEdit_4.setObjectName("lineEdit_4")
        
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(150, 130, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.lineEdit_5.setObjectName("lineEdit_5")
        
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(150, 160, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.lineEdit_6.setObjectName("lineEdit_6")
        
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 190, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.label_5.setObjectName("label_5")
        
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 220, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.label_6.setObjectName("label_6")

        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(150, 190, 221, 22))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dateEdit.setFont(font)
        self.dateEdit.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.dateEdit.setObjectName("dateEdit")
        
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(150, 220, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.lineEdit_8.setObjectName("lineEdit_8")
        
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 250, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.label_7.setObjectName("label_7")
        
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(150, 250, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.lineEdit_9.setObjectName("lineEdit_9")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 290, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(16, 255, 24)")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.save_data)  # Hubungkan tombol simpan
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 290, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color:rgb(255, 238, 48)")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.edit_data)  # Hubungkan tombol edit
        
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(210, 290, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 0, 0)")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.delete_data)  # Hubungkan tombol hapus
        
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(300, 290, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.cancel)  # Hubungkan tombol batal

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(90, 10, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.46, y1:1, x2:0.449, y2:0, stop:0.392045 rgba(255, 255, 255, 255), stop:0.801136 rgba(255, 0, 0, 255))")
        self.label_8.setObjectName("label_8")
        
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(30, 320, 341, 121))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.textEdit.setObjectName("textEdit")
        
        Latihan2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Latihan2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 395, 21))
        Latihan2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Latihan2)
        Latihan2.setStatusBar(self.statusbar)

        self.retranslateUi(Latihan2)
        QtCore.QMetaObject.connectSlotsByName(Latihan2)

    def retranslateUi(self, Latihan2):
        _translate = QtCore.QCoreApplication.translate
        Latihan2.setWindowTitle(_translate("Latihan2", "MainWindow"))
        self.label.setText(_translate("Latihan2", "Nim"))
        self.label_2.setText(_translate("Latihan2", "Nama"))
        self.label_3.setText(_translate("Latihan2", "Kelas"))
        self.label_4.setText(_translate("Latihan2", "Tempat Lahir"))
        self.label_5.setText(_translate("Latihan2", "Tanggal Lahir"))
        self.label_6.setText(_translate("Latihan2", "Telepon"))
        self.label_7.setText(_translate("Latihan2", "Alamat"))
        self.pushButton.setText(_translate("Latihan2", "Simpan"))
        self.pushButton_2.setText(_translate("Latihan2", "Edit"))
        self.pushButton_3.setText(_translate("Latihan2", "Hapus"))
        self.pushButton_4.setText(_translate("Latihan2", "Batal"))
        self.label_8.setText(_translate("Latihan2", "BIODATA"))

    def save_data(self):
        # Mengambil data dari line edits dan menambahkan ke list
        nim = self.lineEdit_3.text()
        nama = self.lineEdit_4.text()
        Kelas = self.lineEdit_5.text()
        tempat_lahir = self.lineEdit_6.text()
        Tanggal_Lahir = self.dateEdit.date().toString("dd/MM/yyyy")
        Telepon = self.lineEdit_8.text()
        Alamat = self.lineEdit_9.text()

        if self.current_index == -1:  # Jika menyimpan entri baru
            self.biodata_list.append({
                "Nim": nim,
                "Nama": nama,
                "Kelas": Kelas,
                "Tempat Lahir": tempat_lahir,
                "Tanggal Lahir": Tanggal_Lahir,
                "Telepon": Telepon,
                "Alamat": Alamat
            })
        else:  # Jika mengedit entri yang sudah ada
            self.biodata_list[self.current_index] = {
                "Nim": nim,
                "Nama": nama,
                "Kelas": Kelas,
                "Tempat Lahir": tempat_lahir,
                "Tanggal Lahir": Tanggal_Lahir,
                "Telepon": Telepon,
                "Alamat": Alamat
            }
            self.current_index = -1  # Reset index setelah edit
        
        self.display_biodata()
        self.clear_inputs()

    def edit_data(self):
        # Mengedit data
        if self.biodata_list:
            row = len(self.biodata_list) - 1  # Ambil entri terakhir
            data = self.biodata_list[row]

            self.lineEdit_3.setText(data["Nim"])
            self.lineEdit_4.setText(data["Nama"])
            self.lineEdit_5.setText(data["Kelas"])
            self.lineEdit_6.setText(data["Tempat Lahir"])
            self.dateEdit.setDate(QtCore.QDate.fromString(data["Tanggal Lahir"], "dd/MM/yyyy"))
            self.lineEdit_8.setText(data["Telepon"])
            self.lineEdit_9.setText(data["Alamat"])

            self.current_index = row  # Set index untuk edit

    def delete_data(self):
        # Menghapus data
        if self.current_index != -1:
            del self.biodata_list[self.current_index]
            self.current_index = -1  # Reset index setelah hapus
            self.display_biodata()
            self.clear_inputs()

    def cancel(self):
        # Mengatur ulang input
        self.clear_inputs()

    def clear_inputs(self):
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.dateEdit.clear()
        self.lineEdit_8.clear()
        self.lineEdit_9.clear()

    def display_biodata(self):
        # Menampilkan biodata di QTextEdit
        self.textEdit.clear()
        for biodata in self.biodata_list:
            self.textEdit.append(f"NIM: {biodata['Nim']}")
            self.textEdit.append(f"Nama: {biodata['Nama']}")
            self.textEdit.append(f"Kelas: {biodata['Kelas']}")
            self.textEdit.append(f"Tempat Lahir: {biodata['Tempat Lahir']}")
            self.textEdit.append(f"Tanggal Lahir: {biodata['Tanggal Lahir']}")
            self.textEdit.append(f"Telepon: {biodata['Telepon']}")
            self.textEdit.append(f"Alamat: {biodata['Alamat']}\n")

    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Latihan2 = QtWidgets.QMainWindow()
    ui = Ui_Latihan2()
    ui.setupUi(Latihan2)
    Latihan2.show()
    sys.exit(app.exec_())
