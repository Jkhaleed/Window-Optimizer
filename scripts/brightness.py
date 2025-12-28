# importing the module
import screen_brightness_control as sbc

def set_brightness(brightness):
    brightness = max(0, min(int(brightness), 100))
    sbc.set_brightness(brightness)

def get_brightness():
    return sbc.get_brightness()

