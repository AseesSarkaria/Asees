import os
import random
import uuid
from confluent_kafka import SerializingProducer
import simplejson as json
from datetime import datetime, timedelta
import time

###

LONDON_COORDINATES = {"latitude": 51.5074, "longitude": -0.1278}
BIRMINGHAM_COORDINATES = {"latitude": 52.4862, "longitude": -1.8904}

# Calculate movement increments
LATITUDE_INCREMENT = (BIRMINGHAM_COORDINATES['latitude'] - LONDON_COORDINATES['latitude']) / 100
LONGITUDE_INCREMENT = (BIRMINGHAM_COORDINATES['longitude'] - LONDON_COORDINATES['longitude']) / 100

# Environment Variables
KAFKA_BOOTSTRAP_SERVERS = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')
VEHICLE_TOPIC = os.getenv('VEHICLE_TOPIC', 'vehicle_data')
GPS_TOPIC = os.getenv('GPS_TOPIC', 'gps_data')
TRAFFIC_TOPIC = os.getenv('TRAFFIC_TOPIC', 'traffic_data')
WEATHER_TOPIC = os.getenv('WEATHER_TOPIC', 'weather_data')
EMERGENCY_TOPIC = os.getenv('EMERGENCY_TOPIC', 'emergency_data')

random.seed(42)
start_time = datetime.now()
start_location = LONDON_COORDINATES.copy()


def get_next_time():
    global start_time
    start_time += timedelta(seconds=random.randint(30, 60))
    return start_time


def generate_gps_data(device_id, timestamp, vehicle_type='private'):
    return {
        'id': uuid.uuid4()
        , 'device_id': device_id
        , 'timestamp': timestamp
        , 'speed': random.uniform(0, 40)  #km/h
        , 'direction': 'North-East'
        , 'vehicle_type': vehicle_type
    }


def generate_traffic_camera_data(device_id, location, timestamp, camera_id):
    return {
        'id': uuid.uuid4()
        , 'device_id': device_id
        , 'camera_id': camera_id
        , 'location': location
        , 'timestamp': timestamp
        , 'snapshot': 'Base64EncodedString'
    }


def generate_weather_data(device_id, timestamp, location):
    return {
        'id': uuid.uuid4()
        , 'device_id': device_id
        , 'location': location
        , 'timestamp': timestamp
        , 'temperature': random.uniform(-5, 26)  #celsius
        , 'weather_condition': random.choice(['Sunny', 'Cloudy', 'Rain', 'Snow'])
        , 'precipitation': random.uniform(0, 25)
        , 'wind_speed': random.uniform(0, 100)
        , 'humidity': random.randint(0, 100)
        , 'air_quality_index': random.uniform(0, 500)
    }


def generate_emergency_incident_data(device_id, timestamp, location):
    return {
        'id': uuid.uuid4()
        , 'device_id': device_id
        , 'incident_id': uuid.uuid4()
        , 'type': random.choice(['Accident', 'Fire', 'Medical', 'Police', 'Home'])
        , 'timestamp': timestamp
        , 'location': location
        , 'status': random.choice(['Active', 'Resolved'])
        , 'description': 'Description of the incident'
    }


def simulate_vehicle_movement():
    global start_location

    # moving towards birmingham
    start_location['latitude'] += LATITUDE_INCREMENT
    start_location['longitude'] += LONGITUDE_INCREMENT

    # add some randomness to simulate variable road conditions
    start_location['latitude'] += random.uniform(-0.0005, 0.0005)
    start_location['longitude'] += random.uniform(-0.0005, 0.0005)

    return start_location


def generate_vehicle_data(device_id):
    location = simulate_vehicle_movement()
    return {
        'id': uuid.uuid4()
        , 'device_id': device_id
        , 'timestamp': get_next_time().isoformat()
        , 'location': (location['latitude'], location['longitude'])
        , 'speed': random.uniform(10, 40)
        , 'direction': 'North-East'
        , 'make': 'Porsche'
        , 'model': '911'
        , 'year': 2023
        , 'fuel_type': 'Gasoline'
    }


def json_serializer(obj):
    if isinstance(obj, uuid.UUID):
        return str(obj)
    raise TypeError(f'Object of type {obj.__clas__.__name__} is not JSON serializable')


def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')


def produce_data_to_kafka(producer, topic, data):
    producer.produce(
        topic
        , key=str(data['id'])
        , value=json.dumps(data, default=json_serializer).encode('utf-8')
        , on_delivery=delivery_report
    )

    producer.flush()


def simulate_journey(producer, device_id):
    while True:
        vehicle_data = generate_vehicle_data(device_id)
        gps_data = generate_gps_data(device_id, vehicle_data['timestamp'])
        traffic_camera_data = generate_traffic_camera_data(device_id, vehicle_data['timestamp'],
                                                           vehicle_data['location'], 'Camera123')
        weather_data = generate_weather_data(device_id, vehicle_data['timestamp'], vehicle_data['location'])
        emergency_incident_data = generate_emergency_incident_data(device_id, vehicle_data['timestamp'],
                                                                   vehicle_data['location'])

        '''  # test: 
        json.dumps(print(f'---Vehicle Data---\n {vehicle_data}'), indent=1)
        json.dumps(print(f'---gps_data---\n {gps_data}'), indent=1)
        json.dumps(print(f'---traffic_camera_data---\n {traffic_camera_data}'), indent=1)
        json.dumps(print(f'---weather_data---\n {weather_data}'), indent=1)
        json.dumps(print(f'---emergency_incident_data---\n {emergency_incident_data}'), indent=1)
        '''

        if (vehicle_data['location'][0] >= BIRMINGHAM_COORDINATES['latitude']
                and vehicle_data['location'][1] <= BIRMINGHAM_COORDINATES['longitude']):
            print('Vehicle has reached Birmingham. Simulation ending...')
            break

        produce_data_to_kafka(producer, VEHICLE_TOPIC, vehicle_data)
        produce_data_to_kafka(producer, GPS_TOPIC, gps_data)
        produce_data_to_kafka(producer, TRAFFIC_TOPIC, traffic_camera_data)
        produce_data_to_kafka(producer, WEATHER_TOPIC, weather_data)
        produce_data_to_kafka(producer, EMERGENCY_TOPIC, emergency_incident_data)

        time.sleep(5)


if __name__ == "__main__":
    producer_config = {
        'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS
        , 'error_cb': lambda err: print(f'Kafak error: {err}')
    }
    producer = SerializingProducer(producer_config)

    try:
        simulate_journey(producer, 'Vehicle-Asees-123')
    except KeyboardInterrupt:
        print('Simulation end by the user')
    except Exception as e:
        print(f'Unexpected error occurred: {e}')
