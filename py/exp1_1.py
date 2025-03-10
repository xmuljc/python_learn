import cv2
import numpy as np
import os


def load_and_validate_image(path):
    """加载图像并验证是否成功"""
    img = cv2.imread(path)
    if img is None:
        raise FileNotFoundError(f"无法加载图像：{path}")
    # 统一转换为三通道（处理可能的灰度图）
    if len(img.shape) == 2:
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    return img


# 图像路径配置
image_paths = [
    'D:/py/data/cat1.jpg',
    'D:/py/data/cat2.jpg',
    'D:/py/data/cat3.jpg',
    'D:/py/data/cat4.jpg'
]

# 加载所有图像
try:
    cats = [load_and_validate_image(path) for path in image_paths]
except Exception as e:
    print(f"错误：{str(e)}")
    exit()

# 统一调整尺寸（以第一张图片为基准）
base_height, base_width = cats[0].shape[:2]
resized_cats = []
for img in cats:
    resized = cv2.resize(img, (base_width, base_height))
    resized_cats.append(resized)

# 创建拼贴画
try:
    top_row = np.hstack((resized_cats[0], resized_cats[1]))
    bottom_row = np.hstack((resized_cats[2], resized_cats[3]))
    collage = np.vstack((top_row, bottom_row))
except Exception as e:
    print(f"拼接失败：{str(e)}")
    exit()

# 保存结果
output_dir = 'D:/py/data'
output_path = os.path.join(output_dir, 'cat_col.jpg')
try:
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    cv2.imwrite(output_path, collage)
    print(f"拼贴画已保存至：{output_path}")
except Exception as e:
    print(f"保存失败：{str(e)}")
    exit()

# 显示结果（添加异常处理）
try:
    cv2.imshow('Cat Collage', collage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except Exception as e:
    print(f"显示图像时出错：{str(e)}")
    cv2.destroyAllWindows()  # 确保在异常情况下也能关闭窗口
