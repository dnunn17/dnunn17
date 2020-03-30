#Destiny Nunn Asset maker tool for folder structure and naming convention

import sys 
from PyQt4 import QtCore, QtGui, uic
import os, shutil, stat 

#get current path
print(os.getcwd())

qtCreatorFile = "AssetMakerUI.ui"
#UI file referenced
Ui_FirstMainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtGui.QMainWindow, Ui_FirstMainWindow):
    def __init__(self):
        '''Initializing the Asset Maker Tool '''
        QtGui.QMainWindow.__init__(self)
        Ui_FirstMainWindow.__init__(self)
        self.setupUi(self)
        self.setupMyUI()
        self.turnOnRadioBtns()
        self.secondSet()

        #to add to the directory later
        self.assetType = '' #this is to add either the Character, Environment or Props folder
        self.querryText = '' #place holder for the user input for the name of the folder to be renamed
             

    def setupMyUI(self):
        '''Setting Up the UI for the Asset Maker Tool '''

        #------------------------#
        #setting up icon pictures
        #------------------------#

        self.ExitBtn.setIcon(QtGui.QIcon('xIcon.png'))
        #Exit Icon
        self.ThreeD_Btn.setIcon(QtGui.QIcon('3D-objects-icon.png'))
        #3D Icon
        self.AssetNameBtn.setIcon(QtGui.QIcon('pen.png'))
        #NameAsset Icon
        self.twoD_Btn.setIcon(QtGui.QIcon('2DIcon.png'))
        #2D Icon
        self.PropRadioBtn.setIcon(QtGui.QIcon('PropIcon.png'))
        #Prop Icon
        self.EnvironmentRadioBtn.setIcon(QtGui.QIcon('EnvIcon.png'))
        #Environment Icon
        self.CharacterRadioBtn.setIcon(QtGui.QIcon('CharIcon.png'))
        #Char Icon
        self.MayaRadioButton.setIcon(QtGui.QIcon('MayaIcon.jpg'))
        #Maya Icon
        self.ZBrushRadioBtn.setIcon(QtGui.QIcon('ZBrushIcon.png'))
        #ZBrush Icon
        self.PhotoshopRadioBtn.setIcon(QtGui.QIcon('PSDIcon.png'))
        #Photoshop Icon
        self.IllustratorRadioBtn.setIcon(QtGui.QIcon('IllustratorIcon.png'))
        #Illustrator Icon

        #-------------------------------#
        #connecting buttons to functions
        #-------------------------------#

        self.ExitBtn.clicked.connect(self.exitButton)
        #EXIT function

        self.twoD_Btn.toggled.connect(self.turnOnRadioBtns)
        self.ThreeD_Btn.toggled.connect(self.turnOnRadioBtns)
        #connects to turnOnRadioBtns function

        self.CharacterRadioBtn.toggled.connect(self.secondSet)
        self.EnvironmentRadioBtn.toggled.connect(self.secondSet)
        self.PropRadioBtn.toggled.connect(self.secondSet)
        #connects to the secondSet function

        self.TextBtn.clicked.connect(self.textSection)
        #connects to the textSection function

        self.MayaRadioButton.toggled.connect(self.softwareBtn)
        self.ZBrushRadioBtn.toggled.connect(self.softwareBtn)
        self.PhotoshopRadioBtn.toggled.connect(self.softwareBtn)
        self.IllustratorRadioBtn.toggled.connect(self.softwareBtn)
        #connects to the CreateBtnEnding function
        
        self.CreateBtn.clicked.connect(self.CreateBtnEnding)
        #connects to the CreateBtnEnding function

    def exitButton(self):
        '''exit button function'''
        reply = QtGui.QMessageBox.question(self,'Message', "Are you sure?", QtGui.QMessageBox.Yes|QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            QtGui.QApplication.quit()

    def turnOnRadioBtns(self):
        '''Once a radio button is selected in a section, the next section will become selectable'''

        if self.twoD_Btn.isChecked():
            #Turns on the character, prop, and envrionment radio buttons if 2D is checked
            self.CharacterRadioBtn.setEnabled(True)
            self.PropRadioBtn.setEnabled(True)
            self.EnvironmentRadioBtn.setEnabled(True) 
            self.AssetType.setEnabled(True)

        if self.ThreeD_Btn.isChecked():
            #Turns on the character, prop, and envrionment radio buttons if 3D is checked
            self.CharacterRadioBtn.setEnabled(True)
            self.PropRadioBtn.setEnabled(True)
            self.EnvironmentRadioBtn.setEnabled(True)
            self.AssetType.setEnabled(True)

    def secondSet(self):
        '''Once Character, Environment, and Prop radio buttons are selected, the lineEdit box, AssetNameBtn and TextBtn unlock'''
        if self.CharacterRadioBtn.isChecked():
            #Turns on the file name if selected
            self.AssetNameBtn.setEnabled(True)
            self.lineEdit.setEnabled(True)
            self.TextBtn.setEnabled(True)
            #add an addition to the file path here to characters folder
            self.assetType = 'Characters'
            return self.assetType

        if self.EnvironmentRadioBtn.isChecked():
            self.AssetNameBtn.setEnabled(True)
            self.lineEdit.setEnabled(True)
            self.TextBtn.setEnabled(True)
            #add an addition to the file path here to environment folder
            self.assetType = 'Environment'
            return self.assetType

        if self.PropRadioBtn.isChecked():
            self.AssetNameBtn.setEnabled(True)
            self.lineEdit.setEnabled(True)
            self.TextBtn.setEnabled(True)
            #add an addition to the file path here to props folder
            self.assetType = 'Props'
            return self.assetType

    def textSection(self):
        '''once you type in a word it will unlock the software section'''
        querryText = self.lineEdit.text() #querries the text
        checkableText = str(querryText) #puts it in a string

        #checks to see if the text enters is both upper and lower case
        if checkableText.islower() == False and checkableText.isupper() == False:
            if self.twoD_Btn.isChecked():
                #unlocks the software btns
                self.PhotoshopRadioBtn.setEnabled(True)
                self.IllustratorRadioBtn.setEnabled(True)
                self.SoftwareLabel.setEnabled(True)
                self.MayaRadioButton.setEnabled(False)
                self.ZBrushRadioBtn.setEnabled(False)
            else: 
                #unlocks the software btns
                self.MayaRadioButton.setEnabled(True)
                self.ZBrushRadioBtn.setEnabled(True)
                self.SoftwareLabel.setEnabled(True)
                self.PhotoshopRadioBtn.setEnabled(False)
                self.IllustratorRadioBtn.setEnabled(False)
        elif checkableText.islower() == True:
            #if its only lowercase it will bring up an error
            print 'its only lowercase'
        else:
            #if its only uppercase you get an error
            print 'only uppercase'
        print self.lineEdit.text()

    def softwareBtn(self):
        '''will unlock the create button'''
        self.CreateBtn.setEnabled(True)

    def CreateBtnEnding(self):
        '''for the file to get added into'''
        #get new path to artdepot folder
        ArtDepotFolder = 'C:/Dev/fiea-capstones/AxolotlProductions/ArtDepot'
        os.chdir(ArtDepotFolder)
        print(os.getcwd())

        #add on either the Characters, Environment, or Props folder
        path = os.path.join(ArtDepotFolder, self.assetType)
        os.chdir(path)
        print (os.getcwd())

        #copy and rename AssetName folder according to what the user has put into the text box
        shutil.copytree(path + '/AssetName', path + '/' + str(self.lineEdit.text()))
        

        #Add and rename folder in maya path
        os.rename('C:/Dev/fiea-capstones/AxolotlProductions/ArtDepot/{}/{}/Maya/SM_Default.ma'.format(self.assetType, self.lineEdit.text()), 'C:/Dev/fiea-capstones/AxolotlProductions/ArtDepot/{}/{}/Maya/SM_{}.ma'.format(self.assetType, self.lineEdit.text(), self.lineEdit.text()))
        #Add and rename folder in Zbrush path
        os.rename('C:/Dev/fiea-capstones/AxolotlProductions/ArtDepot/{}/{}/ZBrush/SM_Default.ZPR'.format(self.assetType, self.lineEdit.text()), 'C:/Dev/fiea-capstones/AxolotlProductions/ArtDepot/{}/{}/ZBrush/SM_{}.ZPR'.format(self.assetType, self.lineEdit.text(), self.lineEdit.text()))

        #Add and rename folder in Photoshop path
        os.rename('C:/Dev/fiea-capstones/AxolotlProductions/ArtDepot/{}/{}/Photoshop/T_Default.psd'.format(self.assetType, self.lineEdit.text()), 'C:/Dev/fiea-capstones/AxolotlProductions/ArtDepot/{}/{}/Photoshop/T_{}.psd'.format(self.assetType, self.lineEdit.text(), self.lineEdit.text()))

        #Add and rename folder in Photoshop path
        os.rename('C:/Dev/fiea-capstones/AxolotlProductions/ArtDepot/{}/{}/Illustrator/T_Default.ai'.format(self.assetType, self.lineEdit.text()), 'C:/Dev/fiea-capstones/AxolotlProductions/ArtDepot/{}/{}/Illustrator/T_{}.ai'.format(self.assetType, self.lineEdit.text(), self.lineEdit.text()))

        #will open up maya
        if self.MayaRadioButton.isChecked():
            mayaFile = 'C:/Dev/fiea-capstones/AxolotlProductions/ArtDepot/{}/{}/Maya/SM_{}.ma'.format(self.assetType, self.lineEdit.text(), self.lineEdit.text())
            os.chmod(mayaFile, 0664)
            os.startfile(mayaFile)
                
        #will open up ZBrush
        elif self.ZBrushRadioBtn.isChecked():
            ZbrushFile = 'C:/Dev/fiea-capstones/AxolotlProductions/ArtDepot/{}/{}/ZBrush/SM_{}.ZPR'.format(self.assetType, self.lineEdit.text(), self.lineEdit.text())
            os.chmod(ZbrushFile, 0664)
            os.startfile(ZbrushFile)

        #Will open up photoshop
        elif self.PhotoshopRadioBtn.isChecked():
            PSDFile = 'C:/Dev/fiea-capstones/AxolotlProductions/ArtDepot/{}/{}/Photoshop/T_{}.psd'.format(self.assetType, self.lineEdit.text(), self.lineEdit.text())
            os.chmod(PSDFile, 0664)
            os.startfile(PSDFile)

        # Will open up Illustrator
        else:
            AIFile = 'C:/Dev/fiea-capstones/AxolotlProductions/ArtDepot/{}/{}/Illustrator/T_{}.ai'.format(self.assetType, self.lineEdit.text(), self.lineEdit.text())
            os.chmod(AIFile, 0664)
            os.startfile(AIFile)
            
        sys.exit(app.exec_())

       
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
