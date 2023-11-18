import csv
import numpy as np
import matplotlib.pyplot as plt
import sys

#你好

#  2----4
vol_1 = [
0.03,
0.49,
0.91,
1.40,
1.96,
2.60,
3.16,
3.56,
4.15,
4.64,
5.17,
]

vol_2 = [
0.03,
0.68,
1.11,
1.94,
2.58,
3.27,
4.01,
4.63,
5.11,
]

vol_3 = [
0,
0.65,
1.17,
1.92,
2.59,
3.22,
3.83,
4.57,
5.16,
]

vol_4 = [
0.02,
0.62,
0.98,
1.53,
2.19,
2.95,
3.39,
4.31,
4.83,
5.19,
]

vol_6 = [
0.03,
0.85,
1.59,
2.17,
2.57,
3.05,
3.79,
4.18,
4.96,
]

vol_7 = [
0,
0.47,
1.16,
1.79,
2.66,
3.23,
3.85,
4.27,
4.79,
5.04,
]

vol_8 = [
0.03,
0.57,
1.11,
1.58,
2.30,
2.95,
3.48,
3.89,
4.35,
4.73,
5,
]

vol_9 = [
0.03,
0.70,
1.29,
1.83,
2.18,
2.92,
3.47,
4.05,
4.41,
5.08,
]

vol_10 = [
0.00,
0.85,
1.41,
2.35,
3.07,
3.72,
4.27,
5.15,
]


vol_11 = [
0.04,
0.55,
1.81,
2.55,
3.20,
3.87,
4.31,
4.98,
]


v1_1 = [

]

v1_2 = [

]

v1_3 = [

]

v1_4 = [

]


v2_1 = [
1.643,
1.537,
1.428,
1.303,
1.166,
1.016,
0.891,
0.799,
0.674,
0.572,
0.465,
]

v2_2 = [
1.638,
1.486,
1.373,
1.177,
1.017,
0.862,
0.700,
0.572,
0.475,
]

v2_3 = [
1.646,
1.494,
1.357,
1.165,
1.013,
0.872,
0.741,
0.582,
0.467,
]

v2_4 = [
1.651,
1.509,
1.418,
1.277,
1.116,
0.940,
0.840,
0.647,
0.538,
0.465,
]

v2_6 = [
1.652,
1.450,
1.264,
1.120,
1.018,
0.906,
0.744,
0.660,
0.495,
]

v2_7 = [
1.648,
1.530,
1.351,
1.188,
0.986,
0.849,
0.711,
0.623,
0.514,
0.460,
]

v2_8 = [
1.652,
1.521,
1.382,
1.263,
1.093,
0.933,
0.815,
0.724,
0.627,
0.546,
0.491,
]


v2_9 = [
1.654,
1.500,
1.349,
1.207,
1.118,
0.944,
0.822,
0.693,
0.615,
0.480,
]


v2_10 = [
1.645,
1.432,
1.280,
1.057,
0.888,
0.737,
0.617,
0.437,
]

v2_11 = [
1.656,
1.538,
1.210,
1.033,
0.882,
0.736,
0.639,
0.500,
]


v3_1 = [
1.453,
1.346,
1.235,
1.108,
0.972,
0.823,
0.697,
0.607,
0.486,
0.385,
0.282,
]

v3_2 = [
1.460,
1.306,
1.192,
0.994,
0.835,
0.682,
0.520,
0.395,
0.297,
]

v3_3 = [
1.468,
1.314,
1.175,
0.985,
0.830,
0.690,
0.563,
0.404,
0.291,
]

v3_4 = [
1.475,
1.330,
1.238,
1.097,
0.937,
0.761,
0.662,
0.475,
0.366,
0.293,
]

v3_6 = [
1.476,
1.277,
1.095,
0.953,
0.854,
0.743,
0.587,
0.505,
0.345,
]

v3_7 = [
1.473,
1.355,
1.179,
1.020,
0.822,
0.689,
0.554,
0.446,
0.363,
0.310,
]

