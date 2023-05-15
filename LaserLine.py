import numpy
import pandas as pd

x_neg = -22.5
x_pos = 22.5
y_neg = -22.5
iteration = 1

time = 0

x_coordinate_mm = []
y_coordinate_mm = []
time_step = []

step_for_x = 1
for x in range(375):

    for y in range(2):
        if step_for_x % 2 != 0:
            x_coordinate_mm.append(x_pos)

            if iteration % 2 != 0:
                time += 45.92
                time_step.append(time)
                y_coordinate_mm.append(y_neg)
            else:
                y_neg += 0.12
                y_coordinate_mm.append(y_neg)
                time += 0.122
                time_step.append(time)

            iteration += 1

        else:
            x_coordinate_mm.append(x_neg)

            if iteration % 2 != 0:
                time += 45.92
                time_step.append(time)
                y_coordinate_mm.append(y_neg)
            else:
                y_neg += 0.12
                y_coordinate_mm.append(y_neg)
                time += 0.122
                time_step.append(time)

            iteration += 1
    step_for_x += 1

x_mm = numpy.array(x_coordinate_mm)
y_mm = numpy.array(y_coordinate_mm)
time_step_ms = numpy.array(time_step)
print("x", x_mm)
print("y", y_mm)
print("time ", time_step_ms)

data = pd.DataFrame([time_step_ms, x_mm, y_mm])
data_trans = data.T
data_add = pd.DataFrame([[0, -22.5, -22.5]], columns=data_trans.columns)
data_final = pd.concat([data_add, data_trans])

print(data_final)
data_final.to_excel('LaserLine.xlsx', index=False, header=False)

