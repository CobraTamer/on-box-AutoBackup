import cli
import time
#Function to save the running config using the built-in cli module
def save_running_config():
    try:
        cli.cli("copy running-config startup-config")
        print("Running configuration saved successfully.")
    except cli.CliError as e:
        print(f"Error saving running configuration: {e}")

while True:
    print("Initiated auto running config backup...")
    save_running_config()
    time.sleep(10800)  # save the running config every 3 hours (in seconds)

