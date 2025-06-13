# Player Re-Identification and Tracking

This project implements a player re-identification system using a custom-trained YOLOv8 model. The system tracks only a specific object class (e.g., players) from a video, assigns persistent IDs, and removes confidence scores from the visual output.

---

## 📁 Files

- `main.py`: Python script to perform tracking and generate annotated video.
- `best.pt`: YOLOv8 model trained to detect players (not included — place in root directory).
- `input_video.mp4`: Sample input video file (not included — place in root directory).
- `output_class1_tracked.mp4`: Output video with bounding boxes and tracking IDs.
- `requirements.txt`: List of Python dependencies.

---

## 🔧 Setup & Running Instructions

### 1. Install Dependencies

Use pip to install required packages:

```bash
pip install -r requirements.txt
````

### 2. Prepare Files

Place the following files in the root folder:

* `best.pt`: Your trained YOLO model.
* `input_video.mp4`: The video you want to process.

### 3. Run the Script

```bash
python main.py
```

The output will be saved as `output_class1_tracked.mp4`.

---

## ✅ Features

* Tracks only **class ID 2** (changeable in `main.py`).
* Removes confidence scores from output.
* Assigns unique IDs to track players across frames.
* Saves annotated video with bounding boxes and IDs.

---

## ⚙️ Requirements

* Python 3.8+
* [Ultralytics YOLO](https://docs.ultralytics.com/)
* OpenCV

Install via:

```bash
pip install ultralytics opencv-python
```

---

## 📌 Notes

* Make sure `best.pt` and `input_video.mp4` are in the same folder as `main.py`.
* Modify `cls_id != 2` in the script if your player class has a different ID.

---

## 📬 Contact

For any issues, feel free to reach out via the repository or email.

