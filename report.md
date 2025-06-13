# 📊 Player Re-Identification – Assignment Report

## 👨‍💻 Author
Dishant Bothra

## 🎯 Objective

The goal of this assignment was to perform **player re-identification** within a single video feed using a custom-trained object detection model. The system must:

- Track players persistently across frames.
- Display **only a specific class** (e.g., players).
- Omit confidence scores.
- Generate an annotated output video.

---

## 🔍 Approach & Methodology

1. **Model Selection**:  
   Used a custom-trained YOLOv8 model (`best.pt`) tailored for detecting players in sports footage.

2. **Tracking Pipeline**:
   - Leveraged `ultralytics.YOLO.track()` with `persist=True` to maintain player IDs.
   - Iterated over results to filter for only class ID = 2.
   - Used OpenCV to draw bounding boxes and player IDs (no confidence).

3. **Output Generation**:
   - Video properties were derived from the first frame.
   - OpenCV’s `VideoWriter` was used to create the output video `output_class1_tracked.mp4`.

---

## 🧪 Techniques Tried & Outcomes

| Technique | Description | Outcome |
|----------|-------------|---------|
| YOLOv8 Tracking | Used `ultralytics` tracking with object ID persistence | Accurate, efficient |
| Class Filtering | Tracked only class ID `2` (assumed to be "player") | Reduced noise, focused output |
| Confidence Hiding | Skipped confidence display in visualization | Cleaner UI |
| ID Annotation | Each player boxed with unique ID | Useful for re-ID evaluation |

---

## 🚧 Challenges Encountered

1. **Class Mapping Confusion**  
   Initially needed to confirm which class ID corresponds to "player" in the dataset. Resolved via inspection.

2. **Path Hardcoding**  
   Original code used absolute paths (`/content/drive/...`). Refactored to use relative paths for portability.

3. **Video Output Frame Rate**  
   Matching FPS with the input video was essential to maintain smooth output. Defaulted to 30fps for simplicity.

---

## 🧩 Incomplete or Future Work

- **Dynamic Class Names**  
  Current implementation hardcodes class ID = 2. A more robust system would use class names from metadata.

- **Multi-Class Tracking Option**  
  Could allow toggling between classes or simultaneously tracking multiple (e.g., players + ball).

- **Stream Interface**  
  Real-time display or Streamlit integration for visual debugging and result playback.

- **Model Improvement**  
  Performance can improve with more annotated training data, fine-tuning, and potentially using ByteTrack for enhanced ID consistency.

---

## 🧠 Reflections

This was a practical, focused exercise in applying object detection for video analysis with real-world constraints. It showcased the balance between simplicity (clear visualization) and functionality (accurate re-identification).

---

## 📎 References

- [Ultralytics YOLOv8 Docs](https://docs.ultralytics.com/)
- [OpenCV VideoWriter](https://docs.opencv.org/4.x/dd/d9e/classcv_1_1VideoWriter.html)

