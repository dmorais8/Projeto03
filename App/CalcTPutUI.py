# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CalcTPutUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(866, 624)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.outputParamsDataFrame = QtWidgets.QFrame(self.centralwidget)
        self.outputParamsDataFrame.setEnabled(True)
        self.outputParamsDataFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.outputParamsDataFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.outputParamsDataFrame.setObjectName("outputParamsDataFrame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.outputParamsDataFrame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.outputTbsIndex = QtWidgets.QLineEdit(self.outputParamsDataFrame)
        self.outputTbsIndex.setEnabled(False)
        self.outputTbsIndex.setObjectName("outputTbsIndex")
        self.gridLayout_3.addWidget(self.outputTbsIndex, 4, 1, 1, 1)
        self.ouputTbsValue = QtWidgets.QLineEdit(self.outputParamsDataFrame)
        self.ouputTbsValue.setEnabled(False)
        self.ouputTbsValue.setObjectName("ouputTbsValue")
        self.gridLayout_3.addWidget(self.ouputTbsValue, 4, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.outputParamsDataFrame)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 2, 4, 1, 2)
        self.outputPRB = QtWidgets.QLineEdit(self.outputParamsDataFrame)
        self.outputPRB.setEnabled(False)
        self.outputPRB.setObjectName("outputPRB")
        self.gridLayout_3.addWidget(self.outputPRB, 4, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.outputParamsDataFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.gridLayout_3.addWidget(self.label_17, 0, 0, 1, 1)
        self.outputNumRE = QtWidgets.QLineEdit(self.outputParamsDataFrame)
        self.outputNumRE.setEnabled(False)
        self.outputNumRE.setObjectName("outputNumRE")
        self.gridLayout_3.addWidget(self.outputNumRE, 4, 6, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.outputParamsDataFrame)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 2, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.outputParamsDataFrame)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 2, 2, 1, 2)
        self.label_15 = QtWidgets.QLabel(self.outputParamsDataFrame)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 2, 6, 1, 2)
        self.label_14 = QtWidgets.QLabel(self.outputParamsDataFrame)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 2, 1, 1, 1)
        self.outputModulacao = QtWidgets.QLineEdit(self.outputParamsDataFrame)
        self.outputModulacao.setEnabled(False)
        self.outputModulacao.setObjectName("outputModulacao")
        self.gridLayout_3.addWidget(self.outputModulacao, 4, 4, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.outputParamsDataFrame)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 2, 8, 1, 1)
        self.outputQtdSimbolos = QtWidgets.QLineEdit(self.outputParamsDataFrame)
        self.outputQtdSimbolos.setEnabled(False)
        self.outputQtdSimbolos.setObjectName("outputQtdSimbolos")
        self.gridLayout_3.addWidget(self.outputQtdSimbolos, 4, 8, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.outputParamsDataFrame)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_3.addWidget(self.line_3, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.outputParamsDataFrame, 5, 1, 1, 2)
        self.inputDataFrame = QtWidgets.QFrame(self.centralwidget)
        self.inputDataFrame.setStyleSheet("")
        self.inputDataFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.inputDataFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.inputDataFrame.setObjectName("inputDataFrame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.inputDataFrame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_5 = QtWidgets.QLabel(self.inputDataFrame)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 3, 4, 1, 1)
        self.comboBanda = QtWidgets.QComboBox(self.inputDataFrame)
        self.comboBanda.setObjectName("comboBanda")
        self.comboBanda.addItem("")
        self.comboBanda.addItem("")
        self.comboBanda.addItem("")
        self.comboBanda.addItem("")
        self.comboBanda.addItem("")
        self.comboBanda.addItem("")
        self.gridLayout_2.addWidget(self.comboBanda, 4, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.inputDataFrame)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 3, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.inputDataFrame)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 3, 6, 1, 1)
        self.comboPrefixCycle = QtWidgets.QComboBox(self.inputDataFrame)
        self.comboPrefixCycle.setObjectName("comboPrefixCycle")
        self.comboPrefixCycle.addItem("")
        self.comboPrefixCycle.addItem("")
        self.gridLayout_2.addWidget(self.comboPrefixCycle, 4, 6, 1, 1)
        self.comboMCS = QtWidgets.QComboBox(self.inputDataFrame)
        self.comboMCS.setObjectName("comboMCS")
        self.comboMCS.addItem("")
        self.comboMCS.addItem("")
        self.comboMCS.addItem("")
        self.comboMCS.addItem("")
        self.comboMCS.addItem("")
        self.comboMCS.addItem("")
        self.comboMCS.addItem("")
        self.comboMCS.addItem("")
        self.comboMCS.addItem("")
        self.comboMCS.addItem("")
        self.comboMCS.addItem("")
        self.comboMCS.addItem("")
        self.comboMCS.addItem("")
        self.comboMCS.addItem("")
        self.comboMCS.addItem("")
        self.comboMCS.addItem("")
        self.comboMCS.addItem("")
        self.comboMCS.addItem("")
        self.comboMCS.addItem("")
        self.comboMCS.addItem("")
        self.comboMCS.addItem("")
        self.comboMCS.addItem("")
        self.comboMCS.addItem("")
        self.comboMCS.addItem("")
        self.comboMCS.addItem("")
        self.comboMCS.addItem("")
        self.comboMCS.addItem("")
        self.comboMCS.addItem("")
        self.comboMCS.addItem("")
        self.gridLayout_2.addWidget(self.comboMCS, 4, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.inputDataFrame)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 3, 1, 1, 1)
        self.ComboMimo = QtWidgets.QComboBox(self.inputDataFrame)
        self.ComboMimo.setObjectName("ComboMimo")
        self.ComboMimo.addItem("")
        self.ComboMimo.addItem("")
        self.ComboMimo.addItem("")
        self.ComboMimo.addItem("")
        self.gridLayout_2.addWidget(self.ComboMimo, 4, 4, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.inputDataFrame)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 3, 8, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.inputDataFrame)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 1, 1, 1, 1)
        self.comboCarrierAgg = QtWidgets.QComboBox(self.inputDataFrame)
        self.comboCarrierAgg.setEnabled(True)
        self.comboCarrierAgg.setObjectName("comboCarrierAgg")
        self.comboCarrierAgg.addItem("")
        self.comboCarrierAgg.addItem("")
        self.comboCarrierAgg.addItem("")
        self.comboCarrierAgg.addItem("")
        self.comboCarrierAgg.addItem("")
        self.gridLayout_2.addWidget(self.comboCarrierAgg, 4, 8, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.inputDataFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.inputDataFrame, 2, 1, 2, 2)
        self.btnCalcTPut = QtWidgets.QPushButton(self.centralwidget)
        self.btnCalcTPut.setEnabled(True)
        self.btnCalcTPut.setStyleSheet("background-color: #4CAF50; /* Green */\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;")
        self.btnCalcTPut.setObjectName("btnCalcTPut")
        self.gridLayout.addWidget(self.btnCalcTPut, 8, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 12, 2, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 14, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 6, 1, 1, 2)
        self.outputEquacao = QtWidgets.QLineEdit(self.centralwidget)
        self.outputEquacao.setEnabled(False)
        self.outputEquacao.setAlignment(QtCore.Qt.AlignCenter)
        self.outputEquacao.setObjectName("outputEquacao")
        self.gridLayout.addWidget(self.outputEquacao, 13, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 2)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 9, 2, 1, 1)
        self.outputTabela = QtWidgets.QLineEdit(self.centralwidget)
        self.outputTabela.setEnabled(False)
        self.outputTabela.setStyleSheet("")
        self.outputTabela.setAlignment(QtCore.Qt.AlignCenter)
        self.outputTabela.setObjectName("outputTabela")
        self.gridLayout.addWidget(self.outputTabela, 10, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_13.setText(_translate("MainWindow", "Modulacao"))
        self.label_17.setText(_translate("MainWindow", "Parametros de Saida"))
        self.label_11.setText(_translate("MainWindow", "PRB"))
        self.label_12.setText(_translate("MainWindow", "Valor TBS"))
        self.label_15.setText(_translate("MainWindow", "N RE"))
        self.label_14.setText(_translate("MainWindow", "TBS Index"))
        self.label_16.setText(_translate("MainWindow", "Qtd. Simbolos"))
        self.label_5.setText(_translate("MainWindow", "Mimo"))
        self.comboBanda.setItemText(0, _translate("MainWindow", "1.4"))
        self.comboBanda.setItemText(1, _translate("MainWindow", "3"))
        self.comboBanda.setItemText(2, _translate("MainWindow", "5"))
        self.comboBanda.setItemText(3, _translate("MainWindow", "10"))
        self.comboBanda.setItemText(4, _translate("MainWindow", "15"))
        self.comboBanda.setItemText(5, _translate("MainWindow", "20"))
        self.label_3.setText(_translate("MainWindow", "MCS"))
        self.label_2.setText(_translate("MainWindow", "CP"))
        self.comboPrefixCycle.setItemText(0, _translate("MainWindow", "Normal"))
        self.comboPrefixCycle.setItemText(1, _translate("MainWindow", "Extendido"))
        self.comboMCS.setItemText(0, _translate("MainWindow", "0"))
        self.comboMCS.setItemText(1, _translate("MainWindow", "1"))
        self.comboMCS.setItemText(2, _translate("MainWindow", "2"))
        self.comboMCS.setItemText(3, _translate("MainWindow", "3"))
        self.comboMCS.setItemText(4, _translate("MainWindow", "4"))
        self.comboMCS.setItemText(5, _translate("MainWindow", "5"))
        self.comboMCS.setItemText(6, _translate("MainWindow", "6"))
        self.comboMCS.setItemText(7, _translate("MainWindow", "7"))
        self.comboMCS.setItemText(8, _translate("MainWindow", "8"))
        self.comboMCS.setItemText(9, _translate("MainWindow", "9"))
        self.comboMCS.setItemText(10, _translate("MainWindow", "10"))
        self.comboMCS.setItemText(11, _translate("MainWindow", "11"))
        self.comboMCS.setItemText(12, _translate("MainWindow", "12"))
        self.comboMCS.setItemText(13, _translate("MainWindow", "13"))
        self.comboMCS.setItemText(14, _translate("MainWindow", "14"))
        self.comboMCS.setItemText(15, _translate("MainWindow", "15"))
        self.comboMCS.setItemText(16, _translate("MainWindow", "16"))
        self.comboMCS.setItemText(17, _translate("MainWindow", "17"))
        self.comboMCS.setItemText(18, _translate("MainWindow", "18"))
        self.comboMCS.setItemText(19, _translate("MainWindow", "19"))
        self.comboMCS.setItemText(20, _translate("MainWindow", "20"))
        self.comboMCS.setItemText(21, _translate("MainWindow", "21"))
        self.comboMCS.setItemText(22, _translate("MainWindow", "22"))
        self.comboMCS.setItemText(23, _translate("MainWindow", "23"))
        self.comboMCS.setItemText(24, _translate("MainWindow", "24"))
        self.comboMCS.setItemText(25, _translate("MainWindow", "25"))
        self.comboMCS.setItemText(26, _translate("MainWindow", "26"))
        self.comboMCS.setItemText(27, _translate("MainWindow", "27"))
        self.comboMCS.setItemText(28, _translate("MainWindow", "28"))
        self.label_4.setText(_translate("MainWindow", "Banda (MHz)"))
        self.ComboMimo.setItemText(0, _translate("MainWindow", "1"))
        self.ComboMimo.setItemText(1, _translate("MainWindow", "2"))
        self.ComboMimo.setItemText(2, _translate("MainWindow", "4"))
        self.ComboMimo.setItemText(3, _translate("MainWindow", "8"))
        self.label_6.setText(_translate("MainWindow", "CA"))
        self.comboCarrierAgg.setItemText(0, _translate("MainWindow", "1"))
        self.comboCarrierAgg.setItemText(1, _translate("MainWindow", "2"))
        self.comboCarrierAgg.setItemText(2, _translate("MainWindow", "3"))
        self.comboCarrierAgg.setItemText(3, _translate("MainWindow", "4"))
        self.comboCarrierAgg.setItemText(4, _translate("MainWindow", "5"))
        self.label_9.setText(_translate("MainWindow", "Parametros de Entrada"))
        self.btnCalcTPut.setText(_translate("MainWindow", "Calcular"))
        self.label_8.setText(_translate("MainWindow", "Equacao"))
        self.label_10.setText(_translate("MainWindow", "Taxa de Transmisao LTE Release 10"))
        self.label.setText(_translate("MainWindow", "Calculadora LTE"))
        self.label_7.setText(_translate("MainWindow", "Tabela"))
