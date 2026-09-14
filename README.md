# Face Detection and Blurring

A Python application that detects faces with MediaPipe and applies a strong blur to each detected face. It can process a single image, a video file, or a live webcam stream.

## Features

- Detects faces with MediaPipe Face Detection.
- Blurs detected faces using OpenCV.
- Supports image, video, and webcam input.
- Saves processed image and video files in the `output/` directory.

## Requirements

- Python 3.8 or newer
- A webcam for webcam mode
- OpenCV and MediaPipe

Install the Python dependencies:

```bash
python -m pip install -r requirements.txt
```

## Usage

Run the script from the project directory.

### Webcam

Webcam mode is the default and uses camera index `0`:

```bash
python main.py
```

You can also specify the mode explicitly:

```bash
python main.py --mode webcam
```

The processed webcam stream is displayed in an OpenCV window. Interrupt the process from the terminal to stop it.

### Image

Pass an image path with `--filepath`:

```bash
python main.py --mode image --filepath data/input.jpg
```

The blurred image is saved as:

```text
output/output.png
```

### Video

Pass a video path with `--filepath`:

```bash
python main.py --mode video --filepath data/input.mp4
```

The processed video is saved as:

```text
output/output.mp4
```

## How It Works

1. OpenCV reads a frame from the selected input source.
2. MediaPipe detects faces and returns relative bounding boxes.
3. Each bounding box is converted to pixel coordinates.
4. OpenCV applies a blur to each face region.
5. The result is displayed or saved, depending on the selected mode.

## Project Structure

```text
FaceDetection&Blurring/
├── main.py            # Application entry point
├── requirements.txt   # Python dependencies
├── data/              # Input files can be stored here
├── output/            # Generated image and video files
└── README.md          # Project documentation
```

## Notes

- Image and video modes require `--filepath`.
- Image output always uses the filename `output/output.png`.
- Video output always uses the filename `output/output.mp4`.
- Existing output files with those names are overwritten.
- The script uses MediaPipe's default face detection model with a minimum detection confidence of `0.5`.
