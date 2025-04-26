# conway
Conway's Game of Life in Python
<br><br>
Goal: To learn Poetry and package management with python
<br><br>
Even though it seemed complex at first, Conway's rules are ultimately really simple
- All you really do is for each node, check it's neighbors to see how many are alive
<br><br>
Figuring out a graphics library for python that did what I wanted to was hard, but after a little bit of searching, using numpy and pyqtgraph made it fairly simple.
```python
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
```

## Instructions:
```bash
# make sure to have poetry installed
poetry install # installs dependencies

# runs the main script from the conway module
poetry run mat 
```

# Gif example:
![hippo](/assets/example.gif)
