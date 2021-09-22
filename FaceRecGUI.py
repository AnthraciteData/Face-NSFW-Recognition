import sys
import cv2
from PyQt6.QtCore import*
from PyQt6.QtWidgets import*
from PyQt6.QtGui import*

from FaceRecMain import FaceRecMain
from NSFWAPIService import NSFWAPIService





class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        #Main Layout
        main_layout = QVBoxLayout()

        self.setFixedSize(QSize(1000, 600))


        #Top layer which is a horizonatl box
        self.top_layer = QHBoxLayout()
        main_layout.addLayout(self.top_layer)



        # Vertical Box for top layer
        box_line_botton = QVBoxLayout()

        # Things in box_line_botton
        label_line = QHBoxLayout()
        label_enterInfo = QLabel("Enter Location:")
        label_enterInfo.setStyleSheet("border: 1px solid black;")
        label_enterInfo.setFixedSize(100,18)

        self.image_input = QLineEdit(self)


        self.image_input.setFixedSize(200,18)
        label_line.addWidget(label_enterInfo)
        label_line.addWidget(self.image_input)
        box_line_botton.addLayout(label_line)

        # Percent checker
        NSFW_percent = QHBoxLayout()
        self.selectPer = QLabel("Select %")
        self.selectPer.setStyleSheet("border: 1px solid black;")
        self.selectPer.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.selectPer.setFixedSize(100, 18)
        NSFW_percent.addWidget(self.selectPer)

        self.nsfwPercent = QLineEdit()
        self.nsfwPercent.setStyleSheet("border: 1px solid black;")
        self.nsfwPercent.setFixedSize(22, 18)
        self.nsfwPercent.setAlignment(Qt.AlignmentFlag.AlignLeft)
        NSFW_percent.addWidget(self.nsfwPercent)
        box_line_botton.addLayout(NSFW_percent)


        btn_enter = QPushButton("Press Me!")
        btn_enter.clicked.connect(self.on_click)
        box_line_botton.addWidget(btn_enter)
        self.top_layer.addLayout(box_line_botton)

        #Creates image label
        self.user_image = QLabel()
        self.user_image.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.user_image.setFixedSize(350, 280)
        self.user_image.setScaledContents(True)
        self.top_layer.addWidget(self.user_image)



        #Bottom Layer which is a horizontal box
        self.bottom_layer = QHBoxLayout()
        main_layout.addLayout(self.bottom_layer)

        #Add infp to bottom
        self.label_numFaces = QLabel("# Faces:")
        self.bottom_layer.addWidget(self.label_numFaces)

        self.label_isNSFW = QLabel("Is it NSFW :")
        self.bottom_layer.addWidget(self.label_isNSFW)



        # if NSFWAPIService.getNSFW(self,self.textBoxV)> 50.00:
        #     label_isNSFW = QLabel("Is it NSFW : Yes")
        #     self.bottom_layer.addWidget(label_isNSFW)
        #     # Image input in the Top Layer very important
        #
        #     self.user_image = QLabel()
        #     self.user_image.setPixmap(QPixmap(FaceRecMain.openCleanImage(self.textBoxV)))
        #     self.user_image.setScaledContents(True)
        #     self.user_image.setFixedSize(300, 230)
        #
        # else:
        #     label_isNSFW = QLabel("Is it NSFW : No")
        #     self.bottom_layer.addWidget(label_isNSFW)

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)











    def on_click(self):

        self.textBoxV = self.image_input.text()
        self.textPercentage = self.nsfwPercent.text()
        if self.textBoxV == "":
            self.user_image.setText("Invalid Input")

            self.image_input.setText("")
        else:
            self.getImageNSFW(self.textBoxV,self.textPercentage)
            self.image_input.setText("")





    def getImageNSFW(self,textBoxV,textPercentage):

        if NSFWAPIService.getNSFW(self, textBoxV) > float(textPercentage):

            self.label_isNSFW.setText("Is it NSFW : Yes")
            self.label_numFaces.setText("# Faces is :  0")
            self.user_image.setPixmap(QPixmap(NSFWAPIService.getNSFWImage(textBoxV)))



        else:
            self.label_isNSFW.setText("Is it NSFW : No ")
            self.getCleanImage(self.textBoxV)

    def getCleanImage(self,textBoxV):

        self.user_image.setPixmap(QPixmap(FaceRecMain.openCleanImage(textBoxV)))

        self.label_numFaces.setText("# of Faces : "+ str(FaceRecMain.facesNum))































