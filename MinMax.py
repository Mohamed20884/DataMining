import sys

__author__ = 'Mohamed'


def get_matrix_from_file(fp):
    f = open(fp, 'r')
    m = []
    while True:
        try:
            t = [float(x) for x in f.readline().strip('\n').split(',')]
        except:
            break
        m.append(t)
    f.close()
    return m

def min_max(v, mx, mi):
    v = (v - mi) / (mx-mi)
    return v
import  csv
import  sys
def get_max_every_column(m):
    print m
    for column in range(len(m[0])):
        max = float('-inf')
        min = float('inf')
        for row in range(len(m)):
            if m[row][column] < min:
                min = m[row][column]
            if m[row][column] > max:
                max = m[row][column]
        for i in range(len(m)):
            m[i][column] = min_max(m[i][column], max, min)
    print m
    p = ''
    p += '%.17f' % m[0][1]
    print p
    f = open("Spambase.txt", "w")
    for r in range(len(m)):
        s = ""
        for c in range(len(m[0])):
            s += "%.17f," % m[r][c]
        print s
        s = s[:-1]
        s += "\n"
        f.write(s)







if __name__ == '__main__':
    m = get_matrix_from_file('Spambase/spambase.data')
    get_max_every_column(m)