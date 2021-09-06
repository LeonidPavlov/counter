import sys
from typing import List
from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout,\
         QWidget, QMainWindow

from chooser_qt.view.view import CalendarView


class NonAppBase(QApplication):

    @staticmethod
    def start(argv: List[str]) -> None:
        NonAppBase(argv=argv)

    def __init__(self, argv: List[str]) -> None:
        super().__init__(argv)
        
        self.window: QWidget = QWidget()
        layout = QVBoxLayout()
        button = QPushButton('LAUNCH CALENDAR')
        self.w = None
        layout.addWidget(button)
        self.window.setLayout(layout)
        button.clicked.connect(self.open_calendar)
        self.window.show()
        self.exec()

    def open_calendar(self):
        if self.w is None:
            self.w = CalendarView()
NonAppBase.start([])
