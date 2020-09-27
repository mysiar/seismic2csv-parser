"""
    Application Main Window
"""
import os
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QToolBar,
    QAction,
    qApp,
    QFileDialog,
    QGridLayout,
    QLabel,
    QWidget,
    QStatusBar,
)

import app_info
import AboutDialog

QApplication.setApplicationName(app_info.TITLE)
QApplication.setApplicationDisplayName(app_info.TITLE)
QApplication.setApplicationVersion(app_info.VERSION)


def about():
    """
        Displays Application About Dialog
    """
    dlg = AboutDialog.AboutDialog()
    dlg.exec_()


class MainWindow(QMainWindow):
    """
        MainWindow
    """
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle(app_info.TITLE)
        self.setFixedSize(QSize(app_info.MAIN_WINDOWS_WIDTH, app_info.MAIN_WINDOW_HEIGHT))

        self.input_filename = None
        self.output_filename = None
        self.window_layout = None

        # TOOLBAR
        toolbar = QToolBar()
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        open_input_action = QAction(QIcon(os.path.join("icons", "folder-open-document.png")), "Open Input file", self)
        open_input_action.setShortcut(QKeySequence("Ctrl+o"))
        open_input_action.triggered.connect(self.open_input_file)
        open_input_action.setStatusTip("Open Input file for conversion")
        toolbar.addAction(open_input_action)

        toolbar.addSeparator()

        run_action = QAction(QIcon(os.path.join("icons", "burn.png")), "Run", self)
        run_action.setShortcut(QKeySequence("Ctrl+r"))
        run_action.triggered.connect(self.run)
        run_action.setStatusTip("Run conversion")
        toolbar.addAction(run_action)

        toolbar.addSeparator()

        about_action = QAction(QIcon(os.path.join("icons", "information-button.png")), "About", self)
        about_action.setShortcut(QKeySequence("Ctrl+i"))
        about_action.triggered.connect(about)
        about_action.setStatusTip("About application")
        toolbar.addAction(about_action)

        toolbar.addSeparator()

        quit_action = QAction(QIcon(os.path.join("icons", "cross.png")), "Quit", self)
        quit_action.setShortcut(QKeySequence("Ctrl+q"))
        quit_action.triggered.connect(qApp.quit)
        quit_action.setStatusTip("Quit the application")
        toolbar.addAction(quit_action)

        # MENU
        menu = self.menuBar()
        file_menu = menu.addMenu("&File")
        file_menu.addAction(open_input_action)
        file_menu.addSeparator()
        file_menu.addAction(quit_action)

        help_menu = menu.addMenu("&Help")
        help_menu.addAction(about_action)

        self.setStatusBar(QStatusBar(self))

        # LAYOUT
        self.window_layout = QGridLayout()
        self.window_layout.setSpacing(5)
        self.window_layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        self.window_layout.addWidget(QLabel('INPUT'), 0, 0)
        self.window_layout.addWidget(QLabel('OUTPUT'), 1, 0)

        widget = QWidget(self)
        widget.setLayout(self.window_layout)

        self.setCentralWidget(widget)

    # @classmethod
    def open_input_file(self):
        """
            Opens Input file
        """
        self.input_filename, _ = QFileDialog.getOpenFileName(
            self,
            "Open file",
            "",
            "Hypertext Markup Language (*.htm *.html);;" "All files (*.*)",
        )

        if not self.input_filename:
            return

        self.output_filename = self.input_filename + '.csv'
        self.window_layout.addWidget(QLabel(self.input_filename), 0, 1, Qt.AlignTop)
        self.window_layout.addWidget(QLabel(self.output_filename), 1, 1, Qt.AlignTop)

    # @classmethod
    def run(self):
        """
            Runs parser to convert to CSV
        """
        if self.output_filename:
            print('Run')
