import cv2
from ultralytics import YOLO

# Load the model
model = YOLO("best.pt")

# Track with persistence (required for object ID tracking)
results = model.track(
    source="15sec_input_720p.mp4",
    persist=True,
    save=False  # We'll handle custom drawing
)

# Get video properties from first frame
first_frame = results[0].orig_img
height, width = first_frame.shape[:2]

# Define VideoWriter
out = cv2.VideoWriter("output_class1_tracked.mp4", cv2.VideoWriter_fourcc(*'mp4v'), 30, (width, height))

# Loop over frames and draw only class 1, no confidence
for result in results:
    frame = result.orig_img.copy()
    boxes = result.boxes

    for box in boxes:
        cls_id = int(box.cls[0])
        if cls_id != 2:  # only class 1
            continue

        x1, y1, x2, y2 = map(int, box.xyxy[0])
        track_id = int(box.id[0]) if box.id is not None else -1

        label = f"ID {track_id}" if track_id != -1 else "Player"

        # Draw box and label (no score)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, label, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    out.write(frame)

out.release()
print("Video saved as output_tracked.mp4")
