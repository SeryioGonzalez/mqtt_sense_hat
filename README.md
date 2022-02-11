# MQTT and SenseHat lab

The purpose of this lab is showing the functionality of an MQTT broker with an IoT device. <br/>
For the, we will use the free MQTT broker from HiveMQ and a Raspberry Pi with the SenseHat board<br/>
First, we will run a script to subscribe to a topic the broker. With other terminal, we will publish something to the previously subscribed topic and this message shall be displayed out of the command line <br/>
Then, we will run another script to display a message in the terminal.<br/>
Finally, we will integrate both scripts, so the message published to the topic is shown in the sense hat display. The logic is shown in the following image:<br/>
![Lab diagram](images/MQTT_1.jpg "Header Image")

## Clone the repo
The first thing you need to do is opening a terminal in your Raspberry Pi, as shown in the following image:<br/>
![Lab diagram](images/MQTT_2.png "Header Image")
