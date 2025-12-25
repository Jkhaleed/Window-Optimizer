# importing the module
import screen_brightness_control as sbc

# get current brightness  value
current_brightness = sbc.get_brightness()
print(current_brightness)

choice = int(input("Enter a number between 0-100: "))
if 0 <= choice <= 100:
    sbc.set_brightness(choice)
    print(sbc.get_brightness())
else:
    print("Invalid number. Must be 0-100.")