v3_8 = [
1.478,
1.350,
1.210,
1.092,
0.926,
0.771,
0.655,
0.567,
0.472,
0.393,
0.338,
]

v3_9 = [
1.481,
1.326,
1.178,
1.039,
0.952,
0.783,
0.664,
0.536,
0.464,
0.332,
]


v3_10 = [
1.472,
1.260,
1.113,
0.893,
0.728,
0.582,
0.464,
0.289,
]

v3_11 = [
1.481,
1.362,
1.042,
0.869,
0.721,
0.579,
0.484,
0.351,
]


v4_1 = [
1.440,
1.328,
1.215,
1.085,
0.945,
0.792,
0.664,
0.573,
0.449,
0.346,
0.238,
]

v4_2 = [
1.446,
1.286,
1.167,
0.965,
0.801,
0.643,
0.479,
0.349,
0.252,
]

v4_3 = [
1.442,
1.282,
1.138,
0.943,
0.785,
0.641,
0.510,
0.349,
0.234,
]

v4_4 = [
1.447,
1.296,
1.200,
1.056,
0.891,
0.711,
0.610,
0.417,
0.307,
0.235,
]

v4_6 = [
1.448,
1.241,
1.051,
0.907,
0.805,
0.691,
0.531,
0.448,
0.285,
]

v4_7 = [
1.441,
1.319,
1.136,
0.971,
0.768,
0.631,
0.495,
0.407,
0.301,
0.249,
]

v4_8 = [
1.446,
1.312,
1.167,
1.047,
0.877,
0.717,
0.598,
0.507,
0.412,
0.331,
0.278,
]

v4_9 = [
1.450,
1.291,
1.136,
0.993,
0.903,
0.729,
0.608,
0.478,
0.402,
0.269,
]


v4_10 = [
1.439,
1.220,
1.066,
0.842,
0.672,
0.522,
0.401,
0.224,
]

v4_11 = [
1.447,
1.324,
0.993,
0.814,
0.663,
0.517,
0.421,
0.285,
]



def v2sv(v):
    return ((11.1*1.348-v)/10.1 - 1.348)*1000

def temp_offset(t):
    return 0.0009996 * ((t + 20) * (t + 20)) - 0.0404788 * (t + 20) - 9.927496 + 10.337232

