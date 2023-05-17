import numpy
import pandas as pd
import openpyxl

x_neg = -22500  # (negative x coordinate in micrometer)
x_pos = 22500  # (positive x coordinate in micrometer)
y_neg = -22500  # (negative y coordinate in micrometer)

scan_space = 120  # scan space 120um or 0.12mm


time = 0  # (first time 0)
scan_time = 45918  # scan speed 980mm/s. so 45 mm travels at (45/980 = 0.045918 s) or 45.918 ms or 45918 us
scan_space_time = 6243.4935  # time for scan space ; scan space speed 19.22 mm/s; for 0.12 mm time is 6.2435ms or
# 6243.4963 us

x_coordinate_um = []
y_coordinate_um = []
time_step = []

step_for_x = 1
for x in range(375):
    iteration = 1

    for y in range(2):  # assigning same sign for x coordinate
        if step_for_x % 2 != 0:  # means for first step 1%2 = 1, then x coordinate positive
            x_coordinate_um.append(x_pos)

            if iteration % 2 != 0:  # means 1%2 = 1, then x coordinate positive, y coordinate negative
                time += scan_time
                time_step.append(time)
                y_coordinate_um.append(y_neg)
            else:
                y_neg += scan_space  # for scan space
                y_coordinate_um.append(y_neg)
                time += scan_space_time
                time_step.append(time)

            iteration += 1

        else:
            x_coordinate_um.append(x_neg)

            if iteration % 2 != 0:
                time += scan_time
                time_step.append(time)
                y_coordinate_um.append(y_neg)
            else:
                y_neg += scan_space
                y_coordinate_um.append(y_neg)
                time += scan_space_time
                time_step.append(time)

            iteration += 1
    step_for_x += 1

x_um = numpy.array(x_coordinate_um)
y_um = numpy.array(y_coordinate_um)
time_step_us = numpy.array(time_step)


data = pd.DataFrame([time_step_us, x_um, y_um])
data_trans = data.T
data_add = pd.DataFrame([[0, -22500, -22500]], columns=data_trans.columns)
data_final = pd.concat([data_add, data_trans])

print(data_final)
data_final.to_excel('LaserLine.xlsx', index=False, header=False)
