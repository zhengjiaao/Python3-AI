import cv2
import time
from ultralytics import YOLO

# 加载支持跟踪功能的YOLO模型，确保模型配置适用于跟踪
model = YOLO("D:\\temp\\yolov8\\models\\yolov8n.pt")  # 确保模型支持跟踪，可能需要特定的配置或权重

# RTSP视频流的URL
rtsp_url = "rtsp://username:password@ip_address:port/path"

# 使用cv2.VideoCapture打开RTSP视频流
cap = cv2.VideoCapture(rtsp_url)

# todo 频繁断开，无法重连，暂时未解决
# 重试计数器
retry_count = 0
max_retries = 3
retry_delays = [5, 10, 20]  # 重试间隔时间列表

while cap.isOpened():
    # 读取一帧
    ret, frame = cap.read()
    if not ret:
        # print("无法获取视频帧，视频流可能已结束或发生错误。")
        # break
        print("无法获取视频帧，尝试重新连接...")
        # cap.release()  # 释放当前连接
        time.sleep(retry_delays[retry_count])  # 等待指定时间后重试
        retry_count += 1
        if retry_count < max_retries:  # 如果未达到最大重试次数
            continue  # 继续下一次尝试
        else:
            print("重试次数已达上限，无法连接视频流。")
            break

    # 使用YOLO模型进行跟踪预测，这里假设model.track方法接受cv2读取的frame
    # 注意：YOLO库的不同版本和实现可能有不同的参数和用法，请根据实际库的文档调整
    results = model.track(frame, persist=True)  # 'persist=True'假设为持续跟踪，具体参数根据你的模型和需求调整

    # 处理并显示结果，这里简单展示如何获取跟踪框并在帧上画出
    if results:
        for r in results[0].boxes.data.tolist():  # 假设results格式包含跟踪框信息
            x1, y1, x2, y2, _, id = r  # 解析框坐标和ID
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 2)  # 绘制矩形框
            cv2.putText(frame, f"ID: {int(id)}", (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0),
                        2)  # 显示ID

    # 显示带有跟踪框的帧
    cv2.imshow('YOLO Tracking on RTSP Stream', frame)

    # 按'q'键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放资源并关闭窗口
cap.release()
cv2.destroyAllWindows()
