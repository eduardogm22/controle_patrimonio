# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\IP\Documents\GitHub\controle_patrimonio\PATP\bckp\asset_ctrl\templates\interfaces\interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 801)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 801))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 801))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        MainWindow.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/server.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(1200, 900))
        self.centralwidget.setStyleSheet("*{\n"
"    color:#000;\n"
"    border:none;\n"
"}\n"
"#leftMenu{\n"
"    background-color: rgb(220, 220, 220)\n"
"\n"
"}\n"
"#mainBody{\n"
"    background-color:transparent;\n"
"}\n"
"\n"
"QLineEdit{\n"
"    background-color:transparent;\n"
"}\n"
"#searchFrame{\n"
"    border-radius:10px;\n"
"    border:2px solid rgb(15, 152, 0);\n"
"}\n"
"#cardFrame>QFrame{\n"
"    background-color:white;\n"
"}\n"
"#menuBottom>QPushButton{\n"
"    margin:15px;\n"
"}\n"
"#menuFrame>QPushButton{\n"
"    margin:15px;\n"
"}\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftMenu = QtWidgets.QWidget(self.centralwidget)
        self.leftMenu.setMaximumSize(QtCore.QSize(210, 16777215))
        self.leftMenu.setStyleSheet("background-color: #057A3A;\n"
"    border-top-right-radius: 15px;  \n"
"    border-bottom-right-radius: 15px;")
        self.leftMenu.setObjectName("leftMenu")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.leftMenu)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.menuFrame = QtWidgets.QFrame(self.leftMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuFrame.sizePolicy().hasHeightForWidth())
        self.menuFrame.setSizePolicy(sizePolicy)
        self.menuFrame.setMinimumSize(QtCore.QSize(0, 0))
        self.menuFrame.setSizeIncrement(QtCore.QSize(0, 0))
        self.menuFrame.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.menuFrame.setStyleSheet("")
        self.menuFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menuFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menuFrame.setObjectName("menuFrame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.menuFrame)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.relBtn = QtWidgets.QPushButton(self.menuFrame)
        self.relBtn.setMaximumSize(QtCore.QSize(120, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.relBtn.setFont(font)
        self.relBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.relBtn.setStyleSheet("QPushButton { color:rgb(254, 253, 247);\n"
"    border-radius:10px;    \n"
" }\n"
"\n"
"QPushButton:pressed{\n"
" padding-left: 5px;\n"
" padding-top:5px;\n"
" \n"
"    background-color: rgb(0, 85, 0);\n"
" \n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/file-text.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.relBtn.setIcon(icon1)
        self.relBtn.setObjectName("relBtn")
        self.verticalLayout_7.addWidget(self.relBtn)
        self.usersBtn = QtWidgets.QPushButton(self.menuFrame)
        self.usersBtn.setMinimumSize(QtCore.QSize(0, 45))
        self.usersBtn.setMaximumSize(QtCore.QSize(120, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.usersBtn.setFont(font)
        self.usersBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.usersBtn.setStyleSheet("QPushButton { color:rgb(254, 253, 247);\n"
"    border-radius:10px;    \n"
" }\n"
"\n"
"QPushButton:pressed{\n"
" padding-left: 5px;\n"
" padding-top:5px;\n"
" \n"
"    background-color: rgb(0, 85, 0);\n"
" \n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/users.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.usersBtn.setIcon(icon2)
        self.usersBtn.setObjectName("usersBtn")
        self.verticalLayout_7.addWidget(self.usersBtn)
        self.bagBtn = QtWidgets.QPushButton(self.menuFrame)
        self.bagBtn.setMaximumSize(QtCore.QSize(120, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bagBtn.setFont(font)
        self.bagBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bagBtn.setStyleSheet("QPushButton { color:rgb(254, 253, 247);\n"
"    border-radius:10px;    \n"
" }\n"
"\n"
"\n"
"QPushButton:pressed{\n"
" padding-left: 5px;\n"
" padding-top:5px;\n"
" \n"
"    background-color: rgb(0, 85, 0);\n"
" \n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/shopping-bag.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bagBtn.setIcon(icon3)
        self.bagBtn.setObjectName("bagBtn")
        self.verticalLayout_7.addWidget(self.bagBtn)
        self.logBtn = QtWidgets.QPushButton(self.menuFrame)
        self.logBtn.setMaximumSize(QtCore.QSize(120, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.logBtn.setFont(font)
        self.logBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.logBtn.setStyleSheet("QPushButton { color:rgb(254, 253, 247);\n"
"    border-radius:10px;    \n"
" }\n"
"\n"
"\n"
"QPushButton:pressed{\n"
" padding-left: 5px;\n"
" padding-top:5px;\n"
" \n"
"    background-color: rgb(0, 85, 0);\n"
" \n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/activity.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logBtn.setIcon(icon4)
        self.logBtn.setObjectName("logBtn")
        self.verticalLayout_7.addWidget(self.logBtn)
        self.bckpBtn = QtWidgets.QPushButton(self.menuFrame)
        self.bckpBtn.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bckpBtn.setFont(font)
        self.bckpBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bckpBtn.setMouseTracking(False)
        self.bckpBtn.setStyleSheet("QPushButton { color:rgb(254, 253, 247);\n"
"    border-radius:10px;    \n"
" }\n"
"\n"
"\n"
"QPushButton:pressed{\n"
" padding-left: 5px;\n"
" padding-top:5px;\n"
" \n"
"    background-color: rgb(0, 85, 0);\n"
" \n"
"}")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/save.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bckpBtn.setIcon(icon5)
        self.bckpBtn.setObjectName("bckpBtn")
        self.verticalLayout_7.addWidget(self.bckpBtn)
        self.verticalLayout_6.addWidget(self.menuFrame, 0, QtCore.Qt.AlignTop)
        self.menuBottom = QtWidgets.QFrame(self.leftMenu)
        self.menuBottom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menuBottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menuBottom.setObjectName("menuBottom")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.menuBottom)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.helpBtn = QtWidgets.QPushButton(self.menuBottom)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.helpBtn.setFont(font)
        self.helpBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.helpBtn.setStyleSheet("QPushButton { color:rgb(254, 253, 247);\n"
"    border-radius:10px;    \n"
" }\n"
"\n"
"QPushButton:pressed{\n"
" padding-left: 5px;\n"
" padding-top:5px;\n"
" \n"
"    background-color: rgb(0, 85, 0);\n"
" \n"
"}")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/help-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.helpBtn.setIcon(icon6)
        self.helpBtn.setObjectName("helpBtn")
        self.verticalLayout_11.addWidget(self.helpBtn)
        self.docBtn = QtWidgets.QPushButton(self.menuBottom)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.docBtn.setFont(font)
        self.docBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.docBtn.setStyleSheet("QPushButton { color:rgb(254, 253, 247);\n"
"    border-radius:10px;    \n"
" }\n"
"\n"
"\n"
"QPushButton:pressed{\n"
" padding-left: 5px;\n"
" padding-top:5px;\n"
" \n"
"    background-color: rgb(0, 85, 0);\n"
" \n"
"}")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/link.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.docBtn.setIcon(icon7)
        self.docBtn.setObjectName("docBtn")
        self.verticalLayout_11.addWidget(self.docBtn)
        self.verticalLayout_6.addWidget(self.menuBottom, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout.addWidget(self.leftMenu)
        self.mainBody = QtWidgets.QWidget(self.centralwidget)
        self.mainBody.setObjectName("mainBody")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainBody)
        self.verticalLayout.setObjectName("verticalLayout")
        self.headerFrame = QtWidgets.QWidget(self.mainBody)
        self.headerFrame.setMinimumSize(QtCore.QSize(0, 45))
        self.headerFrame.setMaximumSize(QtCore.QSize(16777215, 45))
        self.headerFrame.setStyleSheet("background-color:#057a3a;\n"
"border-radius: 9px;\n"
"color:white;")
        self.headerFrame.setObjectName("headerFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.headerFrame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnHome = QtWidgets.QWidget(self.headerFrame)
        self.btnHome.setStyleSheet("border-bottom: none\n"
"")
        self.btnHome.setObjectName("btnHome")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.btnHome)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.homeBtn = QtWidgets.QPushButton(self.btnHome)
        self.homeBtn.setMinimumSize(QtCore.QSize(33, 33))
        self.homeBtn.setMaximumSize(QtCore.QSize(120, 120))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.homeBtn.setFont(font)
        self.homeBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.homeBtn.setStyleSheet("border-bottom: none\n"
"")
        self.homeBtn.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/home.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.homeBtn.setIcon(icon8)
        self.homeBtn.setIconSize(QtCore.QSize(33, 33))
        self.homeBtn.setObjectName("homeBtn")
        self.horizontalLayout_11.addWidget(self.homeBtn, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2.addWidget(self.btnHome, 0, QtCore.Qt.AlignHCenter)
        self.frame_6 = QtWidgets.QFrame(self.headerFrame)
        self.frame_6.setMinimumSize(QtCore.QSize(690, 0))
        self.frame_6.setStyleSheet("border-bottom: none\n"
"")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_2.addWidget(self.frame_6)
        self.btnAccount = QtWidgets.QWidget(self.headerFrame)
        self.btnAccount.setStyleSheet("margin-right:15px;\n"
"border-bottom: none\n"
"")
        self.btnAccount.setObjectName("btnAccount")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.btnAccount)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.labelUser = QtWidgets.QLabel(self.btnAccount)
        self.labelUser.setStyleSheet("border-bottom: none\n"
"")
        self.labelUser.setObjectName("labelUser")
        self.horizontalLayout_6.addWidget(self.labelUser)
        self.accountBtn = QtWidgets.QPushButton(self.btnAccount)
        self.accountBtn.setMaximumSize(QtCore.QSize(120, 120))
        self.accountBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.accountBtn.setStyleSheet("border: none;\n"
"")
        self.accountBtn.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/user.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.accountBtn.setIcon(icon9)
        self.accountBtn.setIconSize(QtCore.QSize(33, 33))
        self.accountBtn.setObjectName("accountBtn")
        self.horizontalLayout_6.addWidget(self.accountBtn)
        self.horizontalLayout_2.addWidget(self.btnAccount, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addWidget(self.headerFrame, 0, QtCore.Qt.AlignVCenter)
        self.bagFrame = QtWidgets.QFrame(self.mainBody)
        self.bagFrame.setMinimumSize(QtCore.QSize(0, 15))
        self.bagFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bagFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bagFrame.setObjectName("bagFrame")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.bagFrame)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.verticalLayout.addWidget(self.bagFrame)
        self.userFrame = QtWidgets.QFrame(self.mainBody)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userFrame.sizePolicy().hasHeightForWidth())
        self.userFrame.setSizePolicy(sizePolicy)
        self.userFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.userFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.userFrame.setObjectName("userFrame")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.userFrame)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayout.addWidget(self.userFrame)
        self.homeFrame = QtWidgets.QFrame(self.mainBody)
        self.homeFrame.setMinimumSize(QtCore.QSize(0, 690))
        self.homeFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.homeFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.homeFrame.setObjectName("homeFrame")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.homeFrame)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.cardFrame = QtWidgets.QWidget(self.homeFrame)
        self.cardFrame.setMinimumSize(QtCore.QSize(0, 150))
        self.cardFrame.setStyleSheet("border-radius:15px;")
        self.cardFrame.setObjectName("cardFrame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.cardFrame)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.card1 = QtWidgets.QFrame(self.cardFrame)
        self.card1.setStyleSheet("background-color:white;    \n"
"border:1px solid #057A3A;\n"
"\n"
"")
        self.card1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.card1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.card1.setObjectName("card1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.card1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.card1)
        self.frame.setStyleSheet("border: 0px")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.textProd = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.textProd.setFont(font)
        self.textProd.setStyleSheet("color:#057a3a;")
        self.textProd.setObjectName("textProd")
        self.horizontalLayout_12.addWidget(self.textProd, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.btnItem = QtWidgets.QPushButton(self.frame)
        self.btnItem.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnItem.setStyleSheet("color:#057a3a;")
        self.btnItem.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/codesandbox.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnItem.setIcon(icon10)
        self.btnItem.setIconSize(QtCore.QSize(30, 30))
        self.btnItem.setObjectName("btnItem")
        self.horizontalLayout_12.addWidget(self.btnItem)
        self.verticalLayout_2.addWidget(self.frame)
        self.label_7 = QtWidgets.QLabel(self.card1)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("border: 0px;\n"
"color:#057a3a;")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_7.addWidget(self.card1)
        self.card2 = QtWidgets.QFrame(self.cardFrame)
        self.card2.setStyleSheet("background-color:white;    \n"
"border:1px solid #057A3A;\n"
"\n"
"")
        self.card2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.card2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.card2.setObjectName("card2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.card2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.card2)
        self.frame_2.setStyleSheet("border: 0px")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.textLogs = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.textLogs.setFont(font)
        self.textLogs.setStyleSheet("color:#057a3a;")
        self.textLogs.setObjectName("textLogs")
        self.horizontalLayout_13.addWidget(self.textLogs, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.btnReg = QtWidgets.QPushButton(self.frame_2)
        self.btnReg.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnReg.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icons/database.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnReg.setIcon(icon11)
        self.btnReg.setIconSize(QtCore.QSize(30, 30))
        self.btnReg.setObjectName("btnReg")
        self.horizontalLayout_13.addWidget(self.btnReg)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.label_11 = QtWidgets.QLabel(self.card2)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("border: 0px;\n"
"color:#057a3a;")
        self.label_11.setObjectName("label_11")
        self.verticalLayout_3.addWidget(self.label_11, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_7.addWidget(self.card2)
        self.card3 = QtWidgets.QFrame(self.cardFrame)
        self.card3.setStyleSheet("background-color:white;    \n"
"border:1px solid #057A3A;\n"
"\n"
"")
        self.card3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.card3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.card3.setObjectName("card3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.card3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_3 = QtWidgets.QFrame(self.card3)
        self.frame_3.setStyleSheet("border: 0px")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.textLocal = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.textLocal.setFont(font)
        self.textLocal.setStyleSheet("color:#057a3a;")
        self.textLocal.setObjectName("textLocal")
        self.horizontalLayout_14.addWidget(self.textLocal, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.btnLocal = QtWidgets.QPushButton(self.frame_3)
        self.btnLocal.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnLocal.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icons/map-pin.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnLocal.setIcon(icon12)
        self.btnLocal.setIconSize(QtCore.QSize(30, 30))
        self.btnLocal.setObjectName("btnLocal")
        self.horizontalLayout_14.addWidget(self.btnLocal)
        self.verticalLayout_4.addWidget(self.frame_3)
        self.label_4 = QtWidgets.QLabel(self.card3)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("border: 0px;\n"
"color:#057a3a;")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_7.addWidget(self.card3)
        self.card4 = QtWidgets.QFrame(self.cardFrame)
        self.card4.setStyleSheet("background-color:white;    \n"
"border:1px solid #057A3A;\n"
"\n"
"")
        self.card4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.card4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.card4.setObjectName("card4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.card4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_4 = QtWidgets.QFrame(self.card4)
        self.frame_4.setStyleSheet("border: 0px")
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.textVp = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.textVp.setFont(font)
        self.textVp.setStyleSheet("color:#057a3a;")
        self.textVp.setObjectName("textVp")
        self.horizontalLayout_15.addWidget(self.textVp, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.btnVP = QtWidgets.QPushButton(self.frame_4)
        self.btnVP.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnVP.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/icons/dollar-sign.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnVP.setIcon(icon13)
        self.btnVP.setIconSize(QtCore.QSize(30, 30))
        self.btnVP.setObjectName("btnVP")
        self.horizontalLayout_15.addWidget(self.btnVP)
        self.verticalLayout_5.addWidget(self.frame_4)
        self.label_5 = QtWidgets.QLabel(self.card4)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("border: 0px;\n"
"color:#057a3a;")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_7.addWidget(self.card4)
        self.verticalLayout_10.addWidget(self.cardFrame)
        self.mainFrame = QtWidgets.QWidget(self.homeFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainFrame.sizePolicy().hasHeightForWidth())
        self.mainFrame.setSizePolicy(sizePolicy)
        self.mainFrame.setMinimumSize(QtCore.QSize(0, 450))
        self.mainFrame.setMaximumSize(QtCore.QSize(1500, 600))
        self.mainFrame.setSizeIncrement(QtCore.QSize(0, 0))
        self.mainFrame.setBaseSize(QtCore.QSize(0, 0))
        self.mainFrame.setStyleSheet("border-radius:9px;")
        self.mainFrame.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.mainFrame.setObjectName("mainFrame")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.mainFrame)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.h_frame2 = QtWidgets.QFrame(self.mainFrame)
        self.h_frame2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.h_frame2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.h_frame2.setObjectName("h_frame2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.h_frame2)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_5 = QtWidgets.QFrame(self.h_frame2)
        self.frame_5.setStyleSheet("background-color:#057a3a;\n"
"border-radius: 15px;\n"
"color:white;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("border-bottom: none;\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.horizontalLayout_10.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_9.addWidget(self.frame_5)
        self.tableView = QtWidgets.QTableView(self.h_frame2)
        self.tableView.setStyleSheet("background-color:white;    \n"
"border:3px solid #057A3A;\n"
"\n"
"")
        self.tableView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView.setTabKeyNavigation(False)
        self.tableView.setProperty("showDropIndicator", False)
        self.tableView.setDragDropOverwriteMode(False)
        self.tableView.setGridStyle(QtCore.Qt.SolidLine)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setVisible(False)
        self.tableView.horizontalHeader().setHighlightSections(False)
        self.tableView.verticalHeader().setVisible(False)
        self.tableView.verticalHeader().setHighlightSections(False)
        self.verticalLayout_9.addWidget(self.tableView)
        self.horizontalLayout_8.addWidget(self.h_frame2)
        self.h_frame1 = QtWidgets.QFrame(self.mainFrame)
        self.h_frame1.setMaximumSize(QtCore.QSize(360, 16777215))
        self.h_frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.h_frame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.h_frame1.setObjectName("h_frame1")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.h_frame1)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_8 = QtWidgets.QFrame(self.h_frame1)
        self.frame_8.setStyleSheet("background-color:#057a3a;\n"
"border-radius: 15px;\n"
"color:white;")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_3 = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border-bottom: none;\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_9.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_8.addWidget(self.frame_8)
        self.tableView_2 = QtWidgets.QTableView(self.h_frame1)
        self.tableView_2.setEnabled(True)
        self.tableView_2.setStyleSheet("background-color:white;    \n"
"border:3px solid #057A3A;\n"
"\n"
"")
        self.tableView_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableView_2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableView_2.setAutoScroll(True)
        self.tableView_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView_2.setTabKeyNavigation(False)
        self.tableView_2.setProperty("showDropIndicator", False)
        self.tableView_2.setDragDropOverwriteMode(False)
        self.tableView_2.setObjectName("tableView_2")
        self.tableView_2.horizontalHeader().setVisible(False)
        self.tableView_2.horizontalHeader().setHighlightSections(False)
        self.tableView_2.verticalHeader().setVisible(False)
        self.tableView_2.verticalHeader().setHighlightSections(False)
        self.verticalLayout_8.addWidget(self.tableView_2)
        self.horizontalLayout_8.addWidget(self.h_frame1)
        self.verticalLayout_10.addWidget(self.mainFrame)
        self.verticalLayout.addWidget(self.homeFrame)
        self.horizontalLayout.addWidget(self.mainBody)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Controle de Patrimônio"))
        self.relBtn.setText(_translate("MainWindow", "Relatório"))
        self.usersBtn.setText(_translate("MainWindow", "Users"))
        self.bagBtn.setText(_translate("MainWindow", "Inventário"))
        self.logBtn.setText(_translate("MainWindow", "Definições"))
        self.bckpBtn.setText(_translate("MainWindow", "Backup"))
        self.helpBtn.setText(_translate("MainWindow", "Ajuda"))
        self.docBtn.setText(_translate("MainWindow", "Sobre"))
        self.labelUser.setText(_translate("MainWindow", "TextLabel"))
        self.textProd.setText(_translate("MainWindow", "Produtos"))
        self.label_7.setText(_translate("MainWindow", "PRODUTOS"))
        self.textLogs.setText(_translate("MainWindow", "Logs"))
        self.label_11.setText(_translate("MainWindow", "REGISTROS"))
        self.textLocal.setText(_translate("MainWindow", "Locais"))
        self.label_4.setText(_translate("MainWindow", "SETORES"))
        self.textVp.setText(_translate("MainWindow", "Patrimônio"))
        self.label_5.setText(_translate("MainWindow", "PATRIMÔNIO"))
        self.label.setText(_translate("MainWindow", "Produtos recentes"))
        self.label_3.setText(_translate("MainWindow", "Últimos Registros"))
import resource_rc
