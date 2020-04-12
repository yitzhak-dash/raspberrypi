from picamera import PiCamera
from time import sleep


class Camera:
    def __init__(self):
        self.camera = PiCamera()
        self.count = 0

    def rec(self, before_wait_sec, rec_length_sec):
        self.count += 1
        file_name = '/home/pi/videos/video_{}.h264'.format(self.count)
        sleep(before_wait_sec)
        self.camera.start_recording(file_name)
        self.camera.wait_recording(rec_length_sec)
        self.camera.stop_recording()
        return file_name

    def capture(self, frame_count, wait_between_frames_sec):
        for i in range(frame_count):
            self.count += 1
            sleep(wait_between_frames_sec)
            self.camera.capture('/home/pi/photos/image_{}.jpg'.format(self.count))

    def dispose(self):
        self.camera.close()
