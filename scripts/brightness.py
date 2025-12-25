# importing the module
import screen_brightness_control as sbc

def set_brightness(brightness):
    brightness = max(0, min(brightness, 100))
    sbc.set_brightness(brightness)
    
def get_brightness():
    return sbc.get_brightness()

if __name__ == "__main__":
	# get current brightness value
	current_brightness = get_brightness()
	print(current_brightness)

	choice = int(input("Enter a number between 0-100: "))
	if 0 <= choice <= 100:
		set_brightness(choice)
		print(f"Set brightness to {choice}")
	else:
		print("Invalid number. Must be 0-100.")