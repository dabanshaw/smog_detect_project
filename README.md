# Practicing Car_Smog_detect

This project is designed to detect whether the car produces excessive smog on the roed. We mainly use opencv to realize image processing and pyqt to design a UI surface.


## Introduction
This is our UI surface. You can follow the steps to easily complete reporting.
1. Input the video and start analyzing.
2. press the button to show which car is available to report.
3. pick a car to show its information. The play button can show the video of the car producing smog.
4. press "save" to save the information into excel. "Web_Link" directs to the reporting web.

## Algorithm

![測試](https://github.com/dabanshaw/smog_detect_project/blob/master/surface.jpeg "test")

This is the capture of sample video. We use opencv to realize image processing. 

![測試](https://github.com/dabanshaw/smog_detect_project/blob/master/sample.jpeg "test")

This is the video captrue after processing obejct detection. You can see the square on car, scooter and the smog.

![測試](https://github.com/dabanshaw/smog_detect_project/blob/master/object_detect.jpeg "test")

When the smog produced by the vehicle is excessive, it is tagged with bad, which is available to report.

![測試](https://github.com/dabanshaw/smog_detect_project/blob/master/smog.jpeg "test")



## requirement
Python 3.8.13
| Package       | Version       |
| ------------- |:-------------:|
| Python        | 3.8.13        |
| opencv        | 3.8.13        |
| pyqt          | 3.8.13        |
| webdriver-manager| 3.8.3      |
| beautifulsoup4| 4.11.1        |
| selenium | 3.141.0        |



# H1
## H2
### H3
#### H4
##### H5
###### H6
