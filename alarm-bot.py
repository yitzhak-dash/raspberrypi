import os
import subprocess
import time
import toml
import telepot
from telepot.loop import MessageLoop


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        # bot.sendMessage(chat_id, msg['text'])
        completed_video = 'video_3.h264'
        filename = 'video_test'
        command = "MP4Box -add {} {}.mp4".format(completed_video, os.path.splitext(filename)[0])
        try:
            output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        except subprocess.CalledProcessError as e:
            print('FAIL:\ncmd:{}\noutput:{}'.format(e.cmd, e.output))

        files = open("./video_test.mp4", 'rb')
        bot.sendVideo(chat_id, files)


config = toml.load('./config/default.toml')
print(str(config))

TOKEN = config['telegram']['token']

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)

