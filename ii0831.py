import csv
import numpy as np
import matplotlib.pyplot as plt
import sys

#你好

#  12  13  14  15  16  17
vol_1 = [
0.01,
0.69,
1.29,
2.07,
2.85,
3.98,
4.98,
]

vol_2 = [
0.03,
0.94,
2.11,
3.08,
4.04,
4.79,
5.05,
]

vol_3 = [
0.00,
0.58,
1.29,
2.07,
3.04,
4.05,
4.72,
]

vol_4 = [
0.00,
2.14,
2.66,
3.29,
3.89,
4.45,
5.02,
]

vol_5 = [
0.02,
0.63,
1.33,
1.94,
2.93,
3.77,
4.39,
5.05,
]

vol_6 = [
0.02,
0.46,
1.21,
2.04,
3.20,
4.00,
4.54,
5.15,
]


v12_1 = [
1.434,
1.255,
1.090,
0.897,
0.716,
0.475,
0.271,
]

v12_2 = [
1.446,
1.212,
0.912,
0.688,
0.479,
0.329,
0.278,
]

v12_3 = [
1.444,
1.296,
1.105,
0.909,
0.686,
0.469,
0.333,
]

v12_4 = [
1.452,
0.907,
0.781,
0.639,
0.513,
0.394,
0.283,
]

v12_5 = [
1.459,
1.301,
1.119,
0.967,
0.739,
0.555,
0.425,
0.296,
]

v12_6 = [
1.459,
1.349,
1.159,
0.945,
0.683,
0.512,
0.397,
0.277,
]


v13_1 = [
1.535,
1.366,
1.210,
1.026,
0.853,
0.621,
0.425,
]

v13_2 = [
1.541,
1.321,
1.036,
0.822,
0.623,
0.476,
0.426,
]

v13_3 = [
1.538,
1.400,
1.219,
1.033,
0.818,
0.609,
0.475,
]

v13_4 = [
1.541,
1.026,
0.905,
0.769,
0.646,
0.533,
0.423,
]

v13_5 = [
1.546,
1.397,
1.224,
1.080,
0.863,
0.686,
0.561,
0.435,
]

v13_6 = [
1.545,
1.441,
1.260,
1.058,
0.807,
0.643,
0.533,
0.416,
]

v14_1 = [
1.522,
1.348,
1.185,
0.995,
0.817,
0.575,
0.368,
]

v14_2 = [
1.529,
1.300,
1.004,
0.781,
0.572,
0.419,
0.364,
]

v14_3 = [
1.525,
1.380,
1.191,
0.997,
0.772,
0.554,
0.413,
]

v14_4 = [
1.531,
0.991,
0.864,
0.722,
0.594,
0.475,
0.363,
]

v14_5 = [
1.536,
1.378,
1.199,
1.046,
0.821,
0.633,
0.502,
0.374,
]

v14_6 = [
1.538,
1.428,
1.239,
1.028,
0.766,
0.591,
0.476,
0.355,  
]

v15_1 = [
1.269,
1.097,
0.940,
0.757,
0.583,
0.354,
0.153,
]

v15_2 = [
1.283,
1.053,
0.766,
0.551,
0.352,
0.204,
0.150,
]

v15_3 = [
1.281,
1.134,
0.951,
0.763,
0.546,
0.335,
0.201,
]

v15_4 = [
1.290,
0.758,
0.637,
0.499,
0.375,
0.261,
0.152,
]

v15_5 = [
1.297,
1.139,
0.962,
0.815,
0.594,
0.413,
0.287,
0.162,
]

v15_6 = [
1.298,
1.187,
1.000,
0.794,
0.538,
0.372,
0.262,
0.144,  
]


v16_1 = [
1.368,
1.197,
1.037,
0.851,
0.673,
0.438,
0.233,
]

v16_2 = [
1.376,
1.150,
0.858,
0.638,
0.434,
0.283,
0.230,
]

v16_3 = [
1.371,
1.229,
1.042,
0.850,
0.629,
0.416,
0.280,
]

v16_4 = [
1.377,
0.843,
0.718,
0.578,
0.455,
0.337,
0.225,
]

v16_5 = [
1.381,
1.225,
1.046,
0.897,
0.673,
0.490,
0.363,
0.234,
]

v16_6 = [
1.381,
1.272,
1.083,
0.875,
0.616,
0.446,
0.333,
0.215,
]

v17_1 = [
1.452,
1.282,
1.126,
0.942,
0.767,
0.531,
0.326,
]

v17_2 = [
1.456,
1.231,
0.943,
0.727,
0.525,
0.379,
0.321,
]

