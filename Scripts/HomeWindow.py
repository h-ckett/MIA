import sys
import webbrowser
import ROIWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QWidget, QListWidget, QMenuBar, QAction
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore

class HomeWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "MIA"
        self.width = 320
        self.height = 420
        self.icon = "mouse.png"

        self.newROIWindow = ROIWindow.ROIWindow()                                   #   ROIWindow
        self.newROIWindow.hide()                                                    #   Hide it for later

        #   declare dictionary that stores lists of all coords & datapoints &c. for each defined ROI

        # le_vidPath        -   line edit for the video path
        self.le_vidPath = QLineEdit(self)                                           #   Create the line edit
        self.le_vidPath.setGeometry(QRect(5, 55, 310, 25))                          #   Set size & pos
        self.le_vidPath.setClearButtonEnabled(True)                                 #   Enable the clear button
        # le_savePath       -   line edit for the save path
        self.le_savePath = QLineEdit(self)
        self.le_savePath.setGeometry(QRect(5, 360, 310, 25))
        self.le_savePath.setClearButtonEnabled(True)
        # lbx_ROIs          -   list box for the ROI list
        self.lbx_ROIs = QListWidget(self)                                           #   Create the combo box
        self.lbx_ROIs.setGeometry(QRect(5, 115, 310, 210))                          #   Set size & pos
        # Create out menu bars
        self.mainMenu = self.menuBar()                                              #   Create a menu bar
        self.fileMenu = self.mainMenu.addMenu("File")                               #   Create a "File" section
        self.aboutMenu = self.mainMenu.addMenu("About")                             #   Create an "About" section
        # Create our menu actions
            # New Project   (Ctrl+N)
        self.newProject = QAction("New Project", self)                              #   Create a QAction
        self.newProject.setShortcut("Ctrl+N")                                       #   Set its shortcut
        self.fileMenu.addAction(self.newProject)                                    #   Add it to a menu
        #self.newProject.triggered.connect(self.functionName)                       #   Add an event
            # Save Project  (Ctrl+S)
        self.saveProject = QAction("Save Project", self)
        self.saveProject.setShortcut("Ctrl+S")
        self.fileMenu.addAction(self.saveProject)
            # Open Project  (Ctrl+O)
        self.openProject = QAction("Open Project", self)
        self.openProject.setShortcut("Ctrl+O")
        self.fileMenu.addAction(self.openProject)
            # Advanced Settings
        self.advSettings = QAction("Advanced Settings", self)
        self.fileMenu.addAction(self.advSettings)
            # GitHub
        self.goToGitHub = QAction("GitHub", self)
        self.aboutMenu.addAction(self.goToGitHub)
        self.goToGitHub.triggered.connect(self.trigger_GitHub)

        self.UIComponents()

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.icon))
        self.setWindowTitle(self.title)
        self.setFixedSize(self.width, self.height)
    
        self.show()
    
    def UIComponents(self):
        # btn_importVideo   -   button for importing the video of choice
        btn_importVideo = QPushButton("Import video...", self)                      #   Create the button
        btn_importVideo.setGeometry(QRect(5, 25, 310, 25))                          #   Set size & pos
        btn_importVideo.setToolTip("Click to choose the video for processing")      #   Set the tooltip
        btn_importVideo.clicked.connect(self.onClick_importVideo)                   #   Set the event for on-click
        # btn_newROI        -   button for opening ROI window to define a new ROI
        btn_newROI = QPushButton("New ROI...", self)
        btn_newROI.setGeometry(QRect(5, 85, 100, 25))
        btn_newROI.setToolTip("Click to open a new ROI definition window")
        btn_newROI.clicked.connect(self.onClick_newROI)
        # btn_loadROI       -   button for loading ROI window to import a previously defined ROI
        btn_loadROI = QPushButton("Load ROI...", self)
        btn_loadROI.setGeometry(QRect(110, 85, 100, 25))
        btn_loadROI.setToolTip("Click to load a previously defined and saved ROI")
        btn_loadROI.clicked.connect(self.onClick_loadROI)
        # btn_deleteROI     -   button for removing the selected ROI from the ROI list
        btn_deleteROI = QPushButton("Delete ROI...", self)
        btn_deleteROI.setGeometry(QRect(215, 85, 100, 25))
        btn_deleteROI.setToolTip("Click to delete the currently selected ROI")
        btn_deleteROI.clicked.connect(self.onClick_deleteROI)
        # btn_savePath      -   button to set the output csv file name and path
        btn_savePath = QPushButton("Save path...", self)
        btn_savePath.setGeometry(QRect(5, 330, 310, 25))
        btn_savePath.setToolTip("Click to set the save path and name of output CSV file")
        btn_savePath.clicked.connect(self.onClick_savePath)
        # btn_start         -   button to start the application
        btn_start = QPushButton("START", self)
        btn_start.setGeometry(QRect(5, 390, 310, 25))
        btn_start.setToolTip("Click to start the application")
        btn_start.clicked.connect(self.onClick_start)
    
    #   :START: ON CLICK EVENTS
    def onClick_importVideo(self):
        pass
    def onClick_newROI(self):
        self.newROIWindow.show()
        #   after window closes, yoink data list/tuple out of it and store in dictionary
        return
    def onClick_loadROI(self):
        pass
    def onClick_deleteROI(self):
        pass
    def onClick_savePath(self):
        pass
    def onClick_start(self):
        pass
    #   :END:   ON CLICK EVENTS
    #   :START: Menu Trigger Events
    #   trigger_GitHub      -   when About->GitHub is clicked, open the github page in a new browser tab
    def trigger_GitHub(self):
        webbrowser.open_new("https://github.com/h-ckett/MIA")
    #   :END:   Menu Trigger Events 

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = HomeWindow()           #   Start up our HomeWindow
    sys.exit(App.exec())

# to do: in design put datapoints checkboxes in ROI window
#       so that each ROI has its own datapoints
# default padding: 5px
# set geometry = left, top, wide, tall
# button.setIcon(QtGui.QIcon("image.png")) | button.setIconSize(QtCore.QSize(x, y))