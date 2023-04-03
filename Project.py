import sys

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import math

width=1600
height=900
location = ['upper right', 'upper left', 'lower left',
            'lower right', 'right', 'center left',
            'center right', 'lower center', 'upper center', 'center']

def import_data_mas(name, name_mas):
    name_f = open(f"{name}.txt", "r")
    line = name_f.readlines()
    name_f.close
    for el in line:
        name_mas.append(float(el))
    return name_mas

def mnk_x(mas, n):
    mnk_x = [[0]*(len(mas[0])+1) for i in range(2*n)]
    for i in range(2*n):
        S = 0
        for j in range(len(mas[0])):
            mnk_x[i][j] = math.pow(mas[0][j], i+1)
            S += mnk_x[i][j]
        mnk_x[i][len(mas[0])] = S
    return mnk_x

def mnk_y(mas, n):
    mnk_y = [[0] * (len(mas[0]) + 1) for i in range(n+1)]
    for i in range(n+1):
        S = 0
        for j in range(len(mas[0])):
            mnk_y[i][j] = mas[1][j]*math.pow(mas[0][j], i)
            S += mnk_y[i][j]
        mnk_y[i][len(mas[0])] = S
    return mnk_y

def mnk(mas, n):
    mnk = [[0] * (n+2) for i in range(n+1)]
    mnk_1 = mnk_x(mas, n)
    mnk_2 = mnk_y(mas, n)
    for i in range(n+1):
        for j in range(n+2):
            if (i==0 and j==0):
                mnk[i][j]=len(mas[0])
            elif (i==0 and j!=n+1):
                mnk[i][j]=mnk_1[j-1][len(mas[0])]
            elif (j!=n+1):
                mnk[i][j] = mnk_1[j+i-1][len(mas[0])]
            if j==n+1:
                mnk[i][n+1] = mnk_2[i][len(mas[0])]
    return mnk

def fill_mas(mas_x, mas_y):
    mas = [[]]
    mas[0] = mas_x
    mas.append(mas_y)
    return mas

def new_mas(mas):
    n = len(mas)
    for k in range(n):
        for i in range(n):
            s = mas[i][k]
            for j in range(len(mas[0])):
                b = mas[k][j] / mas[k][k]
                if (i > k):
                    mas[i][j] = mas[i][j] - s * b
    return mas

def find_x(mas):
    n = len(mas)
    x = [0]*n
    for i in range(n-1, -1, -1):
        sum =0
        for j in range(i+1, n):
            sum += mas[i][j] * x[j]
        x[i]=(float)((mas[i][len(mas[0])-1] - sum) / mas[i][i])
    return x


def find_func(mas_resh, mas_x):
    func_mas = []
    for j in range(len(mas_x)):
        func = 0
        for i in range(len(mas_resh)):
            func += mas_resh[i]*math.pow(mas_x[j], i)
        func_mas.append(func)
    return func_mas

def find_del(mas_x, mas_y, mas_resh):
    mas_del = [0]*len(mas_x)
    for i in range(len(mas_x)-1):
        fun_mnk = find_func(mas_resh, mas_x)
        mas_del[i] = math.fabs(mas_y[i]-fun_mnk[i])
    max_del = max(mas_del)
    return max_del

def inter( mas_coord, mas_line):
    mas = []
    mas_mnk = fill_mas(mas_coord, mas_line)
    mnk_mas = mnk(mas_mnk, 14)
    gauss = find_x(new_mas(mnk_mas))
    y_int = find_func(gauss, mas_coord)


    #f = interpolate.interp1d(mas_coord, mas_line, kind="linear")
    #x_int = np.linspace(mas_coord[0], mas_coord[-1], 20)
    #y_int = f(x_int)
    mas.append(mas_coord)
    mas.append(y_int)
    return mas




class MinAverMax(FigureCanvas):
    def __init__(self, nameF_min, nameF_aver, nameF_max, title, ylabel, xlabel):
        plt.close()
        mas_F = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
        M_max = []
        M_aver = []
        M_min = []

        import_data_mas(nameF_max, M_max)
        import_data_mas(nameF_aver, M_aver)
        import_data_mas(nameF_min, M_min)
        self.fig, self.ax = plt.subplots()
        super().__init__(self.fig)
        self.ax.grid(color='black',
                linewidth=1,
                linestyle='--')
        self.ax.axis([100, 1000, 0, M_max[-1] + 0.002])
        self.ax.plot(mas_F, M_max, 'b', label='MAX', linewidth=2)
        self.ax.plot(mas_F, M_aver, 'r', label='AVER', linewidth=2)
        self.ax.plot(mas_F, M_min, 'yellowgreen', label='MIN', linewidth=2)

        plt.title(title)
        plt.ylabel(ylabel)
        plt.xlabel(xlabel)
        self.ax.legend(loc=location[0])


