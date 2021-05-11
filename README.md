# APSystems-ECU-proxy-for-cloudless-operation

# Purpose
This short script should enable APSystems ECU users to work cloudless. 
Under normal circumstances, the ECU will stop functioning when apsystems.com domains are blocked. This Python 3 script causes the ECU to get fake responses (as if the response came from the EMA cloud).

It works very simply. 
Every five minutes the ECU sends recent data to ecu.apsystemsema.com alternately via port 8995 and 8996
The EMA site responds with a timestamp of the last received data (this is usually the recent data - 5 minutes). The ECU now knows it has fully synchronized with the EMA site and has an internet connection with EMA.

# Why?
- Firmware updates are being pushed to my ECU-R without any notice or release notes 
- I want to prevent others from being able to shut down my PV installation
- Most data (even more than the EMA cloud holds) is present and being read from the ECU to be in control

# Disadvantage
- No large repository of historical data and analisys

# How to use
1. DNS rewrite ecu.apsystemsema.com to a local host running this script (check if a ping to ecu.apsystemsema.com resolves to your host IP-address)
2. You're done

# To Do
- Clean up code
- Add logging / monitoring
- Maybe integrate with the ECU-R Home Assistant integration
- More testing (compatibility with ECU-C)
