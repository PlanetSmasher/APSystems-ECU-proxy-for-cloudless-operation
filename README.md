# APSystems-ECU-proxy-for-cloudless-operation

# Purpose
This short script should enable APSystems ECU users to work cloudless. 
Under normal circumstances, the ECU will stop functioning when apsystems.com domains are blocked. This Python 3 script causes the ECU to get fake responses (as if the response came from the EMA cloud).

It works very simply. Every five minutes the ECU sends data to ecu.apsystemsema.com alternately via port 8995 and 8996

The EMA site responds with a timestamp of the most recently received data (this is usually the recent data - 5 minutes). The ECU thinks it has fully updated the EMA site and has an internet connection with EMA.

# Why?
- Firmware updates are being pushed to my ECU-R without any notice or release notes 
- I want to prevent others from being able to shut down my PV installation (I own the hardware and want control over it)

---work in progress---
- how to use
