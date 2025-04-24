import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtWidgets, QtCore
import random

generation = 0
n = 50
matrix = [[0 for _ in range(n)] for _ in range(n)]
# matrix[3][3] = 1
# matrix[3][4] = 1
# matrix[3][5] = 1

def checkLive():
    global matrix
    global n
    nmatrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            live = 0
            cur = matrix[i][j]
            # each cell has 8 neighbors (since diagonals count)
            dirs = [[0, 1], [1, 1], [-1, 1], [-1, 0], [1, 0], [-1, -1], [0, -1], [1, -1] ]
            for x,y in dirs:
                nx, ny = i+x, j+y
                if nx >= 0 and nx < n and ny >= 0 and ny < n:
                    if matrix[nx][ny] == 1:
                        live += 1
            if cur == 1:
                nmatrix[i][j] = 1 if live in [2,3] else 0
            else:
                nmatrix[i][j] = 1 if live == 3 else 0
    
    matrix = nmatrix


def update(img, label):
    global generation
    generation += 1
    global n
    global matrix
    checkLive()
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
    global matrix
    matrix = [[random.randint(0, 1) for _ in range(n)] for _ in range(n)]
    np_matrix = np.array(matrix, dtype=np.uint8)
    img.setImage(np_matrix)

    # timer for updating the matrix
    timer = QtCore.QTimer()
    timer.timeout.connect(lambda: update(img, label))
    timer.start(500)

    win.show()
    QtWidgets.QApplication.instance().exec_()
