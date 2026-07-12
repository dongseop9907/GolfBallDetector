# ⛳ Golf Ball Detector

YOLO 객체 탐지 모델을 활용하여 이미지와 영상 속 골프공을 탐지하는  
컴퓨터 비전 프로젝트입니다.

사용자 정의 골프공 데이터셋을 학습하고,  
학습된 모델을 이용해 골프공의 위치를 바운딩 박스로 표시하도록 구현했습니다.

---

## 📌 Project Overview

골프공은 크기가 작고 배경과 색상이 비슷한 경우가 많아  
일반적인 객체보다 탐지가 어려울 수 있습니다.

이 프로젝트에서는 YOLO 기반 객체 탐지 모델을 활용하여  
다양한 환경의 이미지에서 골프공을 탐지하는 것을 목표로 했습니다.

---

## ✨ Main Features

- 사용자 정의 골프공 데이터셋 학습
- YOLO 기반 객체 탐지
- 이미지 속 골프공 위치 검출
- 영상 프레임 단위 골프공 탐지
- 학습 결과 및 탐지 결과 저장
- Confidence Score 기반 탐지 결과 확인

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
YOLO 모델 학습
        ↓
학습 결과 평가
        ↓
이미지 및 영상 추론

