"""Run golf-ball detection using a trained YOLO model."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Union
from urllib.parse import urlparse

from ultralytics import YOLO


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(
        description="Detect golf balls in an image, video, folder, URL, or webcam."
    )

    parser.add_argument(
        "--weights",
        type=Path,
        default=Path("weights/best.pt"),
        help="Path to the trained YOLO model. Default: weights/best.pt",
    )

    parser.add_argument(
        "--source",
        type=str,
        required=True,
        help=(
            "Input image, video, directory, URL, or webcam number. "
            "Examples: sample.jpg, video.mp4, images/, or 0"
        ),
    )

    parser.add_argument(
        "--conf",
        type=float,
        default=0.25,
        help="Minimum confidence threshold. Default: 0.25",
    )

    parser.add_argument(
        "--iou",
        type=float,
        default=0.7,
        help="IoU threshold for non-maximum suppression. Default: 0.7",
    )

    parser.add_argument(
        "--imgsz",
        type=int,
        default=640,
        help="Inference image size. Default: 640",
    )

    parser.add_argument(
        "--device",
        type=str,
        default=None,
        help="Inference device, such as 0, cpu, or cuda:0. Default: automatic",
    )

    parser.add_argument(
        "--project",
        type=Path,
        default=Path("runs/detect"),
        help="Directory in which prediction results are saved.",
    )

    parser.add_argument(
        "--name",
        type=str,
        default="golf-ball-predict",
        help="Name of the prediction run.",
    )

    parser.add_argument(
        "--show",
        action="store_true",
        help="Display the prediction result in a window.",
    )

    parser.add_argument(
        "--save-txt",
        action="store_true",
        help="Save detection labels as text files.",
    )

    parser.add_argument(
        "--save-conf",
        action="store_true",
        help="Include confidence scores in saved label files.",
    )

    return parser.parse_args()


def is_remote_source(source: str) -> bool:
    """Return True when the source is a supported remote URL or stream."""

    scheme = urlparse(source).scheme.lower()
    return scheme in {"http", "https", "rtsp", "rtmp", "tcp"}


def resolve_source(source: str) -> Union[str, int]:
    """Validate and normalize the prediction source."""

    # Webcam source: --source 0
    if source.isdigit():
        return int(source)

    # Remote image, video, or stream
    if is_remote_source(source):
        return source

    source_path = Path(source).expanduser()

    # Wildcard patterns may be interpreted by Ultralytics.
    contains_wildcard = any(character in source for character in ("*", "?", "["))

    if not source_path.exists() and not contains_wildcard:
        raise FileNotFoundError(
            "Prediction source was not found.\n"
            f"Checked path: {source_path.resolve()}"
        )

    return str(source_path)


def validate_args(args: argparse.Namespace) -> None:
    """Validate model and prediction arguments."""

    weights = args.weights.expanduser().resolve()

    if not weights.is_file():
        raise FileNotFoundError(
            "YOLO model file was not found.\n"
            f"Checked path: {weights}\n"
            "Use --weights to provide the correct best.pt path."
        )

    if weights.suffix.lower() != ".pt":
        raise ValueError(
            f"The model file must use the .pt extension: {weights}"
        )

    if not 0.0 <= args.conf <= 1.0:
        raise ValueError("--conf must be between 0.0 and 1.0.")

    if not 0.0 <= args.iou <= 1.0:
        raise ValueError("--iou must be between 0.0 and 1.0.")

    if args.imgsz <= 0:
        raise ValueError("--imgsz must be greater than 0.")


def main() -> None:
    """Load the model and run golf-ball detection."""

    args = parse_args()
    validate_args(args)

    weights = args.weights.expanduser().resolve()
    source = resolve_source(args.source)

    print(f"Model: {weights}")
    print(f"Source: {source}")
    print(f"Confidence threshold: {args.conf}")
    print(f"IoU threshold: {args.iou}")

    model = YOLO(str(weights))

    prediction_options = {
        "source": source,
        "conf": args.conf,
        "iou": args.iou,
        "imgsz": args.imgsz,
        "save": True,
        "show": args.show,
        "save_txt": args.save_txt,
        "save_conf": args.save_conf,
        "project": str(args.project),
        "name": args.name,
        "exist_ok": True,
        "verbose": True,
    }

    if args.device is not None:
        prediction_options["device"] = args.device

    results = model.predict(**prediction_options)

    detected_objects = sum(
        len(result.boxes)
        for result in results
        if result.boxes is not None
    )

    print(f"Processed results: {len(results)}")
    print(f"Detected objects: {detected_objects}")

    if results:
        print(f"Results saved to: {results[0].save_dir}")


if __name__ == "__main__":
    main()