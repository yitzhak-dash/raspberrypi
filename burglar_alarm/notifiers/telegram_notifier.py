import os
import subprocess


class TelegramNotifier:
    def __init__(self, bot, chat_id):
        self.chat_id = chat_id
        self.bot = bot

    def notify(self, file_path):
        command = "MP4Box -add {} {}.mp4".format(file_path, os.path.splitext(file_path)[0])
        try:
            output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        except subprocess.CalledProcessError as e:
            print('FAIL:\ncmd:{}\noutput:{}'.format(e.cmd, e.output))

        files = open("./video_test.mp4", 'rb')
        self.bot.sendVideo(self.chat_id, files)
