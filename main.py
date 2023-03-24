import os
import sys
import subprocess
from noises.impulse import *
from noises.Anisotropic import *
from noises.exponential import *
from noises.flimgrain import *
from noises.gamma import *
from noises.gaussian import *
from noises.pepper import *
from noises.periodic import *
from noises.poisson import *
from noises.rayleigh import *
from noises.speckle import *
from noises.uniform import *
# from noises.

from PyQt5.QtCore import Qt,QUrl
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QCheckBox,QFileDialog,QVBoxLayout,QFormLayout,QHBoxLayout,QGridLayout,QLineEdit
from PyQt5.QtGui import QPixmap,QFont,QFontDatabase,QDesktopServices
from PyQt5 import QtCore,QtWidgets
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QWidget, QGridLayout, QPushButton
from PyQt5.QtGui import QPixmap

from multiprocessing import Pool
# p = Pool(10)

flag=0
class ImageLabel(QLabel):
    def __init__(self):
        super().__init__()

        self.setAlignment(Qt.AlignCenter)
        self.setText('\n\n Drop Image Here \n\n')
        # self.setText.setSt
        self.setStyleSheet(
            
                "color: black;"
                "background-color:#ECF9FF;"
                             "border-style: dashed;"
                             "border-width: 5px;"
                             "border-color: black;"
                             "border-radius: 3px"
            
        )


    def setPixmap(self, image):
        super().setPixmap(image)

