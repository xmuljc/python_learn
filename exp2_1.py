import cv2
import dlib

# 初始化 dlib 的人脸检测器和特征点提取器
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("D:\py\shape_predictor_68_face_landmarks.dat")

# 初始化摄像头
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("错误：无法打开摄像头")
    exit()

cv2.namedWindow('Face Landmarks and Detection', cv2.WINDOW_NORMAL)  # 可调整窗口大小
cv2.resizeWindow('Face Landmarks and Detection', 800, 600)  # 设置窗口大小

while True:
    ret, frame = cap.read()
    if not ret:
        print("错误：无法读取帧")
        break

    # 将图像转为灰度
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 检测人脸
    faces = detector(gray)

    for face in faces:
        # 绘制人脸矩形框
        x, y, w, h = (face.left(), face.top(), face.width(), face.height())
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # 获取面部特征点
        landmarks = predictor(gray, face)

        # 绘制面部特征点
        for n in range(68):
            x, y = landmarks.part(n).x, landmarks.part(n).y
            cv2.circle(frame, (x, y), 1, (0, 0, 255), -1)

    # 显示帧率提示
    cv2.putText(frame, "Press 'q' to quit", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # 显示处理后的图像
    cv2.imshow('Face Landmarks and Detection', frame)

    # 按下 'q' 或关闭窗口退出
    if cv2.waitKey(1) & 0xFF == ord('q') or cv2.getWindowProperty('Face Landmarks and Detection', cv2.WND_PROP_VISIBLE) < 1:
        break

cap.release()
cv2.destroyAllWindows()