class LineCont(FigureCanvas):
    def __init__(self, mas_of_name, name_coord, title, ylabel, xlabel):
        plt.close()
        coord = []
        import_data_mas(name_coord, coord)
        mas_of_min_max = []
        M_line_Cont_100 = []
        M_line_Cont_200 = []
        M_line_Cont_300 = []
        M_line_Cont_400 = []
        M_line_Cont_500 = []
        M_line_Cont_600 = []
        M_line_Cont_700 = []
        M_line_Cont_800 = []
        M_line_Cont_900 = []
        M_line_Cont_1000 = []

        self.fig, self.ax = plt.subplots()
        super().__init__(self.fig)
        self.ax.grid(color='black',
                     linewidth=1,
                     linestyle='--')


        if len(mas_of_name)>1:

            import_data_mas(mas_of_name[0], M_line_Cont_100)
            import_data_mas(mas_of_name[1], M_line_Cont_200)
            import_data_mas(mas_of_name[2], M_line_Cont_300)
            import_data_mas(mas_of_name[3], M_line_Cont_400)
            import_data_mas(mas_of_name[4], M_line_Cont_500)
            import_data_mas(mas_of_name[5], M_line_Cont_600)

            import_data_mas(mas_of_name[6], M_line_Cont_700)

            import_data_mas(mas_of_name[7], M_line_Cont_800)

            import_data_mas(mas_of_name[8], M_line_Cont_900)

            import_data_mas(mas_of_name[9], M_line_Cont_1000)


            mas = inter(coord, M_line_Cont_100)
            mas_of_min_max.append(min(mas[1]))
            mas_of_min_max.append(max(mas[1]))
            self.ax.plot(mas[0], mas[1], 'b', label='F=100', linewidth=2)

            mas = inter(coord, M_line_Cont_200)
            mas_of_min_max.append(min(mas[1]))
            mas_of_min_max.append(max(mas[1]))
            self.ax.plot(mas[0], mas[1], 'r', label='F=200', linewidth=2)

            mas = inter(coord, M_line_Cont_300)
            mas_of_min_max.append(min(mas[1]))
            mas_of_min_max.append(max(mas[1]))
            self.ax.plot(mas[0], mas[1], 'yellowgreen', label='F=300', linewidth=2)

            mas = inter(coord, M_line_Cont_400)
            mas_of_min_max.append(min(mas[1]))
            mas_of_min_max.append(max(mas[1]))
            self.ax.plot(mas[0], mas[1], 'blueviolet', label='F=400', linewidth=2)

            mas = inter(coord, M_line_Cont_500)
            mas_of_min_max.append(min(mas[1]))
            mas_of_min_max.append(max(mas[1]))
            self.ax.plot(mas[0], mas[1], 'c', label='F=500', linewidth=2)

            mas = inter(coord, M_line_Cont_600)
            mas_of_min_max.append(min(mas[1]))
            mas_of_min_max.append(max(mas[1]))
            self.ax.plot(mas[0], mas[1], 'gold', label='F=600', linewidth=2)

            mas = inter(coord, M_line_Cont_700)
            mas_of_min_max.append(min(mas[1]))
            mas_of_min_max.append(max(mas[1]))
            self.ax.plot(mas[0], mas[1], 'steelblue', label='F=700', linewidth=2)

            mas = inter(coord, M_line_Cont_800)
            mas_of_min_max.append(min(mas[1]))
            mas_of_min_max.append(max(mas[1]))
            self.ax.plot(mas[0], mas[1], 'palevioletred', label='F=800', linewidth=2)

            mas = inter(coord, M_line_Cont_900)
            mas_of_min_max.append(min(mas[1]))
            mas_of_min_max.append(max(mas[1]))
            self.ax.plot(mas[0], mas[1], 'olive', label='F=900', linewidth=2)

            mas = inter(coord, M_line_Cont_1000)
            mas_of_min_max.append(min(mas[1]))
            mas_of_min_max.append(max(mas[1]))

            self.ax.set_xlim([0, max(mas[0])])
            self.ax.set_ylim([min(mas_of_min_max), max(mas_of_min_max)+1000000])
            self.ax.plot(mas[0], mas[1], 'navy', label='F=1000', linewidth=2)
        else:
            import_data_mas(mas_of_name[0], M_line_Cont_100)
            mas = inter(coord, M_line_Cont_100)
            self.ax.set_xlim([0, max(mas[0])])
            self.ax.set_ylim([min(mas[1]), max(mas[1]) + 1000000])
            if len(mas_of_name[0])>53:
                self.ax.plot(mas[0], mas[1], 'b', label=('F='+mas_of_name[0][len(mas_of_name[0])-9:len(mas_of_name[0])-5]),
                         linewidth=2)
            else:
                self.ax.plot(mas[0], mas[1], 'b', label=('F=' + mas_of_name[0][len(mas_of_name[0]) - 8:len(mas_of_name[0]) - 5]),
                             linewidth=2)
        plt.title(title)
        plt.ylabel(ylabel)
        plt.xlabel(xlabel)
        if "SFRI" in mas_of_name[0]:
            self.ax.legend(loc=location[0])
        else:
            self.ax.legend(loc=location[1])



class DentEmalVkl(FigureCanvas):
    def __init__(self, nameF_Dent, nameF_Emal, nameF_Vkl, title, ylabel, xlabel):
        plt.close()
        mas_F = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
        Dent = []
        Emal = []
        Vkl = []

        import_data_mas(nameF_Dent, Dent)
        import_data_mas(nameF_Emal, Emal)
        import_data_mas(nameF_Vkl, Vkl)
        print(nameF_Dent)
        self.fig, self.ax = plt.subplots()
        super().__init__(self.fig)
        self.ax.grid(color='black',
                linewidth=1,
                linestyle='--')
        self.ax.axis([100, 1000, 0, max(Dent[-1], Emal[-1], Vkl[-1])*1.05])

        self.ax.plot(mas_F, Dent, 'b', label='Dent', linewidth=2)
        self.ax.plot(mas_F, Emal, 'r', label='Emal', linewidth=2)
        self.ax.plot(mas_F, Vkl, 'yellowgreen', label='Vkl', linewidth=2)

        plt.title(title)
        plt.ylabel(ylabel)
        plt.xlabel(xlabel)
        self.ax.legend(loc=location[0])

class AnotherWindow(QWidget):

    def __init__(self, pixmap, parent=None):
        super().__init__(parent)
        self.setWindowFlags(QtCore.Qt.Window)
        self.label = QLabel(self)
        scaled_pixmap = pixmap.scaled(1350, 1000, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        self.label.setPixmap(scaled_pixmap)
        self.setFixedSize(scaled_pixmap.width(), scaled_pixmap.height())
        self.setGeometry(200, 200, scaled_pixmap.width(), scaled_pixmap.height())
        self.setWindowTitle('Image')

class LibraryOfMaterials(QWidget):
    tableChanged = pyqtSignal()
    def __init__(self, list_of_materials, parent=None):
        super().__init__(parent)
        self.setWindowFlags(QtCore.Qt.Window)
        self.list_of_materials = list_of_materials.copy()
        self.tableWidget = QTableWidget(len(self.list_of_materials), 3, self)
        self.tableWidget.setGeometry(50, 50, 1100, 700)
        for i in range(len(self.list_of_materials)):
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(self.list_of_materials[i][0]))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(self.list_of_materials[i][1])))
            self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(self.list_of_materials[i][2])))
        self.tableWidget.setHorizontalHeaderLabels(["Название", "E, МПа", "Сигма"])
        self.tableWidget.verticalHeader().setDefaultSectionSize(20)
        self.tableWidget.verticalHeader().setVisible(False);
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.addButton = QPushButton("+", self)
        self.addButton.setGeometry(self.tableWidget.width() + 100, 50, 50, 50)
        self.addButton.clicked.connect(self.addButton_clicked)
        self.setFixedSize(self.tableWidget.width()+200, self.tableWidget.height()+100)
        self.setWindowTitle('Библиотека материалов')

    def addButton_clicked(self):
        self.w = AddMaterialWindow(self)
        self.w.saveClicked.connect(self.changeTable)
        self.w.show()


    def changeTable(self):
        list_of_names = []
        for i in range(len(self.list_of_materials)):
            list_of_names.append(self.list_of_materials[i][0])
        if self.w.list_of_material[0] in list_of_names:
            QMessageBox.warning(self, "Ошибка", "Данный материал уже был добавлен")
            return
        self.list_of_materials.append(self.w.list_of_material.copy())
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)
        self.tableWidget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(self.w.list_of_material[0]))
        self.tableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(str(self.w.list_of_material[1])))
        self.tableWidget.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(str(self.w.list_of_material[2])))
        self.tableChanged.emit()

