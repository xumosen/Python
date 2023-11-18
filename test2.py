import numpy as np
import matplotlib.pyplot as plt

# 数据
x = np.array([
    0.04, 0.52, 1.21, 1.77, 2.15, 2.67, 3.00, 3.28, 3.62, 3.70, 4.10, 4.50, 4.80, 4.94
])

y = np.array([
    1.471, 1.301, 1.179, 1.06, 0.91, 0.786, 0.696, 0.610, 0.521, 0.410, 0.340, 0.248, 0.125, 0.071
])

x2 = np.array([
    0.05, 0.57, 0.97, 1.30, 1.78, 2.2, 2.51, 2.82, 3.15, 3.6, 3.95, 4.31, 4.7
])

y2 = np.array([
    1.452, 1.301, 1.179, 0.934, 0.801, 0.747, 0.663, 0.518, 0.427, 0.375, 0.269, 0.223, 0.189
])

# 绘制图表
plt.figure(figsize=(12, 6))

# 散点图
plt.subplot(1, 2, 1)
plt.scatter(x, y, label='Data Set 1')
plt.scatter(x2, y2, label='Data Set 2')
plt.title('Scatter Plot of Data Sets')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# 折线图
plt.subplot(1, 2, 2)
plt.plot(x, y, marker='o', label='Data Set 1')
plt.plot(x2, y2, marker='o', label='Data Set 2')
plt.title('Line Plot of Data Sets')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

plt.tight_layout()
plt.show()
