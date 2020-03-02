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

        #   store variables here in a list/tuple for coord data + datapoint selections
        
        self.defROIWindow = DefineROI() #   Set up our ROI def window for later
        self.defROIWindow.hide()        #   Hide it

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
    
    #   method to yoink data out of ROI definition window to combine with data in ROIWindow

class DefineROI(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "Define ROI"
        self.width = 1280
        self.height = 755
        self.icon = "roi.png"

        #   store variables here related to coords &c. gathered
        self.originCoords = [0, 0]          #   Coordinates of the first point in polygon
        self.polyCoords = QtGui.QPolygon()  #   Store multiple coords for each point in polygon

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
        self.lbl_originCoords.setText("Polygon Origin: (%d, %d)" % (self.originCoords[0], self.originCoords[1]))
        self.lbl_originCoords.setGeometry(QRect(285, 725, 275, 25))

        #self.show()
    
    def mouseMoveEvent(self, event):
        self.lbl_cursorCoords.setText("Set Point at: (%d, %d)" % (event.x(), event.y()))
    def mousePressEvent(self, event):
        pass
    def mouseReleaseEvent(self, event):
        pass

#debug
"""
App = QApplication(sys.argv)
window = ROIWindow()
sys.exit(App.exec())
"""
#/debug

# to do: handle origin label and data variables
# to do: do the point by point (allow polygon definition), adding to a list until new point is same as origin
# since clicking directly on origin point is hard, make it a range of pixels near origin
# maybe like error of 5-10 px, then just snap it to origin
# to do: calculate px region inside defined polygon
# to do: update original roi window