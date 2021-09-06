import sys
from typing import Type
from PyQt5.QtWidgets import QLabel, QTimeEdit, QVBoxLayout, QWidget,\
                            QCalendarWidget, QHBoxLayout
from PyQt5.QtCore import QDateTime, QTime, QTimer
from datetime import datetime as dt


class CalendarView(QWidget):
    def __init__(self) -> None:
        super().__init__()
        

        self.label = QLabel()
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.__set_time_in_label()
        self.__set_timer()

        self.calendar: QCalendarWidget = QCalendarWidget(self)
        self.calendar.clicked.connect(self.__on_date_change)
        layout.addWidget(self.calendar)

        self.__set_time_chooser(layout)    

        self.setLayout(layout)
        self.show()
    
    def __set_timer(self) -> None:
        timer: QTimer = QTimer(self)
        timer.timeout.connect(self.__set_time_in_label)
        timer.start(1000)

    def __on_date_change(self) -> None:
        print(str(self.calendar.selectedDate()))

    def __set_time_in_label(self) -> None:
        self.label.setText(dt.now().strftime( '%A  %d %B  %H:%M:%S %Y' ))
    
    def __set_time_chooser(self, layout: QVBoxLayout) -> None:
        d = dt.now()
        self.time_view: QTimeEdit = QTimeEdit()
        label = QLabel('change time, if need')
        self.time_view.setFixedWidth(100)
        time: QTime = QTime()
        self.time_view.setTime(time.currentTime()) 
        hl = QHBoxLayout()
        hl.addWidget(label)
        hl.addWidget(self.time_view)
        layout.addLayout(hl)

    def __on_view_close(self) -> None:
        print('on close method')