# ⛳ Golf Ball Detector

YOLO 객체 탐지 모델을 활용하여 이미지와 영상 속 골프공을 탐지하는  
컴퓨터 비전 프로젝트입니다.

사용자 정의 골프공 데이터셋으로 YOLO 모델을 학습하고,  
학습된 모델을 이용해 골프공의 위치를 바운딩 박스로 표시하도록 구현했습니다.

---

## 📌 Project Overview

골프공은 크기가 작고 주변 배경과 색상이 비슷한 경우가 많아  
일반적인 객체보다 탐지가 어려울 수 있습니다.

이 프로젝트는 다양한 촬영 환경에서 골프공을 탐지할 수 있도록  
사용자 정의 데이터셋을 구축하고 YOLO 객체 탐지 모델을 학습하는 것을 목표로 합니다.

학습된 모델을 활용하여 이미지 또는 영상에서 골프공을 탐지하고,  
탐지 위치와 신뢰도 점수를 확인할 수 있습니다.

---

## ✨ Main Features

- 사용자 정의 골프공 데이터셋 구성
- YOLO 기반 객체 탐지 모델 학습
- 이미지 속 골프공 위치 탐지
- 영상 프레임 단위 골프공 탐지
- 탐지 결과 바운딩 박스 표시
- Confidence Score 기반 탐지 결과 확인
- 학습 결과 및 추론 결과 저장
- 모델 성능 지표 확인

---

## 🛠 Tech Stack

### AI & Computer Vision

<p>
  <img src="https://img.shields.io/badge/YOLO-111F68?style=flat-square&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Ultralytics-111827?style=flat-square&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white"/>
</p>

### Language

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/>
</p>

### Development Tools

<p>
  <img src="https://img.shields.io/badge/PyCharm-000000?style=flat-square&logo=pycharm&logoColor=white"/>
  <img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white"/>
  <img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white"/>
</p>

---

## 🔄 Model Development Flow

```text
골프공 이미지 수집
        ↓
이미지 라벨링
        ↓
학습·검증 데이터 분리
        ↓
데이터셋 설정 파일 작성
        ↓
YOLO 모델 학습
        ↓
모델 성능 평가
        ↓
이미지 및 영상 추론
        ↓
탐지 결과 분석
```

---

## 📁 Recommended Project Structure

```text
GolfBallDetector/
├── README.md
├── requirements.txt
├── data.yaml
├── epochs.py
├── datasets/
│   ├── train/
│   │   ├── images/
│   │   └── labels/
│   └── valid/
│       ├── images/
│       └── labels/
├── results/
└── weights/
```

데이터셋과 학습 모델 파일은 용량이 클 수 있으므로  
GitHub 저장소에 직접 포함하지 않을 수 있습니다.

---

## 🚀 Getting Started

### 1. 저장소 복제

```bash
git clone https://github.com/dongseop9907/GolfBallDetector.git
cd GolfBallDetector
```

### 2. 가상환경 생성

Windows 기준:

```bash
python -m venv .venv
.venv\Scripts\activate
```

macOS 또는 Linux 기준:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. 필수 패키지 설치

```bash
pip install ultralytics opencv-python
```

`requirements.txt`가 있는 경우 다음 명령어를 사용할 수 있습니다.

```bash
pip install -r requirements.txt
```

### 4. 데이터셋 경로 설정

`data.yaml` 파일에서 학습 및 검증 데이터셋 경로를  
현재 실행 환경에 맞게 설정합니다.

```yaml
path: ./datasets
train: train/images
val: valid/images

names:
  0: golf-ball
```

개인 컴퓨터의 절대 경로 대신 프로젝트 기준 상대 경로를 사용하는 것을 권장합니다.

### 5. 모델 학습

```bash
python epochs.py
```

또는 Ultralytics CLI를 이용하여 학습할 수 있습니다.

```bash
yolo detect train data=data.yaml model=yolov8n.pt epochs=100 imgsz=640
```

