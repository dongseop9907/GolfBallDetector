import cv2
from ultralytics import YOLO

# 모델 불러오기
model = YOLO("runs/train/exp/weights/best.pt")  # best.pt 모델 파일 경로

# 이미지 불러오기 (예: 이미지를 OpenCV로 읽기)
image_path = "path/to/your/image.jpg"
image = cv2.imread(image_path)

# YOLOv8 모델을 사용해 객체 감지
results = model(image)

# 감지된 결과에서 객체의 정보 추출 (예: bounding box, confidence score, 클래스 등)
boxes = results.boxes
labels = results.names  # 객체 클래스 이름
confidences = boxes.conf  # 객체 감지의 신뢰도

# 객체 감지된 이미지에 bounding box 그리기
for i, box in enumerate(boxes.xyxy):  # xyxy는 좌측 상단(x1, y1)과 우측 하단(x2, y2) 좌표
    x1, y1, x2, y2 = map(int, box)  # 좌표를 정수로 변환

    # 객체 이름과 신뢰도 표시 (예: "person 0.95")
    label = f"{labels[int(box[5])]} {confidences[i]:.2f}"

    # bounding box 그리기 (초록색)
    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # 레이블 텍스트 그리기 (파란색)
    cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

# 결과 이미지 출력
cv2.imshow("Detection", image)

# 결과 이미지 저장 (선택 사항)
cv2.imwrite("output_image.jpg", image)

# 키를 눌러 창 닫기
cv2.waitKey(0)
cv2.destroyAllWindows()
