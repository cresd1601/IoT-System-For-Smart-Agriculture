#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include <DHT.h>
#include <ArduinoJson.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// WiFi credentials
const char* ssid = "Crescent 5Ghz";
const char* password = "cRescent1!";

// MQTT broker credentials
const char* mqtt_server = "192.168.6.52"; //13.215.30.49
const int mqtt_port = 1883;
const char* mqtt_user = "";
const char* mqtt_password = "";

// MQTT topics
const char* mqtt_topic_dht_sync = "group4/sync/temp";
const char* mqtt_topic_sms_sync = "group4/sync/moist";
const char* mqtt_topic_dht_track = "group4/track/temp";
const char* mqtt_topic_sms_track = "group4/track/moist";
const char* mqtt_topic_led_trigger = "group4/trigger/led";
const char* mqtt_topic_lcd_trigger = "group4/trigger/lcd";
const char* mqtt_topic_pump_trigger = "group4/trigger/pump";  // Topic for pump control
const char* mqtt_topic_fan_trigger = "group4/trigger/fan";  // New topic for fan control

// DHT11 setup
#define DHTPIN 5  // GPIO5 for DHT11
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

// SMS-V1 setup
#define SMS_PIN A0

// LED setup
#define LED_PIN 13  // GPIO13 for LED

// Relay setup (for controlling the pump and fan)
#define RELAY_PIN_PUMP 4  // GPIO4 for Pump Relay control
#define RELAY_PIN_FAN 16  // GPIO16 for Fan Relay control

// LCD setup (use the correct I2C address found from the scanner)
LiquidCrystal_I2C lcd(0x27, 16, 2);  // Replace 0x27 with your I2C address if different

// WiFi and MQTT client objects
WiFiClient espClient;
PubSubClient client(espClient);

// Function declarations
void setup_wifi();
void reconnect();
void callback(char* topic, byte* payload, unsigned int length);
void publishDHT11Data();
void publishSMSV1Data();
void controlLED(const String& message);
void controlPump(const String& message);  // Function to control the pump
void controlFan(const String& message);  // New function to control the fan
void displayTextOnLCD(const String& text);

void setup() {
    // Initialize serial communication
    Serial.begin(9600);

    // Initialize the LED, Pump Relay, and Fan Relay pins as outputs
    pinMode(LED_PIN, OUTPUT);
    pinMode(RELAY_PIN_PUMP, OUTPUT);
    pinMode(RELAY_PIN_FAN, OUTPUT);

    // Initialize the I2C communication with the specified SDA and SCL pins
    Wire.begin(12, 14); // SDA = GPIO12, SCL = GPIO14

    // Initialize the LCD
    lcd.begin(16, 2);  // Specify the number of columns and rows
    lcd.backlight();
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Starting...");

    // Start WiFi and MQTT
    setup_wifi();
    client.setServer(mqtt_server, mqtt_port);
    client.setCallback(callback);

    // Initialize the DHT sensor
    dht.begin();
}

void loop() {
    if (!client.connected()) {
        reconnect();
    }
    client.loop();

    // Publish data from DHT11 sensor
    publishDHT11Data();

    // Publish data from SMS-V1 sensor
    publishSMSV1Data();

    // Wait before sending the next batch of data
    delay(2000);
}

void setup_wifi() {
    delay(10);
    Serial.println();
    Serial.print("Connecting to ");
    Serial.println(ssid);

    WiFi.begin(ssid, password);

    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }

    Serial.println("");
    Serial.println("WiFi connected");
    Serial.println("IP address: ");
    Serial.println(WiFi.localIP());
}

void reconnect() {
    // Loop until we're reconnected
    while (!client.connected()) {
        Serial.print("Attempting MQTT connection...");
        // Attempt to connect
        if (client.connect("ESP8266Client", mqtt_user, mqtt_password)) {
            Serial.println("connected");
            // Subscribe to relevant MQTT topics
            client.subscribe(mqtt_topic_led_trigger);
            client.subscribe(mqtt_topic_lcd_trigger);
            client.subscribe(mqtt_topic_pump_trigger);  // Subscribe to the pump control topic
            client.subscribe(mqtt_topic_fan_trigger);  // Subscribe to the fan control topic
            // Once connected, publish an announcement...
            client.publish("home/connected", "ESP8266 connected");
        } else {
            Serial.print("failed, rc=");
            Serial.print(client.state());
            Serial.println(" try again in 5 seconds");
            // Wait 5 seconds before retrying
            delay(5000);
        }
    }
}

