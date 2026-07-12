"""Resume an interrupted YOLO training run from a last.pt checkpoint."""

from __future__ import annotations

import argparse
from pathlib import Path

from ultralytics import YOLO


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(
        description="Resume YOLO training from an existing last.pt checkpoint."
    )

    parser.add_argument(
        "--checkpoint",
        type=Path,
        default=Path("runs/detect/golf-ball/weights/last.pt"),
        help=(
            "Path to the last.pt checkpoint. "
            "Default: runs/detect/golf-ball/weights/last.pt"
        ),
    )

    return parser.parse_args()


def main() -> None:
    """Load a checkpoint and resume the interrupted training run."""

    args = parse_args()
    checkpoint = args.checkpoint.expanduser().resolve()

    if not checkpoint.is_file():
        raise FileNotFoundError(
            "Training checkpoint was not found.\n"
            f"Checked path: {checkpoint}\n"
            "Use --checkpoint to provide the correct last.pt path."
        )

    print(f"Checkpoint: {checkpoint}")
    print("Resuming training...")

    model = YOLO(str(checkpoint))
    model.train(resume=True)


if __name__ == "__main__":
    main()