if __name__ == '__main__':
    #vol转lel
    vol_1 = list(x*20 for x in vol_1)
    vol_2 = list(x*20 for x in vol_2)
    vol_3 = list(x*20 for x in vol_3)
    vol_4 = list(x*20 for x in vol_4)

    vol_6 = list(x*20 for x in vol_6)
    vol_7 = list(x*20 for x in vol_7)
    vol_8 = list(x*20 for x in vol_8)
    vol_9 = list(x*20 for x in vol_9)

    vol_10 = list(x*20 for x in vol_10)
    vol_11 = list(x*20 for x in vol_11)
    #电压转换

    # v1_1 = list(v2sv(x) for x in v1_1)
    v2_1 = list(v2sv(x) for x in v2_1)
    v3_1 = list(v2sv(x) for x in v3_1)
    v4_1 = list(v2sv(x) for x in v4_1)

    # v1_2 = list(v2sv(x) for x in v1_2)
    v2_2 = list(v2sv(x) for x in v2_2)
    v3_2 = list(v2sv(x) for x in v3_2)
    v4_2 = list(v2sv(x) for x in v4_2)

    # v1_3 = list(v2sv(x) for x in v1_3)
    v2_3 = list(v2sv(x) for x in v2_3)
    v3_3 = list(v2sv(x) for x in v3_3)
    v4_3 = list(v2sv(x) for x in v4_3)


    # v1_4 = list(v2sv(x) for x in v1_4)
    v2_4 = list(v2sv(x) for x in v2_4)
    v3_4 = list(v2sv(x) for x in v3_4)
    v4_4 = list(v2sv(x) for x in v4_4)

    v2_6 = list(v2sv(x) for x in v2_6)
    v3_6 = list(v2sv(x) for x in v3_6)
    v4_6 = list(v2sv(x) for x in v4_6)

    v2_7 = list(v2sv(x) for x in v2_7)
    v3_7 = list(v2sv(x) for x in v3_7)
    v4_7 = list(v2sv(x) for x in v4_7)


    v2_8 = list(v2sv(x) for x in v2_8)
    v3_8 = list(v2sv(x) for x in v3_8)
    v4_8 = list(v2sv(x) for x in v4_8)

    v2_9 = list(v2sv(x) for x in v2_9)
    v3_9 = list(v2sv(x) for x in v3_9)
    v4_9 = list(v2sv(x) for x in v4_9)

    v2_10 = list(v2sv(x) for x in v2_10)
    v3_10 = list(v2sv(x) for x in v3_10)
    v4_10 = list(v2sv(x) for x in v4_10)

    v2_11 = list(v2sv(x) for x in v2_11)
    v3_11 = list(v2sv(x) for x in v3_11)
    v4_11 = list(v2sv(x) for x in v4_11)

    # tmp1 = list(temp_offset(t) for t in t3)
    # tmp = list(zip(v3_3, tmp1))
    # v3_3_t = list(x[0] - x[1] for x in tmp);
    #v2 = v3_3

    #函数拟合
    num_order = 2
 
    # coeffs1_1  = np.polyfit(v1_1, vol_1, num_order)
    # p1_1 = np.poly1d(coeffs1_1)
    coeffs2_1 = np.polyfit(v2_1, vol_1, num_order)
    p2_1 = np.poly1d(coeffs2_1)
    coeffs3_1  = np.polyfit(v3_1, vol_1, num_order)
    p3_1 = np.poly1d(coeffs3_1)
    coeffs4_1 = np.polyfit(v4_1, vol_1, num_order)
    p4_1 = np.poly1d(coeffs4_1)


    # coeffs1_2  = np.polyfit(v1_2, vol_2, num_order)
    # p1_2 = np.poly1d(coeffs1_2)
    coeffs2_2 = np.polyfit(v2_2, vol_2, num_order)
    p2_2 = np.poly1d(coeffs2_2)
    coeffs3_2  = np.polyfit(v3_2, vol_2, num_order)
    p3_2 = np.poly1d(coeffs3_2)
    coeffs4_2 = np.polyfit(v4_2, vol_2, num_order)
    p4_2 = np.poly1d(coeffs4_2)

    # coeffs1_3  = np.polyfit(v1_3, vol_3, num_order)
    # p1_3 = np.poly1d(coeffs1_3)
    coeffs2_3 = np.polyfit(v2_3, vol_3, num_order)
    p2_3 = np.poly1d(coeffs2_3)
    coeffs3_3  = np.polyfit(v3_3, vol_3, num_order)
    p3_3 = np.poly1d(coeffs3_3)
    coeffs4_3 = np.polyfit(v4_3, vol_3, num_order)
    p4_3 = np.poly1d(coeffs4_3)

    # coeffs1_4  = np.polyfit(v1_4, vol_4, num_order)
    # p1_4 = np.poly1d(coeffs1_4)
    coeffs2_4 = np.polyfit(v2_4, vol_4, num_order)
    p2_4 = np.poly1d(coeffs2_4)
    coeffs3_4  = np.polyfit(v3_4, vol_4, num_order)
    p3_4 = np.poly1d(coeffs3_4)
    coeffs4_4 = np.polyfit(v4_4, vol_4, num_order)
    p4_4 = np.poly1d(coeffs4_4)


    coeffs2_6 = np.polyfit(v2_6, vol_6, num_order)
    p2_6 = np.poly1d(coeffs2_6)
    coeffs3_6  = np.polyfit(v3_6, vol_6, num_order)
    p3_6 = np.poly1d(coeffs3_6)
    coeffs4_6 = np.polyfit(v4_6, vol_6, num_order)
    p4_6 = np.poly1d(coeffs4_6)

    coeffs2_7 = np.polyfit(v2_7, vol_7, num_order)
    p2_7 = np.poly1d(coeffs2_7)
    coeffs3_7  = np.polyfit(v3_7, vol_7, num_order)
    p3_7 = np.poly1d(coeffs3_7)
    coeffs4_7 = np.polyfit(v4_7, vol_7, num_order)
    p4_7 = np.poly1d(coeffs4_7)

    coeffs2_8 = np.polyfit(v2_8, vol_8, num_order)
    p2_8 = np.poly1d(coeffs2_8)
    coeffs3_8  = np.polyfit(v3_8, vol_8, num_order)
    p3_8 = np.poly1d(coeffs3_8)
    coeffs4_8 = np.polyfit(v4_8, vol_8, num_order)
    p4_8 = np.poly1d(coeffs4_8)


    coeffs2_9 = np.polyfit(v2_9, vol_9, num_order)
    p2_9 = np.poly1d(coeffs2_9)
    coeffs3_9  = np.polyfit(v3_9, vol_9, num_order)
    p3_9 = np.poly1d(coeffs3_9)
    coeffs4_9 = np.polyfit(v4_9, vol_9, num_order)
    p4_9 = np.poly1d(coeffs4_9)


    coeffs2_10 = np.polyfit(v2_10, vol_10, num_order)
    p2_10 = np.poly1d(coeffs2_10)
    coeffs3_10  = np.polyfit(v3_10, vol_10, num_order)
    p3_10 = np.poly1d(coeffs3_10)
    coeffs4_10 = np.polyfit(v4_10, vol_10, num_order)
    p4_10 = np.poly1d(coeffs4_10)


    coeffs2_11 = np.polyfit(v2_11, vol_11, num_order)
    p2_11 = np.poly1d(coeffs2_11)
    coeffs3_11  = np.polyfit(v3_11, vol_11, num_order)
    p3_11 = np.poly1d(coeffs3_11)
    coeffs4_11 = np.polyfit(v4_11, vol_11, num_order)
    p4_11 = np.poly1d(coeffs4_11)


    #打印函数值

    # print("coeffsn1_1")
    # print(coeffs1_1)
    # print("coeffsn1_2")
    # print(coeffs1_2)
    # print("coeffsn1_3")
    # print(coeffs1_3)
    # print("coeffsn1_4")
    # print(coeffs1_4)
    # print("coeffsn1adv")
    # print((coeffs1_2+coeffs1_3)/2)


    # print("coeffs2_1")
    # print(coeffs2_1)
    # print("coeffs2_2")
    # print(coeffs2_2)
    # print("coeffs2_3")
    # print(coeffs2_3)
    # print("coeffs2_4")
    # print(coeffs2_4)

    print("coeffsn2_6")
    print(coeffs2_6)
    print("coeffsn2_7")
    print(coeffs2_7)
    print("coeffsn2_8")
    print(coeffs2_8)
    print("coeffsn2_9")
    print(coeffs2_9)
    print("coeffsn2_10")
    print(coeffs2_10)
    print("coeffsn2_11")
    print(coeffs2_11)

    print("coeffsn2_adv")
    print((coeffs2_6+coeffs2_7+coeffs2_8+coeffs2_9+coeffs2_10+coeffs2_11)/6)


    # print("coeffs3_1")
    # print(coeffs3_1)
    # print("coeffs3_2")
    # print(coeffs3_2)
    # print("coeffs3_3")
    # print(coeffs3_3)
    # print("coeffs3_4")
    # print(coeffs3_4)
    print("coeffsn3_6")
    print(coeffs3_6)
    # print("coeffsn3_7")
    # print(coeffs3_7)
    print("coeffsn3_8")
    print(coeffs3_8)
    print("coeffsn3_9")
    print(coeffs3_9)
    print("coeffsn3_11")
    print(coeffs3_11)

    print("coeffsn3_adv")
    print((coeffs3_6+coeffs3_8+coeffs3_9+coeffs3_11)/4)


    # print("coeffs4_1")
    # print(coeffs4_1)
    # print("coeffs4_2")
    # print(coeffs4_2)
    # print("coeffs4_3")
    # print(coeffs4_3)
    # print("coeffs4_4")
    # print(coeffs4_4)
    print("coeffsn4_6")
    print(coeffs4_6)
    # print("coeffsn4_7")
    # print(coeffs4_7)  
    print("coeffsn4_8")
    print(coeffs4_8)
    print("coeffsn4_9")
    print(coeffs4_9)    
    print("coeffsn4_11")
    print(coeffs4_11)
    print("coeffsn4_adv")
    print((coeffs4_6+coeffs4_8+coeffs4_9+coeffs4_11)/4)


    #图像设置（不用动）
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

    #画曲线

    #2023.08.9
    #                       鸨色
    # plt.plot(x, p1_1(x), color='#f7acbc', linestyle='-', markersize=5)
    # plt.plot(v1_1, vol_1, color='#f7acbc', linestyle='', marker='>', markersize=5)
    # plt.plot(x, p1_2(x), color='#f7acbc', linestyle='-', markersize=5)
    # plt.plot(v1_2, vol_2, color='#f7acbc', linestyle='', marker='>', markersize=5)

    # plt.plot(x, p1_3(x), color='#f7acbc', linestyle='-', markersize=5)
    # plt.plot(v1_3, vol_3, color='#f7acbc', linestyle='', marker='>', markersize=5)
    # plt.plot(x, p1_4(x), color='#f7acbc', linestyle='-', markersize=5)
    # plt.plot(v1_4, vol_4, color='#f7acbc', linestyle='', marker='>', markersize=5)

    #                       赤白橡
    # plt.plot(x, p2_1(x), color='#deab8a', linestyle='-', markersize=5)
    # plt.plot(v2_1, vol_1, color='#deab8a', linestyle='', marker='>', markersize=5)
    # plt.plot(x, p2_2(x), color='#deab8a', linestyle='-', markersize=5)
    # plt.plot(v2_2, vol_2, color='#deab8a', linestyle='', marker='>', markersize=5)

    # plt.plot(x, p2_3(x), color='#deab8a', linestyle='-', markersize=5)
    # plt.plot(v2_3, vol_3, color='#deab8a', linestyle='', marker='>', markersize=5)
    # plt.plot(x, p2_4(x), color='#deab8a', linestyle='-', markersize=5)
    # plt.plot(v2_4, vol_4, color='#deab8a', linestyle='', marker='>', markersize=5)

    plt.plot(x, p2_6(x), color='#deab8a', linestyle='-', markersize=5)
    plt.plot(v2_6, vol_6, color='#deab8a', linestyle='', marker='>', markersize=5)
    plt.plot(x, p2_7(x), color='#f7acbc', linestyle='-', markersize=5)
    plt.plot(v2_7, vol_7, color='#f7acbc', linestyle='', marker='>', markersize=5)
    plt.plot(x, p2_8(x), color='#817936', linestyle='-', markersize=5)
    plt.plot(v2_8, vol_8, color='#817936', linestyle='', marker='>', markersize=5)
    plt.plot(x, p2_9(x), color='#817936', linestyle='-', markersize=5)
    plt.plot(v2_9, vol_9, color='#817936', linestyle='', marker='>', markersize=5)
    plt.plot(x, p2_10(x), color='#f7acbc', linestyle='-', markersize=5)
    plt.plot(v2_10, vol_10, color='#f7acbc', linestyle='', marker='>', markersize=5)
    plt.plot(x, p2_11(x), color='#f7acbc', linestyle='-', markersize=5)
    plt.plot(v2_11, vol_11, color='#f7acbc', linestyle='', marker='>', markersize=5)
    #                       油色
    # plt.plot(x, p3_1(x), color='#817936', linestyle='-', markersize=5)
    # plt.plot(v3_1, vol_1, color='#817936', linestyle='', marker='>', markersize=5)
    # plt.plot(x, p3_2(x), color='#817936', linestyle='-', markersize=5)
    # plt.plot(v3_2, vol_2, color='#817936', linestyle='', marker='>', markersize=5)

    # plt.plot(x, p3_3(x), color='#817936', linestyle='-', markersize=5)
    # plt.plot(v3_3, vol_3, color='#817936', linestyle='', marker='>', markersize=5)
    # plt.plot(x, p3_4(x), color='#817936', linestyle='-', markersize=5)
    # plt.plot(v3_4, vol_4, color='#817936', linestyle='', marker='>', markersize=5)

    # plt.plot(x, p3_6(x), color='#817936', linestyle='-', markersize=5)
    # plt.plot(v3_6, vol_6, color='#817936', linestyle='', marker='>', markersize=5)
    # # plt.plot(x, p3_7(x), color='#f7acbc', linestyle='-', markersize=5)
    # # plt.plot(v3_7, vol_7, color='#f7acbc', linestyle='', marker='>', markersize=5)
    # plt.plot(x, p3_8(x), color='#444693', linestyle='-', markersize=5)
    # plt.plot(v3_8, vol_8, color='#444693', linestyle='', marker='>', markersize=5)
    # plt.plot(x, p3_9(x), color='#444693', linestyle='-', markersize=5)
    # plt.plot(v3_9, vol_9, color='#444693', linestyle='', marker='>', markersize=5)
    # # plt.plot(x, p3_10(x), color='#f7acbc', linestyle='-', markersize=5)
    # # plt.plot(v3_10, vol_10, color='#f7acbc', linestyle='', marker='>', markersize=5)
    # plt.plot(x, p3_11(x), color='#f7acbc', linestyle='-', markersize=5)
    # plt.plot(v3_11, vol_11, color='#f7acbc', linestyle='', marker='>', markersize=5)
    #                       绀桔梗
    # plt.plot(x, p4_1(x), color='#444693', linestyle='-', markersize=5)
    # plt.plot(v4_1, vol_1, color='#444693', linestyle='', marker='>', markersize=5)
    # plt.plot(x, p4_2(x), color='#444693', linestyle='-', markersize=5)
    # plt.plot(v4_2, vol_2, color='#444693', linestyle='', marker='>', markersize=5)
    
    # plt.plot(x, p4_3(x), color='#444693', linestyle='-', markersize=5)
    # plt.plot(v4_3, vol_3, color='#444693', linestyle='', marker='>', markersize=5)
    # plt.plot(x, p4_4(x), color='#444693', linestyle='-', markersize=5)
    # plt.plot(v4_4, vol_4, color='#444693', linestyle='', marker='>', markersize=5)

    # plt.plot(x, p4_6(x), color='#444693', linestyle='-', markersize=5)
    # plt.plot(v4_6, vol_6, color='#444693', linestyle='', marker='>', markersize=5)
    # # plt.plot(x, p4_7(x), color='#f7acbc', linestyle='-', markersize=5)
    # # plt.plot(v4_7, vol_7, color='#f7acbc', linestyle='', marker='>', markersize=5)
    # plt.plot(x, p4_8(x), color='#817936', linestyle='-', markersize=5)
    # plt.plot(v4_8, vol_8, color='#817936', linestyle='', marker='>', markersize=5)
    # plt.plot(x, p4_9(x), color='#817936', linestyle='-', markersize=5)
    # plt.plot(v4_9, vol_9, color='#817936', linestyle='', marker='>', markersize=5)
    # # plt.plot(x, p4_10(x), color='#f7acbc', linestyle='-', markersize=5)
    # # plt.plot(v4_10, vol_10, color='#f7acbc', linestyle='', marker='>', markersize=5)
    # plt.plot(x, p4_11(x), color='#f7acbc', linestyle='-', markersize=5)
    # plt.plot(v4_11, vol_11, color='#f7acbc', linestyle='', marker='>', markersize=5)
    plt.show()
