class AlarmManager:
    def __init__(self, camera):
        self.camera = camera
        print "alarm manager created."

    def movement_detected(self):
        print 'Movement detected!...'
        # self.camera.capture(1, 0.2)
        self.camera.rec(0, 5)

    def dispose(self):
        self.camera.dispose()
