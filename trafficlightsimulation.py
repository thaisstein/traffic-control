import time
import os

countdown_time = 5  # Initial countdown time

def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def draw_traffic_light(color):
    clear_screen()
    print(f"{color.capitalize()} light: 🚦")

def countdown_timer(light_color, seconds):
    global countdown_time  # Use the global variable
    while seconds > 0:
        clear_screen()
        draw_traffic_light(light_color)
        print(f"Time Left: {seconds} seconds", end='\r')
        time.sleep(1)
        seconds -= 1
    countdown_time = 4  # Reset countdown to 3 after finishing

def start_traffic_light_simulation():
    while True:
        countdown_timer('Green', countdown_time)
        countdown_timer('Red', countdown_time)

if __name__ == "__main__":
    start_traffic_light_simulation()
