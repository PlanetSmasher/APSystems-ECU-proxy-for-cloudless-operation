# APSystems-ECU-proxy-for-cloudless-operation

# Description
This short script should enable APSystems ECU users to work cloudless. 
Under normal circumstances, the ECU will stop functioning when apsystems.com domains are blocked. This Python 3 script causes the ECU to get simulated responses (as if the response came from the EMA cloud).

Every five minutes the ECU sends recent data to ecu.apsystemsema.com alternately via port 8995 and 8996. These ports are opened for a short amount of time to await response and is then being closed again. So EMA site swiftly responds with a timestamp of the last received data (this is usually the recent data - 5 minutes) to the ECU. The ECU now knows it has fully synchronized with the EMA site and also is aware of having an internet connection with EMA.

# Why cloudless
- Firmware updates are being pushed to my ECU-R without any notice or release notes 
- I want to prevent others from being able to shut down my PV installation
- All parameters (even more than the EMA cloud holds) is present and is being read from the ECU
- Ability to privately own the produced data

# Disadvantage
- No large repository of historical data and (trend-)analysis

# How to use
1. DNS rewrite ecu.apsystemsema.com and ecu2.apsystemsema.com to a local host running this script (check if a ping to ecu.apsystemsema.com resolves to your host IP-address)
2. Block all (future) communication with APSystems
* apsystemsema.cn
* ecu.apsema.com
* ecu2.apsema.com
* ecu2.apsystems.com
* ...
3. You're done

# To Do
- Clean up code
- Add logging / monitoring
- Integrate with Home Assistant
- More testing (compatibility with ECU-C)
