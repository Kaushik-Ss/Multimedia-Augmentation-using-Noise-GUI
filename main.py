import os
import sys
import subprocess

import multiprocessing
import concurrent.futures
from noises.impulse import *
from noises.anisotropic import *
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
# from noises.identify_noise import *

# from noises.

from PyQt5.QtCore import Qt,QUrl,QObject, QRunnable, QThreadPool
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QCheckBox,QFileDialog,QVBoxLayout,QFormLayout,QHBoxLayout,QGridLayout,QLineEdit
from PyQt5.QtGui import QPixmap,QFont,QFontDatabase,QDesktopServices
from PyQt5 import QtCore,QtWidgets
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QWidget, QGridLayout, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QHBoxLayout, QSplitter, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QSizePolicy
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtCore import Qt

# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


flag_hover=False
show_name=False
folder_dir='output/'
open_folder_when_done=False
show_preview=True
last_refreshed=0
width=256
height=512

# class HoverPopup(QWidget):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         if flag_hover:
#             self.label = QLabel(self)
#             self.label.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
#             self.label.setAlignment(Qt.AlignCenter)
#             self.setWindowFlags(Qt.Popup | Qt.FramelessWindowHint)
#             self.setAttribute(Qt.WA_TranslucentBackground)
#             self.setStyleSheet("background-color: white; border: 1px solid gray;")

#     def setPixmap(self, pixmap):
#         self.label.setPixmap(pixmap)

#     def show(self, pos):
#         self.move(pos)
#         super().show()

    

# class HoverLabel(QLabel):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.hover_popup = HoverPopup(self)
#         self.hover_popup.hide()
#         self.setMouseTracking(True)
#         self.setAlignment(Qt.AlignCenter)

#     def enterEvent(self, event):
#         pos = self.mapToGlobal(QPoint(0, self.height()))
#         self.hover_popup.setPixmap(self.pixmap())
#         self.hover_popup.show(pos)


#     def leaveEvent(self, event):
#         self.hover_popup.hide()

#     def moveEvent(self, event):
#         self.hover_popup.hide()
#         # return super().moveEvent(a0)



class HoverLabel(QLabel):
    def __init__(self, parent=None):
        QLabel.__init__(self, parent)
        self.setStyleSheet("QLabel:hover { border: 2px solid red; }")
        self.setAlignment(Qt.AlignCenter)

    def enterEvent(self, event):
        if flag_hover:
            pixmap = self.pixmap()
            global width,height
            if pixmap:
                scaled_pixmap = pixmap.scaled(width*2, height*2, Qt.KeepAspectRatio, Qt.FastTransformation)
                self.setPixmap(scaled_pixmap)
                self.setFixedSize(scaled_pixmap.width(), scaled_pixmap.height())
            self.setFixedSize(width*2, height*2)

    def leaveEvent(self, event):
        if flag_hover:
            pixmap=QPixmap()
            pixmap = self.pixmap()
            global width,height
            if pixmap:
                scaled_pixmap = pixmap.scaled(width, height, Qt.KeepAspectRatio, Qt.FastTransformation)
                self.setPixmap(scaled_pixmap)
                self.setFixedSize(scaled_pixmap.width(), scaled_pixmap.height())
            self.setFixedSize(width, height)

        
        
class ImageLabel(QLabel):
    def __init__(self):
        super().__init__()
        self.setAlignment(Qt.AlignCenter)
        self.setText('\n\n Drop Image Here \n\n')
        self.setStyleSheet(
                "color: black;"
                "width: 500px;"
                "background-color:#ECF9FF;"
                             "border-style: dashed;"
                             "border-width: 5px;"
                             "border-color: black;"
                             "border-radius: 3px"    
        )


    def setPixmap(self, image):
        super().setPixmap(image)

