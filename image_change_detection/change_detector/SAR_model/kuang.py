import cv2
import numpy as np

# 查找物体轮廓
def findcontour(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 图像灰度化
    ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)  # 图像二值化
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # 查找物体轮廓
    return contours, hierarchy

def sily():
    original1 = cv2.imread(r'dataset\\result.bmp')
    original2 = cv2.imread(r'dataset\\2.bmp')



    contours, hierarchy = findcontour(original1)

    nums = len(contours)

    for i in range(nums):

        temp = np.zeros(original1.shape, np.uint8)

        # 绘制最小外接矩形框
        rect = cv2.minAreaRect(contours[i])  # rect返回矩形的特征信息，其结构为【最小外接矩形的中心（x，y），（宽度，高度），旋转角度】
        points = cv2.boxPoints(rect)  # 得到最小外接矩形的四个点坐标
        points = np.int0(points)  # 坐标值取整
        image = cv2.drawContours(original2, [points], 0, (0, 0, 255), 2)  # 直接在原图上绘制矩形框
        
        

        #cv2.imshow("result", image)
    cv2.imwrite('static\\images\\sili.bmp', image)   # 保存结果
    cv2.waitKey()