class AddMaterialWindow(QWidget):
    saveClicked = pyqtSignal()
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(QtCore.Qt.Window)
        self.list_of_material = []
        self.vert_layout = QVBoxLayout(self)
        self.vert_layout.addWidget(QLabel("Название"))
        self.name = QLineEdit()
        self.vert_layout.addWidget(self.name)
        self.vert_layout.addWidget(QLabel("Модуль Юнга (E)"))
        self.module_Ung = QLineEdit()
        self.vert_layout.addWidget(self.module_Ung)
        self.vert_layout.addWidget(QLabel("Коэффициент Пуассона"))
        self.coef = QLineEdit()
        self.vert_layout.addWidget(self.coef)
        self.saveButton = QPushButton("Сохранить", self)
        self.saveButton.clicked.connect(self.saveButtonClicked)
        self.vert_layout.addWidget(self.saveButton)
        self.setFixedSize(400, 600)
        self.setWindowTitle('Добавить материал')

    def saveButtonClicked(self):
        if float(self.module_Ung.text())<=0 and (float(self.coef.text())<=0 or float(self.coef.text())>=0.5):
            QMessageBox.warning(self, "Ошибка", "Модуль Юнга должен быть больше 0 \nКоэффициент Пуассона должен быть в интервале (0, 0.5)")
        elif (float(self.coef.text())<=0 or float(self.coef.text())>=0.5):
            QMessageBox.warning(self, "Ошибка", "Коэффициент Пуассона должен быть в интервале (0, 0.5)")
        elif float(self.module_Ung.text())<=0:
            QMessageBox.warning(self, "Ошибка", "Модуль Юнга должен быть больше 0")
        else:
            self.list_of_material.append(self.name.text())
            self.list_of_material.append(float(self.module_Ung.text()))
            self.list_of_material.append(float(self.coef.text()))
            self.saveClicked.emit()
        self.list_of_material.clear()

