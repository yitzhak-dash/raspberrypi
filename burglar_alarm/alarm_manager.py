class AlarmManager:
    def __init__(self, camera, notifier):
        self.camera = camera
        self.notifier = notifier
        print "alarm manager created."

    def movement_detected(self):
        print 'Movement detected!...'
        # self.camera.capture(1, 0.2)
        file_name = self.camera.rec(0, 5)
        self.notifier.notify(file_path=file_name)

    def dispose(self):
        self.camera.dispose()
