import csv
import numpy as np
import matplotlib.pyplot as plt
import sys

#你好

#  1---4
vol_1 = [
0,
1.10,
1.55,
2.09,
2.72,
3.29,
3.60,
4.37,
4.87,
4.98,
]

vol_2 = [
0,
0.58,
1.04,
1.79,
2.56,
3.29,
4.00,
4.57,
5.07,
]

vol_3 = [
0.02,
0.61,
1.40,
2.41,
2.95,
3.57,
4.17,
4.76,
5.06,
]

vol_4 = [
0.03,
0.89,
1.47,
2.02,
2.96,
3.68,
4.44,
5.14,
]

# vol_5 = [
# 0.06,
# 0.98,
# 1.65,
# 2.27,
# 3.03,
# 3.83,
# 4.44,
# 5.43,
# ]

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

v1_1 = [
1.346,
1.023,
0.899,
0.755,
0.602,
0.468,
0.382,
0.231,
0.124,
0.111,
]

v1_2 = [
1.356,
1.198,
1.066,
0.863,
0.668,
0.493,
0.332,
0.216,
0.114,
]

v1_3 = [
1.365,
1.200,
0.982,
0.716,
0.584,
0.442,
0.306,
0.182,
0.129,
]

v1_4 = [
1.374,
1.134,
0.975,
0.831,
0.602,
0.440,
0.272,
0.123,
]


v2_1 = [
1.607,
1.302,
1.177,
1.038,
0.886,
0.756,
0.664,
0.518,
0.411,
0.394,
]

v2_2 = [
1.611,
1.460,
1.332,
1.129,
0.936,
0.763,
0.603,
0.482,
0.379,
]

v2_3 = [
1.623,
1.473,
1.272,
1.023,
0.883,
0.747,
0.619,
0.493,
0.435,
]

v2_4 = [
1.617,
1.398,
1.247,
1.111,
0.891,
0.730,
0.567,
0.429,
]

v2_6 = [
1.629,
1.458,
1.306,
1.119,
0.951,
0.786,
0.591,
]

v3_1 = [
1.423,
1.125,
1.008,
0.874,
0.732,
0.605,
0.523,
0.383,
0.280,
0.262,
]

v3_2 = [
1.432,
1.282,
1.160,
0.940,
0.786,
0.625,
0.471,
0.360,
0.263,
]

v3_3 = [
1.439,
1.281,
1.080,
0.831,
0.709,
0.572,
0.446,
0.330,
0.269,
]

v3_4 = [
1.443,
1.215,
1.067,
0.937,
0.715,
0.563,
0.408,
0.264,
]

v3_6 = [
1.442,
1.228,
1.059,
0.845,
0.668,
0.503,
0.307,
]

v3_7 = [
1.455,
1.350,
1.155,
1.053,
0.928,
0.799,
0.675,
0.589,
0.494,
0.386,
0.280,
]

v4_1 = [
1.411,
1.100,
0.977,
0.838,
0.689,
0.557,
0.472,
0.326,
0.220,
0.206,
]

v4_2 = [
1.416,
1.263,
1.137,
0.942,
0.756,
0.585,
0.431,
0.317,
0.216,
]

v4_3 = [
1.428,
1.275,
1.075,
0.823,
0.694,
0.561,
0.433,
0.311,
0.260,
]

v4_4 = [
1.426,
1.203,
1.055,
0.919,
0.701,
0.544,
0.394,
0.247,
]

v4_6 = [
1.432,
1.285,
1.160,
0.983,
0.835,
0.690,
0.503,
]

