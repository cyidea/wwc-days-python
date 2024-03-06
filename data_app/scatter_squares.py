import matplotlib.pyplot as pyplot

# get x that is in the range
# get y that is square of x

x_range = range(1, 1000)
y = [x**2 for x in x_range]

pyplot.style.use('seaborn-v0_8')
fig, ax = pyplot.subplots()
ax.scatter(x_range, y, s=10)

pyplot.show()