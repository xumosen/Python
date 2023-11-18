import csv
import numpy as np
import matplotlib.pyplot as plt
import sys


v1 = [
1.541,
1.511,
1.425,
1.365,
1.271,
1.17,
1.04,
0.895,
0.776,
0.667,
0.623,
]

v2 = [
1.469,
1.425,
1.304,
1.237,
1.122,
0.999,
0.825,
0.669,
0.535,
0.442,
0.413,
]

t3 = [
33.6,
33.9,
34.3,
34.6,
34.9,
35.1,
35.5,
35.6,
36.1,
36.3,
36.6,
36.6,
37.1,
37.3,
37.4,
37.6,
37.8,
37.9,
38.1,
38.2,
38.4,
38.5,
38.6,
38.6,
38.8,
]

v3 = [
1.422,
1.37,
1.231,
1.158,
1.031,
0.895,
0.707,
0.537,
0.399,
0.3,
0.276,
]

v3_3 = [
1.42,
1.283,
1.172,
1.062,
0.922,
0.848,
0.730,
0.592,
#0.300,
0.441,
0.365,
0.336,
0.326,
]

vol = [
0,
0.24,
0.76,
1.04,
1.52,
2.07,
2.86,
3.62,
4.28,
4.75,
4.9,
]

vol1 = [
0,
0.58,
1.01,
1.46,
2.06,
2.39,
2.88,
3.51,
4.27,
4.63,
4.77,
4.83,
]

vol2 = [
0.02,
0.64,
0.95,
1.43,
2.20,
2.53,
3.35,
3.91,
4.26,
4.96,
]

v3_2 = [
1.411,
1.26,
1.186,
1.066,
0.926,
0.809,
0.632,
0.518,
0.44,
0.307,
]

vol_cool_1 = [
0.01,
0.38,
0.74,
1.4,
1.94,
2.47,
2.85,
3.36,
3.58,
3.81,
4.12,
4.61,
4.92,
]

v3_cool_1 = [
1.434,
1.346,
1.254,
1.090,
0.957,
0.834,
0.744,
0.635,
0.586,
0.536,
0.470,
0.375,
0.310,
]

vol_cool_2 = [
0.03,
0.41,
0.76,
1.21,
1.52,
1.79,
2.25,
2.69,
3.19,
3.44,
3.74,
3.99,
4.22,
4.52,
4.77,
5.03,
]

v3_cool_2 = [
1.414,
1.324,
1.235,
1.125,
1.047,
0.981,
0.875,
0.778,
0.667,
0.614,
0.547,
0.494,
0.451,
0.387,
0.342,
0.288,
]

vol_3_4 = [
0,
0.47,
1.02,
1.45,
2.06,
2.77,
3.21,
3.55,
3.96,
4.2,
4.53,
4.95,
]

v3_4 = [
1.424,
1.302,
1.155,
1.039,
0.888,
0.729,
0.625,
0.547,
0.465,
0.417,
0.355,
0.267,
]

def v2sv(v):
    return ((11.1*1.348-v)/10.1 - 1.348)*1000

def temp_offset(t):
    return 0.0009996 * ((t + 20) * (t + 20)) - 0.0404788 * (t + 20) - 9.927496 + 10.337232

def cool_1(v):
    #  return 0.89483416 * v + 4.61947647
    return 1.14471710e-03 * v * v + 7.78801647e-01 * v + 6.11641759e+00