#         self.setFixedSize(QSize(1000,600))
#
#         self.getSHIT()
#
#     def getSHIT(self):
#         main_layout = QVBoxLayout()
#
#         top_layer = QHBoxLayout()
#         bottom_layer = QHBoxLayout()
#         important_widget = QVBoxLayout()
#         info_vBox = QVBoxLayout()
#         input_layer = QHBoxLayout()
#
#         main_layout.addLayout(top_layer)
#         main_layout.addLayout(bottom_layer)
#         top_layer.addLayout(important_widget)
#         # image_label = QLabel()
#         # image_label.setPixmap(QPixmap(FaceRecMain.openCV("TESTIMAGE.jpeg")))
#         # image_label.setFixedSize(300,230)
#         # image_label.setScaledContents(True)
#
#         btn_toexacute = QPushButton("Button")
#         btn_toexacute.resize(20,20)
#         name_fileLoc = QLabel("Image Location")
#         name_fileLoc.setStyleSheet("border: 1px solid black;")
#         image_input = QLineEdit("Enter Input")
#         name_fileLoc.setFixedSize(100,18)
#         input_layer.addWidget(name_fileLoc)
#         input_layer.addWidget(image_input)
#
#
#         important_widget.addLayout(input_layer)
#
#
#         image_input.setFixedSize(200,15)
#         important_widget.addWidget(btn_toexacute)
#         # top_layer.addWidget(image_label)
#
#         label_isNSFW = QLabel("Is it NSFW:")
#         label_isFace= QLabel("# of faces:")
#
#         bottom_layer.addWidget(label_isFace)
#         bottom_layer.addWidget(label_isNSFW)
#
#         labe1 = QLabel("FIRST LABEL")
#         label2 = QLabel("SECOND LABEL")
#         label3 = QLabel("THIRD LABEL" )
#         info_vBox.addWidget(labe1)
#         info_vBox.addWidget(label2)
#         info_vBox.addWidget(label3)
#         bottom_layer.addLayout(info_vBox)
#
#         top_layer.addWidget(dragAdrop.returnDaD(self))
#         widget = QWidget()
#         widget.setLayout(main_layout)
#         self.setCentralWidget(widget)
#
# class dragAdrop:
#
#     def returnDaD(self):
#         photoViewer = QLabel()
#         photoViewer.setStyleSheet('''
#                    QLabel{
#                        border: 4px dashed #aaa
#                    }
#                ''')
#         photoViewer.setFixedSize(300, 230)
#         photoViewer.setScaledContents(True)
#         photoViewer.setAcceptDrops(True)
#
#         def dragEnterEvent( event):
#             if event.mimeData().hasImage:
#                 event.accept()
#             else:
#                 event.ignore()
#
#         def dragMoveEvent(self, event):
#             if event.mimeData().hasImage:
#                 event.accept()
#             else:
#                 event.ignore()
#
#         def dropEvent(self, event):
#             if event.mimeData().hasImage:
#                 event.setDropAction(Qt.CopyAction)
#                 file_path = event.mimeData().urls()[0].toLocalFile()
#                 self.set_image(file_path)
#
#                 event.accept()
#             else:
#                 event.ignore()
#
#         def set_image(self, file_path):
#             self.photoViewer.setPixmap(QPixmap(file_path))
#
#         return photoViewer






app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()