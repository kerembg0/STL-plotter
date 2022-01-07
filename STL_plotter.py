import re
import numpy as np
import matplotlib.pyplot as plt


# cleaning data
f = open("<ASCII_file_name>.stl", "r")
f_text = f.read()

text = f_text.splitlines()

verticies = []

for i in range(len(text)):
    text[i] = text[i].strip()

for item in text:
    if (re.search("^vertex", item)):
        verticies.append(item)
    
verticies = list(dict.fromkeys(verticies))

for i in range(len(verticies)):
    verticies[i] = verticies[i][7:]

for i in range(len(verticies)):
    verticies[i] = verticies[i].split()

for i in range(len(verticies)):
    for j in range(3):
        verticies[i][j] = float(verticies[i][j])

verticies = np.array(verticies)

# setting axises
x = []
y = []
z = []

for i in range(len(verticies)):
    x.append(verticies[i][0])

for i in range(len(verticies)):
    y.append(verticies[i][1])

for i in range(len(verticies)):
    z.append(verticies[i][2])

x = np.array(x)
y = np.array(y)
z = np.array(z)

# plotting
fig = plt.figure(figsize = (100,100))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x, y ,z)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()


