# Virtual-Drawing

![Demo GIF](demo.gif)

This project utilizes OpenCV in Python to create a virtual paint application that allows users to draw in real-time using colored objects detected by a webcam. The application identifies specific colors and tracks their movement, translating it into drawing strokes on the screen.


## ColorPicker.py

### Description
ColorPicker.py is a real-time color selection tool using HSV trackbars. It captures video from a webcam and allows users to define a color range in the HSV color space, highlighting those colors in the live video feed.

### Features
- Adjust HSV trackbars to define color ranges dynamically.
- Visualize the original video feed, mask, and resulting image with selected colors highlighted.
  
### Requirements
- Python 3.x
- OpenCV (cv2)
- NumPy

### Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo

2.  Install dependencies:
     ```bash
      pip install -r requirements.txt
3.  Run ColorPicker.py:
   ```bash
      python ColorPicker.py
```
4. Adjust trackbars in the GUI window to select different color ranges. The application will display the live video feed with selected colors highlighted.



## VirtualPaint.py

### Description
VirtualPaint.py turns a webcam into a virtual painting canvas. It detects predefined colors in the video feed and enables users to **paint** in real-time by moving those colors within the camera's view.

### Features
- Detect and track predefined colors based on HSV ranges.
- Create strokes based on detected colors, allowing for dynamic painting.
- Adjust brush thickness interactively.
  
### Requirements
- Python 3.x
- OpenCV (cv2)
- NumPy

### Usage
1. Ensure your webcam is set up in a well-lit environment.

2.  Customize **myColors** list in VirtualPaint.py to include HSV ranges for colors to detect.
3.  Run VirtualPaint.py:
   ```bash
      python VirtualPaint.py

```
4. Move the selected colors (e.g., markers) in front of the webcam to paint on the virtual canvas in real-time.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

   