if __name__ == '__main__':
    vol = list(x*20 for x in vol)
    vol1 = list(x*20 for x in vol1)
    vol2 = list(x*20 for x in vol2)
    vol_cool_1 = list(x*20 for x in vol_cool_1)
    vol_cool_2 = list(x*20 for x in vol_cool_2)
    vol_3_4 = list(x*20 for x in vol_3_4)
    v1 = list(v2sv(x) for x in v1)
    v2 = list(v2sv(x) for x in v2)
    v3 = list(v2sv(x) for x in v3)
    v3_3 = list(v2sv(x) for x in v3_3)
    v3_2 = list(v2sv(x) for x in v3_2)
    v3_cool_1 = list(v2sv(x) for x in v3_cool_1)
    v3_cool_2 = list(v2sv(x) for x in v3_cool_2)
    v3_4 = list(v2sv(x) for x in v3_4)

    e_3_cool_1 = list(cool_1(x) for x in v3_cool_2)
    tmp = list(zip(e_3_cool_1, vol_cool_2))
    e_3_cool_1 = list(x[1] - x[0] for x in tmp)
    e_3_cool_1_1 = list(cool_1(x) for x in v3_cool_1)
    tmp = list(zip(e_3_cool_1_1, vol_cool_1))
    e_3_cool_1_1 = list(x[1] - x[0] for x in tmp)
    #  tmp1 = list(temp_offset(t) for t in t3)
    #  tmp = list(zip(v3, tmp1))
    #  v3_3 = list(x[0] - x[1] for x in tmp);
    #v2 = v3_3

    num_order = 2
    coeffs1 = np.polyfit(v1, vol, num_order)
    p1 = np.poly1d(coeffs1)
    coeffs2 = np.polyfit(v2, vol, num_order)
    p2 = np.poly1d(coeffs2)
    coeffs3 = np.polyfit(v3, vol, num_order)
    p3 = np.poly1d(coeffs3)
    coeffs3_3 = np.polyfit(v3_3, vol1, num_order)
    p3_3 = np.poly1d(coeffs3_3);
    coeffs3_2 = np.polyfit(v3_2, vol2, num_order)
    p3_2 = np.poly1d(coeffs3_2);
    coeffs3_cool_1 = np.polyfit(v3_cool_1, vol_cool_1, num_order)
    p3_cool_1 = np.poly1d(coeffs3_cool_1);
    coeffs3_cool_2 = np.polyfit(v3_cool_2, vol_cool_2, num_order)
    p3_cool_2 = np.poly1d(coeffs3_cool_2);
    coeffs3_4 = np.polyfit(v3_4, vol_3_4, num_order)
    p3_4 = np.poly1d(coeffs3_4)

    print(coeffs1)
    print(coeffs2)
    print("coeffs3")
    print(coeffs3)
    print("coeffs3_3")
    print(coeffs3_3)
    print("coeffs3_2")
    print(coeffs3_2)
    print("coeffs3_cool_1")
    print(coeffs3_cool_1)
    print("coeffs3_cool_2")
    print(coeffs3_cool_2)
    print(e_3_cool_1)
    print(e_3_cool_1_1)

    x = np.linspace(-20, 160, 200)

    plt.figure(figsize=(16, 10))
    plt.ylabel('%LEL')
    plt.xlabel('mV')


    ax = plt.gca()
    ax.set_ylim(0, 100)
    ax.set_xlim(-20, 160)
    ax.yaxis.set_major_locator(plt.MultipleLocator(10))
    ax.yaxis.set_minor_locator(plt.MultipleLocator(1))
    ax.xaxis.set_major_locator(plt.MultipleLocator(10))
    ax.xaxis.set_minor_locator(plt.MultipleLocator(1))

    ax.grid(which='major', axis='y', linewidth=0.75, linestyle='-', color='0.75')
    ax.grid(which='minor', axis='y', linewidth=0.25, linestyle='-', color='0.75')
    ax.grid(which='major', axis='x', linewidth=0.75, linestyle='-', color='0.75')
    ax.grid(which='minor', axis='x', linewidth=0.25, linestyle='-', color='0.75')

    plt.plot(
            #  x, p1(x), 'r-',
            #  v1, vol, 'ro',
            x, p2(x), 'g-',
            v2, vol, 'go',
            x, p3(x), 'b-',
            v3, vol, 'bo',
            x, p3_3(x), 'm-',
            v3_3, vol1, 'mo',
            x, p3_2(x), 'y-',
            v3_2, vol2, 'yo',
            x, p3_cool_1(x), 'k-',
            v3_cool_1, vol_cool_1, 'ko',
            x, p3_cool_2(x), 'r-',
            v3_cool_2, vol_cool_2, 'ro',
            x, p3_4(x), 'g-',
            v3_4, vol_3_4, 'go',
            markersize=1)
    plt.show()
