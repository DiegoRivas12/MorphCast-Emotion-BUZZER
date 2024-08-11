#include <Arduino.h>


#define BUZZER_ACTIVO 8
// put function declarations here: 31 65,525 Hz
String txtMsg = "";


void setup() {
    Serial.begin(9600);
    pinMode(BUZZER_ACTIVO, OUTPUT);
   
}


void loop() {
    if(Serial.available()>0){
      char inChar = Serial.read();
      txtMsg += inChar;
      
      if(txtMsg == "SI"){
        tone(BUZZER_ACTIVO, 660, 250);
        delay(3000);
        tone(BUZZER_ACTIVO, 250, 250);
        delay(3000);
        txtMsg="";
      }
    }
    //Serial.println("HOLA");
}