void callback(char* topic, byte* payload, unsigned int length) {
    String message = "";
    for (int i = 0; i < length; i++) {
        message += (char)payload[i];
    }

    Serial.print("Message received in topic: ");
    Serial.println(topic);
    Serial.print("Message: ");
    Serial.println(message);

    // Check if the message is for LED control
    if (String(topic) == mqtt_topic_led_trigger) {
        controlLED(message);
    } else if (String(topic) == mqtt_topic_lcd_trigger) {
        displayTextOnLCD(message);
    } else if (String(topic) == mqtt_topic_pump_trigger) {  // Check if the message is for pump control
        controlPump(message);
    } else if (String(topic) == mqtt_topic_fan_trigger) {  // Check if the message is for fan control
        controlFan(message);
    }
}

// Function to extract the last number from a string
int extractSensorId(const char *str) {
    // Find the last occurrence of '/'
    const char *lastSlash = strrchr(str, '/');
    
    if (lastSlash != NULL) {
        // Move past the last '/'
        lastSlash++;
        
        // Convert the substring to an integer
        return atoi(lastSlash);
    }
    
    // Return -1 if no '/' is found or conversion fails
    return -1;
}

void controlLED(const String& message) {
    if (message == "ON") {
        digitalWrite(LED_PIN, HIGH);
        Serial.println("LED turned ON");
    } else if (message == "OFF") {
        digitalWrite(LED_PIN, LOW);
        Serial.println("LED turned OFF");
    }
}

void controlPump(const String& message) {
    if (message == "ON") {
        digitalWrite(RELAY_PIN_PUMP, HIGH);  // Activating relay for pump
        Serial.println("Pump turned ON");
    } else if (message == "OFF") {
        digitalWrite(RELAY_PIN_PUMP, LOW);  // Deactivating relay for pump
        Serial.println("Pump turned OFF");
    }
}

void controlFan(const String& message) {
    if (message == "ON") {
        digitalWrite(RELAY_PIN_FAN, HIGH);  // Activating relay for fan
        Serial.println("Fan turned ON");
    } else if (message == "OFF") {
        digitalWrite(RELAY_PIN_FAN, LOW);  // Deactivating relay for fan
        Serial.println("Fan turned OFF");
    }
}

void displayTextOnLCD(const String& text) {
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print(text.substring(0, 16));  // Print first 16 characters on the first line
    if (text.length() > 16) {
        lcd.setCursor(0, 1);
        lcd.print(text.substring(16, 32));  // Print the next 16 characters on the second line
    }
}

// Sensor ID = 1
void publishDHT11Data() {
    // Reading temperature and humidity
    float temperature = dht.readTemperature();
    float humidity = dht.readHumidity();

    // Check if any reads failed and exit early (to try again next loop)
    if (isnan(temperature) || isnan(humidity)) {
        Serial.println("Failed to read from DHT sensor!");
        return;
    }

    // Create JSON object
    StaticJsonDocument<200> jsonBuffer;
    jsonBuffer["sensor_id"] =  1;
    jsonBuffer["temperature"] = temperature;
    jsonBuffer["humidity"] = humidity;

    // Serialize JSON object to string
    char jsonString[128];
    serializeJson(jsonBuffer, jsonString);

    // Publish the JSON string to the MQTT topics
    client.publish(mqtt_topic_dht_sync, jsonString);
    client.publish(mqtt_topic_dht_track, jsonString);

    // Print the JSON string to the Serial Monitor
    Serial.println(jsonString);
}

// Sensor ID = 2
void publishSMSV1Data() {
    // Reading soil moisture value
    int sensorValue = analogRead(SMS_PIN);

   // convert analog value to percent for the soil moisture
    int percent = map(sensorValue, 1024, 530, 0, 100);

    // Create JSON object
    StaticJsonDocument<200> jsonBuffer;
    jsonBuffer["sensor_id"] = 2;
    jsonBuffer["soil_moisture"] = percent;

    // Serialize JSON object to string
    char jsonString[128];
    serializeJson(jsonBuffer, jsonString);

    // Publish the JSON string to the MQTT topics
    client.publish(mqtt_topic_sms_sync, jsonString);
    client.publish(mqtt_topic_sms_track, jsonString);

    // Print the JSON string to the Serial Monitor
    Serial.println(jsonString);
}
