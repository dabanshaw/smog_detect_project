import cv2

class opencv_engine(object):

    @staticmethod
    def point_float_to_int(point):
        return (int(point[0]), int(point[1]))

    @staticmethod
    def read_image(file_path):
        return cv2.imread(file_path)

    @staticmethod
    def getvideoinfo(video_path): 
        # https://docs.opencv.org/4.5.3/dc/d3d/videoio_8hpp.html
        videoinfo = {}
        vc = cv2.VideoCapture(video_path)
        videoinfo["vc"] = vc
        videoinfo["fps"] = vc.get(cv2.CAP_PROP_FPS) #讀取每秒偵數
        videoinfo["frame_count"] = int(vc.get(cv2.CAP_PROP_FRAME_COUNT))
        videoinfo["width"] = int(vc.get(cv2.CAP_PROP_FRAME_WIDTH))
        videoinfo["height"] = int(vc.get(cv2.CAP_PROP_FRAME_HEIGHT))
        return videoinfo