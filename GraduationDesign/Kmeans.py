import numpy as np
import cv2

# 读入
img = cv2.imread('../resources/map.jpg')
Z = img.reshape((-1, 3))

# 转换为float类型 
Z = np.float32(Z)

# 定义标准、K值
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 2

# 调用k_means函数
ret, label, center = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

# Now convert back into uint8, and make original image
# 转回uint8格式，恢复图像
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))

cv2.imshow("k聚类", res2)


cv2.waitKey(0)
cv2.destroyAllWindows()