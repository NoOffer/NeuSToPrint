import cv2
import os
import numpy as np

def extract_evenly_spaced_frames(video_path, output_dir, num_frames=150):
    # 创建输出目录
    os.makedirs(output_dir, exist_ok=True)

    # 打开视频
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("无法打开视频文件")
        return

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"视频总帧数: {total_frames}")

    if total_frames < num_frames:
        print("视频帧数少于要提取的数量，直接提取全部帧")
        frame_indices = list(range(total_frames))
    else:
        # 计算要提取的帧的位置（均匀分布）
        frame_indices = np.linspace(0, total_frames - 1, num_frames, dtype=int)

    saved = 0
    for i in range(total_frames):
        ret, frame = cap.read()
        if not ret:
            break

        if i in frame_indices:
            frame_filename = os.path.join(output_dir, f"frame_{saved:05d}.jpg")
            cv2.imwrite(frame_filename, frame)
            saved += 1
            print(f"保存第 {i} 帧为 {frame_filename}")

    cap.release()
    print(f"完成！共保存 {saved} 张图像。")

# 示例用法
video_path = "cup.mp4"
output_dir = "output_frames"
extract_evenly_spaced_frames(video_path, output_dir, num_frames=150)
