import csv
import numpy as np
import matplotlib.pyplot as plt
import sys

#你好

#  7  8  10  11
vol_1 = [
0,
0.91,
1.90,
2.49,
3.18,
3.98,
]

vol_2 = [
0.04,
0.61,
1.35,
2.11,
3.28,
4.27,
4.92,
]

vol_3 = [
0.04,
0.64,
1.40,
2.19,
2.99,
3.66,
4.49,
4.98,
]

vol_4 = [
0.00,
0.52,
1.07,
1.71,
2.53,
3.03,
3.90,
4.63,
5.05,
]

vol_5 = [
0.03,
0.58,
1.36,
2.31,
3.13,
3.87,
4.91,
]

vol_6 = [
0.03,
1.21,
1.94,
2.70,
3.43,
4.20,
5.03,
]


v7_1 = [
1.456,
1.226,
0.982,
0.836,
0.681,
0.512,
]

v7_2 = [
1.462,
1.324,
1.140,
0.961,
0.696,
0.494,
0.359,
]

v7_3 = [
1.466,
1.323,
1.131,
0.938,
0.759,
0.620,
0.452,
0.351,
]

v7_4 = [
1.464,
1.343,
1.201,
1.038,
0.849,
0.742,
0.551,
0.409,
0.327,
]

v7_5 = [
1.475,
1.350,
1.153,
0.931,
0.743,
0.587,
0.377,
]

v7_6 = [
1.473,
1.211,
1.024,
0.853,
0.694,
0.534,
0.364,
]


v8_1 = [
1.621,
1.374,
1.115,
0.967,
0.803,
0.627,
]

v8_2 = [
1.625,
1.476,
1.279,
1.086,
0.808,
0.595,
0.454,
]

v8_3 = [
1.630,
1.472,
1.266,
1.064,
0.874,
0.725,
0.545,
0.441,
]

v8_4 = [
1.626,
1.490,
1.338,
1.170,
0.968,
0.852,
0.651,
0.503,
0.413,
]

v8_5 = [
1.635,
1.494,
1.282,
1.042,
0.846,
0.682,
0.459,
]

v8_6 = [
1.633,
1.338,
1.143,
0.961,
0.792,
0.625,
0.444,
]


v10_1 = [
1.157,
0.923,
0.679,
0.538,
0.385,
0.219,
]

v10_2 = [
1.163,
1.024,
0.840,
0.661,
0.403,
0.202,
0.070,
]

v10_3 = [
1.170,
1.024,
0.833,
0.642,
0.466,
0.328,
0.160,
0.061,
]

v10_4 = [
1.170,
1.046,
0.903,
0.745,
0.554,
0.447,
0.261,
0.121,
0.037,
]

v10_5 = [
1.178,
1.050,
0.853,
0.632,
0.446,
0.293,
0.086,
]

v10_6 = [
1.176,
0.907,
0.724,
0.553,
0.396,
0.240,
0.071,
]

v11_1 = [
1.556,
1.310,
1.045,
0.900,
0.739,
0.562,
]

v11_2 = [
1.547,
1.403,
1.207,
1.017,
0.743,
0.530,
0.389,
]

v11_3 = [
1.558,
1.402,
1.196,
0.994,
0.805,
0.657,
0.480,
0.373,
]

v11_4 = [
1.557,
1.422,
1.270,
1.101,
0.898,
0.785,
0.587,
0.437,
0.347,
]

v11_5 = [
1.560,
1.421,
1.208,
0.969,
0.772,
0.608,
0.386,
]

