# 02. Карта систем и их назначение

## 2.1 Core platform

### `broker/`
Абстракция системной шины. Содержит реализации для Kafka и MQTT.

Ключевые файлы:
- `broker/config.py` — чтение конфигурации брокера;
- `broker/src/system_bus.py` — общий интерфейс шины;
- `broker/src/bus_factory.py` — выбор нужной реализации по env;
- `broker/kafka/kafka_system_bus.py` — Kafka bus;
- `broker/mqtt/mqtt_system_bus.py` — MQTT bus.

### `sdk/`
Базовые классы для систем и компонентов.

Ключевые файлы:
- `sdk/base_component.py` — базовый компонент;
- `sdk/base_gateway.py` — шлюз системы;
- `sdk/base_system.py` — базовая система;
- `sdk/messages.py` — структура сообщений;
- `sdk/safe_bus.py` — защищённая обёртка над шиной;
- `sdk/analytics_journal.py` — журналирование событий.

## 2.2 Системы проекта

### `systems/agregator/`
Бизнес-фасад для заказов, операторов, клиентов и заказов.

Состав:
- `src/agregator_component/` — бизнес-логика агрегатора;
- `src/gateway/` — REST gateway;
- `tests/test_unit.py` — unit-тесты агрегатора.

### `systems/insurer/`
Страховой контур.

Состав:
- `src/insurer_component/` — бизнес-логика страховой;
- `src/gateway/` — API / gateway;
- `tests/test_unit.py` — unit-тесты.

### `systems/regulator/`
Регуляторный контур: регистрация систем, сертификатов и валидации.

Состав:
- `src/regulator_component/` — логика регистрации и проверки;
- `src/gateway/` — gateway/HTTP слой.

### `systems/drone_port/`
Подсистема дронопорта.

Состав:
- `src/charging_manager/` — управление зарядкой;
- `src/drone_manager/` — управление дроном;
- `src/drone_registry/` — реестр дронов;
- `src/orchestrator/` — оркестрация;
- `src/port_manager/` — управление портом;
- `src/state_store/` — состояние и хранилище.

### `systems/dummy_system/`
Тестовая/демонстрационная система.

Состав:
- `src/dummy_component_a/`
- `src/dummy_component_b/`
- `src/gateway/`

### `systems/DroneAnalytics/`
В исходном архиве неполная. Для E2E использовалась mock-реализация backend + init-elastic.

### Внешние подключаемые системы
В исходном проекте ожидались внешние каталоги через symlink/submodule:
- `systems/gcs`
- `systems/operator`
- `systems/orvd_system`

Для учебного демонстрационного E2E использовались:
- реальные директории, скопированные из vendor-путей, если доступны;
- либо mock-реализации для недостающих endpoint/handlers.
