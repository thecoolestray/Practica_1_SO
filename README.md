Prcatica 1 - Bash y Python - extract dand visualize data from MQTT

Discription:
this reposotory contain a operating systems practice developped using Bash y Python 
the objective of this project is to autaumate the capturing, storing and visualizing of enviromental sensor data recieved from an MQTT broker
the QMTT subscriber prints the data directly into the terminal without storing it

the program solves this by:

capturing the program output autumatically
storing it in a log file
processing the data from the log file
extracts the JSON payload 
visualises the data as a png and a ACSII graph

the program uses multiple operating systems concepts such as:
process manigment 
monitoring processes
termination of processes
log processing and visualization using python
output redirection in bash

2. Repository structure






3. System Requirements
Operating system: Linux (tested on Ubuntu 22.04)
shell : bash
python : python 3

Required Python libraries
matplotlib
json` (standard Python library)

Install required libraries
in bash
pip install matplotlib

4. MQTT Data Topics
The system captures data from the following MQTT topics:
sensor/data/gas_sensor and sensor/data/sen55

Example MQTT output received from the subscriber program:
[MSG] Topic: sensor/data/sen55
Payload: {"MassConcentrationPm1p0":0.70,"AmbientTemperature":21.17,...}
The Bash script captures this output and stores it in a log file for later processing

5. Running the Project
1 Give execution permission to the Bash script
chmod +x capture_mqtt.sh
2 Run the capture script
./capture_mqtt.sh
3 Enter capture time (in seconds)
Example:
Enter capture time (seconds): 30

6. Program Execution Flow
1 the bash script executes the MQTT program
2 the programs output is directed to capture_mqtt.log
3 the script get the programs PID using $!
4.the script keeps checking if the program is still active using kill-0
5. after the chosen time the script stopes the program using :
SIGINT , SIGTERM ,SIGKILL (if nececarry)
6.the python code is executed automatically 

7.Python Data Processing
1 the script reads the mqtt_capture.log life
2 extracts the json payload data
3 parses sensor values
4 generates graphs of the stored data:
a png graph saved on /plots directory
a ASCII graph displayed directly in the terminal 

8. Example Output:
After running the program successfully, the following outputs are produced:
A log file containing captured MQTT messages
mqtt_capture.log

Generated graphs in the following directory:
plots/

An ASCII graph displayed in the terminal.

Example:




10. commen problems 
   
Python library not found
Install required library:
pip install matplotlib

Permission denied when running the script
Give execution permission:
chmod +x capture_mqtt.sh

MQTT executable not running
Ensure the MQTT subscriber executable is located in the project directory and has execution permission


10. Authors
naela
Operating Systems
Academic Year 2025–2026

11. Notes

This project was developed as part of an Operating Systems practical assignment focusing on automation, process control, and data visualization.












