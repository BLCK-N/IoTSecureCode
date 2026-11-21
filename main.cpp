#include <Arduino.h>

#include "SecureCode.h"

char device_id[9];

void setup() { Serial.begin(115200); }

void loop() {
#ifdef ESP8266
  sprintf(device_id, "%08X", ESP.getChipId());
#elif defined(ESP32)
  sprintf(device_id, "%08X", (uint32_t)ESP.getEfuseMac());
#endif
  Serial.printf("Device ID: %s\n", device_id);
  if (check_secure_code(device_id, "698406101b5673bfc5b00faef0b9c83d")) {
    Serial.println("Secure code is correct");
  } else {
    Serial.println("Secure code is incorrect");
  }
  delay(5000);
}