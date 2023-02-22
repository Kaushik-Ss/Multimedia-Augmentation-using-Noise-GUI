import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5 import *
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QCheckBox,QFileDialog,QVBoxLayout
from PyQt5.QtGui import QPixmap,QFont, QFontDatabase
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import Qt
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout,QFormLayout,QGridLayout,QLineEdit)
from multiprocessing import Pool
from PyQt5 import QtWidgets
import os
import functools
# p = Pool(10)


class ImageLabel(QLabel):
    def __init__(self):
        super().__init__()

        self.setAlignment(Qt.AlignCenter)
        self.setText('\n\n Drop Image Here \n\n')
        self.setStyleSheet('''
            QLabel{
                border: 4px dashed #aaa
            }
        ''')

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

        noises=['Salt and pepper','Impulse']
        
        self.chkbxs=[]
        self.labels=[]
        folder_dir='images/'

        main_container=QHBoxLayout()
        self.photoViewer = ImageLabel()
        self.labels.append(self.photoViewer)
        main_container.addWidget(self.photoViewer)        
        scrollArea = QtWidgets.QScrollArea()
        scrollArea.setWidgetResizable(True)
        scrollAreaWidgetContents = QtWidgets.QWidget()
        grid_generated = QtWidgets.QGridLayout(scrollAreaWidgetContents)
        scrollArea.setWidget(scrollAreaWidgetContents)
        
        try:
            i=0
            c=0
            max_r=3
            r=0
            for image in os.listdir(folder_dir):
                if (image.endswith(".jpg")):
                            name_image=os.path.join(folder_dir,image)
                            word_image=QLabel(self)
                            self.labels.append(word_image)
                            pixmap=QPixmap(name_image)
                            pixmap=pixmap.scaled(128, 256, Qt.KeepAspectRatio, Qt.FastTransformation)
                            word_image.setPixmap(pixmap)
                            # word_image.mousePressEvent = self.openImage(name_image)
                            word_image.mousePressEvent = lambda event: self.openImage(name_image)
                            grid_generated.addWidget(word_image,r,i)
                            i=i+1
                            if i==max_r:
                                r+=1
                                i=0
            main_container.addWidget(scrollArea)
        except Exception as e:
            print("Image not found.") 

        button_gen = QPushButton('Generate', self)
        self.labels.append(button_gen)
        button_gen.clicked.connect(self.submit)
        

        button_add = QPushButton('Add images', self)
        self.labels.append(button_add)
        button_add.clicked.connect(self.add_image)
        
        title_v_box_op = QHBoxLayout()
        title_v_box_op.addWidget(button_gen)
        title_v_box_op.addStretch()
        title_v_box_op.addWidget(button_add)
        title_v_box_op.addStretch()
        title_v_box_op.setSpacing(60)
        
    
        title_v_box = QVBoxLayout()        
        text_noise=QLabel(self)
        text_noise.setText('Select noises to add')
        self.labels.append(text_noise)
        text_noise.resize(100,100)
        title_v_box.addWidget(text_noise)
        

        for label in noises:
                    checkbox = QCheckBox(label, self)
                    self.labels.append(checkbox)
                    self.chkbxs.append(checkbox)
                    title_v_box.addWidget(checkbox)

        self.checkbox_functions = {}
        self.checkbox_functions['Salt and pepper'] = self.function1
        self.checkbox_functions['Impulse'] = self.function2

        title_v_box.addLayout(title_v_box_op)        
        main_container.addLayout(title_v_box)
        
        self.styles()
        self.setLayout(main_container)
        self.show()

    
    def function1(self):
        print(*self.addedimages)
        print('Function 1 was called')

    def function2(self):
        print('Function 2 was called')

    def submit(self):
        for widget in self.chkbxs:
            if isinstance(widget, QCheckBox) and widget.isChecked():
                label = widget.text()
                self.checkbox_functions[label]()

    def styles(self):
        font_loc="fonts/GothamMedium_1.ttf"
        font_id = QFontDatabase.addApplicationFont(font_loc)
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        font = QFont(font_family)
        font.setPointSize(8)
        font.setItalic(True)
        self.setStyleSheet('font-size: 16pt; font-family: {}; font-weight: italic;'.format(font_family))
        for widget in self.labels:
            widget.setFont(font)
            
        
    def add_image(self):
        self.file_name,_ = QFileDialog.getOpenFileName(self, 'Open File', "/Users/user_name/Desktop/","All Files (*);;Text Files (*.txt)")
        # print(_)
        print(file_name)        
        self.addedimages.append(file_name)
        
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
        QDesktopServices.openUrl(QUrl.fromLocalFile(file_dir))
if __name__ == '__main__':
    app = QApplication(sys.argv)
    id = QFontDatabase.addApplicationFont("fonts/Cubano.ttf")   
    families = QFontDatabase.applicationFontFamilies(id)[0]
    window = Project()
    sys.exit(app.exec_())