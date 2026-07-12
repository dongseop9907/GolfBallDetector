from ultralytics import YOLO

# 기존 50 에폭 학습된 모델의 last.pt를 불러옴 (초기 가중치처럼 사용)
model = YOLO('C:/Users/user/PyCharmMiscProject/runs/detect/train8/weights/last.pt')

# 새로 300 에폭 동안 학습 시작
model.train(
    data='C:/Users/user/Desktop/yolo/data.yaml',  # data.yaml 파일 경로
    epochs=300,                                    # 새로 300 에폭 학습
    imgsz=640,                                     # 이미지 크기 (필요시 조정 가능)
    batch=16,                                      # 배치 사이즈 (GPU 성능에 따라 조정)
    project='runs/detect',                         # 결과 저장 위치
    name='train8',                                  # 새 폴더명 (자동으로 train8 폴더 생성됨)
    resume=True
)
