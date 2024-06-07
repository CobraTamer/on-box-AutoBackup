## On-Box-AutoBackup

## On-Box Appliocation : Automated Running config backups
Overview
Automatically backs saves the running configuration into startup config, every 3 hours
Key Features:
-Continues Automated Backups
-Runs on-box 
-Can also run as acontainer app on-box.


## Files

- `on-box-AutoBackup.py: Contains the on-box python script.

## Installation

1. Clone the repository:

    git clone https://github.com/CobraTamer/on-box-AutoBackup.git


## Usage


	1.	Access Your NX-OS Device:
	•	Open your terminal or SSH client (like PuTTY, SecureCRT, or a terminal emulator on Linux/Mac).
	•	Connect to your NX-OS device using SSH. Example:

ssh admin@your-nxos-device-ip


	2.	Enable Bash Shell:
	•	On the NX-OS device, enable the Bash shell to use Linux-like commands. Enter configuration mode and enable Bash:

conf t
feature bash-shell
exit
run bash


	3.	Create the Script:
	•	Use a text editor like vim to create the script file. Example:

vim AutoBackup.py

	3.	
	•	In vim, press i to enter insert mode, then copy and paste the script above into the editor.
	•	Press Esc, then type :wq and press Enter to save and exit.
	4.	Make the Script Executable:
	•	Change the permissions to make the script executable:

chmod +x Autobackup.py


	5.	Run the Script:
	•	Execute the script using Python, do this in NX-OS mode not bash:

python3 AutoBackup.py




## Example Output

When you run the app, the running-config is saved into the startup config every 3 hours. On execution, you should see the following on your terminal: 
"Initiated auto running config backup..."

When the script saves the running-config you will see output similar to this in your terminal:
"Running configuration saved successfully."
If an error occcurs, the following is displayed on your terminal: 
"Error saving running configuration: (error message)"

 