# pba
Power-Button-Api

Simple API to control your PC with a raspberry pi. The API provides functions for pwr and reset button press and return 
on/off state.

## Prerequisites

Installed python3 and pip3
```bash
sudo apt update
sudo apt install python3 python3-pip
```

## Install requirements

```bash
sudo pip3 install -r requirements.txt 
```
## Install Systemd service
```bash
chmod +x install.sh
sudo ./install.sh
```

## Available endpoints

#### power on
```bash
curl -X POST http://127.0.0.1:5000/poweron
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
curl -X POST http://127.0.0.1:5000/poweroff
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
curl -X POST http://127.0.0.1:5000/reset
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
curl -X GET http://127.0.0.1:5000/status
```
Response:
```json
{
  "status": "success",
  "message": "PC status",
  "power_on": "true"
}
```