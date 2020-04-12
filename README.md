# raspberrypi
### Scan network
`nmap -sP 10.0.0.0/24`
### VNC
run on pi `sudo startx` to enable VNC

##
### Solution:
1. The telegram-bot(TB) manages a pi.
2. TB supports a few basic commands.
    1. start/stop burglar alarm
    2. ...  
3. When the burglar alarm was started the TB runs the `motion_detection` module.
4. `motion_detection` detects motions, once and motion was detected, the detector calls `alarm_manager`.
5. `alarm_manager` has different outputs, `modules` (camera, etc..) and used to react for detection(to alarm).
6. `alarm_manager` also has notifiers(email, telegram chat, etc...)
7. `modules` returns to `alarm_manager` products(in case of camera it will be path to recorded video file).
8. `alarm_manager` sends messages with products via notifiers.
#### Example:
Lets say the `detector` detects some motion and calls the `alarm manager` 
