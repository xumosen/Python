import csv
import numpy as np
import matplotlib.pyplot as plt
import sys

volnew_1 = [
0.04,
0.55,
1.18,
1.50,
2.0,
2.61,
3.22,
3.89,
4.42,
5,
5.18,
5.5,
]

vnew1_1 = [
1.459,
1.338,
1.185,
1.110,
0.998,
0.865,
0.730,
0.600,
0.492,
0.386,
0.352,
0.296,
]

vnew2_1 = [
1.549,
1.438,
1.296,
1.226,
1.123,
0.997,
0.877,
0.750,
0.655,
0.555,
0.516,
0.466,
]


volnew_2 = [
0.05,
0.57,
1.33,
1.83,
2.34,
2.69,
3.01,
3.53,
4,
4.46,
4.96,
]

vnew1_2 = [
1.457,
1.346,
1.174,
1.059,
0.945,
0.865,
0.799,
0.690,
0.595,
0.497,
0.399,
]

vnew2_2 = [
1.547,
1.444,
1.285,
1.180,
1.079,
1.003,
0.940,
0.837,
0.747,
0.664,
0.575,
]

volnew_3 = [
0.05,
0.80,
1.18,
1.56,
2.01,
2.51,
3.08,
3.67,
4.24,
4.74,
4.94,
]

vnew1_3 = [
1.456,
1.294,
1.202,
1.107,
1.004,
0.892,
0.776,
0.651,
0.533,
0.433,
0.390,
]

vnew2_3 = [
1.546,
1.396,
1.313,
1.229,
1.133,
1.031,
0.922,
0.807,
0.698,
0.607,
0.571,
]


volnew_4 = [
0.01,
0.84,
1.21,
1.57,
1.96,
2.50,
2.95,
3.33,
3.96,
4.28,
4.62,
5.01,
]

vnew1_4 = [
1.458,
1.260,
1.168,
1.081,
0.994,
0.871,
0.773,
0.693,
0.566,
0.496,
0.430,
0.349,
]

vnew2_4 = [
1.551,
1.365,
1.281,
1.201,
1.120,
1.005,
0.913,
0.841,
0.723,
0.660,
0.593,
0.529,
]


volnew_5 = [
0.06,
0.70,
1.23,
1.79,
2.23,
2.62,
3.48,
4.10,
4.39,
4.74,
4.97,
]

vnew1_5 = [
1.462,
1.313,
1.188,
1.056,
0.954,
0.863,
0.680,
0.545,
0.482,
0.420,
0.365,
]

vnew2_5 = [
1.555,
1.412,
1.290,
1.169,
1.079,
0.993,
0.823,
0.703,
0.644,
0.577,
0.531,
]

volnew_6 = [
0.02,
0.57,
1.27,
1.99,
2.49,
3.46,
4.00,
4.35,
4.71,
5.02,
]

vnew1_6 = [
1.454,
1.327,
1.156,
0.984,
0.876,
0.666,
0.552,
0.480,
0.409,
0.351,
]

vnew2_6 = [
1.552,
1.429,
1.270,
1.108,
1.008,
0.812,
0.706,
0.640,
0.574,
0.516,
]

