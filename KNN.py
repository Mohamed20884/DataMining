__author__ = 'Mohamed'
import csv
import random
import math
import operator


def get_matrix_from_file(fp):
    f = open(fp, 'r')
    m = []
    while True:
        try:
            t = [float(x) for x in f.readline().strip('\n')[:-1].split(',')]
        except:
            break
        m.append(t)
    f.close()
    return m


def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += pow((instance1[x] - instance2[x]), 2)
    return (distance)


def getAccuracy(m, predictions):
    correct = 0
    for x in range(len(m)):
        if m[x][-1] == predictions[x]:
            correct += 1
    return (correct / float(len(m))) * 100.0


def main():
    # prepare data
    m = get_matrix_from_file('normalisedEEGEye.arff')
    neighbour = -1
    # generate predictions
    predictions = []
    for x in range(len(m)):
        closest = 100000000000
        for row in range(len(m)):
            if x != row:
                e = euclideanDistance(m[x], m[row], 14)
                if e < closest:
                    closest = e
                    neighbour = row

        predictions.append(m[neighbour][-1])
        print ("prediction for %d is  %d") % (x, m[neighbour][-1])
    print getAccuracy(m, predictions)






if __name__ == '__main__':
    main()