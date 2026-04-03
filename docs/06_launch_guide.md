# 06. Руководство по запуску

## 6.1 Переменные окружения

```bash
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
```

## 6.2 Поднять compose-окружение

```bash
docker compose   -f .generated/e2e/docker-compose.yml   -f tests/e2e/analytics-compose.yml   --env-file .generated/e2e/.env   --profile mqtt up -d --build
```

## 6.3 Запустить mock-сервисы

### Окно 1 — HTTP mock GCS
```bash
python scripts/fake_gcs.py
```

### Окно 2 — MQTT mock GCS
```bash
python scripts/fake_gcs_mqtt.py
```

## 6.4 Запустить E2E

```bash
pytest tests/e2e/test_e2e_scenario.py -v -s
```

## 6.5 Показ на паре

### Большой прогон без проблемных внешних частей
```bash
pytest tests systems/drone_port/tests systems/dummy_system/tests systems/insurer/tests --ignore=systems/agregator/tests/test_unit.py --import-mode=importlib
```

### Финальный E2E
```bash
pytest tests/e2e/test_e2e_scenario.py -v -s
```
