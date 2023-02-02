from PyQt5 import QtWidgets, QtCore, QtGui
import pyqtgraph as pg
import sys
import sqlite3


class PreWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.__numberOfGraphs = int()

        self.setWindowTitle("Live Plotter")
        self.setGeometry(0, 0, 320, 90)
        self.__center()
        self.__init_preUI()

    def __init_preUI(self):
        pixmap = QtGui.QPixmap("metu.png")
        label = QtWidgets.QLabel()
        label.setPixmap(pixmap)
        label.resize(pixmap.width(), pixmap.height())

        self.__combo = QtWidgets.QComboBox()
        self.__combo.addItems(["1", "2", "3", "4"])

        line = QtWidgets.QLabel("Please select the number of graph: ")

        applyButton = QtWidgets.QPushButton("Apply")

        self.okayButton = QtWidgets.QPushButton("Okay")

        hbox1 = QtWidgets.QHBoxLayout()
        hbox1.addWidget(line, alignment=QtCore.Qt.AlignTop)
        hbox1.addWidget(self.__combo, alignment=QtCore.Qt.AlignTop)

        hbox2 = QtWidgets.QHBoxLayout()
        hbox2.addSpacing(80)
        hbox2.addWidget(applyButton, alignment=QtCore.Qt.AlignTop)
        hbox2.addSpacing(80)

        hbox3 = QtWidgets.QHBoxLayout()
        hbox3.addSpacing(80)
        hbox3.addWidget(self.okayButton, alignment=QtCore.Qt.AlignTop)
        hbox3.addSpacing(80)

        hbox4 = QtWidgets.QHBoxLayout()
        hbox4.addSpacing(80)
        hbox4.addWidget(QtWidgets.QLabel("Mert Sönmezer 2023"))
        hbox4.addSpacing(80)

        [self.__line1, self.__title1, self.__titleLineEdit1,
         self.__xlabel1, self.__xlabelLineEdit1, self.__ylabel1,
         self.__ylabelLineEdit1, self.__path1, self.__pathLineEdit1,
         self.__pathButton1] = self.__create_graph(1)

        self.__widgets1 = [self.__line1, self.__title1, self.__titleLineEdit1,
                           self.__xlabel1, self.__xlabelLineEdit1, self.__ylabel1,
                           self.__ylabelLineEdit1, self.__path1, self.__pathLineEdit1,
                           self.__pathButton1]

        [self.__line2, self.__title2, self.__titleLineEdit2,
         self.__xlabel2, self.__xlabelLineEdit2, self.__ylabel2,
         self.__ylabelLineEdit2, self.__path2, self.__pathLineEdit2,
         self.__pathButton2] = self.__create_graph(2)

        self.__widgets2 = [self.__line2, self.__title2, self.__titleLineEdit2,
                           self.__xlabel2, self.__xlabelLineEdit2, self.__ylabel2,
                           self.__ylabelLineEdit2, self.__path2, self.__pathLineEdit2,
                           self.__pathButton2]

        [self.__line3, self.__title3, self.__titleLineEdit3,
         self.__xlabel3, self.__xlabelLineEdit3, self.__ylabel3,
         self.__ylabelLineEdit3, self.__path3, self.__pathLineEdit3,
         self.__pathButton3] = self.__create_graph(3)

        self.__widgets3 = [self.__line3, self.__title3, self.__titleLineEdit3,
                           self.__xlabel3, self.__xlabelLineEdit3, self.__ylabel3,
                           self.__ylabelLineEdit3, self.__path3, self.__pathLineEdit3,
                           self.__pathButton3]

        [self.__line4, self.__title4, self.__titleLineEdit4,
         self.__xlabel4, self.__xlabelLineEdit4, self.__ylabel4,
         self.__ylabelLineEdit4, self.__path4, self.__pathLineEdit4,
         self.__pathButton4] = self.__create_graph(4)

        self.__widgets4 = [self.__line4, self.__title4, self.__titleLineEdit4,
                           self.__xlabel4, self.__xlabelLineEdit4, self.__ylabel4,
                           self.__ylabelLineEdit4, self.__path4, self.__pathLineEdit4,
                           self.__pathButton4]

        vboxGraph1 = QtWidgets.QVBoxLayout()
        vboxGraph1.addWidget(self.__line1, alignment=QtCore.Qt.AlignCenter)

        hboxGraph11 = QtWidgets.QHBoxLayout()
        hboxGraph11.addWidget(self.__title1)
        hboxGraph11.addWidget(self.__titleLineEdit1)

        hboxGraph12 = QtWidgets.QHBoxLayout()
        hboxGraph12.addWidget(self.__xlabel1)
        hboxGraph12.addWidget(self.__xlabelLineEdit1)

        hboxGraph13 = QtWidgets.QHBoxLayout()
        hboxGraph13.addWidget(self.__ylabel1)
        hboxGraph13.addWidget(self.__ylabelLineEdit1)

        hboxGraph14 = QtWidgets.QHBoxLayout()
        hboxGraph14.addWidget(self.__path1)
        hboxGraph14.addWidget(self.__pathLineEdit1)
        hboxGraph14.addWidget(self.__pathButton1)

        vboxGraph1.addLayout(hboxGraph11)
        vboxGraph1.addLayout(hboxGraph12)
        vboxGraph1.addLayout(hboxGraph13)
        vboxGraph1.addLayout(hboxGraph14)

        vboxGraph2 = QtWidgets.QVBoxLayout()
        vboxGraph2.addWidget(self.__line2, alignment=QtCore.Qt.AlignCenter)

        hboxGraph21 = QtWidgets.QHBoxLayout()
        hboxGraph21.addWidget(self.__title2)
        hboxGraph21.addWidget(self.__titleLineEdit2)

        hboxGraph22 = QtWidgets.QHBoxLayout()
        hboxGraph22.addWidget(self.__xlabel2)
        hboxGraph22.addWidget(self.__xlabelLineEdit2)

        hboxGraph23 = QtWidgets.QHBoxLayout()
        hboxGraph23.addWidget(self.__ylabel2)
        hboxGraph23.addWidget(self.__ylabelLineEdit2)

        hboxGraph24 = QtWidgets.QHBoxLayout()
        hboxGraph24.addWidget(self.__path2)
        hboxGraph24.addWidget(self.__pathLineEdit2)
        hboxGraph24.addWidget(self.__pathButton2)

        vboxGraph2.addLayout(hboxGraph21)
        vboxGraph2.addLayout(hboxGraph22)
        vboxGraph2.addLayout(hboxGraph23)
        vboxGraph2.addLayout(hboxGraph24)

        vboxGraph3 = QtWidgets.QVBoxLayout()
        vboxGraph3.addWidget(self.__line3, alignment=QtCore.Qt.AlignCenter)

        hboxGraph31 = QtWidgets.QHBoxLayout()
        hboxGraph31.addWidget(self.__title3)
        hboxGraph31.addWidget(self.__titleLineEdit3)

        hboxGraph32 = QtWidgets.QHBoxLayout()
        hboxGraph32.addWidget(self.__xlabel3)
        hboxGraph32.addWidget(self.__xlabelLineEdit3)

        hboxGraph33 = QtWidgets.QHBoxLayout()
        hboxGraph33.addWidget(self.__ylabel3)
        hboxGraph33.addWidget(self.__ylabelLineEdit3)

        hboxGraph34 = QtWidgets.QHBoxLayout()
        hboxGraph34.addWidget(self.__path3)
        hboxGraph34.addWidget(self.__pathLineEdit3)
        hboxGraph34.addWidget(self.__pathButton3)

        vboxGraph3.addLayout(hboxGraph31)
        vboxGraph3.addLayout(hboxGraph32)
        vboxGraph3.addLayout(hboxGraph33)
        vboxGraph3.addLayout(hboxGraph34)

        vboxGraph4 = QtWidgets.QVBoxLayout()
        vboxGraph4.addWidget(self.__line4, alignment=QtCore.Qt.AlignCenter)

        hboxGraph41 = QtWidgets.QHBoxLayout()
        hboxGraph41.addWidget(self.__title4)
        hboxGraph41.addWidget(self.__titleLineEdit4)

        hboxGraph42 = QtWidgets.QHBoxLayout()
        hboxGraph42.addWidget(self.__xlabel4)
        hboxGraph42.addWidget(self.__xlabelLineEdit4)

        hboxGraph43 = QtWidgets.QHBoxLayout()
        hboxGraph43.addWidget(self.__ylabel4)
        hboxGraph43.addWidget(self.__ylabelLineEdit4)

        hboxGraph44 = QtWidgets.QHBoxLayout()
        hboxGraph44.addWidget(self.__path4)
        hboxGraph44.addWidget(self.__pathLineEdit4)
        hboxGraph44.addWidget(self.__pathButton4)

        vboxGraph4.addLayout(hboxGraph41)
        vboxGraph4.addLayout(hboxGraph42)
        vboxGraph4.addLayout(hboxGraph43)
        vboxGraph4.addLayout(hboxGraph44)

        vboxMain = QtWidgets.QVBoxLayout()
        vboxMain.addWidget(label, alignment=QtCore.Qt.AlignCenter)
        vboxMain.addLayout(hbox1)
        vboxMain.addLayout(hbox2)
        vboxMain.addStretch()
        vboxMain.addLayout(vboxGraph1)
        vboxMain.addLayout(vboxGraph2)
        vboxMain.addLayout(vboxGraph3)
        vboxMain.addLayout(vboxGraph4)
        vboxMain.addStretch()
        vboxMain.addLayout(hbox3)
        vboxMain.addLayout(hbox4)

        self.setLayout(vboxMain)

        self.__hide(self.__widgets1)
        self.__hide(self.__widgets2)
        self.__hide(self.__widgets3)
        self.__hide(self.__widgets4)
        self.__hide([self.okayButton])

        applyButton.clicked.connect(self.__display_graphs)

        self.__pathButton1.clicked.connect(lambda: self.__path_finder(1))
        self.__pathButton2.clicked.connect(lambda: self.__path_finder(2))
        self.__pathButton3.clicked.connect(lambda: self.__path_finder(3))
        self.__pathButton4.clicked.connect(lambda: self.__path_finder(4))

    def __center(self):
        window = self.frameGeometry()
        self.__centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        self.__centerPoint.setY(self.__centerPoint.y() - 300)
        window.moveCenter(self.__centerPoint)
        self.move(window.topLeft())

    def __create_graph(self, i):
        line = QtWidgets.QLabel("Graph {}".format(str(i)))

        title = QtWidgets.QLabel("Title:    ")
        titleLineEdit = QtWidgets.QLineEdit()

        xlabel = QtWidgets.QLabel("X Label:")
        xlabelLineEdit = QtWidgets.QLineEdit()

        ylabel = QtWidgets.QLabel("Y Label:")
        ylabelLineEdit = QtWidgets.QLineEdit()

        path = QtWidgets.QLabel("Path:    ")
        pathLineEdit = QtWidgets.QLineEdit()
        pathButton = QtWidgets.QPushButton()

        lst = [line, title, titleLineEdit, xlabel, xlabelLineEdit,
               ylabel, ylabelLineEdit, path, pathLineEdit, pathButton]

        return lst

    def __hide(self, widgets):
        for widget in widgets:
            widget.setHidden(True)

    def __display(self, widgets):
        for widget in widgets:
            widget.setHidden(False)

    def __display_graphs(self):
        self.setMaximumSize(320, 90)

        self.__hide(self.__widgets1)
        self.__hide(self.__widgets2)
        self.__hide(self.__widgets3)
        self.__hide(self.__widgets4)

        self.__numberOfGraphs = int(self.__combo.currentText())

        if self.__numberOfGraphs == 1:
            self.__display(self.__widgets1)

        elif self.__numberOfGraphs == 2:
            self.__display(self.__widgets1)
            self.__display(self.__widgets2)

        elif self.__numberOfGraphs == 3:
            self.__display(self.__widgets1)
            self.__display(self.__widgets2)
            self.__display(self.__widgets3)

        else:
            self.__display(self.__widgets1)
            self.__display(self.__widgets2)
            self.__display(self.__widgets3)
            self.__display(self.__widgets4)

        self.__display([self.okayButton])

    def __path_finder(self, i):
        filt = "Database File (*.db)"
        dbFile = QtGui.QFileDialog.getOpenFileName(self, "Database File",
                                                   r"C:\Users\LENOVO\Desktop",
                                                   filt)
        dbPath = dbFile[0]

        if i == 1:
            self.__pathLineEdit1.setText(dbPath)
        elif i == 2:
            self.__pathLineEdit2.setText(dbPath)
        elif i == 3:
            self.__pathLineEdit3.setText(dbPath)
        else:
            self.__pathLineEdit4.setText(dbPath)

    def __check(self, currentTexts):
        check = True
        for i in range(self.__numberOfGraphs):
            if currentTexts[i][-1][-3:] != ".db":
                check = False

        return check

    def get_currentTexts(self):
        titleLineEdit1 = self.__titleLineEdit1.text()
        xlabelLineEdit1 = self.__xlabelLineEdit1.text()
        ylabelLineEdit1 = self.__ylabelLineEdit1.text()
        pathLineEdit1 = self.__pathLineEdit1.text()

        graph1Texts = [titleLineEdit1, xlabelLineEdit1, ylabelLineEdit1, pathLineEdit1]

        titleLineEdit2 = self.__titleLineEdit2.text()
        xlabelLineEdit2 = self.__xlabelLineEdit2.text()
        ylabelLineEdit2 = self.__ylabelLineEdit2.text()
        pathLineEdit2 = self.__pathLineEdit2.text()

        graph2Texts = [titleLineEdit2, xlabelLineEdit2, ylabelLineEdit2, pathLineEdit2]

        titleLineEdit3 = self.__titleLineEdit3.text()
        xlabelLineEdit3 = self.__xlabelLineEdit3.text()
        ylabelLineEdit3 = self.__ylabelLineEdit3.text()
        pathLineEdit3 = self.__pathLineEdit3.text()

        graph3Texts = [titleLineEdit3, xlabelLineEdit3, ylabelLineEdit3, pathLineEdit3]

        titleLineEdit4 = self.__titleLineEdit4.text()
        xlabelLineEdit4 = self.__xlabelLineEdit4.text()
        ylabelLineEdit4 = self.__ylabelLineEdit4.text()
        pathLineEdit4 = self.__pathLineEdit4.text()

        graph4Texts = [titleLineEdit4, xlabelLineEdit4, ylabelLineEdit4, pathLineEdit4]

        texts = [graph1Texts, graph2Texts, graph3Texts, graph4Texts]
        check = self.__check(texts)

        if check:
            return True, texts, self.__numberOfGraphs

        else:
            self.__error_msg()
            return False, None, None

    def __error_msg(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText("Database path is invalid!")
        msg.setWindowTitle("Path Error")
        msg.exec_()


class MainWindow(QtWidgets.QWidget):
    def __init__(self, currentTexts, currentTexts2, numberOfGraphs):
        super().__init__()

        self.__currentTexts = currentTexts
        self.__currentTexts2 = currentTexts2
        self.__numberOfGraphs = numberOfGraphs

        if self.__currentTexts2 is None:
            self.setWindowTitle("Live Plotter")
            self.setGeometry(0, 0, 1200, 800)
            self.__center()
            self.__init_mainUI()

        else:
            if self.__numberOfGraphs == 1:
                self.__conn1 = sqlite3.connect(currentTexts[0][3])

            elif self.__numberOfGraphs == 2:
                self.__conn1 = sqlite3.connect(currentTexts[0][3])
                self.__conn2 = sqlite3.connect(currentTexts[1][3])

            elif self.__numberOfGraphs == 3:
                self.__conn1 = sqlite3.connect(currentTexts[0][3])
                self.__conn2 = sqlite3.connect(currentTexts[1][3])
                self.__conn3 = sqlite3.connect(currentTexts[2][3])

            else:
                self.__conn1 = sqlite3.connect(currentTexts[0][3])
                self.__conn2 = sqlite3.connect(currentTexts[1][3])
                self.__conn3 = sqlite3.connect(currentTexts[2][3])
                self.__conn4 = sqlite3.connect(currentTexts[3][3])

            self.setWindowTitle("Live Plotter")
            self.setGeometry(0, 0, 1200, 800)
            self.__center()
            self.__init_mainUI()

            self.__timer = QtCore.QTimer()
            self.__timer.setInterval(1000)
            self.__pen = pg.mkPen(color=(0, 0, 0), width=1.5)

    def __init_mainUI(self):
        plot = QtWidgets.QPushButton('Plot')
        pause = QtWidgets.QPushButton('Pause')
        exit = QtWidgets.QPushButton('Exit')

        self.__frequency = QtWidgets.QComboBox()
        self.__frequency.addItems(['0.5', '1', '2'])
        self.__dataInFrame = QtWidgets.QComboBox()
        self.__dataInFrame.addItems(['25', '50', '75', '100'])

        line1 = QtWidgets.QLabel("Frequency (Hz):")
        line2 = QtWidgets.QLabel("    # of data in a frame:")

        styles = {'color': 'b', 'font-size': '12px'}

        self.__graphWidget1 = pg.PlotWidget()
        self.__graphWidget1.setBackground('w')
        self.__graphWidget1.setTitle(self.__currentTexts[0][0])
        self.__graphWidget1.setLabel('bottom', self.__currentTexts[0][1], **styles)
        self.__graphWidget1.setLabel('left', self.__currentTexts[0][2], **styles)
        self.__graphWidget1.showGrid(x=True, y=True)

        self.__graphWidget2 = pg.PlotWidget()
        self.__graphWidget2.setBackground('w')
        self.__graphWidget2.setTitle(self.__currentTexts[1][0])
        self.__graphWidget2.setLabel('bottom', self.__currentTexts[1][1], **styles)
        self.__graphWidget2.setLabel('left', self.__currentTexts[1][2], **styles)
        self.__graphWidget2.showGrid(x=True, y=True)

        self.__graphWidget3 = pg.PlotWidget()
        self.__graphWidget3.setBackground('w')
        self.__graphWidget3.setTitle(self.__currentTexts[2][0])
        self.__graphWidget3.setLabel('bottom', self.__currentTexts[2][1], **styles)
        self.__graphWidget3.setLabel('left', self.__currentTexts[2][2], **styles)
        self.__graphWidget3.showGrid(x=True, y=True)

        self.__graphWidget4 = pg.PlotWidget()
        self.__graphWidget4.setBackground('w')
        self.__graphWidget4.setTitle(self.__currentTexts[3][0])
        self.__graphWidget4.setLabel('bottom', self.__currentTexts[3][1], **styles)
        self.__graphWidget4.setLabel('left', self.__currentTexts[3][2], **styles)
        self.__graphWidget4.showGrid(x=True, y=True)

        self.__graphWidgets = [self.__graphWidget1, self.__graphWidget2,
                               self.__graphWidget3, self.__graphWidget4]

        hbox1 = QtWidgets.QHBoxLayout()
        hbox1.addWidget(self.__graphWidget1)
        hbox1.addWidget(self.__graphWidget2)

        hbox2 = QtWidgets.QHBoxLayout()
        hbox2.addWidget(self.__graphWidget3)
        hbox2.addWidget(self.__graphWidget4)

        hbox3 = QtWidgets.QHBoxLayout()
        hbox3.addWidget(line1, alignment=QtCore.Qt.AlignBottom)
        hbox3.addWidget(self.__frequency, alignment=QtCore.Qt.AlignBottom)
        hbox3.addWidget(line2, alignment=QtCore.Qt.AlignBottom)
        hbox3.addWidget(self.__dataInFrame, alignment=QtCore.Qt.AlignBottom)
        hbox3.addStretch()
        hbox3.addWidget(plot, alignment=QtCore.Qt.AlignBottom)
        hbox3.addWidget(pause, alignment=QtCore.Qt.AlignBottom)
        hbox3.addWidget(exit, alignment=QtCore.Qt.AlignBottom)

        vbox = QtWidgets.QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)

        self.setLayout(vbox)

        self.__hide(self.__graphWidgets)

        plot.clicked.connect(self.__display_graphs)
        plot.clicked.connect(self.__timer)
        pause.clicked.connect(self.__pause)
        exit.clicked.connect(self.__exit)

    def __center(self):
        window = self.frameGeometry()
        self.__centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        self.__centerPoint.setY(self.__centerPoint.y())
        window.moveCenter(self.__centerPoint)
        self.move(window.topLeft())

    def __timer(self):
        self.__timer.timeout.connect(self.__plot)
        self.__timer.start()

    def __plot(self):
        interval = (1 / (float(self.__frequency.currentText()))) * 1000
        self.__timer.setInterval(round(interval))

        if self.__numberOfGraphs == 1:
            cursor1 = self.__conn1.cursor()
            query1 = """SELECT {},{} FROM {} ORDER BY {} DESC LIMIT {}""".format(
                self.__currentTexts2[0][2], self.__currentTexts2[0][3],
                self.__currentTexts2[0][0], self.__currentTexts2[0][1],
                self.__dataInFrame.currentText()
            )
            cursor1.execute(query1)
            data1 = cursor1.fetchall()

            xs1, ys1 = list(), list()
            for x1, y1 in data1:
                xs1.append(x1)
                ys1.append(y1)

            self.__graphWidget1.clear()
            self.__graphWidget1.plot(xs1, ys1, pen=self.__pen)

        elif self.__numberOfGraphs == 2:
            cursor1 = self.__conn1.cursor()
            cursor2 = self.__conn2.cursor()

            query1 = """SELECT {},{} FROM {} ORDER BY {} DESC LIMIT {}""".format(
                self.__currentTexts2[0][2], self.__currentTexts2[0][3],
                self.__currentTexts2[0][0], self.__currentTexts2[0][1],
                self.__dataInFrame.currentText()
            )

            query2 = """SELECT {},{} FROM {} ORDER BY {} DESC LIMIT {}""".format(
                self.__currentTexts2[1][2], self.__currentTexts2[1][3],
                self.__currentTexts2[1][0], self.__currentTexts2[1][1],
                self.__dataInFrame.currentText()
            )

            cursor1.execute(query1)
            cursor2.execute(query2)
            data1 = cursor1.fetchall()
            data2 = cursor2.fetchall()

            xs1, ys1 = list(), list()
            for x1, y1 in data1:
                xs1.append(x1)
                ys1.append(y1)

            xs2, ys2 = list(), list()
            for x2, y2 in data2:
                xs2.append(x2)
                ys2.append(y2)

            self.__graphWidget1.clear()
            self.__graphWidget2.clear()

            self.__graphWidget1.plot(xs1, ys1, pen=self.__pen)
            self.__graphWidget2.plot(xs2, ys2, pen=self.__pen)

        elif self.__numberOfGraphs == 3:
            cursor1 = self.__conn1.cursor()
            cursor2 = self.__conn2.cursor()
            cursor3 = self.__conn3.cursor()

            query1 = """SELECT {},{} FROM {} ORDER BY {} DESC LIMIT {}""".format(
                self.__currentTexts2[0][2], self.__currentTexts2[0][3],
                self.__currentTexts2[0][0], self.__currentTexts2[0][1],
                self.__dataInFrame.currentText()
            )

            query2 = """SELECT {},{} FROM {} ORDER BY {} DESC LIMIT {}""".format(
                self.__currentTexts2[1][2], self.__currentTexts2[1][3],
                self.__currentTexts2[1][0], self.__currentTexts2[1][1],
                self.__dataInFrame.currentText()
            )

            query3 = """SELECT {},{} FROM {} ORDER BY {} DESC LIMIT {}""".format(
                self.__currentTexts2[2][2], self.__currentTexts2[2][3],
                self.__currentTexts2[2][0], self.__currentTexts2[2][1],
                self.__dataInFrame.currentText()
            )

            cursor1.execute(query1)
            cursor2.execute(query2)
            cursor3.execute(query3)
            data1 = cursor1.fetchall()
            data2 = cursor2.fetchall()
            data3 = cursor3.fetchall()

            xs1, ys1 = list(), list()
            for x1, y1 in data1:
                xs1.append(x1)
                ys1.append(y1)

            xs2, ys2 = list(), list()
            for x2, y2 in data2:
                xs2.append(x2)
                ys2.append(y2)

            xs3, ys3 = list(), list()
            for x3, y3 in data3:
                xs3.append(x3)
                ys3.append(y3)

            self.__graphWidget1.clear()
            self.__graphWidget2.clear()
            self.__graphWidget3.clear()

            self.__graphWidget1.plot(xs1, ys1, pen=self.__pen)
            self.__graphWidget2.plot(xs2, ys2, pen=self.__pen)
            self.__graphWidget3.plot(xs3, ys3, pen=self.__pen)

        else:
            cursor1 = self.__conn1.cursor()
            cursor2 = self.__conn2.cursor()
            cursor3 = self.__conn3.cursor()
            cursor4 = self.__conn4.cursor()

            query1 = """SELECT {},{} FROM {} ORDER BY {} DESC LIMIT {}""".format(
                self.__currentTexts2[0][2], self.__currentTexts2[0][3],
                self.__currentTexts2[0][0], self.__currentTexts2[0][1],
                self.__dataInFrame.currentText()
            )

            query2 = """SELECT {},{} FROM {} ORDER BY {} DESC LIMIT {}""".format(
                self.__currentTexts2[1][2], self.__currentTexts2[1][3],
                self.__currentTexts2[1][0], self.__currentTexts2[1][1],
                self.__dataInFrame.currentText()
            )

            query3 = """SELECT {},{} FROM {} ORDER BY {} DESC LIMIT {}""".format(
                self.__currentTexts2[2][2], self.__currentTexts2[2][3],
                self.__currentTexts2[2][0], self.__currentTexts2[2][1],
                self.__dataInFrame.currentText()
            )

            query4 = """SELECT {},{} FROM {} ORDER BY {} DESC LIMIT {}""".format(
                self.__currentTexts2[3][2], self.__currentTexts2[3][3],
                self.__currentTexts2[3][0], self.__currentTexts2[3][1],
                self.__dataInFrame.currentText()
            )

            cursor1.execute(query1)
            cursor2.execute(query2)
            cursor3.execute(query3)
            cursor4.execute(query4)
            data1 = cursor1.fetchall()
            data2 = cursor2.fetchall()
            data3 = cursor3.fetchall()
            data4 = cursor4.fetchall()

            xs1, ys1 = list(), list()
            for x1, y1 in data1:
                xs1.append(x1)
                ys1.append(y1)

            xs2, ys2 = list(), list()
            for x2, y2 in data2:
                xs2.append(x2)
                ys2.append(y2)

            xs3, ys3 = list(), list()
            for x3, y3 in data3:
                xs3.append(x3)
                ys3.append(y3)

            xs4, ys4 = list(), list()
            for x4, y4 in data1:
                xs4.append(x4)
                ys4.append(y4)

            self.__graphWidget1.clear()
            self.__graphWidget2.clear()
            self.__graphWidget3.clear()
            self.__graphWidget4.clear()

            self.__graphWidget1.plot(xs1, ys1, pen=self.__pen)
            self.__graphWidget2.plot(xs2, ys2, pen=self.__pen)
            self.__graphWidget3.plot(xs3, ys3, pen=self.__pen)
            self.__graphWidget4.plot(xs4, ys4, pen=self.__pen)

    def __pause(self):
        self.__timer.stop()

    def __exit(self):
        if self.__numberOfGraphs == 1:
            self.__conn1.close()

        elif self.__numberOfGraphs == 2:
            self.__conn1.close()
            self.__conn2.close()

        elif self.__numberOfGraphs == 3:
            self.__conn1.close()
            self.__conn2.close()
            self.__conn3.close()

        else:
            self.__conn1.close()
            self.__conn2.close()
            self.__conn3.close()
            self.__conn4.close()

        self.close()

    def __hide(self, widgets):
        for widget in widgets:
            widget.setHidden(True)

    def __display(self, widgets):
        for widget in widgets:
            widget.setHidden(False)

    def __display_graphs(self):
        self.__hide(self.__graphWidgets)

        if self.__numberOfGraphs == 1:
            self.__display([self.__graphWidget1])

        elif self.__numberOfGraphs == 2:
            self.__display([self.__graphWidget1])
            self.__display([self.__graphWidget2])

        elif self.__numberOfGraphs == 3:
            self.__display([self.__graphWidget1])
            self.__display([self.__graphWidget2])
            self.__display([self.__graphWidget3])

        else:
            self.__display([self.__graphWidget1])
            self.__display([self.__graphWidget2])
            self.__display([self.__graphWidget3])
            self.__display([self.__graphWidget4])

    def __error_msg(self, title, message):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle(title)
        msg.exec_()


