# importing the required module
import matplotlib.pyplot as plt

def lerp(p0: float, p1: float, t: float) -> float:
    """Linear interpolate on the scale given by a to b, using t as the point on that scale.
    Examples
    --------
        50 == lerp(0, 100, 0.5)
        4.2 == lerp(1, 5, 0.8)
    """
    return (1 - t) * p0 + t * p1

def curve(vector1, vector2):
    lerpA = list()
    lerpB = list()
    lerpPonto = list()
    for i in range(0, 11, 1):
        lerpA.append(lerp(vector1[0][0], vector1[0][1], i/10))
        lerpA.append(lerp(vector1[1][0], vector1[1][1], i/10))

        lerpB.append(lerp(vector2[0][0], vector2[0][1], i/10))
        lerpB.append(lerp(vector2[1][0], vector2[1][1], i/10))



        lerpPonto.append([lerp(lerpA[0], lerpA[1], i / 10)])
        lerpPonto.append([lerp(lerpB[0], lerpB[1], i / 10)])

        lerpA.clear()
        lerpB.clear()




    return lerpPonto

# x axis values
x_first_line = [1, 2]
# corresponding y axis values
y_first_line = [2, 4]

x_second_line = [2, 3]

y_second_line = [4, 2]

lerps1 = list()
lerps2 = list()

lerpA = list()
lerpB = list()

print(curve([x_first_line, y_first_line], [x_second_line, y_second_line]))


lerpA.append(lerp(x_first_line[0],x_first_line[1],0))
lerpA.append(lerp(y_first_line[0],y_first_line[1],0))

lerpB.append(lerp(x_second_line[0],x_second_line[1],0))
lerpB.append(lerp(y_second_line[0],y_second_line[1],0))

print(lerpA[0], " " ,lerpA[1])






# plotting the points

# naming the x_axis
plt.xlabel('x - axis')
# naming the y_axis
plt.ylabel('y - axis')

plt.xlim(0, 5)
plt.ylim(0, 5)

plt.plot(x_first_line, y_first_line)

plt.plot(x_second_line, y_second_line)

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
x = [4]
y = [3]

plt.grid()
plt.plot(lerpA[0], lerpA[1], marker="o", markersize=10, markeredgecolor="red", markerfacecolor="green")
plt.plot(lerpB[0], lerpB[1], marker="o", markersize=10, markeredgecolor="red", markerfacecolor="green")
plt.show()


