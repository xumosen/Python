import csv
import numpy as np
import matplotlib.pyplot as plt
import sys

#你好

#  5----9
#   拟合曲线贴合度相对较高  
vol_1 = [
0.06,
0.98,
1.65,
2.27,
3.03,
3.83,
4.44,
5.43,
]

vol_2 = [
0.03,
0.69,
1.34,
1.93,
2.65,
3.42,
4.20,
4.60,
5.18,
]

vol_3 = [
0,
0.79,
1.30,
1.91,
2.73,
3.34,
4.09,
4.83,
5.34,
]

vol_4 = [
0,
0.96,
1.73,
2.33,
3.49,
4.15,
4.77,
5.07,
]

vol_6 = [
0.00,
0.84,
1.49,
2.39,
3.16,
3.98,
5.01,
]

vol_7 = [
0.03,
0.45,
1.19,
1.60,
2.11,
2.69,
3.24,
3.61,
4.10,
4.60,
5.12,
]

vol_8 = [
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

vol_9 = [
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

vol_10 = [
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

vol_11 = [
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

vol_12 = [
0.00,
0.85,
1.41,
2.35,
3.07,
3.72,
4.27,
5.15,
]

vol_13 = [
0.04,
0.55,
1.81,
2.55,
3.20,
3.87,
4.31,
4.98,
]


v5_1 = [
1.577,
1.372,
1.225,
1.089,
0.930,
0.771,
0.649,
0.471,
]

v5_2 = [
1.584,
1.439,
1.299,
1.166,
1.009,
0.852,
0.701,
0.618,
0.518,
]

v5_3 = [
1.592,
1.420,
1.298,
1.152,
0.993,
0.863,
0.719,
0.566,
0.473,
]

v5_4 = [
1.569,
1.365,
1.193,
1.067,
0.826,
0.699,
0.576,
0.514,
]

v5_6 = [
1.611,
1.410,
1.255,
1.052,
0.883,
0.722,
0.521,
]

v5_7 = [
1.621,
1.522,
1.337,
1.241,
1.124,
0.992,
0.874,
0.794,
0.695,
0.592,
0.490,
]

v5_8 = [
1.613,
1.417,
1.235,
1.103,
1.005,
0.894,
0.743,
0.660,
0.503,
]

v5_9 = [
1.496,
1.325,
1.168,
0.977,
0.842,
0.712,
0.623,
0.520,
0.470,
]

v5_10 = [
1.617,
1.491,
1.354,
1.241,
1.079,
0.925,
0.811,
0.720,
0.630,
0.552,
0.500,
]

v5_11 = [
1.620,
1.470,
1.324,
1.186,
1.103,
0.937,
0.820,
0.695,
0.622,
0.493,
]

v5_12 = [
1.609,
1.403,
1.257,
1.045,
0.885,
0.741,
0.621,
0.451,
]

v5_13 = [
1.618,
1.501,
1.188,
1.019,
0.873,
0.732,
0.641,
0.507,
]


v6_1 = [
1.530,
1.298,
1.136,
0.996,
0.825,
0.658,
0.532,
0.355,
]

v6_2 = [
1.552,
1.384,
1.219,
1.078,
0.908,
0.747,
0.593,
0.512,
0.390,
]

v6_3 = [
1.543,
1.350,
1.217,
1.060,
0.886,
0.753,
0.597,
0.440,
0.354,
]

v6_4 = [
1.542,
1.306,
1.117,
0.978,
0.717,
0.560,
0.460,
0.409,
]

v6_6 = [
1.559,
1.355,
1.196,
0.986,
0.827,
0.649,
0.442,
]

v6_7 = [
1.571,
1.471,
1.286,
1.189,
1.070,
0.937,
0.817,
0.739,
0.641,
0.533,
0.433,
]

v6_8 = [
1.574,
1.368,
1.185,
1.045,
0.947,
0.840,
0.682,
0.600,
0.441,
]

v6_9 = [
1.453,
1.275,
1.116,
0.919,
0.785,
0.653,
0.565,
0.455,
0.415,
]

v6_10 = [
1.580,
1.447,
1.307,
1.191,
1.022,
0.867,
0.753,
0.662,
0.570,
0.490,
0.439,
]

v6_11 = [
1.583,
1.423,
1.273,
1.135,
1.051,
0.881,
0.759,
0.638,
0.563,
0.428,
]

v6_12 = [
1.569,
1.351,
1.209,
0.981,
0.820,
0.677,
0.561,
0.385,
]

v6_13 = [
1.581,
1.457,
1.138,
0.965,
0.818,
0.677,
0.593,
0.445,    
]

v7_1 = [
1.428,
1.209,
1.055,
0.922,
0.766,
0.612,
0.496,
0.317,
]

v7_2 = [
1.446,
1.285,
1.129,
1.000,
0.840,
0.687,
0.545,
0.464,
0.361,
]

v7_3 = [
1.437,
1.250,
1.128,
0.977,
0.819,
0.692,
0.552,
0.412,
0.321,
]

v7_4 = [
1.456,
1.218,
1.038,
0.906,
0.671,
0.547,
0.430,
0.368,
]

v7_6 = [
1.445,
1.247,
1.099,
0.907,
0.750,
0.591,
0.400,
]

v7_7 = [
1.454,
1.357,
1.183,
1.090,
0.981,
0.858,
0.750,
0.674,
0.581,
0.479,
0.395,
]

v8_1 = [
1.573,
1.336,
1.173,
1.033,
0.861,
0.692,
0.569,
0.380,
]

v8_2 = [
1.589,
1.417,
1.254,
1.113,
0.939,
0.775,
0.614,
0.533,
0.426,
]

v8_3 = [
1.586,
1.388,
1.253,
1.094,
0.917,
0.785,
0.625,
0.475,
0.380,
]

v8_4 = [
1.583,
1.346,
1.153,
1.009,
0.754,
0.616,
0.480,
0.439,
]

v8_6 = [
1.603,
1.389,
1.226,
1.018,
0.850,
0.673,
0.465,
]

v8_7 = [
1.611,
1.504,
1.315,
1.215,
1.097,
0.964,
0.843,
0.763,
0.667,
0.565,
0.461,
]


v9_1 = [
1.544,
1.292,
1.118,
0.966,
0.788,
0.612,
0.479,
0.286,
]

v9_2 = [
1.564,
1.383,
1.207,
1.057,
0.872,
0.703,
0.534,
0.452,
0.331,
]

v9_3 = [
1.554,
1.345,
1.204,
1.034,
0.852,
0.709,
0.546,
0.391,
0.290,
]

v9_4 = [
1.560,
1.305,
1.100,
0.952,
0.682,
0.535,
0.412,
0.347,
]

v9_6 = [
1.566,
1.335,
1.159,
0.932,
0.750,
0.567,
0.347,
]

v9_7 = [
1.578,
1.466,
1.263,
1.154,
1.026,
0.883,
0.757,
0.670,
0.576,
0.461,
0.360,
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
    
    vol_12 = list(x*20 for x in vol_12)
    vol_13 = list(x*20 for x in vol_13)
    #电压转换

    v5_1 = list(v2sv(x) for x in v5_1)
    v6_1 = list(v2sv(x) for x in v6_1)
    v7_1 = list(v2sv(x) for x in v7_1)
    v8_1 = list(v2sv(x) for x in v8_1)
    v9_1 = list(v2sv(x) for x in v9_1)

    v5_2 = list(v2sv(x) for x in v5_2)
    v6_2 = list(v2sv(x) for x in v6_2)
    v7_2 = list(v2sv(x) for x in v7_2)
    v8_2 = list(v2sv(x) for x in v8_2)
    v9_2 = list(v2sv(x) for x in v9_2)


    v5_3 = list(v2sv(x) for x in v5_3)
    v6_3 = list(v2sv(x) for x in v6_3)
    v7_3 = list(v2sv(x) for x in v7_3)
    v8_3 = list(v2sv(x) for x in v8_3)
    v9_3 = list(v2sv(x) for x in v9_3)

    v5_4 = list(v2sv(x) for x in v5_4)
    v6_4 = list(v2sv(x) for x in v6_4)
    v7_4 = list(v2sv(x) for x in v7_4)
    v8_4 = list(v2sv(x) for x in v8_4)
    v9_4 = list(v2sv(x) for x in v9_4)

    v5_6 = list(v2sv(x) for x in v5_6)
    v6_6 = list(v2sv(x) for x in v6_6)
    v7_6 = list(v2sv(x) for x in v7_6)
    v8_6 = list(v2sv(x) for x in v8_6)
    v9_6 = list(v2sv(x) for x in v9_6)

    v5_7 = list(v2sv(x) for x in v5_7)
    v6_7 = list(v2sv(x) for x in v6_7)
    v7_7 = list(v2sv(x) for x in v7_7)
    v8_7 = list(v2sv(x) for x in v8_7)
    v9_7 = list(v2sv(x) for x in v9_7)

    v5_8 = list(v2sv(x) for x in v5_8)
    v6_8 = list(v2sv(x) for x in v6_8)

    v5_9 = list(v2sv(x) for x in v5_9)
    v6_9 = list(v2sv(x) for x in v6_9)

    v5_10 = list(v2sv(x) for x in v5_10)
    v6_10 = list(v2sv(x) for x in v6_10)

    v5_11 = list(v2sv(x) for x in v5_11)
    v6_11 = list(v2sv(x) for x in v6_11)

    v5_12 = list(v2sv(x) for x in v5_12)
    v6_12 = list(v2sv(x) for x in v6_12)

    v5_13 = list(v2sv(x) for x in v5_13)
    v6_13 = list(v2sv(x) for x in v6_13)
    # tmp1 = list(temp_offset(t) for t in t3)
    # tmp = list(zip(v3_3, tmp1))
    # v3_3_t = list(x[0] - x[1] for x in tmp);
    #v2 = v3_3

    #函数拟合
    num_order = 2
 
    coeffs5_1  = np.polyfit(v5_1, vol_1, num_order)
    p5_1 = np.poly1d(coeffs5_1)
    coeffs6_1 = np.polyfit(v6_1, vol_1, num_order)
    p6_1 = np.poly1d(coeffs6_1)
    coeffs7_1  = np.polyfit(v7_1, vol_1, num_order)
    p7_1 = np.poly1d(coeffs7_1)
    coeffs8_1 = np.polyfit(v8_1, vol_1, num_order)
    p8_1 = np.poly1d(coeffs8_1)
    coeffs9_1 = np.polyfit(v9_1, vol_1, num_order)
    p9_1 = np.poly1d(coeffs9_1)

    coeffs5_2  = np.polyfit(v5_2, vol_2, num_order)
    p5_2 = np.poly1d(coeffs5_2)
    coeffs6_2 = np.polyfit(v6_2, vol_2, num_order)
    p6_2 = np.poly1d(coeffs6_2)
    coeffs7_2  = np.polyfit(v7_2, vol_2, num_order)
    p7_2 = np.poly1d(coeffs7_2)
    coeffs8_2 = np.polyfit(v8_2, vol_2, num_order)
    p8_2 = np.poly1d(coeffs8_2)
    coeffs9_2 = np.polyfit(v9_2, vol_2, num_order)
    p9_2 = np.poly1d(coeffs9_2)


    coeffs5_3  = np.polyfit(v5_3, vol_3, num_order)
    p5_3 = np.poly1d(coeffs5_3)
    coeffs6_3 = np.polyfit(v6_3, vol_3, num_order)
    p6_3 = np.poly1d(coeffs6_3)
    coeffs7_3  = np.polyfit(v7_3, vol_3, num_order)
    p7_3 = np.poly1d(coeffs7_3)
    coeffs8_3 = np.polyfit(v8_3, vol_3, num_order)
    p8_3 = np.poly1d(coeffs8_3)
    coeffs9_3 = np.polyfit(v9_3, vol_3, num_order)
    p9_3 = np.poly1d(coeffs9_3)


    coeffs5_4  = np.polyfit(v5_4, vol_4, num_order)
    p5_4 = np.poly1d(coeffs5_4)
    coeffs6_4 = np.polyfit(v6_4, vol_4, num_order)
    p6_4 = np.poly1d(coeffs6_4)
    coeffs7_4  = np.polyfit(v7_4, vol_4, num_order)
    p7_4 = np.poly1d(coeffs7_4)
    coeffs8_4 = np.polyfit(v8_4, vol_4, num_order)
    p8_4 = np.poly1d(coeffs8_4)
    coeffs9_4 = np.polyfit(v9_4, vol_4, num_order)
    p9_4 = np.poly1d(coeffs9_4)


    coeffs5_6  = np.polyfit(v5_6, vol_6, num_order)
    p5_6 = np.poly1d(coeffs5_6)
    coeffs6_6 = np.polyfit(v6_6, vol_6, num_order)
    p6_6 = np.poly1d(coeffs6_6)
    coeffs7_6  = np.polyfit(v7_6, vol_6, num_order)
    p7_6 = np.poly1d(coeffs7_6)
    coeffs8_6 = np.polyfit(v8_6, vol_6, num_order)
    p8_6 = np.poly1d(coeffs8_6)
    coeffs9_6 = np.polyfit(v9_6, vol_6, num_order)
    p9_6 = np.poly1d(coeffs9_6)


    coeffs5_7  = np.polyfit(v5_7, vol_7, num_order)
    p5_7 = np.poly1d(coeffs5_7)
    coeffs6_7 = np.polyfit(v6_7, vol_7, num_order)
    p6_7 = np.poly1d(coeffs6_7)
    coeffs7_7  = np.polyfit(v7_7, vol_7, num_order)
    p7_7 = np.poly1d(coeffs7_7)
    coeffs8_7 = np.polyfit(v8_7, vol_7, num_order)
    p8_7 = np.poly1d(coeffs8_7)
    coeffs9_7 = np.polyfit(v9_7, vol_7, num_order)
    p9_7 = np.poly1d(coeffs9_7)

    coeffs5_8  = np.polyfit(v5_8, vol_8, num_order)
    p5_8 = np.poly1d(coeffs5_8)
    coeffs6_8 = np.polyfit(v6_8, vol_8, num_order)
    p6_8 = np.poly1d(coeffs6_8)

    coeffs5_9  = np.polyfit(v5_9, vol_9, num_order)
    p5_9 = np.poly1d(coeffs5_9)
    coeffs6_9 = np.polyfit(v6_9, vol_9, num_order)
    p6_9 = np.poly1d(coeffs6_9)

    coeffs5_10  = np.polyfit(v5_10, vol_10, num_order)
    p5_10 = np.poly1d(coeffs5_10)
    coeffs6_10 = np.polyfit(v6_10, vol_10, num_order)
    p6_10 = np.poly1d(coeffs6_10)


    coeffs5_11  = np.polyfit(v5_11, vol_11, num_order)
    p5_11 = np.poly1d(coeffs5_11)
    coeffs6_11 = np.polyfit(v6_11, vol_11, num_order)
    p6_11 = np.poly1d(coeffs6_11)

    coeffs5_12  = np.polyfit(v5_12, vol_12, num_order)
    p5_12 = np.poly1d(coeffs5_12)
    coeffs6_12 = np.polyfit(v6_12, vol_12, num_order)
    p6_12 = np.poly1d(coeffs6_12)

    coeffs5_13  = np.polyfit(v5_13, vol_13, num_order)
    p5_13 = np.poly1d(coeffs5_13)
    coeffs6_13 = np.polyfit(v6_13, vol_13, num_order)
    p6_13 = np.poly1d(coeffs6_13)

    #打印函数值

    # print("coeffs5_1")
    # print(coeffs5_1)
    # print("coeffs5_2")
    # print(coeffs5_2)
    # print("coeffs5_3")
    # print(coeffs5_3)
    # print("coeffs5_4")
    # print(coeffs5_4)

    print("coeffs5_8")
    print(coeffs5_8)
    print("coeffs5_10")
    print(coeffs5_10)
    print("coeffs5_11")
    print(coeffs5_11)
    print("coeffs5_13")
    print(coeffs5_13)

    print("coeffs5_adv")
    print((coeffs5_8+coeffs5_10+coeffs5_11+coeffs5_13)/4)


    # print("coeffs6_1")
    # print(coeffs6_1)
    # print("coeffs6_2")
    # print(coeffs6_2)
    # print("coeffs6_3")
    # print(coeffs6_3)
    # print("coeffs6_4")
    # print(coeffs6_4)
    
    print("coeffs6_8")
    print(coeffs6_8)
    print("coeffs6_10")
    print(coeffs6_10)
    print("coeffs6_11")
    print(coeffs6_11)
    print("coeffs6_13")
    print(coeffs6_13)

    print("coeffs6_adv")
    print((coeffs6_8+coeffs6_10+coeffs6_11+coeffs6_13)/4)


    # print("coeffs7_1")
    # print(coeffs7_1)
    # print("coeffs7_2")
    # print(coeffs7_2)
    # print("coeffs7_3")
    # print(coeffs7_3)
    # print("coeffs7_4")
    # print(coeffs7_4)
    # print("coeffs7_adv")
    # print((coeffs7_1+coeffs7_2+coeffs7_3+coeffs7_4)/4)

    # print("coeffs8_1")
    # print(coeffs8_1)
    # print("coeffs8_2")
    # print(coeffs8_2)
    # print("coeffs8_3")
    # print(coeffs8_3)
    # print("coeffs8_4")
    # print(coeffs8_4)

    # print("coeffs8_adv")
    # print((coeffs8_1+coeffs8_2+coeffs8_3+coeffs8_4)/4)

    # print("coeffs9_1")
    # print(coeffs9_1)
    # print("coeffs9_2")
    # print(coeffs9_2)
    # print("coeffs9_3")
    # print(coeffs9_3)
    # print("coeffs9_4")
    # print(coeffs9_4)

    # print("coeffs9_adv")
    # print((coeffs9_1+coeffs9_2+coeffs9_3+coeffs9_4)/4)


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

    #2023.08.10
    #                       鸨色
    # plt.plot(x, p5_1(x), color='#f7acbc', linestyle='-', markersize=5)
    # plt.plot(v5_1, vol_1, color='#f7acbc', linestyle='', marker='>', markersize=5)
    # plt.plot(x, p5_2(x), color='#deab8a', linestyle='-', markersize=5)
    # plt.plot(v5_2, vol_2, color='#deab8a', linestyle='', marker='>', markersize=5)

    # plt.plot(x, p5_3(x), color='#817936', linestyle='-', markersize=5)
    # plt.plot(v5_3, vol_3, color='#817936', linestyle='', marker='>', markersize=5)
    # plt.plot(x, p5_4(x), color='#444693', linestyle='-', markersize=5)
    # plt.plot(v5_4, vol_4, color='#444693', linestyle='', marker='>', markersize=5)

    # plt.plot(x, p5_6(x), color='#f7acbc', linestyle='-', markersize=5)
    # plt.plot(v5_6, vol_6, color='#f7acbc', linestyle='', marker='>', markersize=5)
    # plt.plot(x, p5_7(x), color='#f7acbc', linestyle='-', markersize=5)
    # plt.plot(v5_7, vol_7, color='#f7acbc', linestyle='', marker='>', markersize=5)

    plt.plot(x, p5_8(x), color='#f7acbc', linestyle='-', markersize=5)
    plt.plot(v5_8, vol_8, color='#f7acbc', linestyle='', marker='>', markersize=5)
    # plt.plot(x, p5_9(x), color='#f7acbc', linestyle='-', markersize=5)
    # plt.plot(v5_9, vol_9, color='#f7acbc', linestyle='', marker='>', markersize=5)
    plt.plot(x, p5_10(x), color='#f7acbc', linestyle='-', markersize=5)
    plt.plot(v5_10, vol_10, color='#f7acbc', linestyle='', marker='>', markersize=5)
    plt.plot(x, p5_11(x), color='#f7acbc', linestyle='-', markersize=5)
    plt.plot(v5_11, vol_11, color='#f7acbc', linestyle='', marker='>', markersize=5)
    # plt.plot(x, p5_12(x), color='#2e3a1f', linestyle='-', markersize=5)
    # plt.plot(v5_12, vol_12, color='#2e3a1f', linestyle='', marker='>', markersize=5)
    plt.plot(x, p5_13(x), color='#2e3a1f', linestyle='-', markersize=5)
    plt.plot(v5_13, vol_13, color='#2e3a1f', linestyle='', marker='>', markersize=5)
    # #                       赤白橡
    # plt.plot(x, p6_1(x), color='#deab8a', linestyle='-', markersize=5)
    # plt.plot(v6_1, vol_1, color='#deab8a', linestyle='', marker='>', markersize=5)
    # plt.plot(x, p6_2(x), color='#deab8a', linestyle='-', markersize=5)
    # plt.plot(v6_2, vol_2, color='#deab8a', linestyle='', marker='>', markersize=5)

    # plt.plot(x, p6_3(x), color='#deab8a', linestyle='-', markersize=5)
    # plt.plot(v6_3, vol_3, color='#deab8a', linestyle='', marker='>', markersize=5)
    # plt.plot(x, p6_4(x), color='#deab8a', linestyle='-', markersize=5)
    # plt.plot(v6_4, vol_4, color='#deab8a', linestyle='', marker='>', markersize=5)

    # plt.plot(x, p6_6(x), color='#deab8a', linestyle='-', markersize=5)
    # plt.plot(v6_6, vol_6, color='#deab8a', linestyle='', marker='>', markersize=5)
    # plt.plot(x, p6_7(x), color='#f7acbc', linestyle='-', markersize=5)
    # plt.plot(v6_7, vol_7, color='#f7acbc', linestyle='', marker='>', markersize=5)
 
    plt.plot(x, p6_8(x), color='#deab8a', linestyle='-', markersize=5)
    plt.plot(v6_8, vol_8, color='#deab8a', linestyle='', marker='>', markersize=5)
    # plt.plot(x, p6_9(x), color='#f7acbc', linestyle='-', markersize=5)
    # plt.plot(v6_9, vol_9, color='#f7acbc', linestyle='', marker='>', markersize=5)
    plt.plot(x, p6_10(x), color='#f7acbc', linestyle='-', markersize=5)
    plt.plot(v6_10, vol_10, color='#f7acbc', linestyle='', marker='>', markersize=5)
    plt.plot(x, p6_11(x), color='#f7acbc', linestyle='-', markersize=5)
    plt.plot(v6_11, vol_11, color='#f7acbc', linestyle='', marker='>', markersize=5)
    # plt.plot(x, p6_12(x), color='#2e3a1f', linestyle='-', markersize=5)
    # plt.plot(v6_12, vol_12, color='#2e3a1f', linestyle='', marker='>', markersize=5)
    plt.plot(x, p6_13(x), color='#2e3a1f', linestyle='-', markersize=5)
    plt.plot(v6_13, vol_13, color='#2e3a1f', linestyle='', marker='>', markersize=5)
    # #                       油色
    # plt.plot(x, p7_1(x), color='#817936', linestyle='-', markersize=5)
    # plt.plot(v7_1, vol_1, color='#817936', linestyle='', marker='>', markersize=5)
    # plt.plot(x, p7_2(x), color='#817936', linestyle='-', markersize=5)
    # plt.plot(v7_2, vol_2, color='#817936', linestyle='', marker='>', markersize=5)

    # plt.plot(x, p7_3(x), color='#817936', linestyle='-', markersize=5)
    # plt.plot(v7_3, vol_3, color='#817936', linestyle='', marker='>', markersize=5)
    # plt.plot(x, p7_4(x), color='#817936', linestyle='-', markersize=5)
    # plt.plot(v7_4, vol_4, color='#817936', linestyle='', marker='>', markersize=5)

    # plt.plot(x, p7_6(x), color='#817936', linestyle='-', markersize=5)
    # plt.plot(v7_6, vol_6, color='#817936', linestyle='', marker='>', markersize=5)
    # plt.plot(x, p7_7(x), color='#444693', linestyle='-', markersize=5)
    # plt.plot(v7_7, vol_7, color='#444693', linestyle='', marker='>', markersize=5)
    # #                       绀桔梗
    # plt.plot(x, p8_1(x), color='#444693', linestyle='-', markersize=5)
    # plt.plot(v8_1, vol_1, color='#444693', linestyle='', marker='>', markersize=5)
    # plt.plot(x, p8_2(x), color='#444693', linestyle='-', markersize=5)
    # plt.plot(v8_2, vol_2, color='#444693', linestyle='', marker='>', markersize=5)

    # plt.plot(x, p8_3(x), color='#444693', linestyle='-', markersize=5)
    # plt.plot(v8_3, vol_3, color='#444693', linestyle='', marker='>', markersize=5)
    # plt.plot(x, p8_4(x), color='#444693', linestyle='-', markersize=5)
    # plt.plot(v8_4, vol_4, color='#444693', linestyle='', marker='>', markersize=5)

    # plt.plot(x, p8_6(x), color='#444693', linestyle='-', markersize=5)
    # plt.plot(v8_6, vol_6, color='#444693', linestyle='', marker='>', markersize=5)
    # plt.plot(x, p8_7(x), color='#817936', linestyle='-', markersize=5)
    # plt.plot(v8_7, vol_7, color='#817936', linestyle='', marker='>', markersize=5)
    # #                       蓝海松茶
    # plt.plot(x, p9_1(x), color='#2e3a1f', linestyle='-', markersize=5)
    # plt.plot(v9_1, vol_1, color='#2e3a1f', linestyle='', marker='>', markersize=5)
    # plt.plot(x, p9_2(x), color='#2e3a1f', linestyle='-', markersize=5)
    # plt.plot(v9_2, vol_2, color='#2e3a1f', linestyle='', marker='>', markersize=5)

    # plt.plot(x, p9_3(x), color='#2e3a1f', linestyle='-', markersize=5)
    # plt.plot(v9_3, vol_3, color='#2e3a1f', linestyle='', marker='>', markersize=5)
    # plt.plot(x, p9_4(x), color='#2e3a1f', linestyle='-', markersize=5)
    # plt.plot(v9_4, vol_4, color='#2e3a1f', linestyle='', marker='>', markersize=5)

    # plt.plot(x, p9_6(x), color='#2e3a1f', linestyle='-', markersize=5)
    # plt.plot(v9_6, vol_6, color='#2e3a1f', linestyle='', marker='>', markersize=5)
    # plt.plot(x, p9_7(x), color='#817936', linestyle='-', markersize=5)
    # plt.plot(v9_7, vol_7, color='#817936', linestyle='', marker='>', markersize=5)
    plt.show()
