# FUNCTION ARGUMENTS

# 5 TYPES OF FUNCTION ARGUMENTS:

# 1. **Positional Arguments**

def display_weather(temp, humidity, wind_speed):
    print(f'Temparature => {temp}C, Humidity => {humidity}%, wind Speed => {wind_speed}km/h')

display_weather(22, 80, 30)

# 2. **Keyword (Named) Arguments** - Arguments that are explicitly named when passed.

# Using keyword arguments (order does not matter)
display_weather(temp=23, humidity=80, wind_speed=40)

# Mixing positional and keyword arguments (order still matters for positional)
display_weather(25, humidity=70, wind_speed=30)

display_weather(humidity=70, wind_speed=30, temp=23)

display_weather(25, humidity=70, wind_speed=30)

# 3. **Default Arguments**

def adjust_lightning(room, brightness=75, color_temp=4000):
    """Adjusts lighting settings for a given room."""
    print(f'Adjusting lighting in {room} to {brightness}% brightness and {color_temp}K color temp.')

adjust_lightning('Living Room')
adjust_lightning('Kitchen', 50, 3500)
adjust_lightning('Bedroom', brightness=40)