class InterWindow(QtWidgets.QWidget):
    def __init__(self, currentTexts, numberOfGraphs):
        super().__init__()

        self.__numberOfGraphs = numberOfGraphs
        self.__currentTexts = currentTexts

        self.setWindowTitle("DB Settings")
        self.__init_interUI()

    def __init_interUI(self):
        self.okayButton2 = QtWidgets.QPushButton("Okay")

        self.__db1 = QtWidgets.QLabel("Database 1")
        self.__table1Line = QtWidgets.QLabel("Table:")
        self.__table1 = QtWidgets.QComboBox()
        self.__id1Line = QtWidgets.QLabel("ID:")
        self.__id1 = QtWidgets.QComboBox()
        self.__x1Line = QtWidgets.QLabel("X:")
        self.__x1 = QtWidgets.QComboBox()
        self.__y1Line = QtWidgets.QLabel("Y:")
        self.__y1 = QtWidgets.QComboBox()

        self.__widgets1 = [self.__db1, self.__table1, self.__table1Line, self.__id1,
                           self.__id1Line, self.__x1, self.__x1Line, self.__y1, self.__y1Line]

        hbox11 = QtWidgets.QHBoxLayout()
        hbox11.addWidget(self.__table1Line)
        hbox11.addWidget(self.__table1)

        hbox12 = QtWidgets.QHBoxLayout()
        hbox12.addWidget(self.__id1Line)
        hbox12.addWidget(self.__id1)

        hbox13 = QtWidgets.QHBoxLayout()
        hbox13.addWidget(self.__x1Line)
        hbox13.addWidget(self.__x1)

        hbox14 = QtWidgets.QHBoxLayout()
        hbox14.addWidget(self.__y1Line)
        hbox14.addWidget(self.__y1)

        vbox1 = QtWidgets.QVBoxLayout()
        vbox1.addWidget(self.__db1, alignment=QtCore.Qt.AlignCenter)
        vbox1.addLayout(hbox11)
        vbox1.addLayout(hbox12)
        vbox1.addLayout(hbox13)
        vbox1.addLayout(hbox14)

        self.__db2 = QtWidgets.QLabel("Database 2")
        self.__table2Line = QtWidgets.QLabel("Table:")
        self.__table2 = QtWidgets.QComboBox()
        self.__id2Line = QtWidgets.QLabel("ID:")
        self.__id2 = QtWidgets.QComboBox()
        self.__x2Line = QtWidgets.QLabel("X:")
        self.__x2 = QtWidgets.QComboBox()
        self.__y2Line = QtWidgets.QLabel("Y:")
        self.__y2 = QtWidgets.QComboBox()

        self.__widgets2 = [self.__db2, self.__table2, self.__table2Line, self.__id2,
                           self.__id2Line, self.__x2, self.__x2Line, self.__y2, self.__y2Line]

        hbox21 = QtWidgets.QHBoxLayout()
        hbox21.addWidget(self.__table2Line)
        hbox21.addWidget(self.__table2)

        hbox22 = QtWidgets.QHBoxLayout()
        hbox22.addWidget(self.__id2Line)
        hbox22.addWidget(self.__id2)

        hbox23 = QtWidgets.QHBoxLayout()
        hbox23.addWidget(self.__x2Line)
        hbox23.addWidget(self.__x2)

        hbox24 = QtWidgets.QHBoxLayout()
        hbox24.addWidget(self.__y2Line)
        hbox24.addWidget(self.__y2)

        vbox2 = QtWidgets.QVBoxLayout()
        vbox2.addWidget(self.__db2, alignment=QtCore.Qt.AlignCenter)
        vbox2.addLayout(hbox21)
        vbox2.addLayout(hbox22)
        vbox2.addLayout(hbox23)
        vbox2.addLayout(hbox24)

        self.__db3 = QtWidgets.QLabel("Database 3")
        self.__table3Line = QtWidgets.QLabel("Table:")
        self.__table3 = QtWidgets.QComboBox()
        self.__id3Line = QtWidgets.QLabel("ID:")
        self.__id3 = QtWidgets.QComboBox()
        self.__x3Line = QtWidgets.QLabel("X:")
        self.__x3 = QtWidgets.QComboBox()
        self.__y3Line = QtWidgets.QLabel("Y:")
        self.__y3 = QtWidgets.QComboBox()

        self.__widgets3 = [self.__db3, self.__table3, self.__table3Line, self.__id3,
                           self.__id3Line, self.__x3, self.__x3Line, self.__y3, self.__y3Line]

        hbox31 = QtWidgets.QHBoxLayout()
        hbox31.addWidget(self.__table3Line)
        hbox31.addWidget(self.__table3)

        hbox32 = QtWidgets.QHBoxLayout()
        hbox32.addWidget(self.__id3Line)
        hbox32.addWidget(self.__id3)

        hbox33 = QtWidgets.QHBoxLayout()
        hbox33.addWidget(self.__x3Line)
        hbox33.addWidget(self.__x3)

        hbox34 = QtWidgets.QHBoxLayout()
        hbox34.addWidget(self.__y3Line)
        hbox34.addWidget(self.__y3)

        vbox3 = QtWidgets.QVBoxLayout()
        vbox3.addWidget(self.__db3, alignment=QtCore.Qt.AlignCenter)
        vbox3.addLayout(hbox31)
        vbox3.addLayout(hbox32)
        vbox3.addLayout(hbox33)
        vbox3.addLayout(hbox34)

        self.__db4 = QtWidgets.QLabel("Database 4")
        self.__table4Line = QtWidgets.QLabel("Table:")
        self.__table4 = QtWidgets.QComboBox()
        self.__id4Line = QtWidgets.QLabel("ID:")
        self.__id4 = QtWidgets.QComboBox()
        self.__x4Line = QtWidgets.QLabel("X:")
        self.__x4 = QtWidgets.QComboBox()
        self.__y4Line = QtWidgets.QLabel("Y:")
        self.__y4 = QtWidgets.QComboBox()

        self.__widgets4 = [self.__db4, self.__table4, self.__table4Line, self.__id4,
                           self.__id4Line, self.__x4, self.__x4Line, self.__y4, self.__y4Line]

        hbox41 = QtWidgets.QHBoxLayout()
        hbox41.addWidget(self.__table4Line)
        hbox41.addWidget(self.__table4)

        hbox42 = QtWidgets.QHBoxLayout()
        hbox42.addWidget(self.__id4Line)
        hbox42.addWidget(self.__id4)

        hbox43 = QtWidgets.QHBoxLayout()
        hbox43.addWidget(self.__x4Line)
        hbox43.addWidget(self.__x4)

        hbox44 = QtWidgets.QHBoxLayout()
        hbox44.addWidget(self.__y4Line)
        hbox44.addWidget(self.__y4)

        vbox4 = QtWidgets.QVBoxLayout()
        vbox4.addWidget(self.__db4, alignment=QtCore.Qt.AlignCenter)
        vbox4.addLayout(hbox41)
        vbox4.addLayout(hbox42)
        vbox4.addLayout(hbox43)
        vbox4.addLayout(hbox44)

        self.__Widgets = [self.__widgets1, self.__widgets2,
                          self.__widgets3, self.__widgets4]

        vboxMain = QtWidgets.QVBoxLayout()
        vboxMain.addLayout(vbox1)
        vboxMain.addLayout(vbox2)
        vboxMain.addLayout(vbox3)
        vboxMain.addLayout(vbox4)
        vboxMain.addWidget(self.okayButton2, alignment=QtCore.Qt.AlignBottom)

        self.__fill_combos()
        self.setLayout(vboxMain)
        self.__display_dbs()

    def __hide(self, widgets):
        for widget in widgets:
            widget.setHidden(True)

    def __display(self, widgets):
        for widget in widgets:
            widget.setHidden(False)

    def __display_dbs(self):
        self.__hide(self.__widgets1)
        self.__hide(self.__widgets2)
        self.__hide(self.__widgets3)
        self.__hide(self.__widgets4)

        if self.__numberOfGraphs == 1:
            self.__display(self.__widgets1)

        elif self.__numberOfGraphs == 2:
            self.__display(self.__widgets1)
            self.__display(self.__widgets2)

        elif self.__numberOfGraphs == 3:
            self.__display(self.__widgets1)
            self.__display(self.__widgets2)
            self.__display(self.__widgets3)

        else:
            self.__display(self.__widgets1)
            self.__display(self.__widgets2)
            self.__display(self.__widgets3)
            self.__display(self.__widgets4)

    def __fill_combos(self):
        self.connections = [None, None, None, None]
        self.cursors = [None, None, None, None]

        for i in range(self.__numberOfGraphs):
            conn = sqlite3.connect(self.__currentTexts[i][3])
            cursor = conn.cursor()
            self.cursors[i] = cursor
            self.connections[i] = conn

            queryForTableNames = """SELECT name FROM sqlite_master WHERE type='table';"""
            cursor.execute(queryForTableNames)
            tableNames = cursor.fetchall()
            tableNames_ = list()
            for name in tableNames:
                tableNames_.append(name[0])

            self.__Widgets[i][1].addItems(tableNames_)
            self.__fill_columnNames(i)

        self.__Widgets[0][1].currentTextChanged.connect(lambda: self.__fill_columnNames(0))
        self.__Widgets[1][1].currentTextChanged.connect(lambda: self.__fill_columnNames(1))
        self.__Widgets[2][1].currentTextChanged.connect(lambda: self.__fill_columnNames(2))
        self.__Widgets[3][1].currentTextChanged.connect(lambda: self.__fill_columnNames(3))

    def __fill_columnNames(self, i):
        self.__selectedTable = self.__Widgets[i][1].currentText()

        self.__Widgets[i][3].clear()
        self.__Widgets[i][5].clear()
        self.__Widgets[i][7].clear()

        queryForColumns = "PRAGMA table_info('%s');" % self.__selectedTable
        self.cursors[i].execute(queryForColumns)
        columnNames = self.cursors[i].fetchall()
        columnNames_ = list()
        for j in columnNames:
            columnNames_.append(j[1])

        self.__Widgets[i][3].addItems(columnNames_)
        self.__Widgets[i][5].addItems(columnNames_)
        self.__Widgets[i][7].addItems(columnNames_)

    def get_currentTexts2(self):
        textTable1 = self.__Widgets[0][1].currentText()
        textId1 = self.__Widgets[0][3].currentText()
        textX1 = self.__Widgets[0][5].currentText()
        textY1 = self.__Widgets[0][7].currentText()

        textTable2 = self.__Widgets[0][1].currentText()
        textId2 = self.__Widgets[1][3].currentText()
        textX2 = self.__Widgets[1][5].currentText()
        textY2 = self.__Widgets[1][7].currentText()

        textTable3 = self.__Widgets[0][1].currentText()
        textId3 = self.__Widgets[2][3].currentText()
        textX3 = self.__Widgets[2][5].currentText()
        textY3 = self.__Widgets[2][7].currentText()

        textTable4 = self.__Widgets[0][1].currentText()
        textId4 = self.__Widgets[3][3].currentText()
        textX4 = self.__Widgets[3][5].currentText()
        textY4 = self.__Widgets[3][7].currentText()

        db1 = [textTable1, textId1, textX1, textY1]
        db2 = [textTable2, textId2, textX2, textY2]
        db3 = [textTable3, textId3, textX3, textY3]
        db4 = [textTable4, textId4, textX4, textY4]

        currentTexts2 = [db1, db2, db3, db4]
        return currentTexts2


class MainApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.__preWindow = PreWindow()
        self.__preWindow.show()
        self.__preWindow.okayButton.clicked.connect(self.__switch_ui)

    def __switch_ui(self):
        check, self.__currentTexts, self.__numberOfGraphs = self.__preWindow.get_currentTexts()
        self.__currentTexts2 = None
        if check:
            self.__preWindow.close()
            self.__mainWindow = MainWindow(self.__currentTexts, self.__currentTexts2, self.__numberOfGraphs)
            self.__mainWindow.show()

            self.__interWindow = InterWindow(self.__currentTexts, self.__numberOfGraphs)
            self.__interWindow.show()
            self.__interWindow.okayButton2.clicked.connect(self.__close_interUI)

    def __close_interUI(self):
        for i in self.__interWindow.connections:
            if i is not None:
                i.close()

        self.__currentTexts2 = self.__interWindow.get_currentTexts2()
        self.__mainWindow.close()
        self.__interWindow.close()

        self.__mainWindow = MainWindow(self.__currentTexts, self.__currentTexts2, self.__numberOfGraphs)
        self.__mainWindow.show()


app = QtWidgets.QApplication(sys.argv)
gui = MainApp()
sys.exit(app.exec_())
