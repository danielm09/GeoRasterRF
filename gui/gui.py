from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QDialog, QMessageBox
from PyQt5.QtGui import QIntValidator
from core import classification



class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        """MainWindow constructor."""
        super().__init__()
        #self.resize(529, 772)
        self.center()
        self.adjustSize()
        self.setWindowTitle("Random Forest Classifier")
        self.setWindowIcon(QtGui.QIcon('icon.svg'))

        #menubar
        self.menubar = QtWidgets.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 504, 20))

        self.About = QtWidgets.QMenu(self.menubar)
        self.About.setTitle("About")
        self.setMenuBar(self.menubar)
        self.actionsub = QtWidgets.QAction(self)
        self.actionsub.setText("Random Forest Documentation")
        self.actionsub2 = QtWidgets.QAction(self)
        self.actionsub2.setText("Outputs")
        self.actionsub3 = QtWidgets.QAction(self)
        self.actionsub3.setText("Contact")
        self.About.addAction(self.actionsub)
        self.About.addAction(self.actionsub2)
        self.About.addAction(self.actionsub3)
        self.menubar.addAction(self.About.menuAction())
        self.actionsub.triggered.connect(self.on_about)
        self.actionsub2.triggered.connect(self.on_aboutoutputs)
        self.actionsub3.triggered.connect(self.on_contact)
        

        #centralwidget
        self.centralwidget = QtWidgets.QWidget()
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.gridLayout_5 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)

        self.titleAndIconContainer = QtWidgets.QWidget(self.layoutWidget)
        self.gridLayout_x = QtWidgets.QGridLayout(self.titleAndIconContainer)
        self.gridLayout_x.setContentsMargins(0, 0, 0, 0)
        


        #groupboxes
        self.groupBox_inputs = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox_inputs.setTitle("Inputs")
        self.gridLayout_1 = QtWidgets.QGridLayout(self.groupBox_inputs)
        

        self.groupBox_clfMode = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox_clfMode.setTitle("Select Classification Mode")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_clfMode)
        
        #tab
        self.tabs_input = QtWidgets.QTabWidget(self.groupBox_inputs)
        self.image_tab = QtWidgets.QWidget()
        self.image_tab.setAutoFillBackground(True)
        self.validation_tab = QtWidgets.QWidget()
        self.validation_tab.setAutoFillBackground(True)
        self.tabs_input.addTab(self.image_tab,'Image')
        self.tabs_input.addTab(self.validation_tab,'CSV/Validation')
        self.gridLayout_1_1 = QtWidgets.QGridLayout(self.image_tab)
        self.gridLayout_1_2 = QtWidgets.QGridLayout(self.validation_tab)
                
        #labels
        self.label_progTitle = QtWidgets.QLabel(self.layoutWidget,text = "Random Forest Classifier\n v1.1", font=QtGui.QFont('Sans',25))
        self.label_progTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.label_progIcon = QtWidgets.QLabel(self.layoutWidget)
        pixmap = QtGui.QPixmap('icon.svg')
        self.label_progIcon.setPixmap(pixmap)
        self.label_progIcon.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.label_progIcon.setMaximumSize(100,100)
        self.label_progIcon.setScaledContents(True)
        self.label_inpImg = QtWidgets.QLabel(self.image_tab,text = "Input Image")
        self.label_inpBlocks = QtWidgets.QLabel(self.image_tab,text = "Number of Blocks ( >1)")
        self.label_outImgC = QtWidgets.QLabel(self.image_tab,text = "Output Image (Class)")
        self.label_outImgP = QtWidgets.QLabel(self.groupBox_inputs,text = "Ouput Image (Probabilities)")
        self.label_inpCsv = QtWidgets.QLabel(self.validation_tab,text = "Input CSV")
        self.label_inpCsvVar = QtWidgets.QLabel(self.validation_tab,text = "Variables")
        self.label_inpCsvLabel = QtWidgets.QLabel(self.validation_tab,text = "Label")
        self.label_outCsv = QtWidgets.QLabel(self.validation_tab,text = "Output Predictions")
        self.label_outCMatrix = QtWidgets.QLabel(self.validation_tab,text = "Output Confusion Matrix")
        self.label_importTrain = QtWidgets.QLabel(self.groupBox_clfMode,text = "Import training data")
        self.label_trainVar = QtWidgets.QLabel(self.groupBox_clfMode,text = "Training Variables")
        self.label_trainLabel = QtWidgets.QLabel(self.groupBox_clfMode,text = "Training Labels")
        self.label_importClf = QtWidgets.QLabel(self.groupBox_clfMode,text = "Import Classifier")
        
        #buttons
        self.browseInpImg = QtWidgets.QPushButton(self.image_tab,text = "Browse")
        self.saveOutImgC = QtWidgets.QPushButton(self.image_tab,text = "Save")
        self.saveOutImgP = QtWidgets.QPushButton(self.image_tab,text = "Save")
        self.browseInpCsv = QtWidgets.QPushButton(self.validation_tab,text = "Browse")
        self.selectCsvVars = QtWidgets.QPushButton(self.validation_tab,text = "Select From List")
        self.saveOutCsv = QtWidgets.QPushButton(self.validation_tab,text = "Save")
        self.saveOutCMatrix = QtWidgets.QPushButton(self.validation_tab,text = "Save")
        self.browseTrain = QtWidgets.QPushButton(self.groupBox_clfMode,text = "Browse")
        self.browseClf = QtWidgets.QPushButton(self.groupBox_clfMode,text = "Browse")
        self.selectVars = QtWidgets.QPushButton(self.groupBox_clfMode,text = "Select From List")
        self.setClfParameters = QtWidgets.QPushButton(text = "Set Random Forest Parameters")
        self.runClf = QtWidgets.QPushButton(text = "Run")

        #lineEdits
        self.lineEdit_inpImg = QtWidgets.QLineEdit(self.image_tab)
        self.lineEdit_inpBlocks = QtWidgets.QLineEdit(self.image_tab)
        self.lineEdit_outImgC = QtWidgets.QLineEdit(self.image_tab)
        self.lineEdit_outImgP = QtWidgets.QLineEdit(self.image_tab)
        self.lineEdit_inpCsv = QtWidgets.QLineEdit(self.validation_tab)
        self.lineEdit_csvVar = QtWidgets.QLineEdit(self.validation_tab)
        self.lineEdit_csvLabel = QtWidgets.QLineEdit(self.validation_tab)
        self.lineEdit_outCsv = QtWidgets.QLineEdit(self.validation_tab)
        self.lineEdit_outCMatrix = QtWidgets.QLineEdit(self.validation_tab)
        self.lineEdit_importTrain = QtWidgets.QLineEdit(self.groupBox_clfMode)
        self.lineEdit_trainVar = QtWidgets.QLineEdit(self.groupBox_clfMode)
        self.lineEdit_trainLabel = QtWidgets.QLineEdit(self.groupBox_clfMode)
        self.lineEdit_importClf = QtWidgets.QLineEdit(self.groupBox_clfMode)

        #radiobuttons
        self.radioButton_train = QtWidgets.QRadioButton(self.groupBox_clfMode)
        self.radioButton_train.setText("Train Classifier")
        self.radioButton_importClf = QtWidgets.QRadioButton(self.groupBox_clfMode)
        self.radioButton_importClf.setText("Import Classifier")
        self.radioButton_image = QtWidgets.QRadioButton(self.groupBox_inputs)
        self.radioButton_image.setText("Classify image")
        self.radioButton_validation = QtWidgets.QRadioButton(self.groupBox_inputs)
        self.radioButton_validation.setText("Classify CSV (Validation)")
        self.radioButton_imgvalid = QtWidgets.QRadioButton(self.groupBox_inputs)
        self.radioButton_imgvalid.setText("Classify both")

        #checkbox
        self.check_csvlabel = QtWidgets.QCheckBox(self.validation_tab,text="No Label")
        self.check_csvlabel.setChecked(False)


        #layout
        self.gridLayout_x.addWidget(self.label_progIcon, 0, 0, 1, 1)
        self.gridLayout_x.addWidget(self.label_progTitle, 0, 1, 1, 1)

        self.gridLayout_5.addWidget(self.titleAndIconContainer, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_inputs, 1, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_clfMode, 2, 0, 1, 1)
        self.gridLayout_5.addWidget(self.setClfParameters, 3, 0, 1, 1)
        self.gridLayout_5.addWidget(self.runClf, 4, 0, 1, 1)
        
        self.verticalLayout.addWidget(self.splitter)
        self.setCentralWidget(self.centralwidget)
        
                
        self.gridLayout_1.addWidget(self.radioButton_image,0,0)
        self.gridLayout_1.addWidget(self.radioButton_validation,0,1)
        self.gridLayout_1.addWidget(self.radioButton_imgvalid,0,2)
        self.gridLayout_1.addWidget(self.tabs_input,1,0,2,3)
        
        

        ##start of group box input##
        #image tab
        self.gridLayout_1_1.addWidget(self.label_inpImg,0,0,1,1)
        self.gridLayout_1_1.addWidget(self.lineEdit_inpImg,0,1,1,1)
        self.gridLayout_1_1.addWidget(self.browseInpImg,0,2,1,1)
        
        self.gridLayout_1_1.addWidget(self.label_inpBlocks,1,0,1,1)
        self.gridLayout_1_1.addWidget(self.lineEdit_inpBlocks,1,1,1,1)
        
        self.gridLayout_1_1.addWidget(self.label_outImgC,2,0,1,1)
        self.gridLayout_1_1.addWidget(self.lineEdit_outImgC,2,1,1,1)
        self.gridLayout_1_1.addWidget(self.saveOutImgC,2,2,1,1)      
       
        self.gridLayout_1_1.addWidget(self.label_outImgP,3,0,1,1)
        self.gridLayout_1_1.addWidget(self.lineEdit_outImgP,3,1,1,1)
        self.gridLayout_1_1.addWidget(self.saveOutImgP,3,2,1,1)
        #csv tab
        self.gridLayout_1_2.addWidget(self.label_inpCsv,0,0,1,1)
        self.gridLayout_1_2.addWidget(self.lineEdit_inpCsv,0,1,1,1)
        self.gridLayout_1_2.addWidget(self.browseInpCsv,0,2,1,1)
      
        self.gridLayout_1_2.addWidget(self.label_inpCsvVar,1,0,1,1)
        self.gridLayout_1_2.addWidget(self.lineEdit_csvVar,1,1,1,1)
        self.gridLayout_1_2.addWidget(self.selectCsvVars,1,2,1,1)
                
        self.gridLayout_1_2.addWidget(self.label_inpCsvLabel,2,0,1,1)
        self.gridLayout_1_2.addWidget(self.lineEdit_csvLabel,2,1,1,1)
        self.gridLayout_1_2.addWidget(self.check_csvlabel,2,2,1,1)

        self.gridLayout_1_2.addWidget(self.label_outCsv,3,0,1,1)
        self.gridLayout_1_2.addWidget(self.lineEdit_outCsv,3,1,1,1)
        self.gridLayout_1_2.addWidget(self.saveOutCsv,3,2,1,1)
        
        self.gridLayout_1_2.addWidget(self.label_outCMatrix,4,0,1,1)
        self.gridLayout_1_2.addWidget(self.lineEdit_outCMatrix,4,1,1,1)
        self.gridLayout_1_2.addWidget(self.saveOutCMatrix,4,2,1,1)
        
       ##end of groupbox input##

       ##start of groupbox clfmode##

        self.gridLayout_2.addWidget(self.radioButton_train,0,0,1,1)
        
        self.gridLayout_2.addWidget(self.label_importTrain,1,0,1,1)
        self.gridLayout_2.addWidget(self.lineEdit_importTrain,1,1,1,1)
        self.gridLayout_2.addWidget(self.browseTrain,1,2,1,1)
        
        self.gridLayout_2.addWidget(self.label_trainVar,2,0,1,1)
        self.gridLayout_2.addWidget(self.lineEdit_trainVar,2,1,1,1)
        self.gridLayout_2.addWidget(self.selectVars,2,2,1,1)
        
        self.gridLayout_2.addWidget(self.label_trainLabel,3,0,1,1)
        self.gridLayout_2.addWidget(self.lineEdit_trainLabel,3,1,1,1)

        self.gridLayout_2.addWidget(self.radioButton_importClf,4,0,1,1)
        
        self.gridLayout_2.addWidget(self.label_importClf,5,0,1,1)
        self.gridLayout_2.addWidget(self.lineEdit_importClf,5,1,1,1)
        self.gridLayout_2.addWidget(self.browseClf,5,2,1,1)

        ##end of groupbox clfmode##
       

        #other stuff
        self.variables = ''
        self.labels = ''
        classification.no_label = False

        #limit nblocs to only integers
        self.onlyInt = QIntValidator(2, 100000)
        self.lineEdit_inpBlocks.setValidator(self.onlyInt)
        
        #deactivate elements
        self.tabs_input.setEnabled(False)
        self.tabs_input.setTabEnabled(0, False)
        self.tabs_input.setTabEnabled(1, False)
        self.lineEdit_importTrain.setEnabled(False)
        self.lineEdit_trainVar.setEnabled(False)
        self.lineEdit_trainLabel.setEnabled(False)
        self.lineEdit_importClf.setEnabled(False)
        self.browseTrain.setEnabled(False)
        self.selectVars.setEnabled(False)
        self.browseClf.setEnabled(False)
        self.setClfParameters.setEnabled(False)
        self.runClf.setEnabled(False)
        
        

        #click and connect
        self.radioButton_train.toggled.connect(self.importTraining)
        self.radioButton_importClf.toggled.connect(self.importClassifier)
        self.radioButton_image.toggled.connect(self.classifyImage)
        self.radioButton_validation.toggled.connect(self.classifyCsv)
        self.radioButton_imgvalid.toggled.connect(self.classifyBoth)
        self.browseInpImg.clicked.connect(self.selectFile)
        self.saveOutImgC.clicked.connect(self.saveFileC)
        self.saveOutImgP.clicked.connect(self.saveFileP)
        self.browseInpCsv.clicked.connect(self.browseCsv)
        self.selectCsvVars.clicked.connect(self.selectFromList2)
        self.check_csvlabel.stateChanged.connect(self.check_nocsvlabel)
        self.saveOutCsv.clicked.connect(self.saveCsv)
        self.saveOutCMatrix.clicked.connect(self.saveCMatrix)
        self.browseTrain.clicked.connect(self.selectFileTrain)
        self.browseClf.clicked.connect(self.selectFileClf)
        self.selectVars.clicked.connect(self.selectFromList)
        self.setClfParameters.clicked.connect(self.pressedSelectClfPar)
        self.runClf.clicked.connect(self.pressedRun)


        #initialize clf parameters as empty, in case user wants to run with default
        classification.estimators_user=''
        classification.maxfeatures_user=''
        classification.njobs_user=''
        classification.bootstrap_user=''
        classification.criterion_user=''
        classification.max_depth_user=''
        classification.minsamplessplit_user=''
        classification.minsamplesleaf_user=''
        classification.minweightleaf_user=''
        classification.maxleafnodes_user=''
        classification.minimpdecrease_user=''
        classification.minimpsplit_user=''
        classification.oobscore_user=''
        #classification.randomstate_user=self.lineEdit_randomstate.text() #to be implemented
        classification.verbose_user=''
        classification.warmstart_user=''
        #classification.classweight_user=self.lineEdit_classweight.text() # to be implemented
        classification.ccpalpha_user=''
        classification.maxsamples_user=''

    def center(self):
        qr = self.frameGeometry() #gets geometry of the main window
        cp = QtWidgets.QDesktopWidget().availableGeometry().center() #gets geometry of the screen and returns the center
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    def importTraining(self, enabled):
        if enabled:
            self.lineEdit_importTrain.setEnabled(True)
            self.lineEdit_trainVar.setEnabled(True)
            self.lineEdit_trainLabel.setEnabled(True)
            self.lineEdit_importClf.setEnabled(False)
            self.browseTrain.setEnabled(True)
            self.selectVars.setEnabled(True)
            self.browseClf.setEnabled(False)
            self.setClfParameters.setEnabled(True)
            if self.radioButton_image.isChecked() or self.radioButton_validation.isChecked() or self.radioButton_imgvalid.isChecked():
                self.runClf.setEnabled(True)
            
    def importClassifier(self, enabled):
        if enabled:
            self.lineEdit_importClf.setEnabled(True)
            self.lineEdit_importTrain.setEnabled(False)
            self.lineEdit_trainVar.setEnabled(False)
            self.lineEdit_trainLabel.setEnabled(False)
            self.browseTrain.setEnabled(False)
            self.selectVars.setEnabled(False)
            self.browseClf.setEnabled(True)
            self.setClfParameters.setEnabled(False)
            if self.radioButton_image.isChecked() or self.radioButton_validation.isChecked() or self.radioButton_imgvalid.isChecked():
                self.runClf.setEnabled(True)
            

    def classifyImage(self,enabled):
        if enabled:
            self.tabs_input.setEnabled(True)
            self.tabs_input.setTabEnabled(0, True)
            self.tabs_input.setTabEnabled(1, False)
            if self.radioButton_importClf.isChecked() or self.radioButton_train.isChecked():
                self.runClf.setEnabled(True)
            self.tabs_input.setCurrentIndex(0)
            
    def classifyCsv(self,enabled):
        if enabled:
            self.tabs_input.setEnabled(True)
            self.tabs_input.setTabEnabled(1, True)
            self.tabs_input.setTabEnabled(0, False)
            if self.radioButton_importClf.isChecked() or self.radioButton_train.isChecked():
                self.runClf.setEnabled(True)
            self.tabs_input.setCurrentIndex(1)

    def classifyBoth(self,enabled):
        if enabled:
            self.tabs_input.setEnabled(True)
            self.tabs_input.setTabEnabled(0, True)
            self.tabs_input.setTabEnabled(1, True)
            if self.radioButton_importClf.isChecked() or self.radioButton_train.isChecked():
                self.runClf.setEnabled(True)

    def selectFile(self):

        filename = QFileDialog.getOpenFileName(None, "Browse input image", "", "Image (*.tif *.png *.jpg *.bmp *.jpeg)")
        self.lineEdit_inpImg.setText(filename[0])            
        
    def saveFileC(self):

        filename = QFileDialog.getSaveFileName(None, "Save output image (class)", "", "Image (*.tif *.png *.jpg *.bmp *.jpeg)")
        self.lineEdit_outImgC.setText(filename[0])
        
    def saveFileP(self):

        filename = QFileDialog.getSaveFileName(None, "Save output image (prob.)", "", "Image (*.tif *.png *.jpg *.bmp *.jpeg)")
        self.lineEdit_outImgP.setText(filename[0])

    def browseCsv(self):
        filename = QFileDialog.getOpenFileName(None, "Browse input CSV", "", "CSV (*.csv)")
        self.lineEdit_inpCsv.setText(filename[0])

    def saveCsv(self):

        filename = QFileDialog.getSaveFileName(None, "Save output predictions", "", "CSV (*.csv)")
        self.lineEdit_outCsv.setText(filename[0])
        
    def saveCMatrix(self):

        filename = QFileDialog.getSaveFileName(None, "Save Confusion Matrix", "", "CSV (*.csv)")
        self.lineEdit_outCMatrix.setText(filename[0])

    def selectFileTrain(self):

        filename = QFileDialog.getOpenFileName(None, "Browse train file", "", "CSV (*.csv)")
        self.lineEdit_importTrain.setText(filename[0])

    def selectFileClf(self):

        filename = QFileDialog.getOpenFileName(None, "Browse classifier", "","Pickle (*.pickle)")
        self.lineEdit_importClf.setText(filename[0])

    @QtCore.pyqtSlot(str,str)
    def setVarLabels(self, variables, labels):

        self.variables = variables
        self.labels = labels
        self.lineEdit_trainVar.setText(self.variables)
        self.lineEdit_trainLabel.setText(self.labels)

    def setVarLabels2(self, variables, labels):

        #self.variables_csv = variables
        #self.labels_csv = labels
        self.lineEdit_csvVar.setText(variables)
        self.lineEdit_csvLabel.setText(labels)

    def selectFromList(self):

        if self.lineEdit_importTrain.text():
                
            classification.csv_file=self.lineEdit_importTrain.text()
            #print(classification.getColumns())

            
            self.dialog = DialogWindow(classification.getColumns(),False)
            self.dialog.submitted.connect(self.setVarLabels)
            self.dialog.show()
        else:
            msg = QMessageBox()
            msg.setWindowTitle('Error')
            msg.setText('No train CSV file selected')
            msg.setTextFormat(QtCore.Qt.MarkdownText)
            msg.setIcon(QMessageBox.Critical)
            x = msg.exec_()

    def selectFromList2(self):
        
        if self.lineEdit_inpCsv.text():
            
            classification.csv_file=self.lineEdit_inpCsv.text()
            #print(classification.getColumns())

            
            self.dialog_x = DialogWindow(classification.getColumns(),self.check_csvlabel.isChecked())
            self.dialog_x.submitted.connect(self.setVarLabels2)
            self.dialog_x.show()
        else:
            msg = QMessageBox()
            msg.setWindowTitle('Error')
            msg.setText('No input CSV selected')
            msg.setTextFormat(QtCore.Qt.MarkdownText)
            msg.setIcon(QMessageBox.Critical)
            x = msg.exec_()

    def check_nocsvlabel(self):
        if self.check_csvlabel.isChecked():
            classification.no_label = True
            self.lineEdit_csvLabel.setText('')
            self.lineEdit_csvLabel.setEnabled(False)
            self.lineEdit_outCMatrix.setEnabled(False)
            self.saveOutCMatrix.setEnabled(False)
        else:
            classification.no_label = False
            self.lineEdit_csvLabel.setEnabled(True)
            self.lineEdit_outCMatrix.setEnabled(True)
            self.saveOutCMatrix.setEnabled(True)
            
    def pressedSelectClfPar(self):
        self.dialog2 = DialogWindow2()
        #self.dialog2
        self.dialog2.show()
        

    def pressedRun(self):

        #pass classification mode
        if self.radioButton_train.isChecked():
            classification.clfMode = 1
            classification.treino = self.lineEdit_importTrain.text()
            classification.variables = self.lineEdit_trainVar.text().split(sep=',')
            classification.labelCod = self.lineEdit_trainLabel.text()
        else:
            classification.clfMode = 2
            classification.clfPickle = self.lineEdit_importClf.text()

        if self.radioButton_image.isChecked():
            classification.inputType = 1 #1 - only image

            classification.fn=self.lineEdit_inpImg.text()
            classification.blocks=int(self.lineEdit_inpBlocks.text())
            classification.outRaster=self.lineEdit_outImgC.text()
            classification.outRaster2=self.lineEdit_outImgP.text()

        if self.radioButton_validation.isChecked():
            classification.inputType = 2 #2 - only csv

            classification.input_csv=self.lineEdit_inpCsv.text()
            classification.csv_vars=self.lineEdit_csvVar.text().split(sep=',')
            classification.csv_labels=self.lineEdit_csvLabel.text()
            classification.out_csv_pred=self.lineEdit_outCsv.text()
            classification.out_csv_cmatrix=self.lineEdit_outCMatrix.text()

        if self.radioButton_imgvalid.isChecked():
            classification.inputType = 3 #3 - both image and csv

            classification.fn=self.lineEdit_inpImg.text()
            classification.blocks=int(self.lineEdit_inpBlocks.text())
            classification.outRaster=self.lineEdit_outImgC.text()
            classification.outRaster2=self.lineEdit_outImgP.text()
            classification.input_csv=self.lineEdit_inpCsv.text()
            classification.csv_vars=self.lineEdit_csvVar.text().split(sep=',')
            classification.csv_labels=self.lineEdit_csvLabel.text()
            classification.out_csv_pred=self.lineEdit_outCsv.text()
            classification.out_csv_cmatrix=self.lineEdit_outCMatrix.text()

        #run script
        try:
            classification.runScript()
        except Exception as e:
            print('Error:')
            print(e)
            #raise SystemExit
            

        
    def on_about(self):
        msg = QMessageBox()
        msg.setWindowTitle('About')
        msg.setText('This Random Forest implementation is based on Python Scikit-learn. Detailed information can be found at the following link: https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html')
        msg.setTextFormat(QtCore.Qt.MarkdownText)
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()
        
    def on_aboutoutputs(self):
        self.dialog3 = DialogWindow3()
        self.dialog3.show()

    def on_contact(self):
        msg = QMessageBox()
        msg.setWindowTitle('Contact')
        msg.setText('Developed by Daniel Moraes (https://github.com/danielm09/)')
        msg.setTextFormat(QtCore.Qt.MarkdownText)
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()
    
        

