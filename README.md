# IoT-System-For-Smart-Agriculture

This repository contains four distinct projects related to the implementation of MQTT systems:

1. **Cloud-Based Deployment** (`mqtt-project-cloud`)
2. **Raspberry Pi Deployment** (`mqtt-project-rasp`)
3. **Mobile Interface** (`mqtt-project-mobile`)
4. **Embedded Device (Arduino) Deployment** (`mqtt-project-embedded`)

These projects work together within the broader IoT ecosystem by sharing sensor data, synchronizing cloud and edge operations, and providing both mobile and embedded control interfaces.

## Project Structure

```text
.
├── mqtt-project-cloud/
│   ├── README.md
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── src/
│   ├── configs/
│   └── ...
├── mqtt-project-rasp/
│   ├── README.md
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── sensors/
│   └── ...
├── mqtt-project-mobile/
│   ├── README.md
│   ├── android/
│   ├── ios/
│   ├── lib/
│   ├── pubspec.yaml
│   ├── test/
│   ├── web/
│   └── ...
├── mqtt-project-embedded/
│   ├── Arduino_MQTT_IoT_Node.ino
└── README.md
```

## Overview of Projects

### 1. `mqtt-project-cloud`
Manages cloud-side logic for MQTT subscriptions and publishing sensor data to a web API. It includes integration with cloud services like Azure, web services, and database storage.

### 2. `mqtt-project-rasp`
Runs on a Raspberry Pi, collecting real-time sensor data and sending it to the cloud MQTT broker.

### 3. `mqtt-project-mobile`
A Flutter-based mobile application that provides a user interface for monitoring and interacting with the MQTT system.

### 4. `mqtt-project-embedded`
An Arduino-based IoT node using MQTT to collect data from sensors and publish it to the MQTT broker. The node is designed to run on an Arduino device, equipped with various sensors (e.g., temperature, moisture).

## Prerequisites

- Docker and Docker Compose (for cloud and Raspberry Pi projects)
- Python 3.x (for `mqtt-project-rasp`)
- Raspberry Pi with sensors (for `mqtt-project-rasp`)
- Flutter SDK (for `mqtt-project-mobile`)
- Arduino IDE (for `mqtt-project-embedded`)
- Arduino hardware with sensors (e.g., temperature, soil moisture)
- Redis for task queueing
- MariaDB or MySQL for cloud storage

## Getting Started

### 1. Cloud Deployment (`mqtt-project-cloud`)

#### Build and Run
1. Navigate to the `mqtt-project-cloud` directory:
   ```bash
   cd mqtt-project-cloud
   ```

2. Build and start the services using Docker Compose:
   ```bash
   docker-compose up --build
   ```

3. Verify that the API and worker services are running correctly.

### 2. Raspberry Pi Deployment (`mqtt-project-rasp`)

#### Build and Run
1. SSH into your Raspberry Pi and clone the repository:
   ```bash
   git clone https://github.com/your-repo/mqtt-project.git
   ```

2. Navigate to the `mqtt-project-rasp` directory:
   ```bash
   cd mqtt-project-rasp
   ```

3. Build and start the services using Docker Compose:
   ```bash
   docker-compose up --build
   ```

4. Verify that sensor data collection is running correctly and the MQTT broker connection is established.

### 3. Mobile Interface (`mqtt-project-mobile`)

#### Running the Flutter App

1. **Install Flutter**  
   If you do not have Flutter installed, follow the [official installation guide](https://flutter.dev/docs/get-started/install) to set up the Flutter environment on your machine.

2. **Install Dependencies**  
   Navigate to the `mqtt-project-mobile` directory:
   ```bash
   cd mqtt-project-mobile
   ```
   Install the required Flutter dependencies:
   ```bash
   flutter pub get
   ```

3. **Run on an Emulator or Mobile Device**  
   Use a mobile device or emulator to access the interface:
   ```bash
   flutter run
   ```

### 4. Arduino Embedded Device (`mqtt-project-embedded`)

#### Setup and Run

1. **Install the Arduino IDE**  
   Download and install the [Arduino IDE](https://www.arduino.cc/en/software) if you don't have it installed already.

2. **Connect the Arduino and Sensors**  
   - Connect your Arduino to sensors like temperature and moisture sensors.
   - Make sure the connections are properly set up (e.g., GPIO pins, power).

3. **Upload the Sketch**  
   - Open the `Arduino_MQTT_IoT_Node.ino` file in the Arduino IDE:
     ```bash
     cd mqtt-project-embedded
     open Arduino_MQTT_IoT_Node.ino
     ```
   - Modify the MQTT broker settings in the sketch to match your setup (e.g., broker IP, port, and topic).
   - Compile and upload the sketch to your Arduino device.

4. **Monitor and Verify Data**  
   Once the Arduino is connected, it will start publishing data to the MQTT broker. You can monitor this data from the cloud or mobile interface.

#### Configurations
- The Arduino sketch is pre-configured to work with common sensors like temperature and soil moisture sensors.
- Modify the sketch for additional sensor types as needed.

## Contributing

Feel free to contribute to this repository by creating a pull request. You can improve the cloud deployment, Raspberry Pi integration, or add support for new sensors and embedded devices.

## License

This repository is licensed under the MIT License. See the `LICENSE` file for more details.
