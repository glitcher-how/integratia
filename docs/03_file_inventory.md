# 03. Инвентаризация файлов

Ниже перечислено, где смотреть подробный состав проекта.

## Основные ссылки
- `references/broker_tree.md`
- `references/sdk_tree.md`
- `references/systems_tree.md`
- `references/tests_tree.md`
- `references/scripts_tree.md`
- `references/docker_tree.md`
- `references/docs_tree.md`
- `references/full_file_index.txt`

## Что обязательно показать проверяющему

### Брокер и миграция на MQTT
- `broker/mqtt/mqtt_system_bus.py`
- `broker/src/bus_factory.py`
- `broker/src/system_bus.py`

### Core tests
- `tests/unit/test_broker_config.py`
- `tests/unit/test_broker_factory.py`
- `tests/integration/test_broker_integration.py`
- `tests/e2e/test_e2e_scenario.py`
- `tests/e2e/conftest.py`

### Основные бизнес-системы
- `systems/agregator/src/gateway/src/gateway.py`
- `systems/agregator/src/agregator_component/src/agregator_component.py`
- `systems/regulator/src/regulator_component/src/regulator_component.py`
- `systems/insurer/src/insurer_component/src/insurer_component.py`
- `systems/drone_port/src/...`

## Комментарий

Полный индекс вынесен в `references/`, чтобы основной пакет оставался читаемым и пригодным для сдачи.