class Project(QWidget):
    def __init__(self):
        super().__init__()
        self.intitalizeUI()
        self.setAcceptDrops(True)
        

    def intitalizeUI(self): 
        self.setWindowTitle('Image Augment')
        self.addedimages=[]

        noises=['Impulse','Gaussian','Periodic','Speckle','Anisotropic','Exponential','Flimgrain','Gamma','Pepper','Poisson','Rayleigh','Uniform']
        
        self.chkbxs=[]
        self.labels=[]
        self.folder_dir='output/'

        self.main_container=QHBoxLayout()
        self.photoViewer = ImageLabel()
        self.labels.append(self.photoViewer)
        self.main_container.addWidget(self.photoViewer)        
        
        
        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.gird_generated = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea.setStyleSheet("background-color:#93BFCF")
        
        
        self.add_image_grid()
        
        
        self.main_container.addWidget(self.scrollArea)
        # self.scroll_area = QScrollArea(self)
        # self.grid_widget = QWidget()
        # self.grid_layout = QGridLayout(self.grid_widget)
        # self.scroll_area.setWidget(self.grid_widget)
        # self.load_images()

        # # Set the layout of the main widget
        # main_layout = QVBoxLayout(self)
        # main_layout.addWidget(self.scroll_area)
        
        
        
        
        
        
        

        button_gen = QPushButton('Generate', self)
        self.labels.append(button_gen)
        button_gen.clicked.connect(self.submit)
        button_gen.setStyleSheet("background-color : white;button_gen:hover")
        

        button_add = QPushButton('Add images', self)
        self.labels.append(button_add)
        button_add.clicked.connect(self.add_image)
        button_add.setStyleSheet("background-color : white")
        
        title_h_box = QHBoxLayout()
        title_h_box.addWidget(button_gen)
        # title_h_box.addStretch()
        title_h_box.addWidget(button_add)
        # title_h_box.addStretch()
        # title_h_box.setSpacing(60)
        
    
        title_v_box = QVBoxLayout()   
        title_v_box.setAlignment(Qt.AlignCenter)     
        text_noise=QLabel(self)
        text_noise.setText('Select noises to add')
        self.labels.append(text_noise)
        # text_noise.resize(100,100)
        title_v_box.addWidget(text_noise)
        # title_v_box.setStretchFactor(text_noise, 1)
        # hbox.setStretchFactor(line_edit, 1

        for label in noises:
            checkbox = QCheckBox(label, self)
            self.labels.append(checkbox)
            self.chkbxs.append(checkbox)
            title_v_box.addWidget(checkbox)
            title_v_box.setStretchFactor(checkbox, 1)

        self.checkbox_functions = {}
        self.checkbox_functions['Impulse'] = self.impulse
        self.checkbox_functions['Anisotropic'] = self.anisotropic
        self.checkbox_functions['Exponential'] = self.exponential
        self.checkbox_functions['Flimgrain'] = self.flimgrain
        self.checkbox_functions['Gamma'] = self.gamma
        self.checkbox_functions['Gaussian'] = self.gaussian
        self.checkbox_functions['Pepper'] = self.pepper
        self.checkbox_functions['Periodic'] = self.periodic
        self.checkbox_functions['Poisson'] = self.poisson
        self.checkbox_functions['Rayleigh'] = self.rayleigh
        self.checkbox_functions['Speckle'] = self.speckle
        self.checkbox_functions['Uniform'] = self.uniform


        title_v_box.addLayout(title_h_box)        
        self.main_container.addLayout(title_v_box)
        self.main_container.setStretchFactor(title_v_box, 1)
        
        self.styles()
        self.setLayout(self.main_container)
        self.show()

    
    def impulse(self):
        generatedimages = []
        for i in self.addedimages:
            generatedimages.append(impulse(i))
        for i in range(len(generatedimages)):
            print('output/impulse'+str(i+1)+'.jpg')
            cv2.imwrite('output/impulse'+str(i+1)+'.jpg',generatedimages[i])


    def anisotropic(self):
        generatedimages = []
        for i in self.addedimages:
            generatedimages.append(anisotropic(i))
        for i in range(len(generatedimages)):
            print('output/anisotropic'+str(i+1)+'.jpg')
            cv2.imwrite('output/anisotropic'+str(i+1)+'.jpg',generatedimages[i])

    def exponential(self):
        generatedimages = []
        for i in self.addedimages:
            generatedimages.append(exponential(i))
        for i in range(len(generatedimages)):
            print('output/exponential'+str(i+1)+'.jpg')
            cv2.imwrite('output/exponential'+str(i+1)+'.jpg',generatedimages[i])

    def flimgrain(self):
        generatedimages = []
        for i in self.addedimages:
            generatedimages.append(flimgrain(i))
        for i in range(len(generatedimages)):
            print('output/flimgrain'+str(i+1)+'.jpg')
            cv2.imwrite('output/flimgrain'+str(i+1)+'.jpg',generatedimages[i])

    def gamma(self):
        generatedimages = []
        for i in self.addedimages:
            generatedimages.append(gamma(i))
        for i in range(len(generatedimages)):
            print('output/gamma'+str(i+1)+'.jpg')
            cv2.imwrite('output/gamma'+str(i+1)+'.jpg',generatedimages[i])

    def gaussian(self):
        generatedimages = []
        for i in self.addedimages:
            generatedimages.append(gaussian(i))
        for i in range(len(generatedimages)):
            print('output/gaussian'+str(i+1)+'.jpg')
            cv2.imwrite('output/gaussian'+str(i+1)+'.jpg',generatedimages[i])

    def pepper(self):
        generatedimages = []
        for i in self.addedimages:
            generatedimages.append(pepper(i))
        for i in range(len(generatedimages)):
            print('output/pepper'+str(i+1)+'.jpg')
            cv2.imwrite('output/pepper'+str(i+1)+'.jpg',generatedimages[i])

    def periodic(self):
        generatedimages = []
        for i in self.addedimages:
            generatedimages.append(periodic(i))
        for i in range(len(generatedimages)):
            print("output/periodic"+str(i+1)+'.jpg')
            cv2.imwrite('output/periodic'+str(i+1)+'.jpg',generatedimages[i])

    def poisson(self):
        generatedimages = []
        for i in self.addedimages:
            generatedimages.append(poisson(i))
        for i in range(len(generatedimages)):
            print('output/poisson'+str(i+1)+'.jpg')
            cv2.imwrite('output/poisson'+str(i+1)+'.jpg',generatedimages[i])

    def rayleigh(self):
        generatedimages = []
        for i in self.addedimages:
            generatedimages.append(add_rayleigh_noise(i))
        for i in range(len(generatedimages)):
            print('output/rayleigh'+str(i+1)+'.jpg')
            cv2.imwrite('output/rayleigh'+str(i+1)+'.jpg',generatedimages[i])

    def speckle(self):
        generatedimages = []
        for i in self.addedimages:
            generatedimages.append(speckle(i))
        for i in range(len(generatedimages)):
            print('output/speckle'+str(i+1)+'.jpg')
            cv2.imwrite('output/speckle'+str(i+1)+'.jpg',generatedimages[i])

    def uniform(self):
        generatedimages = []
        for i in self.addedimages:
            generatedimages.append(uniform(i))
        for i in range(len(generatedimages)):
            print('output/uniform'+str(i+1)+'.jpg')
            cv2.imwrite('output/uniform'+str(i+1)+'.jpg',generatedimages[i])


    def submit(self):
        for widget in self.chkbxs:
            if isinstance(widget, QCheckBox) and widget.isChecked():
                label = widget.text()
                self.checkbox_functions[label]()
        to_open=os.path.abspath(self.folder_dir)
        subprocess.Popen(r'explorer '+to_open)
        self.add_image_grid()

    def styles(self):
        font_loc="fonts/GothamMedium_1.ttf"
        font_id = QFontDatabase.addApplicationFont(font_loc)
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        font = QFont(font_family)
        font.setPointSize(8)
        font.setItalic(True)
        
        self.setStyleSheet(
                           'background-color:#6096B4;'
                           'font-size: 16pt; font-family: {}; font-weight: italic;'.format(font_family))
        for widget in self.labels:
            widget.setFont(font)
            
    def add_image_grid(self):
        
        
        self.folder_dir='output/'
        isExist = os.path.exists(self.folder_dir)
        if not isExist:
            os.makedirs(self.folder_dir)
            
        # self.gird_generated.update()
        # self.grid_layout.activate()
        

        # layout = QVBoxLayout()
        # self.scene.clear()
        
        # for file in os.listdir(self.folder_dir):
        #     if file.endswith(".jpg"):
        #         print(file)
        #         self.scene = QGraphicsScene()
        #         self.view = QGraphicsView(self.scene)
                # image_paths.append(file)
                # name_image=os.path.join(self.folder_dir,file)

                # pixmap = 
                # print(pixmap)
                # pixmap=
                # item = self.scene.addPixmap(
                # pixmap=QPixmap(os.path.join(self.folder_dir, file)).scaled(256, 512, Qt.KeepAspectRatio, Qt.FastTransformation)
                
                # layout.addWidget(pixmap, 0, Qt.AlignCenter)
                # layout.addWidget(self.view)
        # self.gird_generated = QtWidgets.QGridLayout()
        # layout = QVBoxLayout()
        
            # print(os.getcwd())

        # self.main_container.addLayout(layout)
        
           # Create a new dir
        # self.gird_generated.clearContents()
        # scrollAreaWidgetContents = self.scrollArea.widget()
        # for child_widget in scrollAreaWidgetContents.children():
        #     child_widget.deleteLater()
        # if self.scrollArea is not None and self.scrollArea in self.main_container.children():
        #     self.main_container.removeWidget(self.scrollArea)
        # if self.scrollArea:
        #     self.main_container.removeWidget(self.scrollArea)
        while self.gird_generated.count():
            child = self.gird_generated.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
                
        try:
            i=0
            c=0
            max_r=3
            r=0
            for image in os.listdir(self.folder_dir):
                if (image.endswith(".jpg")):
                    self.name_image=os.path.join(self.folder_dir,image)
                    self.word_image=QLabel(self)
                    self.labels.append(self.word_image)
                    pixmap=QPixmap(self.name_image)
                    # pixmap=pixmap.scaled(128, 256, Qt.KeepAspectRatio, Qt.FastTransformation)
                    pixmap=pixmap.scaled(256, 512, Qt.KeepAspectRatio, Qt.FastTransformation)
                    
                    self.word_image.setPixmap(pixmap)
                    # self.word_image.mousePressEvent = self.openImage(name_image)
                    self.word_image.mousePressEvent = lambda event: self.openImage(self.name_image)
                    
                    
                    

                    self.gird_generated.addWidget(self.word_image,r,i)
                    i=i+1
                    if i==max_r:
                        r+=1
                        i=0
                self.gird_generated.update()
                self.gird_generated.activate()
            
            self.gird_generated.update()
            self.gird_generated.activate()
            # self.scrollArea.deleteLater()

            # scrollArea.deleteLater()
            # self.main_container.replaceWidget(self.scrollArea,self.scrollArea)
        except Exception as e:
            print("Image not found.",e) 
            

        
    def add_image(self):
        self.file_name,_ = QFileDialog.getOpenFileName(self, 'Open File', "/Users/user_name/Desktop/","All Files (*);;Text Files (*.txt)")
        # print(_)
        print(self.file_name)        
        self.addedimages.append(self.file_name)
        
    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        
        if event.mimeData().hasImage:
            event.setDropAction(Qt.CopyAction)
            file_path = event.mimeData().urls()[0].toLocalFile()
            self.set_image(file_path)
            event.accept()
        else:
            event.ignore()

    def set_image(self, file_path):
        self.addedimages.append(file_path)
        pixmap=QPixmap(file_path)
        print(file_path)
        pixmap=pixmap.scaled(128, 256, Qt.KeepAspectRatio, Qt.FastTransformation)
        pixmap.mousePressEvent = self.openImage
        self.photoViewer.setPixmap(pixmap)
        
    def openImage(self, file_dir):    # Open a file dialog to select an image file
        
        print(file_dir)
        print(os.getcwd())
        QDesktopServices.openUrl(QUrl.fromLocalFile(file_dir))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    id = QFontDatabase.addApplicationFont("fonts/Cubano.ttf")   
    families = QFontDatabase.applicationFontFamilies(id)[0]
    window = Project()
    sys.exit(app.exec_())