# Create three function
def red_light():
    print(f'Stop! The light is red.')

def yellow_light():
    print(f'Caution! The light is yellow.')

def green_light():
    print(f'Go! The light is green.')

# Create function to control traffic light
def traffic_light(state):
    if state == "red":
        red_light()
    elif state == "yellow":
        yellow_light()
    elif state == "green":
        green_light()
    else:
        print(f'Invalid State Error.')

# Call the traffic_light function, including invalid state
traffic_light("red")
traffic_light("green")
traffic_light("yellow")
traffic_light("tangerine")