v4_7 = [
1.443,
1.369,
1.215,
1.130,
1.029,
0.906,
0.807,
0.725,
0.613,
0.513,
0.415,
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
    #电压转换

    v1_1 = list(v2sv(x) for x in v1_1)
    v2_1 = list(v2sv(x) for x in v2_1)
    v3_1 = list(v2sv(x) for x in v3_1)
    v4_1 = list(v2sv(x) for x in v4_1)

    v1_2 = list(v2sv(x) for x in v1_2)
    v2_2 = list(v2sv(x) for x in v2_2)
    v3_2 = list(v2sv(x) for x in v3_2)
    v4_2 = list(v2sv(x) for x in v4_2)

    v1_3 = list(v2sv(x) for x in v1_3)
    v2_3 = list(v2sv(x) for x in v2_3)
    v3_3 = list(v2sv(x) for x in v3_3)
    v4_3 = list(v2sv(x) for x in v4_3)


    v1_4 = list(v2sv(x) for x in v1_4)
    v2_4 = list(v2sv(x) for x in v2_4)
    v3_4 = list(v2sv(x) for x in v3_4)
    v4_4 = list(v2sv(x) for x in v4_4)

    v2_6 = list(v2sv(x) for x in v2_6)
    v3_6 = list(v2sv(x) for x in v3_6)
    v4_6 = list(v2sv(x) for x in v4_6)

    v3_7 = list(v2sv(x) for x in v3_7)
    v4_7 = list(v2sv(x) for x in v4_7)

    # tmp1 = list(temp_offset(t) for t in t3)
    # tmp = list(zip(v3_3, tmp1))
    # v3_3_t = list(x[0] - x[1] for x in tmp);
    #v2 = v3_3

    #函数拟合
    num_order = 2
 
    coeffs1_1  = np.polyfit(v1_1, vol_1, num_order)
    p1_1 = np.poly1d(coeffs1_1)
    coeffs2_1 = np.polyfit(v2_1, vol_1, num_order)
    p2_1 = np.poly1d(coeffs2_1)
    coeffs3_1  = np.polyfit(v3_1, vol_1, num_order)
    p3_1 = np.poly1d(coeffs3_1)
    coeffs4_1 = np.polyfit(v4_1, vol_1, num_order)
    p4_1 = np.poly1d(coeffs4_1)


    coeffs1_2  = np.polyfit(v1_2, vol_2, num_order)
    p1_2 = np.poly1d(coeffs1_2)
    coeffs2_2 = np.polyfit(v2_2, vol_2, num_order)
    p2_2 = np.poly1d(coeffs2_2)
    coeffs3_2  = np.polyfit(v3_2, vol_2, num_order)
    p3_2 = np.poly1d(coeffs3_2)
    coeffs4_2 = np.polyfit(v4_2, vol_2, num_order)
    p4_2 = np.poly1d(coeffs4_2)

    coeffs1_3  = np.polyfit(v1_3, vol_3, num_order)
    p1_3 = np.poly1d(coeffs1_3)
    coeffs2_3 = np.polyfit(v2_3, vol_3, num_order)
    p2_3 = np.poly1d(coeffs2_3)
    coeffs3_3  = np.polyfit(v3_3, vol_3, num_order)
    p3_3 = np.poly1d(coeffs3_3)
    coeffs4_3 = np.polyfit(v4_3, vol_3, num_order)
    p4_3 = np.poly1d(coeffs4_3)

    coeffs1_4  = np.polyfit(v1_4, vol_4, num_order)
    p1_4 = np.poly1d(coeffs1_4)
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


    coeffs3_7  = np.polyfit(v3_7, vol_7, num_order)
    p3_7 = np.poly1d(coeffs3_7)
    coeffs4_7 = np.polyfit(v4_7, vol_7, num_order)
    p4_7 = np.poly1d(coeffs4_7)

    #打印函数值

    print("coeffsn1_1")
    print(coeffs1_1)
    print("coeffsn1_2")
    print(coeffs1_2)
    print("coeffsn1_3")
    print(coeffs1_3)
    print("coeffsn1_4")
    print(coeffs1_4)
    print("coeffsn1adv")
    print((coeffs1_2+coeffs1_3)/2)


    print("coeffs2_1")
    print(coeffs2_1)
    print("coeffs2_2")
    print(coeffs2_2)
    print("coeffs2_3")
    print(coeffs2_3)
    print("coeffs2_4")
    print(coeffs2_4)
    print("coeffsn2adv")
    print((coeffs2_1+coeffs2_2+coeffs2_3+coeffs2_4)/4)
    print("coeffsn2_6")
    print(coeffs2_6)

    print("coeffs3_1")
    print(coeffs3_1)
    print("coeffs3_2")
    print(coeffs3_2)
    print("coeffs3_3")
    print(coeffs3_3)
    print("coeffs3_4")
    print(coeffs3_4)
    print("coeffsn3adv")
    print((coeffs3_1+coeffs3_2+coeffs3_3+coeffs3_4)/4)
    print("coeffsn3_6")
    print(coeffs3_6)
    print("coeffsn3_7")
    print(coeffs3_7)

    print("coeffs4_1")
    print(coeffs4_1)
    print("coeffs4_2")
    print(coeffs4_2)
    print("coeffs4_3")
    print(coeffs4_3)
    print("coeffs4_4")
    print(coeffs4_4)
    print("coeffsn4adv")
    print((coeffs4_3+coeffs4_4)/2)
    print("coeffsn4_6")
    print(coeffs4_6)
    print("coeffsn4_7")
    print(coeffs4_7)

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
    plt.plot(x, p2_1(x), color='#deab8a', linestyle='-', markersize=5)
    plt.plot(v2_1, vol_1, color='#deab8a', linestyle='', marker='>', markersize=5)
    plt.plot(x, p2_2(x), color='#deab8a', linestyle='-', markersize=5)
    plt.plot(v2_2, vol_2, color='#deab8a', linestyle='', marker='>', markersize=5)

    plt.plot(x, p2_3(x), color='#deab8a', linestyle='-', markersize=5)
    plt.plot(v2_3, vol_3, color='#deab8a', linestyle='', marker='>', markersize=5)
    plt.plot(x, p2_4(x), color='#deab8a', linestyle='-', markersize=5)
    plt.plot(v2_4, vol_4, color='#deab8a', linestyle='', marker='>', markersize=5)

    plt.plot(x, p2_6(x), color='#deab8a', linestyle='-', markersize=5)
    plt.plot(v2_6, vol_6, color='#deab8a', linestyle='', marker='>', markersize=5)

    #                       油色
    plt.plot(x, p3_1(x), color='#817936', linestyle='-', markersize=5)
    plt.plot(v3_1, vol_1, color='#817936', linestyle='', marker='>', markersize=5)
    plt.plot(x, p3_2(x), color='#817936', linestyle='-', markersize=5)
    plt.plot(v3_2, vol_2, color='#817936', linestyle='', marker='>', markersize=5)

    plt.plot(x, p3_3(x), color='#817936', linestyle='-', markersize=5)
    plt.plot(v3_3, vol_3, color='#817936', linestyle='', marker='>', markersize=5)
    plt.plot(x, p3_4(x), color='#817936', linestyle='-', markersize=5)
    plt.plot(v3_4, vol_4, color='#817936', linestyle='', marker='>', markersize=5)

    plt.plot(x, p3_6(x), color='#444693', linestyle='-', markersize=5)
    plt.plot(v3_6, vol_6, color='#444693', linestyle='', marker='>', markersize=5)
    plt.plot(x, p3_7(x), color='#444693', linestyle='-', markersize=5)
    plt.plot(v3_7, vol_7, color='#444693', linestyle='', marker='>', markersize=5)
    #                       绀桔梗
    plt.plot(x, p4_1(x), color='#444693', linestyle='-', markersize=5)
    plt.plot(v4_1, vol_1, color='#444693', linestyle='', marker='>', markersize=5)
    plt.plot(x, p4_2(x), color='#444693', linestyle='-', markersize=5)
    plt.plot(v4_2, vol_2, color='#444693', linestyle='', marker='>', markersize=5)
    
    plt.plot(x, p4_3(x), color='#444693', linestyle='-', markersize=5)
    plt.plot(v4_3, vol_3, color='#444693', linestyle='', marker='>', markersize=5)
    plt.plot(x, p4_4(x), color='#444693', linestyle='-', markersize=5)
    plt.plot(v4_4, vol_4, color='#444693', linestyle='', marker='>', markersize=5)

    plt.plot(x, p4_6(x), color='#817936', linestyle='-', markersize=5)
    plt.plot(v4_6, vol_6, color='#817936', linestyle='', marker='>', markersize=5)
    plt.plot(x, p4_7(x), color='#817936', linestyle='-', markersize=5)
    plt.plot(v4_7, vol_7, color='#817936', linestyle='', marker='>', markersize=5)
    plt.show()
