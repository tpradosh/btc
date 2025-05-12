from matplotlib import pyplot as plt


x = [1,2,3,4]
y = [5,6,7,8]

plt.scatter(x,y)

other_x = [0,1,2,3,4]
other_y = [0,4,2,3,8]


plt.plot(other_x, other_y, color = "navy")

plt.show()