volnew_7 = [
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

vnew1_7 = [
1.458,
1.215,
1.111,
0.986,
0.857,
0.741,
0.664,
0.520,
0.418,
0.393,
]

volnew_8 = [
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

vnew1_8 = [
1.418,
1.295,
1.191,
1.024,
0.859,
0.713,
0.568,
0.458,
0.359,
]

volnew_9 = [
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

vnew1_9 = [
1.454,
1.319,
1.141,
0.914,
0.802,
0.668,
0.548,
0.420,
0.368,
]




def v2sv(v):
    return ((11.1*1.348-v)/10.1 - 1.348)*1000

def temp_offset(t):
    return 0.0009996 * ((t + 20) * (t + 20)) - 0.0404788 * (t + 20) - 9.927496 + 10.337232

if __name__ == '__main__':
    #vol转lel
    volnew_1 = list(x*20 for x in volnew_1)
    volnew_2 = list(x*20 for x in volnew_2)
    volnew_3 = list(x*20 for x in volnew_3)
    volnew_4 = list(x*20 for x in volnew_4)
    volnew_5 = list(x*20 for x in volnew_5)
    volnew_6 = list(x*20 for x in volnew_6)

    volnew_7 = list(x*20 for x in volnew_7)

    volnew_8 = list(x*20 for x in volnew_8)
    volnew_9 = list(x*20 for x in volnew_9)
    #电压转换

    vnew1_1 = list(v2sv(x) for x in vnew1_1)
    vnew2_1 = list(v2sv(x) for x in vnew2_1)

    vnew1_2 = list(v2sv(x) for x in vnew1_2)
    vnew2_2 = list(v2sv(x) for x in vnew2_2)

    vnew1_3 = list(v2sv(x) for x in vnew1_3)
    vnew2_3 = list(v2sv(x) for x in vnew2_3)

    vnew1_4 = list(v2sv(x) for x in vnew1_4)
    vnew2_4 = list(v2sv(x) for x in vnew2_4)

    vnew1_5 = list(v2sv(x) for x in vnew1_5)
    vnew2_5 = list(v2sv(x) for x in vnew2_5)

    vnew1_6 = list(v2sv(x) for x in vnew1_6)
    vnew2_6 = list(v2sv(x) for x in vnew2_6)

    vnew1_7 = list(v2sv(x) for x in vnew1_7)

    vnew1_8 = list(v2sv(x) for x in vnew1_8)
    vnew1_9 = list(v2sv(x) for x in vnew1_9)

    # tmp1 = list(temp_offset(t) for t in t3)
    # tmp = list(zip(v3_3, tmp1))
    # v3_3_t = list(x[0] - x[1] for x in tmp);
    #v2 = v3_3

    #函数拟合
    num_order = 2
 
    coeffsnew1_1  = np.polyfit(vnew1_1, volnew_1, num_order)
    pnew1_1 = np.poly1d(coeffsnew1_1)
    coeffsnew2_1 = np.polyfit(vnew2_1, volnew_1, num_order)
    pnew2_1 = np.poly1d(coeffsnew2_1)

    coeffsnew1_2  = np.polyfit(vnew1_2, volnew_2, num_order)
    pnew1_2 = np.poly1d(coeffsnew1_2)
    coeffsnew2_2 = np.polyfit(vnew2_2, volnew_2, num_order)
    pnew2_2 = np.poly1d(coeffsnew2_2)

    coeffsnew1_3  = np.polyfit(vnew1_3, volnew_3, num_order)
    pnew1_3 = np.poly1d(coeffsnew1_3)
    coeffsnew2_3 = np.polyfit(vnew2_3, volnew_3, num_order)
    pnew2_3 = np.poly1d(coeffsnew2_3)

    coeffsnew1_4  = np.polyfit(vnew1_4, volnew_4, num_order)
    pnew1_4 = np.poly1d(coeffsnew1_4)
    coeffsnew2_4 = np.polyfit(vnew2_4, volnew_4, num_order)
    pnew2_4 = np.poly1d(coeffsnew2_4)

    coeffsnew1_5  = np.polyfit(vnew1_5, volnew_5, num_order)
    pnew1_5 = np.poly1d(coeffsnew1_5)
    coeffsnew2_5 = np.polyfit(vnew2_5, volnew_5, num_order)
    pnew2_5 = np.poly1d(coeffsnew2_5)

    coeffsnew1_6  = np.polyfit(vnew1_6, volnew_6, num_order)
    pnew1_6 = np.poly1d(coeffsnew1_6)
    coeffsnew2_6 = np.polyfit(vnew2_6, volnew_6, num_order)
    pnew2_6 = np.poly1d(coeffsnew2_6)

    coeffsnew1_7  = np.polyfit(vnew1_7, volnew_7, num_order)
    pnew1_7 = np.poly1d(coeffsnew1_7)
    coeffsnew1_8  = np.polyfit(vnew1_8, volnew_8, num_order)
    pnew1_8 = np.poly1d(coeffsnew1_8)
    coeffsnew1_9  = np.polyfit(vnew1_9, volnew_9, num_order)
    pnew1_9 = np.poly1d(coeffsnew1_9)

    #打印函数值

    # print("coeffsnew1_1")
    # print(coeffsnew1_1)
    print("coeffsnew2_1")
    print(coeffsnew2_1)

    # print("coeffsnew1_2")
    # print(coeffsnew1_2)
    print("coeffsnew2_2")
    print(coeffsnew2_2)


    # print("coeffsnew1_3")
    # print(coeffsnew1_3)
    print("coeffsnew2_3")
    print(coeffsnew2_3)

    # print("coeffsnew1_4")
    # print(coeffsnew1_4)
    print("coeffsnew2_4")
    print(coeffsnew2_4)

    # print("coeffsnew1_5")
    # print(coeffsnew1_5)
    print("coeffsnew2_5")
    print(coeffsnew2_5)

    # print("coeffsnew1_6")
    # print(coeffsnew1_6)
    print("coeffsnew2_6")
    print(coeffsnew2_6)


    print("coeffsnew1_7")
    print(coeffsnew1_7)
    print("coeffsnew1_8")
    print(coeffsnew1_8)
    print("coeffsnew1_9")
    print(coeffsnew1_9)

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

    # #2023.07.31
    # #                       水鸭色
    # plt.plot(x, p2_8(x), color='#000080', linestyle='-', markersize=5)
    # plt.plot(v2_8, vol_8, color='#000080', linestyle='', marker='>', markersize=5)
    # #                       洋红
    # plt.plot(x, p3_8(x), color='#FF00FF', linestyle='-', markersize=5)
    # plt.plot(v3_8, vol_8, color='#FF00FF', linestyle='', marker='>', markersize=5)

    #2023.08.1
    #                       浅粉红
    plt.plot(x, pnew1_1(x), color='#FFB6C1', linestyle='-', markersize=5)
    plt.plot(vnew1_1, volnew_1, color='#FFB6C1', linestyle='', marker='>', markersize=5)
    #                       纯蓝
    plt.plot(x, pnew2_1(x), color='#0000FF', linestyle='-', markersize=5)
    plt.plot(vnew2_1, volnew_1, color='#0000FF', linestyle='', marker='>', markersize=5)

    #2023.08.2
    #                       猩红
    plt.plot(x, pnew1_2(x), color='#DC143C', linestyle='-', markersize=5)
    plt.plot(vnew1_2, volnew_2, color='#DC143C', linestyle='', marker='>', markersize=5)
    #                       皇家蓝
    plt.plot(x, pnew2_2(x), color='#4169E1', linestyle='-', markersize=5)
    plt.plot(vnew2_2, volnew_2, color='#4169E1', linestyle='', marker='>', markersize=5)

    #2023.08.3
    #                        深粉色
    plt.plot(x, pnew1_3(x), color='#FF1493', linestyle='-', markersize=5)
    plt.plot(vnew1_3, volnew_3, color='#FF1493', linestyle='', marker='>', markersize=5)
    #                       道奇蓝
    plt.plot(x, pnew2_3(x), color='#1E90FF', linestyle='-', markersize=5)
    plt.plot(vnew2_3, volnew_3, color='#1E90FF', linestyle='', marker='>', markersize=5)

    #2023.08.7
    #                       青紫
    plt.plot(x, pnew1_4(x), color='#6950a1', linestyle='-', markersize=5)
    plt.plot(vnew1_4, volnew_4, color='#6950a1', linestyle='', marker='>', markersize=5)
    #                       萌葱色
    plt.plot(x, pnew2_4(x), color='#006c54', linestyle='-', markersize=5)
    plt.plot(vnew2_4, volnew_4, color='#006c54', linestyle='', marker='>', markersize=5)

    #                       青紫
    plt.plot(x, pnew1_5(x), color='#6950a1', linestyle='-', markersize=5)
    plt.plot(vnew1_5, volnew_5, color='#6950a1', linestyle='', marker='>', markersize=5)
    #                       萌葱色
    plt.plot(x, pnew2_5(x), color='#006c54', linestyle='-', markersize=5)
    plt.plot(vnew2_5, volnew_5, color='#006c54', linestyle='', marker='>', markersize=5)


    #2023.08.8
    #                       青
    plt.plot(x, pnew1_6(x), color='#009ad6', linestyle='-', markersize=5)
    plt.plot(vnew1_6, volnew_6, color='#009ad6', linestyle='', marker='>', markersize=5)
    #                       黄檗色
    plt.plot(x, pnew2_6(x), color='#fcf16e', linestyle='-', markersize=5)
    plt.plot(vnew2_6, volnew_6, color='#fcf16e', linestyle='', marker='>', markersize=5)

    #2023.08.9
    #                       青
    plt.plot(x, pnew1_7(x), color='#009ad6', linestyle='-', markersize=5)
    plt.plot(vnew1_7, volnew_7, color='#009ad6', linestyle='', marker='>', markersize=5)

    plt.plot(x, pnew1_8(x), color='#009ad6', linestyle='-', markersize=5)
    plt.plot(vnew1_8, volnew_8, color='#009ad6', linestyle='', marker='>', markersize=5)

    plt.plot(x, pnew1_9(x), color='#009ad6', linestyle='-', markersize=5)
    plt.plot(vnew1_9, volnew_9, color='#009ad6', linestyle='', marker='>', markersize=5)

    plt.show()
