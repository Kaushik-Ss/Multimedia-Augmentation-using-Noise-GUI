import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5 import *
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QCheckBox,QFileDialog,QVBoxLayout
from PyQt5.QtGui import QPixmap,QFont, QFontDatabase
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

class prism(QWidget):
    noises=['Salt and pepper','Impulse']
    noise_dict={'noise_1':'Salt and pepper','noise_2':'Impulse'}
    noise_chkx=[]


    selected=[]


    def salt():
        print('ssdasalt')
    
    def impulse():
        print("Impulse")
        


    def __init__(self):
        super().__init__()
        self.intitalizeUI()
        self.setAcceptDrops(True)
        self.checked=[]
        self.noise_chkx=[]
        self.d={"Salt and pepper":self.salt(),"Impulse":self.impulse()}
        

    def intitalizeUI(self):	
        self.setWindowTitle('Image Augment')
        self.display()
        self.show()
    
        
    def display(self):
        main_container=QHBoxLayout()
        self.photoViewer = ImageLabel()
        main_container.addWidget(self.photoViewer)        
        scrollArea = QtWidgets.QScrollArea()
        scrollArea.setWidgetResizable(True)
        scrollAreaWidgetContents = QtWidgets.QWidget()
        grid_generated = QtWidgets.QGridLayout(scrollAreaWidgetContents)
        scrollArea.setWidget(scrollAreaWidgetContents)
        
        folder_dir='images/'
        try:
            i=0
            c=0
            max_r=3
            r=0
            for image in os.listdir(folder_dir):
                if (image.endswith(".jpg")):
                            name_image=os.path.join(folder_dir,image)
                            word_image=QLabel(self)
                            pixmap=QPixmap(name_image)
                            pixmap=pixmap.scaled(128, 256, Qt.KeepAspectRatio, Qt.FastTransformation)
                            word_image.setPixmap(pixmap)
                            
                            grid_generated.addWidget(word_image,r,i)
                            i=i+1
                            if i==max_r:
                                r+=1
                                i=0
            main_container.addWidget(scrollArea)
        except Exception as e:
            print("Image not found."+e.message)        
        button_gen = QPushButton('Generate', self)
        
        #signal connect and self.generate_image is slots in pyqt5
        button_gen.clicked.connect(self.generate_image)
        
        button_add = QPushButton('Add images', self)
        
        #signal connect and self.generate_image is slots in pyqt5
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
        text_noise.resize(100,100)
        title_v_box.addWidget(text_noise)
        
        
        
        
        ind=0        
        noise_1=QCheckBox('Salt and pepper', self)
        noise_1.clicked.connect(self.add_to_generate)
        title_v_box.addWidget(noise_1)
        


        noise_2=QCheckBox('Impulse', self)
        noise_2.clicked.connect(self.add_to_generate)
        title_v_box.addWidget(noise_2)
        
        ###
        # TO DO: DYNAMICALLY ADD NOISES AND SLOT TO CHECKBOX
        ###
        # for noise in self.noises:
        #     noise_list.append(QCheckBox(noise, self))
        #     print(noise_list,ind,noise_list[ind])
        #     noise_list[ind].clicked.connect(lambda x:self.add_to_generate(noise_list[ind]))
        #     self.noise_chkx.append(noise_list[ind])
        #     title_v_box.addWidget(noise_list[ind])
        #     print('added')
        #     title_v_box.addStretch()
        #     ind+=1
        # title_v_box.setSpacing(30)
        
        
        
        title_v_box.addLayout(title_v_box_op)        
        main_container.addLayout(title_v_box)
        
        self.setLayout(main_container)
                
        

    
    def generate_image(self):
        # print('clicked')
        c=[]
        for i in self.selected:
            # print(self.d[i])
            self.d[i]
            print(i,'function called')
            # print(i,'selected')
            
            
            #
            # call respective functions
            #
            
        
    def add_to_generate(self,state):
        if state:
            self.selected.append(self.sender().text())
        else:
            self.selected.remove(self.sender().text())
                
            
    def add_image(self):
        # print('clicked')
        file_name,_ = QFileDialog.getOpenFileName(self, 'Open File', "/Users/user_name/Desktop/","All Files (*);;Text Files (*.txt)")
        # print(_)
        print(file_name)    
        
        
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
        pixmap=QPixmap(file_path)
        pixmap=pixmap.scaled(128, 256, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.photoViewer.setPixmap(pixmap)

	
if __name__ == '__main__':
	app = QApplication(sys.argv)
	id = QFontDatabase.addApplicationFont("fonts/Cubano.ttf")	
	families = QFontDatabase.applicationFontFamilies(id)[0]
	window = prism()
	sys.exit(app.exec_())