class DialogWindow(QtWidgets.QWidget):

    submitted = QtCore.pyqtSignal(str, str)

    def __init__(self, listitems,is_nolabel_checked):
        super().__init__()
        self.resize(777, 566)
        self.setWindowTitle("Select Variables and Labels")
        self.list1 = QtWidgets.QListWidget()
        self.list1.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
       
        self.list2 = QtWidgets.QListWidget()
        
        #block list2 if user sets no label to True
        if is_nolabel_checked:
            self.list2.setEnabled(False)

        i = 0
        for elem in listitems:
            
            item = QtWidgets.QListWidgetItem()
            self.list1.addItem(item)
            item2 = QtWidgets.QListWidgetItem()
            self.list2.addItem(item2)
            item = self.list1.item(i)
            item2 = self.list2.item(i)
            item.setText(str(elem))
            item2.setText(str(elem))
            i = i+1
        i = None
                          
        self.cancel_button = QtWidgets.QPushButton('Cancel')
        self.submit_button = QtWidgets.QPushButton('Submit')

        self.setLayout(QtWidgets.QFormLayout())
        self.layout().addRow('Select Variables', self.list1)
        self.layout().addRow('Select Label', self.list2)
        buttons = QtWidgets.QWidget()
        buttons.setLayout(QtWidgets.QHBoxLayout())
        buttons.layout().addWidget(self.cancel_button)
        buttons.layout().addWidget(self.submit_button)
        self.layout().addRow('', buttons)

        self.submit_button.clicked.connect(self.on_submit)
        self.cancel_button.clicked.connect(self.close)


    def on_submit(self):
        
        #convert to string
        variables_array = [x.data() for x in self.list1.selectedIndexes()]
        variables_str = ''
        for elem in variables_array:
            variables_str = variables_str + str(elem)+ ','

        variables_str = variables_str[:-1]

        if self.list2.selectedIndexes():
            labels_array = [x.data() for x in self.list2.selectedIndexes()]
            labels_str = str(labels_array[0])
        else:
            labels_str = ''
        
        
        self.submitted.emit(variables_str,labels_str)
        self.close()


