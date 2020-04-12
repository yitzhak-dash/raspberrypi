import os
import subprocess
import time
import toml
import telepot
from telepot.loop import MessageLoop
from burglar_alarm.motion_detector import MotionDetector
from burglar_alarm.alarm_manager import AlarmManager
from burglar_alarm.output_modules.camera import Camera
from burglar_alarm.notifiers.telegram_notifier import TelegramNotifier


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    command = msg['text']
    # create detector
    motion_detector = MotionDetector(AlarmManager(Camera(), TelegramNotifier(bot=bot, chat_id=chat_id)))

    if command == '/start_alarm':
        motion_detector.setup()
        try:
            motion_detector.loop()
        except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
            motion_detector.destroy()
    elif command == '/stop_alarm':
        motion_detector.destroy()


config = toml.load('./config/default.toml')
TOKEN = config['telegram']['token']


def send_message(msg):
    bot.sendMessage(config['telegram']['chat_id'], msg)


if __name__ == '__main__':
    bot = telepot.Bot(TOKEN)
    MessageLoop(bot, handle).run_as_thread()
    print ('Listening ...')
    send_message('We are looking for you...')

    # Keep the program running.
    while 1:
        time.sleep(10)
