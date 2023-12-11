from flask import Flask, render_template
import time
from datetime import datetime


def trigger_safety_alert():
  print("Safety Alert: Safety-critical scenario detected!")
  # Simulate the safety alert action, e.g., turning on an LED


def reset_alert():
  print("Resetting safety alert.")
  # Simulate resetting the alert, e.g., turning off an LED


def log_alert():
  with open("safety_alert_log.txt", "a") as log_file:
    log_file.write(f"{datetime.now()}: Safety-critical scenario detected!\n")


# Simulate safety-critical scenario (e.g., triggered by a sensor)
def simulate_safety_critical_scenario():
  time.sleep(5)  # Simulate a delay before triggering the alert
  trigger_safety_alert()


try:
  while True:
    simulate_safety_critical_scenario()
except KeyboardInterrupt:
  print("Exiting the safety alert system.")

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/acknowledge', methods=['POST'])
def acknowledge_alert():
  reset_alert()
  return render_template('index.html', status='Alert Acknowledged')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
