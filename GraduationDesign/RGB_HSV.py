import cv2 as cv


def img_in(str_path):
    # 图片输入
    image = cv.imread(str_path)
    return image


def img_out(win_name, image):
    # 图片输出
    cv.imshow(win_name, image)


def split(image):
    # 分量的提取
    ch1, ch2, ch3 = cv.split(image)
    return ch3, ch2, ch1


# 输入输出原图
img = img_in("../resources/map.jpg")
img_out("original", img)

# RGB输出
B, G, R = split(img)
img_out("R", R)
img_out("G", G)
img_out("B", B)

# RGB转HSV
hsv = cv.cvtColor(img, cv.COLOR_RGB2HSV)
img_out("hsv", hsv)

# HSV输出
H, S, V = split(hsv)
img_out("H", H)
img_out("S", S)
img_out("V", V)

# 等待
cv.waitKey(0)
cv.destroyAllWindows()