v11_6 = [
1.556,
1.260,
1.064,
0.880,
0.715,
0.546,
0.368,
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

    vol_5 = list(x*20 for x in vol_5)
    vol_6 = list(x*20 for x in vol_6)
    #电压转换

    v7_1 = list(v2sv(x) for x in v7_1)
    v8_1 = list(v2sv(x) for x in v8_1)
    v10_1 = list(v2sv(x) for x in v10_1)
    v11_1 = list(v2sv(x) for x in v11_1)

    v7_2 = list(v2sv(x) for x in v7_2)
    v8_2 = list(v2sv(x) for x in v8_2)
    v10_2 = list(v2sv(x) for x in v10_2)
    v11_2 = list(v2sv(x) for x in v11_2)

    v7_3= list(v2sv(x) for x in v7_3)
    v8_3 = list(v2sv(x) for x in v8_3)
    v10_3 = list(v2sv(x) for x in v10_3)
    v11_3 = list(v2sv(x) for x in v11_3)

    v7_4= list(v2sv(x) for x in v7_4)
    v8_4 = list(v2sv(x) for x in v8_4)
    v10_4 = list(v2sv(x) for x in v10_4)
    v11_4 = list(v2sv(x) for x in v11_4)


    v7_5= list(v2sv(x) for x in v7_5)
    v8_5 = list(v2sv(x) for x in v8_5)
    v10_5 = list(v2sv(x) for x in v10_5)
    v11_5 = list(v2sv(x) for x in v11_5)


    v7_6= list(v2sv(x) for x in v7_6)
    v8_6 = list(v2sv(x) for x in v8_6)
    v10_6 = list(v2sv(x) for x in v10_6)
    v11_6 = list(v2sv(x) for x in v11_6)


    # tmp1 = list(temp_offset(t) for t in t3)
    # tmp = list(zip(v3_3, tmp1))
    # v3_3_t = list(x[0] - x[1] for x in tmp);
    #v2 = v3_3

    #函数拟合
    num_order = 2
 
    coeffs7_1  = np.polyfit(v7_1, vol_1, num_order)
    p7_1 = np.poly1d(coeffs7_1)
    coeffs8_1 = np.polyfit(v8_1, vol_1, num_order)
    p8_1 = np.poly1d(coeffs8_1)
    coeffs10_1  = np.polyfit(v10_1, vol_1, num_order)
    p10_1 = np.poly1d(coeffs10_1)
    coeffs11_1 = np.polyfit(v11_1, vol_1, num_order)
    p11_1 = np.poly1d(coeffs11_1)

    coeffs7_2  = np.polyfit(v7_2, vol_2, num_order)
    p7_2 = np.poly1d(coeffs7_2)
    coeffs8_2 = np.polyfit(v8_2, vol_2, num_order)
    p8_2 = np.poly1d(coeffs8_2)
    coeffs10_2  = np.polyfit(v10_2, vol_2, num_order)
    p10_2 = np.poly1d(coeffs10_2)
    coeffs11_2 = np.polyfit(v11_2, vol_2, num_order)
    p11_2 = np.poly1d(coeffs11_2)


    coeffs7_3  = np.polyfit(v7_3, vol_3, num_order)
    p7_3 = np.poly1d(coeffs7_3)
    coeffs8_3 = np.polyfit(v8_3, vol_3, num_order)
    p8_3 = np.poly1d(coeffs8_3)
    coeffs10_3  = np.polyfit(v10_3, vol_3, num_order)
    p10_3 = np.poly1d(coeffs10_3)
    coeffs11_3 = np.polyfit(v11_3, vol_3, num_order)
    p11_3 = np.poly1d(coeffs11_3)


    coeffs7_4  = np.polyfit(v7_4, vol_4, num_order)
    p7_4 = np.poly1d(coeffs7_4)
    coeffs8_4 = np.polyfit(v8_4, vol_4, num_order)
    p8_4 = np.poly1d(coeffs8_4)
    coeffs10_4  = np.polyfit(v10_4, vol_4, num_order)
    p10_4 = np.poly1d(coeffs10_4)
    coeffs11_4 = np.polyfit(v11_4, vol_4, num_order)
    p11_4 = np.poly1d(coeffs11_4)


    coeffs7_5  = np.polyfit(v7_5, vol_5, num_order)
    p7_5 = np.poly1d(coeffs7_5)
    coeffs8_5 = np.polyfit(v8_5, vol_5, num_order)
    p8_5 = np.poly1d(coeffs8_5)
    coeffs10_5  = np.polyfit(v10_5, vol_5, num_order)
    p10_5 = np.poly1d(coeffs10_5)
    coeffs11_5 = np.polyfit(v11_5, vol_5, num_order)
    p11_5 = np.poly1d(coeffs11_5)


    coeffs7_6  = np.polyfit(v7_6, vol_6, num_order)
    p7_6 = np.poly1d(coeffs7_6)
    coeffs8_6 = np.polyfit(v8_6, vol_6, num_order)
    p8_6 = np.poly1d(coeffs8_6)
    coeffs10_6  = np.polyfit(v10_6, vol_6, num_order)
    p10_6 = np.poly1d(coeffs10_6)
    coeffs11_6 = np.polyfit(v11_6, vol_6, num_order)
    p11_6 = np.poly1d(coeffs11_6)


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

    # print("coeffsn7_1")
    # print(coeffs7_1)
    # print("coeffsn7_2")
    # print(coeffs7_2)
    # print("coeffsn7_3")
    # print(coeffs7_3)
    # print("coeffsn7_4")
    # print(coeffs7_4)
    # print("coeffsn7_5")
    # print(coeffs7_5)
    # print("coeffsn7_6")
    # print(coeffs7_6) 
    # print("coeffsn7adv")
    # print((coeffs7_2+coeffs7_3+coeffs7_5+coeffs7_6)/4)

    # print("coeffsn8_1")
    # print(coeffs8_1)
    print("coeffsn8_2")
    print(coeffs8_2)
    print("coeffsn8_3")
    print(coeffs8_3)
    # print("coeffsn8_4")
    # print(coeffs8_4)
    print("coeffsn8_5")
    print(coeffs8_5)
    print("coeffsn8_6")
    print(coeffs8_6) 
    print("coeffsn8adv")
    print((coeffs8_2+coeffs8_3+coeffs8_5+coeffs8_6)/4)

    # print("coeffsn10_1")
    # print(coeffs10_1)
    # print("coeffsn10_2")
    # print(coeffs10_2)
    # print("coeffsn10_3")
    # print(coeffs10_3)
    # print("coeffsn10_4")
    # print(coeffs10_4)
    # print("coeffsn10_5")
    # print(coeffs10_5)
    # print("coeffsn10_6")
    # print(coeffs10_6) 
    # print("coeffsn10adv")
    # print((coeffs10_2+coeffs10_3+coeffs10_5+coeffs10_6)/4)
    

    # # print("coeffsn11_1")
    # # print(coeffs11_1)
    # print("coeffsn11_2")
    # print(coeffs11_2)
    # print("coeffsn11_3")
    # print(coeffs11_3)
    # # print("coeffsn11_4")
    # # print(coeffs11_4)
    # print("coeffsn11_5")
    # print(coeffs11_5)
    # print("coeffsn11_6")
    # print(coeffs11_6) 
    # print("coeffsn11adv")
    # print((coeffs11_2+coeffs11_3+coeffs11_5+coeffs11_6)/4)


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

    #2023.08.29
    #                       鸨色
    # plt.plot(x, p7_1(x), color='#f7acbc', linestyle='-', markersize=5)
    # plt.plot(v7_1, vol_1, color='#f7acbc', linestyle='', marker='>', markersize=5)

    # plt.plot(x, p7_2(x), color='#f7acbc', linestyle='-', markersize=5)
    # plt.plot(v7_2, vol_2, color='#f7acbc', linestyle='', marker='>', markersize=5)
    # plt.plot(x, p7_3(x), color='#f7acbc', linestyle='-', markersize=5)
    # plt.plot(v7_3, vol_3, color='#f7acbc', linestyle='', marker='>', markersize=5)

    # plt.plot(x, p7_4(x), color='#f7acbc', linestyle='-', markersize=5)
    # plt.plot(v7_4, vol_4, color='#f7acbc', linestyle='', marker='>', markersize=5)

    # plt.plot(x, p7_5(x), color='#444693', linestyle='-', markersize=5)
    # plt.plot(v7_5, vol_5, color='#444693', linestyle='', marker='>', markersize=5)
    # plt.plot(x, p7_6(x), color='#444693', linestyle='-', markersize=5)
    # plt.plot(v7_6, vol_6, color='#444693', linestyle='', marker='>', markersize=5)

    #                       赤白橡
    # plt.plot(x, p8_1(x), color='#deab8a', linestyle='-', markersize=5)
    # plt.plot(v8_1, vol_1, color='#deab8a', linestyle='', marker='>', markersize=5)

    plt.plot(x, p8_2(x), color='#deab8a', linestyle='-', markersize=5)
    plt.plot(v8_2, vol_2, color='#deab8a', linestyle='', marker='>', markersize=5)
    plt.plot(x, p8_3(x), color='#deab8a', linestyle='-', markersize=5)
    plt.plot(v8_3, vol_3, color='#deab8a', linestyle='', marker='>', markersize=5)

    # plt.plot(x, p8_4(x), color='#deab8a', linestyle='-', markersize=5)
    # plt.plot(v8_4, vol_4, color='#deab8a', linestyle='', marker='>', markersize=5)
  
    plt.plot(x, p8_5(x), color='#444693', linestyle='-', markersize=5)
    plt.plot(v8_5, vol_5, color='#444693', linestyle='', marker='>', markersize=5)   
    plt.plot(x, p8_6(x), color='#444693', linestyle='-', markersize=5)
    plt.plot(v8_6, vol_6, color='#444693', linestyle='', marker='>', markersize=5)

    #                       油色
    # plt.plot(x, p10_1(x), color='#817936', linestyle='-', markersize=5)
    # plt.plot(v10_1, vol_1, color='#817936', linestyle='', marker='>', markersize=5)

    # plt.plot(x, p10_2(x), color='#817936', linestyle='-', markersize=5)
    # plt.plot(v10_2, vol_2, color='#817936', linestyle='', marker='>', markersize=5)
    # plt.plot(x, p10_3(x), color='#817936', linestyle='-', markersize=5)
    # plt.plot(v10_3, vol_3, color='#817936', linestyle='', marker='>', markersize=5)

    # plt.plot(x, p10_4(x), color='#817936', linestyle='-', markersize=5)
    # plt.plot(v10_4, vol_4, color='#817936', linestyle='', marker='>', markersize=5)

    # plt.plot(x, p10_5(x), color='#444693', linestyle='-', markersize=5)
    # plt.plot(v10_5, vol_5, color='#444693', linestyle='', marker='>', markersize=5)
    # plt.plot(x, p10_6(x), color='#444693', linestyle='-', markersize=5)
    # plt.plot(v10_6, vol_6, color='#444693', linestyle='', marker='>', markersize=5)

    #                       绀桔梗
    # plt.plot(x, p11_1(x), color='#444693', linestyle='-', markersize=5)
    # plt.plot(v11_1, vol_1, color='#444693', linestyle='', marker='>', markersize=5)
    
    # plt.plot(x, p11_2(x), color='#444693', linestyle='-', markersize=5)
    # plt.plot(v11_2, vol_2, color='#444693', linestyle='', marker='>', markersize=5)
    # plt.plot(x, p11_3(x), color='#444693', linestyle='-', markersize=5)
    # plt.plot(v11_3, vol_3, color='#444693', linestyle='', marker='>', markersize=5)

    # plt.plot(x, p11_4(x), color='#444693', linestyle='-', markersize=5)
    # plt.plot(v11_4, vol_4, color='#444693', linestyle='', marker='>', markersize=5)

    # plt.plot(x, p11_5(x), color='#444693', linestyle='-', markersize=5)
    # plt.plot(v11_5, vol_5, color='#444693', linestyle='', marker='>', markersize=5)
    # plt.plot(x, p11_6(x), color='#444693', linestyle='-', markersize=5)
    # plt.plot(v11_6, vol_6, color='#444693', linestyle='', marker='>', markersize=5)
    
    plt.show()
