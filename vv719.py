import csv
import numpy as np
import matplotlib.pyplot as plt
import sys


v1 = [
1.573,
1.460,
1.288,
1.150,
1.060,
0.939,
0.869,
0.802,
0.726,
0.695,
0.613,
0.527,
0.471,
0.442,
]

v2 = [
1.468,
1.326,
1.109,
0.938,
0.831,
0.687,
0.601,
0.527,
0.436,
0.404,
0.305,
0.204,
0.132,
0.107,
]

t3 = [
34.8,
35.5,
36,
36.5,
37.1,
37.6,
37.9,
38.3,
38.7,
39.6,
39.5,
39.7,
40,
40.1,
40.3,
]

v3 = [
1.418,
1.271,
1.043,
0.871,
0.765,
0.610,
0.532,
0.468,
0.374,
0.341,
0.237,
0.151,
0.081,
0.042,
]

vol = [
0.04,
0.52,
1.21,
1.77,
2.15,
2.67,
3.00,
3.28,
3.62,
3.70,
4.10,
4.50,
4.80,
4.94,
]

v2_1 = [
1.471,
1.301,
1.179,
1.06,
0.91,
0.786,
0.696,
0.610,
0.521,
0.410,
0.340,
0.248,
0.125,
0.071,
]

v3_1 = [
1.423,
1.250,
1.120,
1.014,
0.863,
0.743,
0.646,
0.563,
0.468,
0.358,
0.273,
0.196,
0.089,
0.02,
]

vol_1 = [
0.05,
0.57,
0.97,
1.30,
1.78,
2.2,
2.51,
2.82,
3.15,
3.6,
3.95,
4.31,
4.7,
4.99,
]


v1_2 = [
1.452,
1.301,
1.179,
0.934,
0.801,
0.747,
0.663,
0.518,
0.427,
0.375,
0.269,
0.223,
0.189,
]

v2_2 = [
1.468,
1.305,
1.172,
0.895,
0.754,
0.695,
0.611,
0.457,
0.360,
0.296,
0.174,
0.140,
0.088,
]

v3_2 = [
1.418,
1.251,
1.117,
0.840,
0.681,
0.633,
0.553,
0.389,
0.289,
0.230,
0.120,
0.071,
0.035,
]

vol_2 = [
0,
0.52,
0.93,
1.80,
2.30,
2.52,
2.83,
3.45,
3.83,
4.06,
4.57,
4.83,
5.03,
]

v2_3 = [
1.466,
1.382,
1.282,
1.181,
1.107,
1.004,
0.954,
0.865,
0.769,
0.667,
0.564,
0.491,
0.405,
0.369,
0.303,
]

v3_3 = [
1.410,
1.323,
1.220,
1.116,
1.04,
0.937,
0.889,
0.795,
0.701,
0.595,
0.495,
0.421,
0.333,
0.298,
0.229,
]

vol_3 = [
0.04,
0.39,
0.78,
1.18,
1.49,
1.92,
2.13,
2.54,
2.97,
3.48,
3.99,
4.36,
4.81,
4.99,
5.35,
]

