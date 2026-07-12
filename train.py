"""Train a YOLO model for golf-ball detection."""

from __future__ import annotations

import argparse
from pathlib import Path

import torch
from ultralytics import YOLO


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(
        description="Train a YOLO model on a custom golf-ball dataset."
    )

    parser.add_argument(
        "--data",
        type=Path,
        default=Path("data.yaml"),
        help="Path to the dataset YAML file. Default: data.yaml",
    )

    parser.add_argument(
        "--model",
        type=str,
        default="yolov8m.pt",
        help="Initial YOLO model or weight file. Default: yolov8m.pt",
    )

    parser.add_argument(
        "--epochs",
        type=int,
        default=100,
        help="Number of training epochs. Default: 100",
    )

    parser.add_argument(
        "--imgsz",
        type=int,
        default=640,
        help="Training image size. Default: 640",
    )

    parser.add_argument(
        "--batch",
        type=int,
        default=16,
        help="Training batch size. Default: 16",
    )

    parser.add_argument(
        "--workers",
        type=int,
        default=8,
        help="Number of data-loading workers. Default: 8",
    )

    parser.add_argument(
        "--project",
        type=Path,
        default=Path("runs/detect"),
        help="Directory in which training results are saved.",
    )

    parser.add_argument(
        "--name",
        type=str,
        default="golf-ball",
        help="Name of the training run. Default: golf-ball",
    )

    return parser.parse_args()


def main() -> None:
    """Load the model and start training."""

    args = parse_args()

    if not args.data.exists():
        raise FileNotFoundError(
            f"Dataset configuration file was not found: {args.data.resolve()}"
        )

    device = 0 if torch.cuda.is_available() else "cpu"

    print(f"Dataset: {args.data.resolve()}")
    print(f"Model: {args.model}")
    print(f"Device: {'CUDA GPU' if device == 0 else 'CPU'}")

    model = YOLO(args.model)

    model.train(
        data=str(args.data),
        epochs=args.epochs,
        imgsz=args.imgsz,
        batch=args.batch,
        workers=args.workers,
        device=device,
        project=str(args.project),
        name=args.name,
        augment=True,
    )


if __name__ == "__main__":
    main()