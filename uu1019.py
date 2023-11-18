import csv
import numpy as np
import matplotlib.pyplot as plt
import sys
import random

vol_1 = [
# 0,
# 700,
# 1800,
3300,
4600,
5700,
6900,
7700,
9400,
10200,
]

vol_2 = [
# 100,
# 600,
# 1600,
3300,
4000,
4600,
5600,
6700,
8300,
9000,
9800,
]

vol_3 = [

]

v1_1 = [
# 535,
# 2229,
# 2844,
3235,
3411,
3525,
3614,
3656,
3744,
3768,
]

v1_2 = [
# 539,
# 1959,
# 2665,
3167,
3307,
3405,
3501,
3586,
3689,
3719,
3746,
]

v1_3 = [

]

v2_1 = [
# 589,
# 2544,
# 3096,
3431,
3577,
3673,
3755,
3755,
3755,
3755,
]

v2_2 = [
# 598,
# 2293,
# 2971,
3378,
3482,
3557,
3641,
3708,
3793,
3833,
3857,
]

v3_1 = [
# 570,
# 2302,
# 2923,
3308,
3485,
3608,
3702,
3744,
3840,
3871,
]

v3_2 = [
# 643,
# 2098,
# 2841,
3305,
3428,
3517,
3614,
3700,
3799,
3837,
3866,
]

if __name__ == '__main__':

    v1_1 = list(x for x in v1_1) 
    v1_2 = list(x for x in v1_2) 
    v1_3 = list(x for x in v1_3) 

    v2_1 = list(x for x in v2_1) 
    v2_2 = list(x for x in v2_2) 

    v3_1 = list(x for x in v3_1) 
    v3_2 = list(x for x in v3_2) 

    vol_1 = list(x for x in vol_1)
    vol_2 = list(x for x in vol_2)
    vol_3 = list(x for x in vol_3)

    num_order = 1

    coeffs1_1 = np.polyfit(v1_1, vol_1, num_order)
    p1_1 = np.poly1d(coeffs1_1)

    coeffs1_2 = np.polyfit(v1_2, vol_2, num_order)
    p1_2 = np.poly1d(coeffs1_2)

    # coeffs1_3 = np.polyfit(v1_3, vol_3, num_order)
    # p1_3 = np.poly1d(coeffs1_3)

    coeffs2_1 = np.polyfit(v2_1, vol_1, num_order)
    p2_1 = np.poly1d(coeffs2_1)

    coeffs2_2 = np.polyfit(v2_2, vol_2, num_order)
    p2_2 = np.poly1d(coeffs2_2)

    coeffs3_1 = np.polyfit(v3_1, vol_1, num_order)
    p3_1 = np.poly1d(coeffs3_1)

    coeffs3_2 = np.polyfit(v3_2, vol_2, num_order)
    p3_2 = np.poly1d(coeffs3_2)


    # 生成第一个随机数
    print ("random 1 : ", random.random())
    # 生成第二个随机数
    print ("random 2 : ", random.random())

    print(coeffs1_1)
    print("coeffs1_1")
    print(coeffs1_2)
    print("coeffs1_2")
    # print(coeffs1_3)
    # print("coeffs1_3")

    print(coeffs2_1)
    print("coeffs2_1")
    print(coeffs2_2)
    print("coeffs2_2")

    print(coeffs3_1)
    print("coeffs3_1")
    print(coeffs3_2)
    print("coeffs3_2")


    x = np.linspace(-12000, 12000, 12000)
    plt.figure(figsize=(8, 10))
    plt.ylabel('Y')
    plt.xlabel('X')

    ax = plt.gca()
    ax.set_ylim(-100, 12000)
    ax.set_xlim(-100, 5000)

    ax.yaxis.set_major_locator(plt.MultipleLocator(500))
    ax.yaxis.set_minor_locator(plt.MultipleLocator(500))
    ax.xaxis.set_major_locator(plt.MultipleLocator(500))
    ax.xaxis.set_minor_locator(plt.MultipleLocator(500))

    # ax.grid(which='major', axis='y', linewidth=0.75, linestyle='-', color='0.75')
    # ax.grid(which='minor', axis='y', linewidth=0.25, linestyle='-', color='0.75')
    # ax.grid(which='major', axis='x', linewidth=0.75, linestyle='-', color='0.75')
    # ax.grid(which='minor', axis='x', linewidth=0.25, linestyle='-', color='0.75')

    # ax.grid(which='major', axis='y', linewidth=1, linestyle='-', color='0.75')
    # ax.grid(which='minor', axis='y', linewidth=1, linestyle='-', color='0.75')
    # ax.grid(which='major', axis='x', linewidth=1, linestyle='-', color='0.75')
    # ax.grid(which='minor', axis='x', linewidth=1, linestyle='-', color='0.75')

    #       红
    plt.plot(x, p1_1(x), color='#a7324a', linestyle='-', markersize=5)
    plt.plot(v1_1, vol_1, color='#a7324a', linestyle='', marker='>', markersize=5) 
    plt.plot(x, p1_2(x), color='#a7324a', linestyle='-', markersize=5)
    plt.plot(v1_2, vol_2, color='#a7324a', linestyle='', marker='>', markersize=5)   

    #       油色
    plt.plot(x, p2_1(x), color='#817936', linestyle='-', markersize=5)
    plt.plot(v2_1, vol_1, color='#817936', linestyle='', marker='>', markersize=5)  
    plt.plot(x, p2_2(x), color='#817936', linestyle='-', markersize=5)
    plt.plot(v2_2, vol_2, color='#817936', linestyle='', marker='>', markersize=5)  

    #       蓝色
    plt.plot(x, p3_1(x), color='#444693', linestyle='-', markersize=5)
    plt.plot(v3_1, vol_1, color='#444693', linestyle='', marker='>', markersize=5)  
    plt.plot(x, p3_2(x), color='#444693', linestyle='-', markersize=5)
    plt.plot(v3_2, vol_2, color='#444693', linestyle='', marker='>', markersize=5)  


    plt.show()
