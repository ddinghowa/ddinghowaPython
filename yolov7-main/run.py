import os

terminal_command = f"python yolov7-main/detect.py --weights yolov7-main/runs/train/exp/weights/best.pt --conf 0.2 --source image/test.jpg"

os.system(terminal_command)