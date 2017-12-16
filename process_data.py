import math
import sys
import numpy as np


def calculateNodesDistances(file):
    speeds = []
    times = []
    distance = []
    prev_x = 0
    prev_y = 0
    with open(file, "r") as source:
        while True:
            line = source.readline()
            if line == "":
                break
            x, y, z = line.split(" - ")[0].split(",")
            times.append(int(line.split(" - ")[1]))
            x = float(x)
            y = float(y)
            distance.append(math.sqrt((x-prev_x)**2 + (y-prev_y)**2))
    for i in range(2, len(distance)):
        speeds.append(abs(distance[i]-distance[i-1])/(times[i]-times[i-1]))
    return speeds

if __name__ == "__main__":
    speeds = calculateNodesDistances(sys.argv[1])
    print("Max speed found: %f" % max(speeds))
    print("Min speed found: %f" % min(speeds))
    print("Variance %.3f" % np.var(speeds))
    print("Median %.3f" % np.median(speeds))
    print("Average %.3f" % np.average(speeds))