v2_or = [
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

v3_or = [
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

vol_or = [
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

def v2sv(v):
    return ((11.1*1.348-v)/10.1 - 1.348)*1000

def temp_offset(t):
    return 0.0009996 * ((t + 20) * (t + 20)) - 0.0404788 * (t + 20) - 9.927496 + 10.337232


if __name__ == '__main__':
    vol = list(x*20 for x in vol)
    vol_1 = list(x*20 for x in vol_1)
    vol_2 = list(x*20 for x in vol_2)
    vol_3 = list(x*20 for x in vol_3)
    vol_or = list(x*20 for x in vol_or)
    v1 = list(v2sv(x) for x in v1)
    v2 = list(v2sv(x) for x in v2)
    v3 = list(v2sv(x) for x in v3)
    v2_1 = list(v2sv(x) for x in v2_1)
    v3_1 = list(v2sv(x) for x in v3_1)
    v2_2 = list(v2sv(x) for x in v2_2)
    v3_2 = list(v2sv(x) for x in v3_2)
    v2_3 = list(v2sv(x) for x in v2_3)
    v3_3 = list(v2sv(x) for x in v3_3)
    v2_or = list(v2sv(x) for x in v2_or)
    v3_or = list(v2sv(x) for x in v3_or)

    tmp1 = list(temp_offset(t) for t in t3)
    tmp = list(zip(v3_3, tmp1))
    v3_3_t = list(x[0] - x[1] for x in tmp);
    #v2 = v3_3

    num_order = 2
    coeffs1 = np.polyfit(v1, vol, num_order)
    p1 = np.poly1d(coeffs1)
    coeffs2 = np.polyfit(v2, vol, num_order)
    p2 = np.poly1d(coeffs2)
    coeffs3 = np.polyfit(v3, vol, num_order)
    p3 = np.poly1d(coeffs3)
    
    coeffs2_1 = np.polyfit(v2_1, vol_1, num_order)
    p2_1 = np.poly1d(coeffs2_1)
    coeffs3_1 = np.polyfit(v3_1, vol_1, num_order)
    p3_1 = np.poly1d(coeffs3_1)
    coeffs2_2 = np.polyfit(v2_2, vol_2, num_order)
    p2_2 = np.poly1d(coeffs2_2)
    coeffs3_2 = np.polyfit(v3_2, vol_2, num_order)
    p3_2 = np.poly1d(coeffs3_2)
    coeffs2_3 = np.polyfit(v2_3, vol_3, num_order)
    p2_3 = np.poly1d(coeffs2_3)
    coeffs3_3 = np.polyfit(v3_3, vol_3, num_order)
    p3_3 = np.poly1d(coeffs3_3)
    coeffs3_3_t = np.polyfit(v3_3_t, vol_3, num_order)
    p3_3_t = np.poly1d(coeffs3_3_t)

    coeffs2_or = np.polyfit(v2_or, vol_or, num_order)
    p2_or = np.poly1d(coeffs2_or)
    coeffs3_or = np.polyfit(v3_or, vol_or, num_order)
    p3_or = np.poly1d(coeffs3_or)

    print(coeffs1)
    print("coeffs2")
    print(coeffs2)
    print("coeffs2_1")
    print(coeffs2_1)
    print("coeffs3")
    print(coeffs3)
    print("coeffs3_1")
    print(coeffs3_1)

    print("coeffs2_2")
    print(coeffs2_2)
    print("coeffs3_2")
    print(coeffs3_2)

    print("coeffs2_3")
    print(coeffs2_3)
    print("coeffs3_3")
    print(coeffs3_3)
    print("coeffs2_or")
    print(coeffs2_or)
    print("coeffs3_or")
    print(coeffs3_or)

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
  #          x, p1(x), 'r-',
  #          v1, vol, 'ro',
            x, p2(x), 'g-',
            v2, vol, 'go',
            x, p3(x), 'b-',
            v3, vol, 'bo',
            x, p2_1(x), 'k-',
            v2_1, vol_1, 'k>',
            x, p3_1(x), 'c-',
            v3_1, vol_1, 'c>',
            markersize=5)
    plt.plot(x, p2_2(x), color='#00ff00', linestyle='-', markersize=5)
    plt.plot(v2_2, vol_2, color='#00ff00', linestyle='', marker='>', markersize=5)
    plt.plot(x, p3_2(x), color='#ff0000', linestyle='-', markersize=5)
    plt.plot(v3_2, vol_2, color='#ff0000', linestyle='', marker='>', markersize=5)

    plt.plot(x, p2_3(x), color='#353500', linestyle='-', markersize=5)
    plt.plot(v2_3, vol_3, color='#353500', linestyle='', marker='>', markersize=5)
    plt.plot(x, p3_3(x), color='#550055', linestyle='-', markersize=5)
    plt.plot(v3_3, vol_3, color='#550055', linestyle='', marker='>', markersize=5)
    plt.plot(x, p3_3_t(x), color='#ff0000', linestyle='-', markersize=5)
    plt.plot(v3_3_t, vol_3, color='#ff0000', linestyle='', marker='>', markersize=5)

    plt.plot(x, p2_or(x), color='#707000', linestyle='-', markersize=5)
    plt.plot(v2_or, vol_or, color='#707000', linestyle='', marker='>', markersize=5)
    plt.plot(x, p3_or(x), color='#aa00aa', linestyle='-', markersize=5)
    plt.plot(v3_or, vol_or, color='#aa00aa', linestyle='', marker='>', markersize=5)
    plt.show()