class Project(QWidget):
    def test_multi_processing(self):
        print("Using", multiprocessing.cpu_count(),"CPU cores")

    def __getstate__(self):
        return {'some_data': self.addedimages}

    def __setstate__(self, state):
        self.addedimages = state['some_data']
        
    def __init__(self):
        super().__init__()
        self.intitalizeUI()
        self.setAcceptDrops(True)
        
    def intitalizeUI(self): 
        self.test_multi_processing()
        self.setWindowTitle('Image Augment')
        self.addedimages=[]
        self.chkbxs=[]
        self.labels=[]
        self.buttons=[]
        # self.move(0,0)
        self.setWindowState(QtCore.Qt.WindowMaximized)
                
        
        noises=['Impulse','Gaussian','Periodic','Speckle','Anisotropic','Exponential',
                'Flimgrain','Gamma','Pepper','Poisson','Rayleigh','Uniform']
        
        slider_one={'Gaussian','Gamma','Flimgrain','Pepper','Poisson','Speckle','Uniform'}
        slider_two={'Anisotropic','Periodic'}
        slider_no={'Impulse','Rayleigh'}
        
        #         anisotropic mean stddev
        #   gaussian   peak (0-1)
        # gamma   peak (0-1)
        
        # flimgrain flimgrain (idk 0-1)
        
        # impulse b/w why?? number_of_pixels = random.randint(300, 10000) why??
        # pepper amountrange (idk 0-1)
        # periodic noise_level noise_freq (idk 0-1)
        # poisson (idk 0-1)
        # add_rayleigh_noise why ?? function name?? scale=(0,100)
        # speckle noise_level (idk 0-1)
        # uniform intensity (idk 0-1)
        

        self.main_container=QHBoxLayout()
        self.photoViewer = ImageLabel()
        # self.photoViewer.setSizePolicy(QSizePolicy(QSizePolicy::Fixed, QSizePolicy::Fixed));
        self.photoViewer.setMinimumWidth(300);
        self.labels.append(self.photoViewer)
        self.main_container.addWidget(self.photoViewer)        
        
        
        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        
        self.gird_generated = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea.setStyleSheet("background-color:#93BFCF")
        
        
        self.add_image_grid()
        ###############################   
        self.main_container.addWidget(self.scrollArea)
        
        self.scrollArea.setMinimumWidth(1000)
        

        button_gen = QPushButton('Generate', self)
        self.labels.append(button_gen)
        button_gen.clicked.connect(self.submit)

        self.buttons.append(button_gen)
        

        button_add = QPushButton('Add images', self)
        self.labels.append(button_add)
        button_add.clicked.connect(self.add_image)
        self.buttons.append(button_add)

        button_iden = QPushButton('Add all noises', self)
        self.labels.append(button_iden)
        # self.button_iden.setChecked(False)
        button_iden.clicked.connect(self.on_stateChanged)
        # button_iden.clicked.connect(self.identify)
        button_iden.setStyleSheet("background-color : white")

        button_inv = QPushButton('Invert Selection',self)
        self.labels.append(button_inv)
        button_inv.clicked.connect(self.invertSelection)
        button_inv.setStyleSheet("background-color : white")

        
        self.b1 = QCheckBox("Hover over preview")
        self.b1.stateChanged.connect(lambda:self.settings(self.b1))
        self.b2 = QCheckBox("Show preview name")
        self.b2.stateChanged.connect(lambda:self.settings(self.b2))
        # self.b3 = QCheckBox("Show preview")
        # self.b3.stateChanged.connect(lambda:self.settings(self.b3))
        self.b4 = QCheckBox("Open Output folder when done")
        self.b4.stateChanged.connect(lambda:self.settings(self.b4))
        
        
        
        
        show_preview=True


        self.buttons.append(button_iden)
        self.buttons.append(button_inv)
        
        
        
        
        title_h_box_a = QHBoxLayout()
        title_h_box_a.addWidget(button_gen)
        title_h_box_a.addWidget(button_add)
        title_h_box_b=QHBoxLayout()
        title_h_box_b.addWidget(button_iden)
        title_h_box_b.addWidget(button_inv)
        
        title_h_box_c=QVBoxLayout()
        title_h_box_c.addWidget(self.b1)
        title_h_box_c.addWidget(self.b2)
        # title_h_box_c.addWidget(self.b3)
        title_h_box_c.addWidget(self.b4)
        
        
        # title_h_box_b.addStretch(10)
        # title_h_box.setSpacing(20)
        
    
        title_v_box = QVBoxLayout()   
        title_v_box.setAlignment(Qt.AlignCenter) 
        title_text_lable=QHBoxLayout()    
        text_noise=QLabel(self)
        text_noise.setText('Select noises to add')
        self.labels.append(text_noise)
        refresh_image=QPushButton('Refresh preview')
        self.buttons.append(refresh_image)
        # self.labels.append(refresh_image)
        # self.button_iden.setChecked(False)
        refresh_image.clicked.connect(self.refresh)
        # text_noise.resize(100,100)
        title_text_lable.addWidget(text_noise)
        title_text_lable.addWidget(refresh_image)
        
        title_v_box.addLayout(title_text_lable)
        title_v_box.addStretch(10)
        
        
        


        for label in noises:
            layout = QHBoxLayout()
            checkbox = QCheckBox(label, self)
            self.labels.append(checkbox)
            self.chkbxs.append(checkbox)
            title_v_box.addWidget(checkbox)
            title_v_box.setStretchFactor(checkbox, 0)
            layout.addWidget(checkbox)
            title_v_box.addStretch(10)
            liders = {}
            
            def updateLabel(label, value):
                    print(liders)
                    print(liders[label])        
                    liders[label].setText(str(value))
                
            
            
            # if label in slider_one:
            #     sld = QSlider(Qt.Orientation.Horizontal)
            #     sld.setFixedWidth(100)
            #     sld.setRange(0, 1)
            #     sld.setTickPosition(QSlider.TickPosition.TicksAbove)
            #     layout.addWidget(sld)
            #     result_label1 = QLabel('')
            #     liders[label] = result_label1
            #     sld.valueChanged.connect(lambda value: updateLabel(label, value))
                
            #     layout.addWidget(result_label1)

            # if label in slider_two:
            #     sld1 = QSlider(Qt.Orientation.Horizontal)
            #     sld1.setFixedWidth(100)
            #     sld1.setRange(0, 1)
            #     sld1.setTickPosition(QSlider.TickPosition.TicksAbove)
            #     layout.addWidget(sld1)    
            #     result_label1 = QLabel('')
            #     liders[label] = result_label1
            #     layout.addWidget(result_label1)
            #     sld1.valueChanged.connect(lambda value: updateLabel(label, value))
                
            #     sld2 = QSlider(Qt.Orientation.Horizontal)
            #     sld2.setFixedWidth(100)
            #     sld2.setRange(0, 1)
            #     sld2.setTickPosition(QSlider.TickPosition.TicksAbove)
            #     result_label2 = QLabel('')
            #     layout.addWidget(sld2)
            #     result_label2 = QLabel('')
            #     liders[label] = result_label2
            #     sld2.valueChanged.connect(lambda value: updateLabel(label, value))
            #     layout.addWidget(result_label2)

            # if label in slider_no:
            #     textbox1 = QLineEdit()
            #     textbox2 = QLineEdit()
            #     layout.addWidget(textbox1)
            #     layout.addWidget(textbox2)

                
                
            # title_v_box.addLayout(layout)
            # title_v_box.setStretchFactor(checkbox, 1)
            # title_v_box.addStretch(10)
        # for label in noises:
        #     layout = QHBoxLayout()
        #     checkbox = QCheckBox(label, self)
        #     self.labels.append(checkbox)
        #     self.chkbxs.append(checkbox)
        #     layout.addWidget(checkbox)
            
            
        #     #REMVOVE THIS LINE AFTER SLIDER FIXED
        #     title_v_box.addLayout(layout)
            

        #     def updateLabel(label, value):
        #         label.setText(str(value))

            # if label in slider_one:
            #     sld = QSlider(Qt.Orientation.Horizontal)
            #     sld.setFixedWidth(100)
            #     sld.setRange(0, 1)
            #     sld.setTickPosition(QSlider.TickPosition.TicksAbove)

            #     result_label = QLabel('')
            #     sld.valueChanged.connect(lambda value: updateLabel(result_label, value))

            #     liders[sld] = result_label  # add slider and label to the dictionary

            #     layout.addWidget(sld)
            #     layout.addWidget(result_label)

            # if label in slider_two:
            #     sld1 = QSlider(Qt.Orientation.Horizontal)
            #     sld1.setFixedWidth(100)
            #     sld1.setRange(0, 1)
            #     sld1.setTickPosition(QSlider.TickPosition.TicksAbove)

            #     result_label1 = QLabel('')
            #     sld1.valueChanged.connect(lambda value: updateLabel(result_label1, value))

            #     liders[sld1] = result_label1  # add slider and label to the dictionary

            #     layout.addWidget(sld1)
            #     layout.addWidget(result_label1)

            #     sld2 = QSlider(Qt.Orientation.Horizontal)
            #     sld2.setFixedWidth(100)
            #     sld2.setRange(0, 1)
            #     sld2.setTickPosition(QSlider.TickPosition.TicksAbove)

            #     result_label2 = QLabel('')
            #     sld2.valueChanged.connect(lambda value: updateLabel(result_label2, value))

            #     liders[sld2] = result_label2  # add slider and label to the dictionary

            #     layout.addWidget(sld2)
            #     layout.addWidget(result_label2)

            # if label in slider_no:
            #     textbox1 = QLineEdit()
            #     textbox2 = QLineEdit()
            #     layout.addWidget(textbox1)
            #     layout.addWidget(textbox2)

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


        title_v_box.addLayout(title_h_box_a)     
        title_v_box.addLayout(title_h_box_b)
        title_v_box.addLayout(title_h_box_c)     
        title_v_box.setStretchFactor(title_h_box_a, 1)
        title_v_box.setStretchFactor(title_h_box_b, 1)
        title_v_box.setStretchFactor(title_h_box_c, 1)    
        self.main_container.setStretchFactor(title_v_box, 1)
         
        self.main_container.addLayout(title_v_box)
        self.main_container.setStretchFactor(title_v_box, 1)
        
        
        
        
        self.styles()
        self.setLayout(self.main_container)
        self.show()

    def settings(self,b):
        m=b.text()
        # update the settings 
        # hover working others not working
        global show_preview,flag_hover,show_name
        if m == "Hover over preview":
            if b.isChecked() == True:
                flag_hover=True
            else:
                flag_hover=False
        elif m=="Show preview name":
            if b.isChecked() == True:
                show_name=True
            else:
                show_name=False
        elif m=="Show preview":
            if b.isChecked() == True:
                show_preview=True
            else:
                show_preview=False
        elif m=="Open Output folder when done":
            if b.isChecked() == True:
                open_folder_when_done=True
            else:
                open_folder_when_done=False
                
    def impulse(self):
        generatedimages = []
        for i in self.addedimages:
            generatedimages.append(impulse(i))
        for i in range(len(generatedimages)):
            print('output/impulse'+str(i+1)+'.jpg')
            cv2.imwrite('output/impulse'+str(i+1)+'.jpg',generatedimages[i])
    def refresh(self):
        global last_refreshed
        if time.time()-last_refreshed > 2:
            self.add_image_grid()
            last_refreshed = time.time()
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
        return True

    def uniform(self):
        generatedimages = []
        for i in self.addedimages:
            generatedimages.append(uniform(i))
        for i in range(len(generatedimages)):
            print('output/uniform'+str(i+1)+'.jpg')
            cv2.imwrite('output/uniform'+str(i+1)+'.jpg',generatedimages[i])

    def identify(self):
        self.file_name,_ = QFileDialog.getOpenFileName(self, 'Open File', "/Users/user_name/Desktop/","All Files (*);;Text Files (*.txt)")        
                  
    def submit(self):
        if len(self.addedimages) == 0:
            print('Please enter')
            ret = QMessageBox.question(self, 'Critical', "Add Images!", QMessageBox.Ok, QMessageBox.Cancel)
            if ret==QMessageBox.Ok:
                pass
            else:
                # for error close lol 
                # need to remove this
                QMessageBox(self, "Title", "Message")
            return 
        
        
        import timeit
        start = timeit.default_timer()
        # bar = QProgressBar(self)
        
        results = {}
        with concurrent.futures.ProcessPoolExecutor() as executor:
            for widget in self.chkbxs:
                if isinstance(widget, QCheckBox) and widget.isChecked():
                    label = widget.text()
                    future=executor.submit(self.checkbox_functions[label])
                    results[label] = future 
                    print("Submitted future for checkbox:", label)

        concurrent.futures.wait(results.values())
        
        for label, future in results.items():
            if future.done():
                time_taken = timeit.timeit(lambda: future.result(), number=1)
                print(f"Time taken for '{label}': {time_taken:.6f} seconds")
                result = future.result()
        stop= timeit.default_timer()
        print('Completed in ',stop-start,'seconds')
        if open_folder_when_done:
            to_open = os.path.abspath(folder_dir)
            subprocess.Popen(r'explorer ' + to_open)
        self.gird_generated.update()
        self.gird_generated.activate()
        # self.add_image_grid()
            
    def on_stateChanged(self, state):
        for widget in self.chkbxs:
            widget.setChecked(True)

    def invertSelection(self,state):
        for widget in self.chkbxs:
            if(widget.isChecked()):
                widget.setChecked(False)
            else:
                widget.setChecked(True)
            
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
        for widget in self.buttons:
            widget.setStyleSheet("""
        QPushButton {
            background-color: white; 
        }
        QPushButton:hover {
             background-color:green;
             color:white;
        }
        """)
            
    def add_image_grid(self):
        if show_preview:
            isExist = os.path.exists(folder_dir)
            if not isExist:
                os.makedirs(folder_dir)
                
            while self.gird_generated.count():
                child = self.gird_generated.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()
                    
            try:
                # splitter = QSplitter(Qt.Horizontal, self)
                i=0
                c=0
                max_r=3
                r=0
                for image in os.listdir(folder_dir):
                    if (image.endswith(".jpg")):
                        small_grid=QGridLayout()
                        self.name_image=os.path.join(folder_dir,image)
                        self.text_def=QLabel(self)
                        self.word_image=HoverLabel()
                        self.labels.append(self.word_image)
                        pixmap=QPixmap(self.name_image)
                        pixmap=pixmap.scaled(256, 512, Qt.KeepAspectRatio, Qt.FastTransformation)
                        self.text_def.setText(image)
                        self.text_def.setFixedHeight(40)
                        self.text_def.setStyleSheet(
                            'background-color:#6096B4;'
                            'font-size: 10pt; font-weight: italic;')
                        self.word_image.setPixmap(pixmap)
                        
                        def create_image_handler(image_name):
                            def handler(event):
                                self.openImage(image_name)
                            return handler
        
                        self.word_image.mousePressEvent = create_image_handler(self.name_image)
                        
                        small_grid.addWidget(self.word_image,0,0)
                        if show_name:
                            small_grid.addWidget(self.text_def,1,0)
                        self.gird_generated.addLayout(small_grid,r,i)
                        
                        i=i+1
                        if i==max_r:
                            r+=1
                            i=0
                    # self.gird_generated.setMinimumWidth(500)

                    self.gird_generated.update()
                    self.gird_generated.activate()
                
                self.gird_generated.update()
                self.gird_generated.activate()
            except Exception as e:
                print("Image not found.",e) 
        else:
            self.deleteItemsOfLayout(self.gird_generated)
       
    def deleteItemsOfLayout(self,layout):
         if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)
                else:
                    self.deleteItemsOfLayout(item.layout())

    def add_image(self):
        self.file_name,_ = QFileDialog.getOpenFileName(self, 'Open File', "/Users/user_name/Desktop/","All Files (*);;Text Files (*.txt)")
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
        pixmap=pixmap.scaled(self.photoViewer.width(), self.photoViewer.height(), Qt.KeepAspectRatio, Qt.FastTransformation)
        pixmap.mousePressEvent = self.openImage
        self.photoViewer.setPixmap(pixmap)
        
    def openImage(self, file_dir): 
        # self.gird_generated.update()
        # self.gird_generated.activate()
        print(file_dir) 
        QDesktopServices.openUrl(QUrl.fromLocalFile(file_dir))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    id = QFontDatabase.addApplicationFont("fonts/Cubano.ttf")   
    families = QFontDatabase.applicationFontFamilies(id)[0]
    window = Project()
    sys.exit(app.exec_())