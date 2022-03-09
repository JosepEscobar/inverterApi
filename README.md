# inverterApi - WIP

This project has been designed to take monitoring data from Voltronic, Axpert, Mppsolar PIP, Voltacon, Effekta. You will get a fully functional API to access your inverter from any API Client.

## Pre Requisites
- systemd installed in your system
- pyUSB installed
- sudo pip install tornado

## Start as a service
- Edit and Copy inverterApi.service into `/etc/systemd/system/`
- Execute `sudo systemctl daemon-reload` to reload daemon
- Execute `sudo systemctl enable inverterApi.service` to enable our service
- Execute `sudo systemctl start inverterApi.service` to start our new service! Lets go! 

## Endpoints
- /status/
- /configuration/
- /flag-status/