class MyLineEdit(QLineEdit):
    def __init__(self):
        super().__init__()
        self.focused = False
    def focusInEvent(self, event):
        self.focused = True

    def focusOutEvent(self, event):
        self.focused = False

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.window = QMainWindow()

        self.combo_1 = QComboBox(self.window)
        self.combo_1.addItems(["Материал 1", "Материал 2", "Материал 3"])
        self.combo_1.setGeometry(20, 20, int(width/10), int(height/25))

        self.combo_2 = QComboBox(self.window)
        self.combo_2.addItems(["Сила 100", "Сила 200", "Сила 300", "Сила 400", "Сила 500", "Сила 600", "Сила 700", "Сила 800", "Сила 900", "сила 1000", "Все"])
        self.combo_2.setGeometry(20, int(20 + height / 20), int(width / 10), int(height / 25))

        self.btn = QPushButton("Построить", self.window)
        self.btn.setGeometry(int(width/4), int(20+height/20), int(width / 10), int(height / 25))

        self.btn.clicked.connect(self.button_clicked)

        self.label_1 = QLabel()
        self.label_2 = QLabel()
        self.label_3 = QLabel()
        self.label_4 = QLabel()

        self.tabs = QTabWidget(self.window)
        self.tab_1 = QWidget()
        self.tab_2 = QWidget()
        self.tabs.setGeometry(20, int(30+height/10), int(4*width /5-20), int(4 * height / 5+20))
        self.tabs.addTab(self.tab_1, "1")
        self.tabs.addTab(self.tab_2, "2")

        self.tab_1_layout = QVBoxLayout()
        self.tab_1_hor1_layout = QHBoxLayout()
        self.tab_1_hor2_layout = QHBoxLayout()
        self.tab_1_combo_name = QLabel("Выбор линии:")
        self.tab_1_combo = QComboBox()

        self.tab_1_graph1_name = QLabel("PRES")
        self.tab_1_graph2_name = QLabel("SFRI")
        self.tab_1_graph1_name.setFixedSize(int(width / 10), int(height / 25))
        self.tab_1_graph2_name.setFixedSize(int(width / 10), int(height / 25))
        self.tab_1_hor1_layout.addWidget(self.tab_1_graph1_name)
        self.tab_1_hor1_layout.addWidget(self.tab_1_graph2_name)

        self.tab_1_graph1 = QLabel()
        self.tab_1_graph2 = QLabel()
        self.tab_1_hor2_layout.addWidget(self.tab_1_graph1)
        self.tab_1_hor2_layout.addWidget(self.tab_1_graph2)

        self.tab_1_combo.addItems(["Линия 1", "Линия 2", "Линия 3", "Линия 4"])
        self.tab_1_combo.setFixedSize( int(width / 10), int(height / 25))
        self.tab_1_combo_name.setFixedSize( int(width / 10), int(height / 25))

        self.tab_1_layout.addWidget(self.tab_1_combo_name)
        self.tab_1_layout.addWidget(self.tab_1_combo)

        self.tab_1_layout.addLayout(self.tab_1_hor1_layout)

        self.tab_1_layout.addLayout(self.tab_1_hor2_layout)

        self.tab_1.setLayout(self.tab_1_layout)

        self.tab_2_layout_hor = QHBoxLayout()
        self.tab_2_layout_hor_name = QHBoxLayout() #для обозначения списка
        self.tab_2_layout_ver = QVBoxLayout()
        self.tab_2_layout_hor2 = QHBoxLayout()
        self.tab_2_layout_hor3 = QHBoxLayout()
        self.tab_2_combo_1 = QComboBox()
        self.tab_2_combo_1.addItems(["эмаль","дентин","вкладка","все"])
        self.tab_2_combo_1.setFixedSize(int(width/10), int(height/25))

        self.tab_2_combo_1_name = QLabel("Выберите элемент")
        self.tab_2_combo_1_name.setFixedSize(int(width / 10), int(height / 25))
        self.tab_2_layout_hor_name.addWidget(self.tab_2_combo_1_name)
        self.tab_2_layout_ver.addLayout(self.tab_2_layout_hor_name)
        self.tab_2_layout_hor.addWidget(self.tab_2_combo_1)

        self.tab_2_combo_2 = QComboBox()
        self.combo_2_visible = False
        self.tab_2_combo_1.currentIndexChanged.connect(self.on_combobox_func)

        self.tab_2_graph1 = QLabel()
        self.tab_2_graph2 = QLabel()
        self.tab_2_layout_hor2.addWidget(self.tab_2_graph1)
        self.tab_2_layout_hor2.addWidget(self.tab_2_graph2)

        self.tab_2_graph1_name = QLabel("Sint")
        self.tab_2_graph2_name = QLabel("Eint")

        self.tab_2_graph1_name.setFixedSize(int(width / 10), int(height / 25))
        self.tab_2_graph2_name.setFixedSize(int(width / 10), int(height / 25))
        self.tab_2_layout_hor3.addWidget(self.tab_2_graph1_name)
        self.tab_2_layout_hor3.addWidget(self.tab_2_graph2_name)

        self.tab_2_layout_ver.addLayout(self.tab_2_layout_hor)
        self.tab_2_layout_ver.addLayout(self.tab_2_layout_hor3)
        self.tab_2_layout_ver.addLayout(self.tab_2_layout_hor2)

        self.tab_2.setLayout(self.tab_2_layout_ver)

        self.layout_hor = QHBoxLayout()
        self.layout_vert_1 = QVBoxLayout()
        self.layout_vert_2 = QVBoxLayout()

        self.layout_vert_1.addWidget(self.window)

        self.layout_hor.addLayout(self.layout_vert_1)
        self.layout_hor.addLayout(self.layout_vert_2)

        self.central_tabs = QTabWidget()
        self.central_tabs.setStyleSheet(f"font-size: {height / 100 + 2}pt;")

        self.central_tab_1 = QWidget()
        self.central_tab_1.setLayout(self.layout_hor)

        self.central_tab_2 = QWidget()
        self.central_tab_2_layout_hor = QHBoxLayout()
        self.central_tab_2_layout_vert_1 = QVBoxLayout()
        self.central_tab_2_layout_vert_2 = QVBoxLayout()

        self.cental_tab_2_btn = QPushButton("Выгрузить файл")
        self.cental_tab_2_btn.clicked.connect(self.openFileDialog)
        self.central_tab_2_label = QLabel()
        self.central_tab_2_label.setPixmap(QPixmap("empty.png").scaled(int(2*width / 3) - 20, int(height - 40), Qt.IgnoreAspectRatio,
                                                   Qt.SmoothTransformation))
        self.central_tab_2_layout_vert_1.addWidget(self.cental_tab_2_btn)
        self.central_tab_2_layout_vert_1.addWidget(self.central_tab_2_label)

        self.central_tab_2_layout_vert_2_hor = QHBoxLayout()
        self.central_tab_2_layout_vert_2_comboBox = QComboBox()

        self.list_of_data = []
        self.loadListOfData()
        self.list_of_materials = []
        for i in range(len(self.list_of_data)):
            self.list_of_materials.append(self.list_of_data[i][0])
        self.central_tab_2_layout_vert_2_comboBox.addItems(self.list_of_materials)
        self.central_tab_2_layout_vert_2_comboBox.currentTextChanged.connect(self.changeTable)
        self.central_tab_2_layout_vert_2_hor.addWidget(self.central_tab_2_layout_vert_2_comboBox)
        self.central_tab_2_layout_vert_2_hor_btn = QPushButton("Добавить")
        self.central_tab_2_layout_vert_2_hor_btn.clicked.connect(self.addMaterial)
        self.central_tab_2_layout_vert_2_hor.addWidget(self.central_tab_2_layout_vert_2_hor_btn)
        self.central_tab_2_layout_vert_2.addLayout(self.central_tab_2_layout_vert_2_hor)

        self.tableWidget = QTableWidget(1, 2)
        self.tableWidget.setFixedSize(int(width/3), int(height/10))
        self.tableWidget.setHorizontalHeaderLabels([ "E, МПа","Сигма"])
        self.tableWidget.verticalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False);
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(str(self.list_of_data[self.central_tab_2_layout_vert_2_comboBox.currentIndex()][1])))
        self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(str(
            self.list_of_data[self.central_tab_2_layout_vert_2_comboBox.currentIndex()][2])))
        self.central_tab_2_layout_vert_2.addWidget(self.tableWidget)

        self.list_of_size = []
        self.central_tab_2_layout_vert_2_hor_1 = QHBoxLayout()
        self.central_tab_2_layout_vert_2_hor_1.addWidget(QLabel("h = "))
        self.line1 = MyLineEdit()
        self.h_dist = 0
        self.central_tab_2_layout_vert_2_hor_1.addWidget(self.line1)
        self.central_tab_2_layout_vert_2_hor_1_btn =  QPushButton("Ok")
        self.central_tab_2_layout_vert_2_hor_1_btn.clicked.connect(lambda : self.acceptData(self.line1))
        self.central_tab_2_layout_vert_2_hor_1.addWidget(self.central_tab_2_layout_vert_2_hor_1_btn)
        self.central_tab_2_layout_vert_2.addLayout(self.central_tab_2_layout_vert_2_hor_1)

        self.central_tab_2_layout_vert_2_hor_2 = QHBoxLayout()
        self.central_tab_2_layout_vert_2_hor_2.addWidget(QLabel("le = "))
        self.line2 = MyLineEdit()
        self.le_dist = 0
        self.central_tab_2_layout_vert_2_hor_2.addWidget(self.line2)
        self.central_tab_2_layout_vert_2_hor_2_btn = QPushButton("Ok")
        self.central_tab_2_layout_vert_2_hor_2_btn.clicked.connect(lambda :self.acceptData(self.line2))
        self.central_tab_2_layout_vert_2_hor_2.addWidget(self.central_tab_2_layout_vert_2_hor_2_btn)
        self.central_tab_2_layout_vert_2.addLayout(self.central_tab_2_layout_vert_2_hor_2)

        self.central_tab_2_layout_vert_2_hor_3 = QHBoxLayout()
        self.central_tab_2_layout_vert_2_hor_3.addWidget(QLabel("lp = "))
        self.line3 = MyLineEdit()
        self.lp_dist = 0
        self.central_tab_2_layout_vert_2_hor_3.addWidget(self.line3)
        self.central_tab_2_layout_vert_2_hor_3_btn = QPushButton("Ok")
        self.central_tab_2_layout_vert_2_hor_3_btn.clicked.connect(lambda :self.acceptData(self.line3))
        self.central_tab_2_layout_vert_2_hor_3.addWidget(self.central_tab_2_layout_vert_2_hor_3_btn)
        self.central_tab_2_layout_vert_2.addLayout(self.central_tab_2_layout_vert_2_hor_3)

        self.central_tab_2_layout_vert_2_hor_4 = QHBoxLayout()
        self.central_tab_2_layout_vert_2_hor_4.addWidget(QLabel("l = "))
        self.line4 = MyLineEdit()
        self.l_dist = 0
        self.central_tab_2_layout_vert_2_hor_4.addWidget(self.line4)
        self.central_tab_2_layout_vert_2_hor_4_btn = QPushButton("Ok")
        self.central_tab_2_layout_vert_2_hor_4_btn.clicked.connect(lambda :self.acceptData(self.line4))
        self.central_tab_2_layout_vert_2_hor_4.addWidget(self.central_tab_2_layout_vert_2_hor_4_btn)
        self.central_tab_2_layout_vert_2.addLayout(self.central_tab_2_layout_vert_2_hor_4)

        self.central_tab_2_layout_vert_2_hor_5 = QHBoxLayout()
        self.central_tab_2_layout_vert_2_hor_5.addWidget(QLabel("hw = "))
        self.line5 = MyLineEdit()
        self.hw_dist = 0
        self.central_tab_2_layout_vert_2_hor_5.addWidget(self.line5)
        self.central_tab_2_layout_vert_2_hor_5_btn = QPushButton("Ok")
        self.central_tab_2_layout_vert_2_hor_5_btn.clicked.connect(lambda :self.acceptData(self.line5))
        self.central_tab_2_layout_vert_2_hor_5.addWidget(self.central_tab_2_layout_vert_2_hor_5_btn)
        self.central_tab_2_layout_vert_2.addLayout(self.central_tab_2_layout_vert_2_hor_5)

        self.central_tab_2_layout_vert_2_hor_6 = QHBoxLayout()
        self.central_tab_2_layout_vert_2_hor_6.addWidget(QLabel("lw = "))
        self.line6 = MyLineEdit()
        self.lw_dist = 0
        self.central_tab_2_layout_vert_2_hor_6.addWidget(self.line6)
        self.central_tab_2_layout_vert_2_hor_6_btn = QPushButton("Ok")
        self.central_tab_2_layout_vert_2_hor_6_btn.clicked.connect(lambda :self.acceptData(self.line6))
        self.central_tab_2_layout_vert_2_hor_6.addWidget(self.central_tab_2_layout_vert_2_hor_6_btn)
        self.central_tab_2_layout_vert_2.addLayout(self.central_tab_2_layout_vert_2_hor_6)

        self.central_tab_2_layout_vert_2_saveButton = QPushButton("Сохранить")
        self.central_tab_2_layout_vert_2_saveButton.clicked.connect(self.saveMaterialsAndSizesInFile)
        self.central_tab_2_layout_vert_2.addWidget(self.central_tab_2_layout_vert_2_saveButton)

        self.central_tab_2_layout_hor.addLayout(self.central_tab_2_layout_vert_1)
        self.central_tab_2_layout_hor.addLayout(self.central_tab_2_layout_vert_2)
        self.central_tab_2.setLayout(self.central_tab_2_layout_hor)

        self.central_tabs.addTab(self.central_tab_1, "Пользователь")
        self.central_tabs.addTab(self.central_tab_2, "Доктор")
        self.setCentralWidget(self.central_tabs)

        self.setGeometry(0, 0, width, height)
        self.setWindowTitle('NCCL-research')

    def mousePressEvent(self, QMouseEvent):
        if self.h_dist == 0:
            if self.line1.focused:
                self.h_dist = QMouseEvent.pos().y()
        else:
            self.h_dist = math.fabs(self.h_dist-QMouseEvent.pos().y())
            self.line1.setText(str(self.h_dist))
            self.h_dist = 0

        if self.le_dist == 0:
            if self.line2.focused:
                self.le_dist = QMouseEvent.pos().x()
        else:
            self.le_dist = math.fabs(self.le_dist - QMouseEvent.pos().x())
            self.line2.setText(str(self.le_dist))
            self.le_dist = 0

        if self.lp_dist == 0:
            if self.line3.focused:
                self.lp_dist = QMouseEvent.pos().x()
        else:
            self.lp_dist = math.fabs(self.lp_dist - QMouseEvent.pos().x())
            self.line3.setText(str(self.lp_dist))
            self.lp_dist = 0

        if self.l_dist == 0:
            if self.line4.focused:
                self.l_dist = QMouseEvent.pos().x()
        else:
            self.l_dist = math.fabs(self.l_dist - QMouseEvent.pos().x())
            self.line4.setText(str(self.l_dist))
            self.l_dist = 0

        if self.hw_dist == 0:
            if self.line5.focused:
                self.hw_dist = QMouseEvent.pos().y()
        else:
            self.hw_dist = math.fabs(self.hw_dist-QMouseEvent.pos().y())
            self.line5.setText(str(self.hw_dist))
            self.hw_dist = 0

        if self.lw_dist == 0:
            if self.line6.focused:
                self.lw_dist = QMouseEvent.pos().x()
        else:
            self.lw_dist = math.fabs(self.lw_dist - QMouseEvent.pos().x())
            self.line6.setText(str(self.lw_dist))
            self.lw_dist = 0

    def acceptData(self, data):
        if (data.text()!=""):
            if float(data.text())>0:
                self.list_of_size.append(float(data.text()))
        print(self.list_of_size)

    def loadListOfData(self):
        with open("Materials.txt", "r") as file:
            for line in file:
                line = line[:len(line)-1]
                new_list = line.split("\t")
                self.list_of_data.append(new_list)

    def saveMaterialsAndSizesInFile(self):
        with open("Materials.txt", "w") as file:
            for material in self.list_of_data:
                file.write(material[0] + "\t"+str(material[1])+ "\t" + str(material[2])+"\n")
        with open("Size.txt", "w") as file:
            for size in self.list_of_size:
                file.write(str(size) + "\t")

    def addMaterial(self):
        self.lib = LibraryOfMaterials( self.list_of_data, self)
        self.lib.tableChanged.connect(self.changeComboBox)
        self.lib.show()

    def changeComboBox(self):
        self.list_of_data = self.lib.list_of_materials.copy()
        self.central_tab_2_layout_vert_2_comboBox.clear()
        self.list_of_materials.clear()
        for i in range(len(self.list_of_data)):
            self.list_of_materials.append(self.list_of_data[i][0])
        self.central_tab_2_layout_vert_2_comboBox.addItems(self.list_of_materials)

    def changeTable(self):
        self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(
            str(self.list_of_data[self.central_tab_2_layout_vert_2_comboBox.currentIndex()][1])))
        self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(str(
            self.list_of_data[self.central_tab_2_layout_vert_2_comboBox.currentIndex()][2])))

    def openFileDialog(self):
        fileName = QFileDialog.getOpenFileName(self, "Open File")
        if fileName[0][-3:] != "jpg" and fileName[0][-3:] != "png":
            QMessageBox.warning(self, "Предупреждение", "Выбранный файл неверного формата")
        elif fileName[0]!='':
            self.tab_2_pixmap_1 = QPixmap(fileName[0])
            scaled_pixmap = self.tab_2_pixmap_1.scaled(int(2*width / 3) + 20, int(height - 40), Qt.IgnoreAspectRatio,
                                                   Qt.SmoothTransformation)
            self.central_tab_2_label.setPixmap(scaled_pixmap)
        else:
            self.tab_2_pixmap_1 = QPixmap("empty.png")
            scaled_pixmap = self.tab_2_pixmap_1.scaled(int(2 * width / 3) + 20, int(height - 40), Qt.IgnoreAspectRatio,
                                                       Qt.SmoothTransformation)
            self.central_tab_2_label.setPixmap(scaled_pixmap)

    def on_combobox_func(self):
        if self.tab_2_combo_1.currentText() == "все" and self.combo_2_visible == False:
            self.tab_2_combo_2.addItems(["min", "сред", "max"])
            self.tab_2_combo_2.setFixedSize(int(width / 10), int(height / 25))
            self.tab_2_layout_hor.addWidget(self.tab_2_combo_2)
            self.combo_2_visible = True
        else:
            if self.tab_2_layout_hor.count()>1:
                self.tab_2_layout_hor.itemAt(self.tab_2_layout_hor.count()-1).widget().setParent(None)
                for i in range(3):
                    self.tab_2_combo_2.removeItem(0)
            self.combo_2_visible = False

    def deleteItemsOfLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)
                else:
                    self.deleteItemsOfLayout(item.layout())

    def button_clicked(self):
        self.deleteItemsOfLayout(self.tab_2_layout_hor2)
        self.deleteItemsOfLayout(self.tab_1_hor2_layout)
        self.deleteItemsOfLayout(self.layout_vert_2)

        name_of_data1 = "Material "+str(self.combo_1.currentIndex()+1) +"\line "+str(self.tab_1_combo.currentIndex()+1)+\
                       "\Material_"+str(self.combo_1.currentIndex()+1)+"_p_line_"+str(self.tab_1_combo.currentIndex()+1)+\
                       "_Cont_F_"
        name_of_coord = "coor\coor_line_" + str(self.tab_1_combo.currentIndex()+1)+"_F_Y"
        mas_of_name_pres = []
        mas_of_name_sfri = []
        if self.combo_2.currentIndex()>9:
            for i in range(10):
                mas_of_name_pres.append(name_of_data1+str(i+1)+"00_PRES")
                mas_of_name_sfri.append(name_of_data1+str(i+1)+"00_SFRI")
            self.tab_1_graph1 = LineCont(mas_of_name_pres, name_of_coord,
                                         "Контакт", "Pres", "coord")
            self.tab_1_graph2 = LineCont(mas_of_name_sfri, name_of_coord,
                                         "Контакт", "Sfri", "coord")
        else:
            mas_of_name_pres.append(name_of_data1+str(self.combo_2.currentIndex()+1)+"00_PRES")
            mas_of_name_sfri.append(name_of_data1 + str(self.combo_2.currentIndex()+1) + "00_SFRI")

            self.tab_1_graph1 = LineCont(mas_of_name_pres, name_of_coord, "Контакт", "Pres", "coord")
            self.tab_1_graph2 = LineCont(mas_of_name_sfri, name_of_coord, "Контакт", "Sfri", "coord")

        name_of_data2 = "Material "+str(self.combo_1.currentIndex()+1)
        if self.tab_2_combo_1.currentIndex()==1:
            name_of_data2_sint = name_of_data2 + "\dent" +"\sint\Material_" + str(self.combo_1.currentIndex()+1)+"_dent_sint_"
            name_of_data2_eint = name_of_data2 + "\dent" + "\eint\Material_" + str(self.combo_1.currentIndex() + 1) + "_dent_eint_"
            self.tab_2_graph1 = MinAverMax(name_of_data2_sint+"minimum", name_of_data2_sint+"average", name_of_data2_sint+"maximum", "Дентит", "Sint", "F")
            self.tab_2_graph2 =  MinAverMax(name_of_data2_eint+"minimum", name_of_data2_eint+"average", name_of_data2_eint+"maximum", "Дентит", "Eint", "F")
        if self.tab_2_combo_1.currentIndex() == 2:
            name_of_data2_sint = name_of_data2 + "//vkl" + "\sint\Material_" + str(self.combo_1.currentIndex() + 1) + "_vkl_sint_"
            name_of_data2_eint = name_of_data2 + "//vkl" + "\eint\Material_" + str(self.combo_1.currentIndex() + 1) + "_vkl_eint_"
            self.tab_2_graph1 = MinAverMax(name_of_data2_sint + "minimum", name_of_data2_sint + "average",
                                           name_of_data2_sint + "maximum", "Вкладка", "Sint", "F")
            self.tab_2_graph2 = MinAverMax(name_of_data2_eint + "minimum", name_of_data2_eint + "average",
                                           name_of_data2_eint + "maximum", "Вкладка", "Eint", "F")
        if self.tab_2_combo_1.currentIndex() == 0:
            name_of_data2_sint = name_of_data2 + "\emal" + "\sint\Material_" + str(self.combo_1.currentIndex() + 1) + "_emal_sint_"
            name_of_data2_eint = name_of_data2 + "\emal" + "\eint\Material_" + str(self.combo_1.currentIndex() + 1) + "_emal_eint_"
            self.tab_2_graph1 = MinAverMax(name_of_data2_sint + "minimum", name_of_data2_sint + "average",
                                           name_of_data2_sint + "maximum", "Эмаль", "Sint", "F")
            self.tab_2_graph2 = MinAverMax(name_of_data2_eint + "minimum", name_of_data2_eint + "average",
                                           name_of_data2_eint + "maximum", "Эмаль", "Eint", "F")
        else:
            name_of_data2_sint_emal = name_of_data2 + "\emal" + "\sint\Material_" + str(
                self.combo_1.currentIndex() + 1) + "_emal_sint_"
            name_of_data2_eint_emal = name_of_data2 + "\emal" + "\eint\Material_" + str(
                self.combo_1.currentIndex() + 1) + "_emal_eint_"
            name_of_data2_sint_vkl = name_of_data2 + "//vkl" + "\sint\Material_" + str(
                self.combo_1.currentIndex() + 1) + "_vkl_sint_"
            name_of_data2_eint_vkl = name_of_data2 + "//vkl" + "\eint\Material_" + str(
                self.combo_1.currentIndex() + 1) + "_vkl_eint_"
            name_of_data2_sint_dent = name_of_data2 + "\dent" + "\sint\Material_" + str(
                self.combo_1.currentIndex() + 1) + "_dent_sint_"
            name_of_data2_eint_dent = name_of_data2 + "\dent" + "\eint\Material_" + str(
                self.combo_1.currentIndex() + 1) + "_dent_eint_"
            if self.tab_2_combo_2.currentIndex() == 0:
                self.tab_2_graph1 = DentEmalVkl(
                    name_of_data2_sint_dent + "minimum",
                    name_of_data2_sint_emal + "minimum",
                    name_of_data2_sint_vkl + "minimum",
                    "Сравнение", "Sint", "F")
                self.tab_2_graph2 = DentEmalVkl(
                    name_of_data2_eint_dent + "minimum",
                    name_of_data2_eint_emal + "minimum",
                    name_of_data2_eint_vkl + "minimum",
                    "Сравнение", "Eint", "F")
            if self.tab_2_combo_2.currentIndex() == 2:
                self.tab_2_graph1 = DentEmalVkl(
                    name_of_data2_sint_dent + "maximum",
                    name_of_data2_sint_emal + "maximum",
                    name_of_data2_sint_vkl + "maximum",
                    "Сравнение", "Sint", "F")
                self.tab_2_graph2 = DentEmalVkl(
                    name_of_data2_eint_dent + "maximum",
                    name_of_data2_eint_emal + "maximum",
                    name_of_data2_eint_vkl + "maximum",
                    "Сравнение", "Eint", "F")
            if self.tab_2_combo_2.currentIndex() == 1:
                self.tab_2_graph1 = DentEmalVkl(
                    name_of_data2_sint_dent + "average",
                    name_of_data2_sint_emal + "average",
                    name_of_data2_sint_vkl + "average",
                    "Сравнение", "Sint", "F")
                self.tab_2_graph2 = DentEmalVkl(
                    name_of_data2_eint_dent + "average",
                    name_of_data2_eint_emal + "average",
                    name_of_data2_eint_vkl + "average",
                    "Сравнение", "Eint", "F")

        self.tab_2_layout_hor2.addWidget(self.tab_2_graph1)
        self.tab_2_layout_hor2.addWidget(self.tab_2_graph2)
        self.tab_1_hor2_layout.addWidget(self.tab_1_graph1)
        self.tab_1_hor2_layout.addWidget(self.tab_1_graph2)


        self.path_to_pic = "pic_0522\\material_" + str(self.combo_1.currentIndex()+1)+"\\Material_" + str(self.combo_1.currentIndex()+1)
        if self.combo_2.currentIndex()>9:
            QMessageBox.warning(self, "Предупреждение", "При заданных настройках невозможно отображение картинок")
            return

        self.mas_of_pic_1 = [self.path_to_pic+"_dent_sint00"+str(self.combo_2.currentIndex())+".jpg", self.path_to_pic+"_dent_epint00"+str(self.combo_2.currentIndex())+".jpg"]
        self.mas_of_pic_2 = [self.path_to_pic+"_emal_sint00"+str(self.combo_2.currentIndex())+".jpg", self.path_to_pic+"_emal_epint00"+str(self.combo_2.currentIndex())+".jpg"]
        self.mas_of_pic_3 = [self.path_to_pic+"_vkl_sint00"+str(self.combo_2.currentIndex())+".jpg", self.path_to_pic+"_vkl_epint00"+str(self.combo_2.currentIndex())+".jpg"]
        self.mas_of_pic_4 = [self.path_to_pic+"_all_sint00"+str(self.combo_2.currentIndex())+".jpg", self.path_to_pic+"_all_epint00"+str(self.combo_2.currentIndex())+".jpg"]
        self.counter_1 = 0
        self.counter_2 = 0
        self.counter_3 = 0
        self.counter_4 = 0



        self.pixmap_1 = QPixmap(self.mas_of_pic_1[self.counter_1]).copy(0, 200, 1750, 1100)
        self.pixmap_2 = QPixmap(self.mas_of_pic_2[self.counter_2]).copy(0, 200, 1750, 1100)
        self.pixmap_3 = QPixmap(self.mas_of_pic_3[self.counter_3]).copy(0, 200, 1750, 1100)
        self.pixmap_4 = QPixmap(self.mas_of_pic_4[self.counter_4]).copy(0, 200, 1750, 1100)
        scaled_pixmap_1 = self.pixmap_1.scaled(int(width/5), int(height/5), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        scaled_pixmap_2 = self.pixmap_2.scaled(int(width/5), int(height/5), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        scaled_pixmap_3 = self.pixmap_3.scaled(int(width/5), int(height/5), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        scaled_pixmap_4 = self.pixmap_4.scaled(int(width/5), int(height/5), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)

        while self.layout_vert_2.itemAt(0)!=None:
            if self.layout_vert_2.itemAt(0).layout():
                self.layout_vert_2.itemAt(0).layout().setParent(None)
            else:
                self.layout_vert_2.itemAt(0).widget().setParent(None)

        self.hbox_btn_1 = QHBoxLayout()
        self.pic1_btn_1 = QPushButton("<-")
        self.pic1_btn_2 = QPushButton("->")
        self.pic1_btn_icon = QPushButton()
        self.pic1_btn_icon.setIcon(QIcon("icon.png"))
        self.hbox_btn_1.addWidget(self.pic1_btn_1)
        self.hbox_btn_1.addWidget(self.pic1_btn_icon)
        self.hbox_btn_1.addWidget(self.pic1_btn_2)
        self.label1_name = QLabel("Дентин")

        self.hbox_btn_2 = QHBoxLayout()
        self.pic2_btn_1 = QPushButton("<-")
        self.pic2_btn_2 = QPushButton("->")
        self.pic2_btn_icon = QPushButton()
        self.pic2_btn_icon.setIcon(QIcon("icon.png"))
        self.hbox_btn_2.addWidget(self.pic2_btn_1)
        self.hbox_btn_2.addWidget(self.pic2_btn_icon)
        self.hbox_btn_2.addWidget(self.pic2_btn_2)
        self.label2_name = QLabel("Эмаль")

        self.hbox_btn_3 = QHBoxLayout()
        self.pic3_btn_1 = QPushButton("<-")
        self.pic3_btn_2 = QPushButton("->")
        self.pic3_btn_icon = QPushButton()
        self.pic3_btn_icon.setIcon(QIcon("icon.png"))
        self.hbox_btn_3.addWidget(self.pic3_btn_1)
        self.hbox_btn_3.addWidget(self.pic3_btn_icon)
        self.hbox_btn_3.addWidget(self.pic3_btn_2)
        self.label3_name = QLabel("Вкладка")

        self.hbox_btn_4 = QHBoxLayout()
        self.pic4_btn_1 = QPushButton("<-")
        self.pic4_btn_2 = QPushButton("->")
        self.pic4_btn_icon = QPushButton()
        self.pic4_btn_icon.setIcon(QIcon("icon.png"))
        self.hbox_btn_4.addWidget(self.pic4_btn_1)
        self.hbox_btn_4.addWidget(self.pic4_btn_icon)
        self.hbox_btn_4.addWidget(self.pic4_btn_2)
        self.label4_name = QLabel("Все")

        self.label_1.setPixmap(scaled_pixmap_1)
        self.label_2.setPixmap(scaled_pixmap_2)
        self.label_3.setPixmap(scaled_pixmap_3)
        self.label_4.setPixmap(scaled_pixmap_4)

        self.pic1_btn_1.clicked.connect(self.pic1_btn1_clicked)
        self.pic1_btn_icon.clicked.connect(self.pic1_btn_icon_clicked)
        self.pic1_btn_2.clicked.connect(self.pic1_btn2_clicked)

        self.pic2_btn_1.clicked.connect(self.pic2_btn1_clicked)
        self.pic2_btn_icon.clicked.connect(self.pic2_btn_icon_clicked)
        self.pic2_btn_2.clicked.connect(self.pic2_btn2_clicked)

        self.pic3_btn_1.clicked.connect(self.pic3_btn1_clicked)
        self.pic3_btn_icon.clicked.connect(self.pic3_btn_icon_clicked)
        self.pic3_btn_2.clicked.connect(self.pic3_btn2_clicked)

        self.pic4_btn_1.clicked.connect(self.pic4_btn1_clicked)
        self.pic4_btn_icon.clicked.connect(self.pic4_btn_icon_clicked)
        self.pic4_btn_2.clicked.connect(self.pic4_btn2_clicked)

        self.layout_vert_2.addWidget(self.label4_name)
        self.layout_vert_2.addWidget(self.label_4)
        self.layout_vert_2.addLayout(self.hbox_btn_4)

        self.layout_vert_2.addWidget(self.label1_name)
        self.layout_vert_2.addWidget(self.label_1)
        self.layout_vert_2.addLayout(self.hbox_btn_1)

        self.layout_vert_2.addWidget(self.label2_name)
        self.layout_vert_2.addWidget(self.label_2)
        self.layout_vert_2.addLayout(self.hbox_btn_2)

        self.layout_vert_2.addWidget(self.label3_name)
        self.layout_vert_2.addWidget(self.label_3)
        self.layout_vert_2.addLayout(self.hbox_btn_3)


    def keyPressEvent(self, event):
        if self.path_to_pic!="":
            if event.key() == QtCore.Qt.Key_Left:
                if self.counter_1 != 0:
                    self.counter_1 -= 1
                if self.counter_2 != 0:
                    self.counter_2 -= 1
                if self.counter_3 != 0:
                    self.counter_3 -= 1
                if self.counter_4 != 0:
                    self.counter_4 -= 1
                else:
                    self.counter_1 = len(self.mas_of_pic_1) - 1
                    self.counter_2 = len(self.mas_of_pic_2) - 1
                    self.counter_3 = len(self.mas_of_pic_3) - 1
                    self.counter_4 = len(self.mas_of_pic_4) - 1
            if event.key() == QtCore.Qt.Key_Right:
                if self.counter_1 != len(self.mas_of_pic_1) - 1:
                    self.counter_1 += 1
                if self.counter_2 != len(self.mas_of_pic_2) - 1:
                    self.counter_2 += 1
                if self.counter_3 != len(self.mas_of_pic_3) - 1:
                    self.counter_3 += 1
                if self.counter_4 != len(self.mas_of_pic_4) - 1:
                    self.counter_4 += 1
                else:
                    self.counter_1 = 0
                    self.counter_2 = 0
                    self.counter_3 = 0
                    self.counter_4 = 0
            self.pixmap_1 = QPixmap(self.mas_of_pic_1[self.counter_1]).copy(0, 200, 1750, 1100)
            scaled_pixmap = self.pixmap_1.scaled(int(width/5)-20, int(height/4-40) , Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
            self.label_1.setPixmap(scaled_pixmap)
            self.pixmap_2 = QPixmap(self.mas_of_pic_2[self.counter_2]).copy(0, 200, 1750, 1100)
            scaled_pixmap = self.pixmap_2.scaled(int(width/5)-20, int(height/4-40), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
            self.label_2.setPixmap(scaled_pixmap)
            self.pixmap_3 = QPixmap(self.mas_of_pic_3[self.counter_3]).copy(0, 200, 1750, 1100)
            scaled_pixmap = self.pixmap_3.scaled(int(width/5)-20, int(height/4-40), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
            self.label_3.setPixmap(scaled_pixmap)
            self.pixmap_4 = QPixmap(self.mas_of_pic_4[self.counter_4]).copy(0, 200, 1750, 1100)
            scaled_pixmap = self.pixmap_4.scaled(int(width/5)-20, int(height/4-40), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
            self.label_4.setPixmap(scaled_pixmap)

    def pic1_btn1_clicked(self):
        if self.counter_1 != 0:
            self.counter_1 -= 1
        else:
            self.counter_1 = len(self.mas_of_pic_1)-1

        self.pixmap_1 = QPixmap(self.mas_of_pic_1[self.counter_1]).copy(0, 200, 1750, 1100)
        scaled_pixmap = self.pixmap_1.scaled(int(width/5)-20, int(height/4-40), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        self.label_1.setPixmap(scaled_pixmap)

    def pic1_btn2_clicked(self):
        if self.counter_1 != len(self.mas_of_pic_1)-1:
            self.counter_1 += 1

        else:
            self.counter_1 = 0

        self.pixmap_1 = QPixmap(self.mas_of_pic_1[self.counter_1]).copy(0, 200, 1750, 1100)
        scaled_pixmap = self.pixmap_1.scaled(int(width/5)-20, int(height/4-40), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        self.label_1.setPixmap(scaled_pixmap)

    def pic1_btn_icon_clicked(self):
        self.w = AnotherWindow(self.pixmap_1, self)
        self.w.show()

    def pic2_btn1_clicked(self):
        if self.counter_2 != 0:
            self.counter_2 -= 1
        else:
            self.counter_2 = len(self.mas_of_pic_2)-1

        self.pixmap_2 = QPixmap(self.mas_of_pic_2[self.counter_2]).copy(0, 200, 1750, 1100)
        scaled_pixmap = self.pixmap_2.scaled(int(width/5)-20, int(height/4-40), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        self.label_2.setPixmap(scaled_pixmap)

    def pic2_btn2_clicked(self):
        if self.counter_2 != len(self.mas_of_pic_2)-1:
            self.counter_2 += 1

        else:
            self.counter_2 = 0

        self.pixmap_2 = QPixmap(self.mas_of_pic_2[self.counter_2]).copy(0, 200, 1750, 1100)
        scaled_pixmap = self.pixmap_2.scaled(int(width/5)-20, int(height/4-40), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        self.label_2.setPixmap(scaled_pixmap)

    def pic2_btn_icon_clicked(self):
        self.w = AnotherWindow(self.pixmap_2, self)
        self.w.show()

    def pic3_btn1_clicked(self):
        if self.counter_3 != 0:
            self.counter_3 -= 1
        else:
            self.counter_3=len(self.mas_of_pic_3)-1

        self.pixmap_3 = QPixmap(self.mas_of_pic_3[self.counter_3]).copy(0, 200, 1750, 1100)
        scaled_pixmap = self.pixmap_3.scaled(int(width/5)-20, int(height/4-40), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        self.label_3.setPixmap(scaled_pixmap)

    def pic3_btn2_clicked(self):
        if self.counter_3 != len(self.mas_of_pic_3)-1:
            self.counter_3 += 1

        else:
            self.counter_3 = 0

        self.pixmap_3 = QPixmap(self.mas_of_pic_3[self.counter_3]).copy(0, 200, 1750, 1100)
        scaled_pixmap = self.pixmap_3.scaled(int(width/5)-20, int(height/4-40), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        self.label_3.setPixmap(scaled_pixmap)

    def pic3_btn_icon_clicked(self):
        self.w = AnotherWindow(self.pixmap_3, self)
        self.w.show()

    def pic4_btn1_clicked(self):
        if self.counter_4 != 0:
            self.counter_4 -= 1
        else:
            self.counter_4 = len(self.mas_of_pic_4) - 1

        self.pixmap_4 = QPixmap(self.mas_of_pic_4[self.counter_4]).copy(0, 200, 1750, 1100)
        scaled_pixmap = self.pixmap_4.scaled(int(width/5)-20, int(height/4-40), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        self.label_4.setPixmap(scaled_pixmap)

    def pic4_btn2_clicked(self):
        if self.counter_4 != len(self.mas_of_pic_4) - 1:
            self.counter_4 += 1

        else:
            self.counter_4 = 0

        self.pixmap_4 = QPixmap(self.mas_of_pic_4[self.counter_4]).copy(0, 200, 1750, 1100)
        scaled_pixmap = self.pixmap_4.scaled(int(width/5)-20, int(height/4-40), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        self.label_4.setPixmap(scaled_pixmap)

    def pic4_btn_icon_clicked(self):
        self.w = AnotherWindow(self.pixmap_4, self)
        self.w.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())