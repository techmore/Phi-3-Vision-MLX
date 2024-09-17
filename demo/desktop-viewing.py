from phi_3_vision_mlx import generate
from phi_3_vision_mlx import Agent
from PIL import ImageGrab
import time

# Create an instance of the Agent
agent = Agent()

def take_screenshot_and_describe():
    # Take a screenshot
    screenshot = ImageGrab.grab()

    # Save the screenshot locally
    screenshot_path = "/Users/sdolbec/Desktop/vision.png"
    screenshot.save(screenshot_path)

    # Feed the screenshot to the agent for analysis
    description = agent('Describe this image:', screenshot_path)
    
    # Print the description for validation
    print(f"Screenshot Description: {description}")

    # Return description for further use if needed
    return description

def loop_screenshots(interval_seconds=10):
    try:
        while True:
            # Take a screenshot, feed it to the agent and describe it
            take_screenshot_and_describe()
            
            # Wait for a given interval before taking another screenshot
            time.sleep(interval_seconds)

    except KeyboardInterrupt:
        # Stop the loop when interrupted (e.g., with Ctrl+C)
        print("Stopped screenshot loop.")
        agent.end()  # End the conversation and clear memory

# Start the loop to take screenshots every 10 seconds
loop_screenshots(interval_seconds=10)