### 6. 이미지 객체 탐지

```bash
yolo predict model=weights/best.pt source=sample.jpg
```

### 7. 영상 객체 탐지

```bash
yolo predict model=weights/best.pt source=sample.mp4
```

탐지 결과는 기본적으로 `runs/detect/predict` 경로에 저장됩니다.

---

## 📊 Model Evaluation

모델 성능은 다음 지표를 기준으로 평가합니다.

- Precision
- Recall
- mAP50
- mAP50-95
- Training Loss
- Validation Loss

| Metric | Result |
|---|---:|
| Precision | 추후 추가 |
| Recall | 추후 추가 |
| mAP50 | 추후 추가 |
| mAP50-95 | 추후 추가 |

학습 완료 후 생성되는 결과 파일을 확인하여  
실제 성능 지표를 README에 추가할 예정입니다.

---

## 🖼 Detection Results

학습된 YOLO 모델을 이용하여 검증 이미지에서 골프공을 탐지한 결과입니다.

<p align="center">
  <img src="./assets/detection-result.jpg" width="750"/>
</p>

모델은 잔디, 실내 및 다중 객체 환경에서 골프공의 위치를  
바운딩 박스와 Confidence Score로 표시합니다.

```text
results/
├── detection-result-01.jpg
├── detection-result-02.jpg
└── detection-video.mp4
```

---

## ⚠️ Model Files

학습된 모델 파일인 `.pt` 파일은 용량이 클 수 있기 때문에  
GitHub 저장소에 직접 포함하지 않습니다.

특히 GitHub는 일반 파일 하나의 용량이 100MB를 초과하면  
일반적인 방식으로 업로드할 수 없습니다.

모델 파일을 공개할 경우 다음 방법을 사용할 수 있습니다.

- GitHub Releases
- Google Drive
- Hugging Face
- 외부 파일 다운로드 링크

다음 파일과 폴더는 `.gitignore`에 추가하는 것을 권장합니다.

```gitignore
.venv/
.idea/
__pycache__/
*.pyc
*.pt
runs/
datasets/
```

---

## 👨‍💻 My Role

- 골프공 이미지 데이터 수집
- 골프공 객체 라벨링
- 학습 및 검증 데이터셋 구성
- YOLO 모델 학습
- 학습 파라미터 설정
- 이미지 및 영상 추론
- 탐지 결과 분석
- 모델 성능 지표 확인
- GitHub 프로젝트 구조 정리

---

## 💡 Troubleshooting

### 모델 파일을 찾을 수 없는 경우

`model`에 입력한 경로에 실제 `.pt` 파일이 존재하는지 확인합니다.

```bash
yolo predict model=weights/best.pt source=sample.jpg
```

### 데이터셋 경로 오류가 발생하는 경우

`data.yaml` 안의 경로가 실제 데이터셋 폴더와 일치하는지 확인합니다.

가능하면 다음과 같은 개인 컴퓨터 절대 경로는 사용하지 않습니다.

```text
C:/Users/user/Desktop/...
```

프로젝트를 다른 환경에서도 실행할 수 있도록 상대 경로를 사용합니다.

```text
./datasets/train/images
```

### GitHub 업로드 용량 오류가 발생하는 경우

`.pt`, `runs`, 데이터셋 압축 파일 등 대용량 파일을 Git 추적 대상에서 제거해야 합니다.

```bash
git rm --cached 파일명
```

이후 `.gitignore`에 해당 파일 또는 폴더를 추가합니다.

---

## 📚 Future Improvements

- 데이터셋 이미지 수 확대
- 촬영 거리와 조명 환경 다양화
- 작은 객체 탐지 성능 개선
- 모델 성능 지표 추가
- 골프공 탐지 결과 이미지 추가
- 실시간 카메라 탐지 기능 구현
- 모바일 애플리케이션 연동
- 골프공 이동 경로 추적 기능 구현
- 탐지 모델 경량화 및 배포
