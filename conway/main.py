import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtWidgets, QtCore

generation = 0
n = 50

def update(img, label):
    global generation
    generation += 1
    global n
    matrix = matrix = [[0 for _ in range(n)] for _ in range(n)]
    matrix[0][0] = 1
    np_matrix = np.array(matrix, dtype=np.uint8)
    img.setImage(np_matrix)
    label.setText(f"Generation: {generation}")

def main():
    global n
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
    matrix = matrix = [[0 for _ in range(n)] for _ in range(n)]
    matrix[0][0] = 1
    np_matrix = np.array(matrix, dtype=np.uint8)
    img.setImage(np_matrix)

    # timer for updating the matrix
    timer = QtCore.QTimer()
    timer.timeout.connect(lambda: update(img, label))
    timer.start(500)

    win.show()
    QtWidgets.QApplication.instance().exec_()





