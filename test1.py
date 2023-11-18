import csv
import numpy as np
import matplotlib.pyplot as plt
import sys
import random

vol_1 = [
# 10000,
# 9000,
# 8100,
# 6200,
# 5300,
# 4500,
# 3700,

2800,
2000,

]

vol_2 = [
# 9900,
# 8700,
# 7700,
# 7100,
# 6100,
# 4800,
# 3600,

1800,
800,
200,
]

vol_3 = [
# 9800,
# 8900,
# 8000,
# 6900,
# 6300,
# 5300,
# 4700,
# 3700,

2900,
2100,
1000,
300,
]

v1_1 = [

# 3831,
# 3792,
# 3746,
# 3617,
# 3544,
# 3454,
# 3340,

3167,
2952,
]

v1_2 = [
# 3822,
# 3772,
# 3717,
# 3675,
# 3698,
# 3474,
# 3301,

2829,
2212,
477,
]

v1_3 = [
# 3798,
# 3752,
# 3702,
# 3628,
# 3581,
# 3500,
# 3420,
# 3268,

3118,
2870,
2199,
462,
]

v2_1 = [

]

v2_2 = [

]


if __name__ == '__main__':

    v1_1 = list(x for x in v1_1) 
    v1_2 = list(x for x in v1_2) 
    v1_3 = list(x for x in v1_3) 

    v2_1 = list(x for x in v2_1) 
    v2_2 = list(x for x in v2_2) 

    vol_1 = list(x for x in vol_1)
    vol_2 = list(x for x in vol_2)
    vol_3 = list(x for x in vol_3)

    num_order = 1

    coeffs1_1 = np.polyfit(v1_1, vol_1, num_order)
    p1_1 = np.poly1d(coeffs1_1)

    coeffs1_2 = np.polyfit(v1_2, vol_2, num_order)
    p1_2 = np.poly1d(coeffs1_2)

    coeffs1_3 = np.polyfit(v1_3, vol_3, num_order)
    p1_3 = np.poly1d(coeffs1_3)

    # coeffs2_1 = np.polyfit(v2_1, vol_1, num_order)
    # p2_1 = np.poly1d(coeffs2_1)

    # coeffs2_2 = np.polyfit(v2_2, vol_2, num_order)
    # p2_2 = np.poly1d(coeffs2_2)


    # 生成第一个随机数
    print ("random 1 : ", random.random())
    # 生成第二个随机数
    print ("random 2 : ", random.random())

    print(coeffs1_1)
    print("coeffs1_1")
    print(coeffs1_2)
    print("coeffs1_2")
    print(coeffs1_3)
    print("coeffs1_3")

    # print(coeffs2_1)
    # print("coeffs2_1")
    # print(coeffs2_2)
    # print("coeffs2_2")


    x = np.linspace(-15000, 15000, 15000)
    plt.figure(figsize=(16, 20))
    plt.ylabel('Y')
    plt.xlabel('X')

    ax = plt.gca()
    ax.set_ylim(-100, 12000)
    ax.set_xlim(-100, 12000)

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
    #       江戸紫
    plt.plot(x, p1_2(x), color='#6f599c', linestyle='-', markersize=5)
    plt.plot(v1_2, vol_2, color='#6f599c', linestyle='', marker='>', markersize=5)  

    #       油色
    plt.plot(x, p1_3(x), color='#817936', linestyle='-', markersize=5)
    plt.plot(v1_3, vol_3, color='#817936', linestyle='', marker='>', markersize=5)  

    # #       红
    # plt.plot(x, p2_1(x), color='#a7324a', linestyle='-', markersize=5)
    # plt.plot(v2_1, vol_1, color='#a7324a', linestyle='', marker='>', markersize=5)  
    # #       江戸紫
    # plt.plot(x, p2_2(x), color='#6f599c', linestyle='-', markersize=5)
    # plt.plot(v2_2, vol_2, color='#6f599c', linestyle='', marker='>', markersize=5)  


    plt.show()
