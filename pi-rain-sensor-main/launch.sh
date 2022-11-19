#!/usr/bin/env bash


echo "Performing environment setup..."
ORIGINAL_DIRECTORY="`pwd`"
LOCAL_DIRECTORY="`dirname ${0}`"
cd ${LOCAL_DIRECTORY}
LOG_FILE=./rainSensorLog.log
if [[ ! -f "$LOG_FILE" ]]; then
    touch ${LOG_FILE}
fi
chmod -R 757 ${LOG_FILE}
VENV_DIR=venv
if [[ ! -d "$VENV_DIR" ]]; then
    echo "$VENV_DIR directory not detected. Creating virtual environment..."
    virtualenv ${VENV_DIR}
fi
source ${VENV_DIR}/bin/activate
pip3 install -r requirements.txt


echo "Launching Pi Rain Sensor..."
python3 main.py


echo "Performing environment teardown..."
deactivate
cd ${ORIGINAL_DIRECTORY}
echo "Pi Rain Sensor terminated."