v17_3 = [
1.452,
1.309,
1.127,
0.938,
0.721,
0.510,
0.373,
]

v17_4 = [
1.456,
0.931,
0.810,
0.670,
0.545,
0.429,
0.318,
]

v17_5 = [
1.459,
1.305,
1.130,
0.983,
0.761,
0.580,
0.452,
0.328,
]

v17_6 = [
1.458,
1.351,
1.165,
0.961,
0.704,
0.536,
0.426,
0.308,    
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

    v12_1 = list(v2sv(x) for x in v12_1)
    v13_1 = list(v2sv(x) for x in v13_1)
    v14_1 = list(v2sv(x) for x in v14_1)
    v15_1 = list(v2sv(x) for x in v15_1)
    v16_1 = list(v2sv(x) for x in v16_1)
    v17_1 = list(v2sv(x) for x in v17_1)

    v12_2 = list(v2sv(x) for x in v12_2)
    v13_2 = list(v2sv(x) for x in v13_2)
    v14_2 = list(v2sv(x) for x in v14_2)
    v15_2 = list(v2sv(x) for x in v15_2)
    v16_2 = list(v2sv(x) for x in v16_2)
    v17_2 = list(v2sv(x) for x in v17_2)


    v12_3 = list(v2sv(x) for x in v12_3)
    v13_3 = list(v2sv(x) for x in v13_3)
    v14_3 = list(v2sv(x) for x in v14_3)
    v15_3 = list(v2sv(x) for x in v15_3)
    v16_3 = list(v2sv(x) for x in v16_3)
    v17_3 = list(v2sv(x) for x in v17_3)

    v12_4 = list(v2sv(x) for x in v12_4)
    v13_4 = list(v2sv(x) for x in v13_4)
    v14_4 = list(v2sv(x) for x in v14_4)
    v15_4 = list(v2sv(x) for x in v15_4)
    v16_4 = list(v2sv(x) for x in v16_4)
    v17_4 = list(v2sv(x) for x in v17_4)

    v12_5 = list(v2sv(x) for x in v12_5)
    v13_5 = list(v2sv(x) for x in v13_5)
    v14_5 = list(v2sv(x) for x in v14_5)
    v15_5 = list(v2sv(x) for x in v15_5)
    v16_5 = list(v2sv(x) for x in v16_5)
    v17_5 = list(v2sv(x) for x in v17_5)

    v12_6 = list(v2sv(x) for x in v12_6)
    v13_6 = list(v2sv(x) for x in v13_6)
    v14_6 = list(v2sv(x) for x in v14_6)
    v15_6 = list(v2sv(x) for x in v15_6)
    v16_6 = list(v2sv(x) for x in v16_6)
    v17_6 = list(v2sv(x) for x in v17_6)

    # tmp1 = list(temp_offset(t) for t in t3)
    # tmp = list(zip(v3_3, tmp1))
    # v3_3_t = list(x[0] - x[1] for x in tmp);
    #v2 = v3_3

    #函数拟合
    num_order = 2
 
    coeffs12_1  = np.polyfit(v12_1, vol_1, num_order)
    p12_1 = np.poly1d(coeffs12_1)
    coeffs13_1 = np.polyfit(v13_1, vol_1, num_order)
    p13_1 = np.poly1d(coeffs13_1)
    coeffs14_1  = np.polyfit(v14_1, vol_1, num_order)
    p14_1 = np.poly1d(coeffs14_1)
    coeffs15_1 = np.polyfit(v15_1, vol_1, num_order)
    p15_1 = np.poly1d(coeffs15_1)
    coeffs16_1 = np.polyfit(v16_1, vol_1, num_order)
    p16_1 = np.poly1d(coeffs16_1)
    coeffs17_1 = np.polyfit(v17_1, vol_1, num_order)
    p17_1 = np.poly1d(coeffs17_1)

    coeffs12_2  = np.polyfit(v12_2, vol_2, num_order)
    p12_2 = np.poly1d(coeffs12_2)
    coeffs13_2 = np.polyfit(v13_2, vol_2, num_order)
    p13_2 = np.poly1d(coeffs13_2)
    coeffs14_2  = np.polyfit(v14_2, vol_2, num_order)
    p14_2 = np.poly1d(coeffs14_2)
    coeffs15_2 = np.polyfit(v15_2, vol_2, num_order)
    p15_2 = np.poly1d(coeffs15_2)
    coeffs16_2  = np.polyfit(v16_2, vol_2, num_order)
    p16_2 = np.poly1d(coeffs16_2)
    coeffs17_2 = np.polyfit(v17_2, vol_2, num_order)
    p17_2 = np.poly1d(coeffs17_2)


    coeffs12_3  = np.polyfit(v12_3, vol_3, num_order)
    p12_3 = np.poly1d(coeffs12_3)
    coeffs13_3 = np.polyfit(v13_3, vol_3, num_order)
    p13_3 = np.poly1d(coeffs13_3)
    coeffs14_3  = np.polyfit(v14_3, vol_3, num_order)
    p14_3 = np.poly1d(coeffs14_3)
    coeffs15_3 = np.polyfit(v15_3, vol_3, num_order)
    p15_3 = np.poly1d(coeffs15_3)
    coeffs16_3  = np.polyfit(v16_3, vol_3, num_order)
    p16_3 = np.poly1d(coeffs16_3)
    coeffs17_3 = np.polyfit(v17_3, vol_3, num_order)
    p17_3 = np.poly1d(coeffs17_3)

    coeffs12_4  = np.polyfit(v12_4, vol_4, num_order)
    p12_4 = np.poly1d(coeffs12_4)
    coeffs13_4 = np.polyfit(v13_4, vol_4, num_order)
    p13_4 = np.poly1d(coeffs13_4)
    coeffs14_4  = np.polyfit(v14_4, vol_4, num_order)
    p14_4 = np.poly1d(coeffs14_4)
    coeffs15_4 = np.polyfit(v15_4, vol_4, num_order)
    p15_4 = np.poly1d(coeffs15_4)
    coeffs16_4  = np.polyfit(v16_4, vol_4, num_order)
    p16_4 = np.poly1d(coeffs16_4)
    coeffs17_4 = np.polyfit(v17_4, vol_4, num_order)
    p17_4 = np.poly1d(coeffs17_4)

    coeffs12_5  = np.polyfit(v12_5, vol_5, num_order)
    p12_5 = np.poly1d(coeffs12_5)
    coeffs13_5 = np.polyfit(v13_5, vol_5, num_order)
    p13_5 = np.poly1d(coeffs13_5)
    coeffs14_5  = np.polyfit(v14_5, vol_5, num_order)
    p14_5 = np.poly1d(coeffs14_5)
    coeffs15_5 = np.polyfit(v15_5, vol_5, num_order)
    p15_5 = np.poly1d(coeffs15_5)
    coeffs16_5  = np.polyfit(v16_5, vol_5, num_order)
    p16_5 = np.poly1d(coeffs16_5)
    coeffs17_5 = np.polyfit(v17_5, vol_5, num_order)
    p17_5 = np.poly1d(coeffs17_5)

    coeffs12_6  = np.polyfit(v12_6, vol_6, num_order)
    p12_6 = np.poly1d(coeffs12_6)
    coeffs13_6 = np.polyfit(v13_6, vol_6, num_order)
    p13_6 = np.poly1d(coeffs13_6)
    coeffs14_6  = np.polyfit(v14_6, vol_6, num_order)
    p14_6 = np.poly1d(coeffs14_6)
    coeffs15_6 = np.polyfit(v15_6, vol_6, num_order)
    p15_6 = np.poly1d(coeffs15_6)
    coeffs16_6  = np.polyfit(v16_6, vol_6, num_order)
    p16_6 = np.poly1d(coeffs16_6)
    coeffs17_6 = np.polyfit(v17_6, vol_6, num_order)
    p17_6 = np.poly1d(coeffs17_6)

    #打印函数值

    # print("coeffsn12_1")
    # print(coeffs12_1)
    # print("coeffsn12_2")
    # print(coeffs12_2)
    # print("coeffsn12_3")
    # print(coeffs12_3)
    # print("coeffsn12_4")
    # print(coeffs12_4)
    # print("coeffsn12_5")
    # print(coeffs12_5)
    # print("coeffsn12_6")
    # print(coeffs12_6)
    # print("coeffsn12adv")
    # print((coeffs12_2+coeffs12_5+coeffs12_6)/3)

    # print("coeffsn13_1")
    # print(coeffs13_1)
    # print("coeffsn13_2")
    # print(coeffs13_2)
    # print("coeffsn13_3")
    # print(coeffs13_3)
    # print("coeffsn13_4")
    # print(coeffs13_4)
    # print("coeffsn13_5")
    # print(coeffs13_5)
    # print("coeffsn13_6")
    # print(coeffs13_6)
    # print("coeffsn13adv")
    # print((coeffs13_2+coeffs13_5+coeffs13_6)/3)

    # print("coeffsn14_1")
    # print(coeffs14_1)
    # print("coeffsn14_2")
    # print(coeffs14_2)
    # print("coeffsn14_3")
    # print(coeffs14_3)
    # print("coeffsn14_4")
    # print(coeffs14_4)
    # print("coeffsn14_5")
    # print(coeffs14_5)
    # print("coeffsn14_6")
    # print(coeffs14_6)
    # print("coeffsn14adv")
    # print((coeffs14_2+coeffs14_5+coeffs14_6)/3)

    # print("coeffsn15_1")
    # print(coeffs15_1)
    # print("coeffsn15_2")
    # print(coeffs15_2)
    # print("coeffsn15_3")
    # print(coeffs15_3)
    # print("coeffsn15_4")
    # print(coeffs15_4)
    # print("coeffsn15_5")
    # print(coeffs15_5)
    # print("coeffsn15_6")
    # print(coeffs15_6)
    # print("coeffsn15adv")
    # print((coeffs15_2+coeffs15_5+coeffs15_6)/3)

    # print("coeffsn16_1")
    # print(coeffs16_1)
    # print("coeffsn16_2")
    # print(coeffs16_2)
    # print("coeffsn16_3")
    # print(coeffs16_3)
    # print("coeffsn16_4")
    # print(coeffs16_4)
    # print("coeffsn16_5")
    # print(coeffs16_5)
    # print("coeffsn16_6")
    # print(coeffs16_6)
    # print("coeffsn16adv")
    # print((coeffs16_2+coeffs16_5+coeffs16_6)/3)

    print("coeffsn17_1")
    print(coeffs17_1)
    print("coeffsn17_2")
    print(coeffs17_2)
    print("coeffsn17_3")
    print(coeffs17_3)
    print("coeffsn17_4")
    print(coeffs17_4)
    print("coeffsn17_5")
    print(coeffs17_5)
    print("coeffsn17_6")
    print(coeffs17_6)
    print("coeffsn17adv")
    print((coeffs17_2+coeffs17_5+coeffs17_6)/3)


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
    # plt.plot(x, p12_1(x), color='#444693', linestyle='-', markersize=5)
    # plt.plot(v12_1, vol_1, color='#444693', linestyle='', marker='>', markersize=5)

    # plt.plot(x, p12_2(x), color='#817936', linestyle='-', markersize=5)
    # plt.plot(v12_2, vol_2, color='#817936', linestyle='', marker='>', markersize=5)

    # plt.plot(x, p12_3(x), color='#444693', linestyle='-', markersize=5)
    # plt.plot(v12_3, vol_3, color='#444693', linestyle='', marker='>', markersize=5)
    # plt.plot(x, p12_4(x), color='#444693', linestyle='-', markersize=5)
    # plt.plot(v12_4, vol_4, color='#444693', linestyle='', marker='>', markersize=5)

    # plt.plot(x, p12_5(x), color='#817936', linestyle='-', markersize=5)
    # plt.plot(v12_5, vol_5, color='#817936', linestyle='', marker='>', markersize=5)
    # plt.plot(x, p12_6(x), color='#817936', linestyle='-', markersize=5)
    # plt.plot(v12_6, vol_6, color='#817936', linestyle='', marker='>', markersize=5)

    #                       赤白橡
    # plt.plot(x, p13_1(x), color='#444693', linestyle='-', markersize=5)
    # plt.plot(v13_1, vol_1, color='#444693', linestyle='', marker='>', markersize=5)

    # plt.plot(x, p13_2(x), color='#817936', linestyle='-', markersize=5)
    # plt.plot(v13_2, vol_2, color='#817936', linestyle='', marker='>', markersize=5)

    # plt.plot(x, p13_3(x), color='#444693', linestyle='-', markersize=5)
    # plt.plot(v13_3, vol_3, color='#444693', linestyle='', marker='>', markersize=5)
    # plt.plot(x, p13_4(x), color='#444693', linestyle='-', markersize=5)
    # plt.plot(v13_4, vol_4, color='#444693', linestyle='', marker='>', markersize=5)

    # plt.plot(x, p13_5(x), color='#817936', linestyle='-', markersize=5)
    # plt.plot(v13_5, vol_5, color='#817936', linestyle='', marker='>', markersize=5)
    # plt.plot(x, p13_6(x), color='#817936', linestyle='-', markersize=5)
    # plt.plot(v13_6, vol_6, color='#817936', linestyle='', marker='>', markersize=5)

    #                       油色
    # plt.plot(x, p14_1(x), color='#444693', linestyle='-', markersize=5)
    # plt.plot(v14_1, vol_1, color='#444693', linestyle='', marker='>', markersize=5)

    # plt.plot(x, p14_2(x), color='#817936', linestyle='-', markersize=5)
    # plt.plot(v14_2, vol_2, color='#817936', linestyle='', marker='>', markersize=5)

    # plt.plot(x, p14_3(x), color='#444693', linestyle='-', markersize=5)
    # plt.plot(v14_3, vol_3, color='#444693', linestyle='', marker='>', markersize=5)
    # plt.plot(x, p14_4(x), color='#444693', linestyle='-', markersize=5)
    # plt.plot(v14_4, vol_4, color='#444693', linestyle='', marker='>', markersize=5)

    # plt.plot(x, p14_5(x), color='#817936', linestyle='-', markersize=5)
    # plt.plot(v14_5, vol_5, color='#817936', linestyle='', marker='>', markersize=5)
    # plt.plot(x, p14_6(x), color='#817936', linestyle='-', markersize=5)
    # plt.plot(v14_6, vol_6, color='#817936', linestyle='', marker='>', markersize=5)

    #                       绀桔梗
    # plt.plot(x, p15_1(x), color='#444693', linestyle='-', markersize=5)
    # plt.plot(v15_1, vol_1, color='#444693', linestyle='', marker='>', markersize=5)
    
    # plt.plot(x, p15_2(x), color='#817936', linestyle='-', markersize=5)
    # plt.plot(v15_2, vol_2, color='#817936', linestyle='', marker='>', markersize=5)

    # plt.plot(x, p15_3(x), color='#444693', linestyle='-', markersize=5)
    # plt.plot(v15_3, vol_3, color='#444693', linestyle='', marker='>', markersize=5)
    # plt.plot(x, p15_4(x), color='#444693', linestyle='-', markersize=5)
    # plt.plot(v15_4, vol_4, color='#444693', linestyle='', marker='>', markersize=5)

    # plt.plot(x, p15_5(x), color='#817936', linestyle='-', markersize=5)
    # plt.plot(v15_5, vol_5, color='#817936', linestyle='', marker='>', markersize=5)
    # plt.plot(x, p15_6(x), color='#817936', linestyle='-', markersize=5)
    # plt.plot(v15_6, vol_6, color='#817936', linestyle='', marker='>', markersize=5)

    #                       绀桔梗
    # plt.plot(x, p16_1(x), color='#444693', linestyle='-', markersize=5)
    # plt.plot(v16_1, vol_1, color='#444693', linestyle='', marker='>', markersize=5)
    
    # plt.plot(x, p16_2(x), color='#817936', linestyle='-', markersize=5)
    # plt.plot(v16_2, vol_2, color='#817936', linestyle='', marker='>', markersize=5)

    # plt.plot(x, p16_3(x), color='#444693', linestyle='-', markersize=5)
    # plt.plot(v16_3, vol_3, color='#444693', linestyle='', marker='>', markersize=5)  
    # plt.plot(x, p16_4(x), color='#444693', linestyle='-', markersize=5)
    # plt.plot(v16_4, vol_4, color='#444693', linestyle='', marker='>', markersize=5)

    # plt.plot(x, p16_5(x), color='#817936', linestyle='-', markersize=5)
    # plt.plot(v16_5, vol_5, color='#817936', linestyle='', marker='>', markersize=5)
    # plt.plot(x, p16_6(x), color='#817936', linestyle='-', markersize=5)
    # plt.plot(v16_6, vol_6, color='#817936', linestyle='', marker='>', markersize=5)

    #                       绀桔梗
    # plt.plot(x, p17_1(x), color='#444693', linestyle='-', markersize=5)
    # plt.plot(v17_1, vol_1, color='#444693', linestyle='', marker='>', markersize=5)
    
    plt.plot(x, p17_2(x), color='#817936', linestyle='-', markersize=5)
    plt.plot(v17_2, vol_2, color='#817936', linestyle='', marker='>', markersize=5)

    # plt.plot(x, p17_3(x), color='#444693', linestyle='-', markersize=5)
    # plt.plot(v17_3, vol_3, color='#444693', linestyle='', marker='>', markersize=5)   
    # plt.plot(x, p17_4(x), color='#444693', linestyle='-', markersize=5)
    # plt.plot(v17_4, vol_4, color='#444693', linestyle='', marker='>', markersize=5)

    plt.plot(x, p17_5(x), color='#817936', linestyle='-', markersize=5)
    plt.plot(v17_5, vol_5, color='#817936', linestyle='', marker='>', markersize=5)
    plt.plot(x, p17_6(x), color='#817936', linestyle='-', markersize=5)
    plt.plot(v17_6, vol_6, color='#817936', linestyle='', marker='>', markersize=5)

    plt.show()
