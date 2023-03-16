import RPi.GPIO as GPIO
import time
from flask import Flask, jsonify, request

# Set the GPIO pin numbers
power_pin = 17
ground_pin = 18
reset_pin = 27
power_led_pin = 22

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(power_pin, GPIO.OUT)
GPIO.setup(ground_pin, GPIO.OUT)
GPIO.setup(reset_pin, GPIO.OUT)
GPIO.setup(power_led_pin, GPIO.IN)

# Initialize the Flask app
app = Flask(__name__)


# Define the endpoints
@app.route('/poweron', methods=['POST'])
def poweron():
    # Turn on the PC
    GPIO.output(power_pin, GPIO.LOW)
    time.sleep(0.5)  # Hold the power button for half a second
    GPIO.output(power_pin, GPIO.HIGH)
    return jsonify({'status': 'success', 'message': 'PC turned on'})


@app.route('/poweroff', methods=['POST'])
def poweroff():
    # Turn off the PC
    GPIO.output(power_pin, GPIO.LOW)
    time.sleep(4)  # Hold the power button for 5 seconds
    GPIO.output(power_pin, GPIO.HIGH)
    return jsonify({'status': 'success', 'message': 'PC turned off'})


@app.route('/reset', methods=['POST'])
def reset():
    # Trigger the reset button on the motherboard
    GPIO.output(reset_pin, GPIO.LOW)
    time.sleep(0.5)  # Hold the reset button for half a second
    GPIO.output(reset_pin, GPIO.HIGH)
    return jsonify({'status': 'success', 'message': 'PC reset'})


@app.route('/status', methods=['GET'])
def status():
    # Read the power pin to check if the PC is on or off
    power_status = GPIO.input(power_led_pin)
    return jsonify({'status': 'success', 'message': 'PC status', 'power_on': bool(power_status)})


# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# Clean up the GPIO pins
GPIO.cleanup()
