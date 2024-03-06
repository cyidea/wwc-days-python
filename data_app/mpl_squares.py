import matplotlib.pyplot as pyplot

inputs = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
cubs = [1, 8, 27, 64, 225]

pyplot.style.use('seaborn-v0_8')
fig, ax = pyplot.subplots()
ax.plot(inputs, squares, linewidth=3)
ax.scatter(inputs, cubs)


pyplot.show()