class DialogWindow2(QtWidgets.QWidget):

    #submitted = QtCore.pyqtSignal(str, str)

    def __init__(self):
        super().__init__()
        self.resize(300, 566)
        self.setWindowTitle("Classification Parameters")

        self.groupboxMain = QtWidgets.QGroupBox()
        self.groupboxMain.setTitle('Main')
        self.groupboxSecondary = QtWidgets.QGroupBox()
        self.groupboxSecondary.setTitle('Secondary')
        self.groupboxObs = QtWidgets.QGroupBox()
        self.groupboxObs.setTitle('Observations')

        self.gridLayout_1 = QtWidgets.QGridLayout(self.groupboxMain)
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupboxSecondary)
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupboxObs)

        self.n_estimators_label = QtWidgets.QLabel(self.groupboxMain,text="Number of trees")
        self.lineEdit_estimators = QtWidgets.QLineEdit(self.groupboxMain)
        self.max_features_label = QtWidgets.QLabel(self.groupboxMain,text="Max features")
        self.lineEdit_maxfeatures = QtWidgets.QLineEdit(self.groupboxMain)
        self.njobs_label = QtWidgets.QLabel(self.groupboxMain,text="Number of jobs (processor usage)")
        self.lineEdit_njobs = QtWidgets.QLineEdit(self.groupboxMain)
        
        
        self.bootstrap_label = QtWidgets.QLabel(self.groupboxSecondary,text="Bootstrap")
        self.lineEdit_bootstrap = QtWidgets.QLineEdit(self.groupboxSecondary)
        self.criterion_label = QtWidgets.QLabel(self.groupboxSecondary,text="Criterion")
        self.lineEdit_criterion = QtWidgets.QLineEdit(self.groupboxSecondary)
        self.maxdepth_label = QtWidgets.QLabel(self.groupboxSecondary,text="Max. depth")
        self.lineEdit_maxdepth = QtWidgets.QLineEdit(self.groupboxSecondary)
        self.minsamplessplit_label = QtWidgets.QLabel(self.groupboxSecondary,text="Min. samples split")
        self.lineEdit_minsamplessplit = QtWidgets.QLineEdit(self.groupboxSecondary)
        self.minsamplesleaf_label = QtWidgets.QLabel(self.groupboxSecondary,text="Min. samples leaf")
        self.lineEdit_minsamplesleaf = QtWidgets.QLineEdit(self.groupboxSecondary)
        self.minweightfleaf_label = QtWidgets.QLabel(self.groupboxSecondary,text="Min. weight fraction leaf")
        self.lineEdit_minweightfleaf = QtWidgets.QLineEdit(self.groupboxSecondary)
        self.maxleafnodes_label = QtWidgets.QLabel(self.groupboxSecondary,text="Max. leaf nodes")
        self.lineEdit_maxleafnodes = QtWidgets.QLineEdit(self.groupboxSecondary)
        self.minimpdecrease_label = QtWidgets.QLabel(self.groupboxSecondary,text="Min. impurity decrease")
        self.lineEdit_minimpdecrease = QtWidgets.QLineEdit(self.groupboxSecondary)
        self.minimpsplit_label = QtWidgets.QLabel(self.groupboxSecondary,text="Min. impurity split")
        self.lineEdit_minimpsplit = QtWidgets.QLineEdit(self.groupboxSecondary)
        self.oobscore_label = QtWidgets.QLabel(self.groupboxSecondary,text="Out of bag score")
        self.lineEdit_oobscore = QtWidgets.QLineEdit(self.groupboxSecondary)
        self.randomstate_label = QtWidgets.QLabel(self.groupboxSecondary,text="Random state*")
        self.lineEdit_randomstate = QtWidgets.QLineEdit(self.groupboxSecondary)
        self.verbose_label = QtWidgets.QLabel(self.groupboxSecondary,text="Verbose")
        self.lineEdit_verbose = QtWidgets.QLineEdit(self.groupboxSecondary)
        self.warmstart_label = QtWidgets.QLabel(self.groupboxSecondary,text="Warm start")
        self.lineEdit_warmstart = QtWidgets.QLineEdit(self.groupboxSecondary)
        self.classweight_label = QtWidgets.QLabel(self.groupboxSecondary,text="Class weight*")
        self.lineEdit_classweight = QtWidgets.QLineEdit(self.groupboxSecondary)
        self.ccpalpha_label = QtWidgets.QLabel(self.groupboxSecondary,text="CCP alpha")
        self.lineEdit_ccpalpha = QtWidgets.QLineEdit(self.groupboxSecondary)
        self.maxsamples_label = QtWidgets.QLabel(self.groupboxSecondary,text="Max. samples")
        self.lineEdit_maxsamples = QtWidgets.QLineEdit(self.groupboxSecondary)

        self.obs1_label = QtWidgets.QLabel(self.groupboxObs,text="1) Leave empty to use default")
        self.obs2_label = QtWidgets.QLabel(self.groupboxObs,text="2) Use Number of jobs = -1 to use all CPUs")
        self.obs3_label = QtWidgets.QLabel(self.groupboxObs,text="\n*This version does not support setting such parameters")
        

        self.gridLayout_1.addWidget(self.n_estimators_label,0,0,1,1)
        self.gridLayout_1.addWidget(self.lineEdit_estimators,0,1,1,1)
        self.gridLayout_1.addWidget(self.max_features_label,1,0,1,1)
        self.gridLayout_1.addWidget(self.lineEdit_maxfeatures,1,1,1,1)
        self.gridLayout_1.addWidget(self.njobs_label,2,0,1,1)
        self.gridLayout_1.addWidget(self.lineEdit_njobs,2,1,1,1)

        self.gridLayout_2.addWidget(self.bootstrap_label,0,0,1,1)
        self.gridLayout_2.addWidget(self.lineEdit_bootstrap,0,1,1,1)
        self.gridLayout_2.addWidget(self.criterion_label,1,0,1,1)
        self.gridLayout_2.addWidget(self.lineEdit_criterion,1,1,1,1)
        self.gridLayout_2.addWidget(self.maxdepth_label,2,0,1,1)
        self.gridLayout_2.addWidget(self.lineEdit_maxdepth,2,1,1,1)
        self.gridLayout_2.addWidget(self.minsamplessplit_label,3,0,1,1)
        self.gridLayout_2.addWidget(self.lineEdit_minsamplessplit,3,1,1,1)
        self.gridLayout_2.addWidget(self.minsamplesleaf_label,4,0,1,1)
        self.gridLayout_2.addWidget(self.lineEdit_minsamplesleaf,4,1,1,1)
        self.gridLayout_2.addWidget(self.minweightfleaf_label,5,0,1,1)
        self.gridLayout_2.addWidget(self.lineEdit_minweightfleaf,5,1,1,1)
        self.gridLayout_2.addWidget(self.maxleafnodes_label,6,0,1,1)
        self.gridLayout_2.addWidget(self.lineEdit_maxleafnodes,6,1,1,1)
        self.gridLayout_2.addWidget(self.minimpdecrease_label,7,0,1,1)
        self.gridLayout_2.addWidget(self.lineEdit_minimpdecrease,7,1,1,1)
        self.gridLayout_2.addWidget(self.minimpsplit_label,8,0,1,1)
        self.gridLayout_2.addWidget(self.lineEdit_minimpsplit,8,1,1,1)
        self.gridLayout_2.addWidget(self.oobscore_label,9,0,1,1)
        self.gridLayout_2.addWidget(self.lineEdit_oobscore,9,1,1,1)
        self.gridLayout_2.addWidget(self.randomstate_label,10,0,1,1)
        self.gridLayout_2.addWidget(self.lineEdit_randomstate,10,1,1,1)
        self.gridLayout_2.addWidget(self.verbose_label,11,0,1,1)
        self.gridLayout_2.addWidget(self.lineEdit_verbose,11,1,1,1)
        self.gridLayout_2.addWidget(self.warmstart_label,12,0,1,1)
        self.gridLayout_2.addWidget(self.lineEdit_warmstart,12,1,1,1)
        self.gridLayout_2.addWidget(self.classweight_label,13,0,1,1)
        self.gridLayout_2.addWidget(self.lineEdit_classweight,13,1,1,1)
        self.gridLayout_2.addWidget(self.ccpalpha_label,14,0,1,1)
        self.gridLayout_2.addWidget(self.lineEdit_ccpalpha,14,1,1,1)
        self.gridLayout_2.addWidget(self.maxsamples_label,15,0,1,1)
        self.gridLayout_2.addWidget(self.lineEdit_maxsamples,15,1,1,1)

        self.gridLayout_3.addWidget(self.obs1_label,0,0,1,1)
        self.gridLayout_3.addWidget(self.obs2_label,1,0,1,1)
        self.gridLayout_3.addWidget(self.obs3_label,3,0,1,1)
        
        self.cancel_button = QtWidgets.QPushButton('Cancel')
        self.submit_button = QtWidgets.QPushButton('Submit')
        self.help_button = QtWidgets.QPushButton('Help')

        self.setLayout(QtWidgets.QFormLayout())
        self.layout().addRow(self.groupboxMain)
        self.layout().addRow(self.groupboxSecondary)
        self.layout().addRow(self.groupboxObs)
               
        buttons = QtWidgets.QWidget()
        buttons.setLayout(QtWidgets.QHBoxLayout())
        buttons.layout().addWidget(self.cancel_button)
        buttons.layout().addWidget(self.submit_button)
        buttons.layout().addWidget(self.help_button)
        self.layout().addRow('', buttons)

        self.submit_button.clicked.connect(self.on_submit)
        self.cancel_button.clicked.connect(self.close)
        self.help_button.clicked.connect(self.on_help)

        #other configs
        self.lineEdit_randomstate.setEnabled(False)
        self.lineEdit_classweight.setEnabled(False)
        self.onlyInt = QIntValidator(1, 100000)
        self.onlyIntjobs = QIntValidator(-1, 100000)
        self.lineEdit_estimators.setValidator(self.onlyInt)
        self.lineEdit_maxdepth.setValidator(self.onlyInt)
        self.lineEdit_maxleafnodes.setValidator(self.onlyInt)
        self.lineEdit_njobs.setValidator(self.onlyIntjobs)
        self.lineEdit_verbose.setValidator(self.onlyInt)
        


    def on_submit(self):
        
        classification.estimators_user=self.lineEdit_estimators.text()
        classification.maxfeatures_user=self.lineEdit_maxfeatures.text()
        classification.njobs_user=self.lineEdit_njobs.text()
        classification.bootstrap_user=self.lineEdit_bootstrap.text()
        classification.criterion_user=self.lineEdit_criterion.text()
        classification.max_depth_user=self.lineEdit_maxdepth.text()
        classification.minsamplessplit_user=self.lineEdit_minsamplessplit.text()
        classification.minsamplesleaf_user=self.lineEdit_minsamplesleaf.text()
        classification.minweightleaf_user=self.lineEdit_minweightfleaf.text()
        classification.maxleafnodes_user=self.lineEdit_maxleafnodes.text()
        classification.minimpdecrease_user=self.lineEdit_minimpdecrease.text()
        classification.minimpsplit_user=self.lineEdit_minimpsplit.text()
        classification.oobscore_user=self.lineEdit_oobscore.text()
        #classification.randomstate_user=self.lineEdit_randomstate.text() #to be implemented
        classification.verbose_user=self.lineEdit_verbose.text()
        classification.warmstart_user=self.lineEdit_warmstart.text()
        #classification.classweight_user=self.lineEdit_classweight.text() # to be implemented
        classification.ccpalpha_user=self.lineEdit_ccpalpha.text()
        classification.maxsamples_user=self.lineEdit_maxsamples.text()
        
        self.close()

    def on_help(self):
        msg = QMessageBox()
        msg.setWindowTitle('Help')
        msg.setText('This Random Forest implementation is based on Python Scikit-learn. Detailed information can be found at the following link: https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html')
        msg.setTextFormat(QtCore.Qt.MarkdownText)
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()
        
