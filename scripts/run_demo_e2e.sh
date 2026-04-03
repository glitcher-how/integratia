#!/usr/bin/env bash
set -e

export PYTHONPATH=.
export BROKER_TYPE=mqtt
export MQTT_HOST=localhost
export MQTT_PORT=1883
export BROKER_USER=admin
export BROKER_PASSWORD=admin_secret_123
export MQTT_USER=admin
export MQTT_PASSWORD=admin_secret_123
export ADMIN_USER=admin
export ADMIN_PASSWORD=admin_secret_123
export PYTHONUTF8=1
export PYTHONIOENCODING=utf-8

pytest tests/e2e/test_e2e_scenario.py -v -s
