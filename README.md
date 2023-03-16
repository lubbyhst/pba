# pba
Power-Button-Api

Simple API to control your PC with a raspberry pi. The API provides functions for pwr and reset button press and return 
on/off state.

## Prerequisites

Installed python3 and pip

## Install requirements

```bash
pip3 install -r requirements.txt 
```
## Install Systemd service
```bash
chmod +x install.sh
sudo ./install.sh
```

## Available endpoints

#### power on
```bash
curl -X PUT http://127.0.0.1/poweron
```
Response:
```json
{
  "status": "success",
  "message": "PC turned on"
}
```
#### power off
```bash
curl -X PUT http://127.0.0.1/poweroff
```
Response:
```json
{
  "status": "success",
  "message": "PC turned off"
}
```
#### reset
```bash
curl -X PUT http://127.0.0.1/reset
```
Response:
```json
{
  "status": "success",
  "message": "PC reset"
}
```
#### status
```bash
curl -X GET http://127.0.0.1/status
```
Response:
```json
{
  "status": "success",
  "message": "PC status",
  "power_on": 1
}
```