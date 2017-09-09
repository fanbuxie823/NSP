
//
//    FILE: dht11_test.ino
//  AUTHOR: Rob Tillaart
// VERSION: 0.1.01
// PURPOSE: DHT library test sketch for DHT11 && Arduino
//     URL:
//
// Released to the public domain
//

#include "DHT.h"

#define DHTTYPE DHT11

#define DHT11_PIN 5

void setup()
{
  Serial.begin(9600);
  //Serial.println("DHT TEST PROGRAM ");
  //Serial.print("LIBRARY VERSION: ");
  //Serial.println(DHT_LIB_VERSION);
  //Serial.println("Type,\tstatus,\tHumidity (%),\tTemperature (C)");
}

void loop()
{
  // READ DATA
  //Serial.print("DHT11,\t");
  char chk = DHT.read11(DHT11_PIN);
  switch (chk)
  {
    case DHTLIB_OK:  
    Serial.write("OK"); 
    break;
    case DHTLIB_ERROR_CHECKSUM: 
    Serial.write("Checksum error"); 
    break;
    case DHTLIB_ERROR_TIMEOUT: 
    Serial.write("Time out error"); 
    break;
    case DHTLIB_ERROR_CONNECT:
        Serial.write("Connect error");
        break;
    case DHTLIB_ERROR_ACK_L:
        Serial.write("Ack Low error");
        break;
    case DHTLIB_ERROR_ACK_H:
        Serial.write("Ack High error");
        break;
    default: 
    Serial.write("Unknown error"); 
    break;
  }
  // DISPLAY DATA
  Serial.println(DHT.humidity, 1);
  Serial.println(DHT.temperature, 1);

  delay(2000);
}
//
// END OF FILE
//
