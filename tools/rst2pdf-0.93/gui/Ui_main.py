# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#

#      by: PyQt4 UI code generator 4.5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(574, 601)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/kaddressbook.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.centralWidget)
        self.horizontalLayout_3.setMargin(3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tabs = QtGui.QTabWidget(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabs.sizePolicy().hasHeightForWidth())
        self.tabs.setSizePolicy(sizePolicy)
        self.tabs.setObjectName("tabs")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout = QtGui.QHBoxLayout(self.tab)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.text = CodeEditor(self.tab)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        self.text.setFont(font)
        self.text.setFrameShape(QtGui.QFrame.NoFrame)
        self.text.setFrameShadow(QtGui.QFrame.Plain)
        self.text.setLineWidth(0)
        self.text.setObjectName("text")
        self.horizontalLayout.addWidget(self.text)
        self.tabs.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.tab_2)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.style = CodeEditor(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        self.style.setFont(font)
        self.style.setFrameShape(QtGui.QFrame.NoFrame)
        self.style.setObjectName("style")
        self.horizontalLayout_2.addWidget(self.style)
        self.tabs.addTab(self.tab_2, "")
        self.horizontalLayout_3.addWidget(self.tabs)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 574, 32))
        self.menuBar.setObjectName("menuBar")
        self.menuText = QtGui.QMenu(self.menuBar)
        self.menuText.setObjectName("menuText")
        self.menuView = QtGui.QMenu(self.menuBar)
        self.menuView.setObjectName("menuView")
        self.menuEdit = QtGui.QMenu(self.menuBar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtGui.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.pdfbar = QtGui.QToolBar(MainWindow)
        self.pdfbar.setObjectName("pdfbar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.pdfbar)
        self.dock = QtGui.QDockWidget(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/pdf.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dock.setWindowIcon(icon1)
        self.dock.setObjectName("dock")
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dockLayout = QtGui.QVBoxLayout()
        self.dockLayout.setSpacing(0)
        self.dockLayout.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.dockLayout.setContentsMargins(-1, -1, -1, 0)
        self.dockLayout.setObjectName("dockLayout")
        self.verticalLayout.addLayout(self.dockLayout)
        self.dock.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dock)
        self.editbar = QtGui.QToolBar(MainWindow)
        self.editbar.setObjectName("editbar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.editbar)
        self.searchbar = QtGui.QToolBar(MainWindow)
        self.searchbar.setMovable(False)
        self.searchbar.setAllowedAreas(QtCore.Qt.BottomToolBarArea)
        self.searchbar.setFloatable(False)
        self.searchbar.setObjectName("searchbar")
        MainWindow.addToolBar(QtCore.Qt.BottomToolBarArea, self.searchbar)
        self.structure = QtGui.QDockWidget(MainWindow)
        self.structure.setObjectName("structure")
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tree = QtGui.QTreeWidget(self.dockWidgetContents_2)
        self.tree.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tree.setProperty("showDropIndicator", QtCore.QVariant(False))
        self.tree.setAlternatingRowColors(True)
        self.tree.setHeaderHidden(False)
        self.tree.setObjectName("tree")
        self.tree.header().setVisible(True)
        self.tree.header().setStretchLastSection(False)
        self.verticalLayout_2.addWidget(self.tree)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.structure.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.structure)
        self.actionLoad_Text = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/fileopen.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLoad_Text.setIcon(icon2)
        self.actionLoad_Text.setObjectName("actionLoad_Text")
        self.actionLoad_Style = QtGui.QAction(MainWindow)
        self.actionLoad_Style.setIcon(icon2)
        self.actionLoad_Style.setObjectName("actionLoad_Style")
        self.actionRender = QtGui.QAction(MainWindow)
        self.actionRender.setIcon(icon1)
        self.actionRender.setObjectName("actionRender")
        self.actionSave_Text = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/filesave.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_Text.setIcon(icon3)
        self.actionSave_Text.setObjectName("actionSave_Text")
        self.actionSave_Style = QtGui.QAction(MainWindow)
        self.actionSave_Style.setIcon(icon3)
        self.actionSave_Style.setObjectName("actionSave_Style")
        self.actionSave_PDF = QtGui.QAction(MainWindow)
        self.actionSave_PDF.setIcon(icon1)
        self.actionSave_PDF.setObjectName("actionSave_PDF")
        self.actionSaveAs_Text = QtGui.QAction(MainWindow)
        self.actionSaveAs_Text.setIcon(icon3)
        self.actionSaveAs_Text.setObjectName("actionSaveAs_Text")
        self.actionSaveAs_Style = QtGui.QAction(MainWindow)
        self.actionSaveAs_Style.setIcon(icon3)
        self.actionSaveAs_Style.setObjectName("actionSaveAs_Style")
        self.actionSaveAs_PDF = QtGui.QAction(MainWindow)
        self.actionSaveAs_PDF.setIcon(icon1)
        self.actionSaveAs_PDF.setObjectName("actionSaveAs_PDF")
        self.actionUndo1 = QtGui.QAction(MainWindow)
        self.actionUndo1.setEnabled(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/undo.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUndo1.setIcon(icon4)
        self.actionUndo1.setObjectName("actionUndo1")
        self.actionRedo1 = QtGui.QAction(MainWindow)
        self.actionRedo1.setEnabled(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/redo.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRedo1.setIcon(icon5)
        self.actionRedo1.setObjectName("actionRedo1")
        self.actionCut1 = QtGui.QAction(MainWindow)
        self.actionCut1.setEnabled(False)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/editcut.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCut1.setIcon(icon6)
        self.actionCut1.setObjectName("actionCut1")
        self.actionCopy1 = QtGui.QAction(MainWindow)
        self.actionCopy1.setEnabled(False)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/editcopy.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopy1.setIcon(icon7)
        self.actionCopy1.setObjectName("actionCopy1")
        self.actionPaste1 = QtGui.QAction(MainWindow)
        self.actionPaste1.setEnabled(False)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/editpaste.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPaste1.setIcon(icon8)
        self.actionPaste1.setObjectName("actionPaste1")
        self.actionUndo2 = QtGui.QAction(MainWindow)
        self.actionUndo2.setEnabled(False)
        self.actionUndo2.setIcon(icon4)
        self.actionUndo2.setObjectName("actionUndo2")
        self.actionRedo2 = QtGui.QAction(MainWindow)
        self.actionRedo2.setEnabled(False)
        self.actionRedo2.setIcon(icon5)
        self.actionRedo2.setObjectName("actionRedo2")
        self.actionCut2 = QtGui.QAction(MainWindow)
        self.actionCut2.setEnabled(False)
        self.actionCut2.setIcon(icon6)
        self.actionCut2.setObjectName("actionCut2")
        self.actionCopy2 = QtGui.QAction(MainWindow)
        self.actionCopy2.setEnabled(False)
        self.actionCopy2.setIcon(icon7)
        self.actionCopy2.setObjectName("actionCopy2")
        self.actionPaste2 = QtGui.QAction(MainWindow)
        self.actionPaste2.setEnabled(False)
        self.actionPaste2.setIcon(icon8)
        self.actionPaste2.setObjectName("actionPaste2")
        self.actionFind = QtGui.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/find.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFind.setIcon(icon9)
        self.actionFind.setObjectName("actionFind")
        self.actionAbout_Bookrest = QtGui.QAction(MainWindow)
        self.actionAbout_Bookrest.setObjectName("actionAbout_Bookrest")
        self.actionTest_Action = QtGui.QAction(MainWindow)
        self.actionTest_Action.setObjectName("actionTest_Action")
        self.actionSettings = QtGui.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/configure.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettings.setIcon(icon10)
        self.actionSettings.setObjectName("actionSettings")
        self.menuText.addAction(self.actionLoad_Text)
        self.menuText.addAction(self.actionLoad_Style)
        self.menuText.addSeparator()
        self.menuText.addAction(self.actionSave_Text)
        self.menuText.addAction(self.actionSaveAs_Text)
        self.menuText.addAction(self.actionSave_Style)
        self.menuText.addAction(self.actionSaveAs_Style)
        self.menuText.addAction(self.actionSave_PDF)
        self.menuText.addAction(self.actionSaveAs_PDF)
        self.menuEdit.addAction(self.actionUndo1)
        self.menuEdit.addAction(self.actionUndo2)
        self.menuEdit.addAction(self.actionRedo1)
        self.menuEdit.addAction(self.actionRedo2)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCut1)
        self.menuEdit.addAction(self.actionCut2)
        self.menuEdit.addAction(self.actionCopy1)
        self.menuEdit.addAction(self.actionCopy2)
        self.menuEdit.addAction(self.actionPaste1)
        self.menuEdit.addAction(self.actionPaste2)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionFind)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionSettings)
        self.menuHelp.addAction(self.actionAbout_Bookrest)
        self.menuBar.addAction(self.menuText.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionLoad_Text)
        self.toolBar.addAction(self.actionRender)
        self.toolBar.addAction(self.actionSettings)
        self.editbar.addAction(self.actionUndo1)
        self.editbar.addAction(self.actionUndo2)
        self.editbar.addAction(self.actionRedo1)
        self.editbar.addAction(self.actionRedo2)
        self.editbar.addAction(self.actionCut1)
        self.editbar.addAction(self.actionCut2)
        self.editbar.addAction(self.actionCopy1)
        self.editbar.addAction(self.actionCopy2)
        self.editbar.addAction(self.actionPaste1)
        self.editbar.addAction(self.actionPaste2)

        self.retranslateUi(MainWindow)
        self.tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.text, self.tabs)
        MainWindow.setTabOrder(self.tabs, self.style)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Bookrest", None, QtGui.QApplication.UnicodeUTF8))
        self.tabs.setTabText(self.tabs.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Text", None, QtGui.QApplication.UnicodeUTF8))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "StyleSheet", None, QtGui.QApplication.UnicodeUTF8))
        self.menuText.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuView.setTitle(QtGui.QApplication.translate("MainWindow", "View", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setTitle(QtGui.QApplication.translate("MainWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.pdfbar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar_2", None, QtGui.QApplication.UnicodeUTF8))
        self.dock.setWindowTitle(QtGui.QApplication.translate("MainWindow", "PDF Preview", None, QtGui.QApplication.UnicodeUTF8))
        self.editbar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar_2", None, QtGui.QApplication.UnicodeUTF8))
        self.searchbar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar_2", None, QtGui.QApplication.UnicodeUTF8))
        self.structure.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Document Structure", None, QtGui.QApplication.UnicodeUTF8))
        self.tree.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "Section", None, QtGui.QApplication.UnicodeUTF8))
        self.tree.headerItem().setText(1, QtGui.QApplication.translate("MainWindow", "Line", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad_Text.setText(QtGui.QApplication.translate("MainWindow", "Open Text", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad_Text.setToolTip(QtGui.QApplication.translate("MainWindow", "Open Text", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad_Text.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad_Style.setText(QtGui.QApplication.translate("MainWindow", "Open Style", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad_Style.setToolTip(QtGui.QApplication.translate("MainWindow", "Open Style", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRender.setText(QtGui.QApplication.translate("MainWindow", "Render", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_Text.setText(QtGui.QApplication.translate("MainWindow", "Save Text", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_Text.setToolTip(QtGui.QApplication.translate("MainWindow", "Save Text", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_Text.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_Style.setText(QtGui.QApplication.translate("MainWindow", "Save Style", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_Style.setToolTip(QtGui.QApplication.translate("MainWindow", "Save Style", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_PDF.setText(QtGui.QApplication.translate("MainWindow", "Save PDF", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_PDF.setToolTip(QtGui.QApplication.translate("MainWindow", "Save PDF", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveAs_Text.setText(QtGui.QApplication.translate("MainWindow", "Save Text As", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveAs_Text.setToolTip(QtGui.QApplication.translate("MainWindow", "Save Text", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveAs_Style.setText(QtGui.QApplication.translate("MainWindow", "Save Style As", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveAs_Style.setToolTip(QtGui.QApplication.translate("MainWindow", "Save Style", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveAs_PDF.setText(QtGui.QApplication.translate("MainWindow", "Save PDF As", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveAs_PDF.setToolTip(QtGui.QApplication.translate("MainWindow", "Save PDF", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUndo1.setText(QtGui.QApplication.translate("MainWindow", "Undo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUndo1.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Z", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRedo1.setText(QtGui.QApplication.translate("MainWindow", "Redo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRedo1.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+Z", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCut1.setText(QtGui.QApplication.translate("MainWindow", "Cut", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCut1.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+X", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopy1.setText(QtGui.QApplication.translate("MainWindow", "Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopy1.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+C", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPaste1.setText(QtGui.QApplication.translate("MainWindow", "Paste", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPaste1.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+V", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUndo2.setText(QtGui.QApplication.translate("MainWindow", "Undo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUndo2.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Z", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRedo2.setText(QtGui.QApplication.translate("MainWindow", "Redo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRedo2.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+Z", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCut2.setText(QtGui.QApplication.translate("MainWindow", "Cut", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCut2.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+X", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopy2.setText(QtGui.QApplication.translate("MainWindow", "Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopy2.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+C", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPaste2.setText(QtGui.QApplication.translate("MainWindow", "Paste", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPaste2.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+V", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFind.setText(QtGui.QApplication.translate("MainWindow", "Find", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFind.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+F", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_Bookrest.setText(QtGui.QApplication.translate("MainWindow", "About Bookrest", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTest_Action.setText(QtGui.QApplication.translate("MainWindow", "Test Action", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSettings.setText(QtGui.QApplication.translate("MainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))

from codeeditor import CodeEditor
import icons_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