class DialogWindow3(QtWidgets.QWidget):

    #submitted = QtCore.pyqtSignal(str, str)

    def __init__(self):
        super().__init__()
        self.resize(350, 200)
        self.setWindowTitle("About outputs")

        self.text_label = QtWidgets.QLabel(text="1) Output Class: The program will generate a raster file with 2 bands, where band 1 is the predicted class (most tree votes) and band 2 is the second most voted class\n")
        self.text_label.setWordWrap(True)
        self.text2_label = QtWidgets.QLabel(text="2) Output Probabilities: The program will output a one-band raster containing the difference between the highest and second highest class probabilites\n")
        self.text2_label.setWordWrap(True)
        self.text3_label = QtWidgets.QLabel(text="3) In order to generate images, the training labels should be integer, not string\n")
        self.text3_label.setWordWrap(True)
        self.text_label.setAlignment(QtCore.Qt.AlignJustify)
        self.text2_label.setAlignment(QtCore.Qt.AlignJustify)
        self.text3_label.setAlignment(QtCore.Qt.AlignJustify)
        self.Ok_button = QtWidgets.QPushButton('Ok')
        
        self.setLayout(QtWidgets.QFormLayout())
        self.layout().addRow(self.text_label)
        self.layout().addRow(self.text2_label)
        self.layout().addRow(self.text3_label)
        self.layout().addRow(self.Ok_button)

        self.Ok_button.clicked.connect(self.close)

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = MainWindow()
#     #ui = Ui_MainWindow()
#     #ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
