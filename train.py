import torch  # torch 모듈을 임포트

from ultralytics import YOLO

# GPU 설정 확인 (CUDA가 설치되어 있으면 GPU 사용)
device = 'cuda' if torch.cuda.is_available() else 'cpu'

# YOLO 모델 로드 (모델 크기는 'yolov8m.yaml'을 사용)
model = YOLO('yolov8m.yaml')

# 모델 학습
model.train(
    data='C:/Users/user/Desktop/yolo/data.yaml',  # 데이터 경로
    workers=8,  # 데이터 로더의 워커 수 (CPU 코어 수에 맞게 조정)
    imgsz=640,  # 이미지 크기
    epochs=3,  # 학습 에포크 수
    lr0=0.01,  # 초기 학습률
    batch=16,  # 배치 크기 (GPU 메모리에 맞게 설정)
    device=device,  # GPU 사용 (CUDA)
    augment=True,  # 데이터 증강 사용
    multi_scale=True,  # 다양한 크기의 이미지를 사용하여 학습
)

# 학습이 완료된 후 모델을 저장
model.save('yolov8.pt')
