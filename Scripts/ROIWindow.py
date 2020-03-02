import sys
from PyQt5.QtWidgets import QDialog, QApplication, QLabel, QPushButton, QLineEdit, QWidget, QListWidget, QMenuBar, QAction
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap

class ROIWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "MIA ROI Editor"
        self.width = 800
        self.height = 600
        self.icon = "roi.png"
        
        self.defROIWindow = DefineROI()
        self.defROIWindow.hide()

        self.UIComponents()
        self.InitWindow()
    
    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.icon))
        self.setWindowTitle(self.title)
        self.setFixedSize(self.width, self.height) 

        self.show()

    def UIComponents(self):
        # btn_defineROI   -   button for opening ROI definition window
        btn_defineROI = QPushButton("Define ROI", self)                           #   Create the button
        btn_defineROI.setGeometry(QRect(5, 5, 100, 25))                           #   Set size & pos
        btn_defineROI.setToolTip("Open the ROI Definition screen")                #   Set the tooltip
        btn_defineROI.clicked.connect(self.onClick_openDefineROI)                 #   Set the event for on-click

    def onClick_openDefineROI(self): 
        self.defROIWindow.show()

class DefineROI(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "Define ROI"
        self.width = 1280
        self.height = 755
        self.icon = "roi.png"

        self.InitWindow()
        self.setMouseTracking(True)
    
    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.icon))
        self.setWindowTitle(self.title)
        self.setFixedSize(self.width, self.height)

         #   preview             -   shows a preview of the first frame of the video
        self.lbl_preview = QLabel(self)                  #   Create a label
        self.pxm_preview = QPixmap("frame00001.jpg")     #   Create a pixmap for the label
        self.lbl_preview.setPixmap(self.pxm_preview)     #   Set the pixmap to the label
        self.lbl_preview.setGeometry(QRect(0, 0, 1280, 720))
        self.lbl_preview.setMouseTracking(True)
        #   cursorCoords        -   shows the coord position of the cursor while defining
        self.lbl_cursorCoords = QLabel(self)
        self.lbl_cursorCoords.setFont(QtGui.QFont("Sanserif", 16))
        self.lbl_cursorCoords.setText("Current Position: (1280, 720)")
        self.lbl_cursorCoords.setGeometry(QRect(5, 725, 275, 25))
        #   originCoords        -   shows the coords of the region's origin point
        self.lbl_originCoords = QLabel(self)
        self.lbl_originCoords.setFont(QtGui.QFont("Sanserif", 16))
        self.lbl_originCoords.setText("Region Origin: (1280, 720)")
        self.lbl_originCoords.setGeometry(QRect(285, 725, 275, 25))
        #   endptCoords         -   shows the coords of the region's end point
        self.lbl_endptCoords = QLabel(self)
        self.lbl_endptCoords.setFont(QtGui.QFont("Sanserif", 16))
        self.lbl_endptCoords.setText("Region End: (1280, 720)")
        self.lbl_endptCoords.setGeometry(QRect(565, 725, 275, 25))

        self.show()
    
    def mouseMoveEvent(self, event):
        self.lbl_cursorCoords.setText("Current Position: (%d, %d)" % (event.x(), event.y()))
    def mousePressEvent(self, event):
        pass
    def mouseReleaseEvent(self, event):
        pass

#debug
App = QApplication(sys.argv)
window = ROIWindow()
sys.exit(App.exec())
#/debug

# to do: handle set origin and set end
# to do: calculate region sq
# to do: maybe do the point by point, adding to a list until new point is same as origin?
# to do: update original roi window