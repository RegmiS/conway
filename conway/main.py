import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtWidgets, QtCore

generation = 0

def update(img, label):
    global generation
    generation += 1
    new_matrix = np.random.randint(0, 2, (20, 20)) * 255
    img.setImage(new_matrix)
    label.setText(f"Generation: {generation}")

def main():
    app = QtWidgets.QApplication([])
    
    # main layout window
    win = QtWidgets.QWidget()
    layout = QtWidgets.QVBoxLayout()
    win.setLayout(layout)

    #label for generation counter
    label = QtWidgets.QLabel("Generation: 0")
    label.setAlignment(QtCore.Qt.AlignCenter)
    label.setStyleSheet("font-size:18px; margin-bottom: 8px;")
    layout.addWidget(label)

    #matrix visualization
    graphics = pg.GraphicsLayoutWidget()
    view = graphics.addViewBox()
    img = pg.ImageItem()
    view.addItem(img)
    view.setAspectLocked(True)
    view.invertY(True)
    layout.addWidget(graphics)

    # Initial Matrix
    matrix = np.random.randint(0, 2, (20, 20)) * 255
    img.setImage(matrix)

    # timer for updating the matrix
    timer = QtCore.QTimer()
    timer.timeout.connect(lambda: update(img, label))
    timer.start(400)

    win.show()
    QtWidgets.QApplication.instance().exec_()





