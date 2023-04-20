# Practicing Car_Smog_detect

This project is designed to detect whether the car produces excessive smog on the roed. We mainly use opencv to realize image processing and pyqt to design a UI surface. What I've learned so far can only make it work on local video. This project will get improved in the future with more learning in image processing. 

Here's the sample video https://reurl.cc/9VA408 and demo video https://youtu.be/yk0oV3okW8k

## Introduction
This is our UI surface. You can follow the steps to easily complete reporting.
1. Input the video file and start analyzing.
2. Select the vehicle in the list to grab the info on the web. The system will show them in the table below.
3. The button on the right-hand side can play, stop and restart the video clip.

![測試](https://github.com/dabanshaw/smog_detect_project/blob/master/UI_surface.png "result")

## Algorithm


By uploading the sample video on the platform, the system detects the vehicles in the video and check whether it produces excessive smog. 

![測試](https://github.com/dabanshaw/smog_detect_project/blob/master/smog.jpeg "result")






## requirement
| Package       | Version       |
| ------------- |:-------------:|
| Python        | 3.8.12        |
| opencv        | 4.3.0        |
| pyqt          | 5.15.7        |
| webdriver-manager| 3.8.3      |
| selenium | 4.5.0        |



