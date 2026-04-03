import json
import os
import time
import paho.mqtt.client as mqtt

MQTT_HOST = os.environ.get("MQTT_HOST", "localhost")
MQTT_PORT = int(os.environ.get("MQTT_PORT", "1883"))
MQTT_USER = os.environ.get("BROKER_USER") or os.environ.get("MQTT_USER") or "admin"
MQTT_PASSWORD = os.environ.get("BROKER_PASSWORD") or os.environ.get("MQTT_PASSWORD") or "admin_secret_123"
TOPIC = "systems.gcs"


def on_connect(client, userdata, flags, reason_code, properties=None):
    print("fake_gcs_mqtt connected:", reason_code)
    client.subscribe(TOPIC, qos=1)


def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode("utf-8"))
        action = data.get("action")
        reply_to = data.get("reply_to")
        correlation_id = data.get("correlation_id")
        payload = data.get("payload") or {}
        if not reply_to or not correlation_id:
            return

        if action == "plan_mission_route":
            pickup = payload.get("pickup") or {"lat": 55.75, "lon": 37.62}
            dropoff = payload.get("dropoff") or {"lat": 55.80, "lon": 37.70}
            response = {
                "success": True,
                "correlation_id": correlation_id,
                "payload": {
                    "route": [
                        pickup,
                        {
                            "lat": round((pickup["lat"] + dropoff["lat"]) / 2, 6),
                            "lon": round((pickup["lon"] + dropoff["lon"]) / 2, 6),
                        },
                        dropoff,
                    ]
                },
            }
        else:
            response = {
                "success": True,
                "correlation_id": correlation_id,
                "payload": {},
            }

        client.publish(reply_to, json.dumps(response), qos=1)
    except Exception as exc:
        print("fake_gcs_mqtt error:", exc)


client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
client.username_pw_set(MQTT_USER, MQTT_PASSWORD)
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_HOST, MQTT_PORT, keepalive=60)
client.loop_start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass
finally:
    client.loop_stop()
    client.disconnect()
