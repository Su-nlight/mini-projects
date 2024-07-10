#include<IRremoteESP8266.h>
#include<IRrecv.h>
#include<WiFi.h>
#include<HTTPClient.h>

const char* ssid = "SSID";
const char* password = "Password";

//Your Domain name with URL path or IP address with path
const char* serverName = "https://ntfy.com:80/";


IRrecv irrecv(15); //defines gpio pin to which ir reviever is connected
decode_results results;

void setup() {
  // setup code is here, to run once:
  
  Serial.begin(115200); //baudrate conditon
  irrecv.enableIRIn();

  WiFi.begin(ssid, password);
  Serial.println("Connecting");
  while(WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
  }
  Serial.println(".");
  //following 2 lines are used for active serial debug
  Serial.print("Connected & IP Address: "); 
  Serial.println(WiFi.localIP());
  
}

void loop() {
  // put your main code here, to run repeatedly:
  if(WiFi.status()==WL_CONNECTED){
    WiFiClient client;
    HTTPClient http;
    
    

    //put the ir code here
    if(irrecv.decode(&results)){
      Serial.println(results.value, HEX);
      
      int httpRespo;
      http.begin(serverName);
      http.addHeader("Content-Type","text/plain");
      //put the ir switching statement here
      switch(results.value){
        // build post request as per requirement
        case 0xFFA25D:{httpRespo=http.POST("text msg1");break;}
        case 0xFF38C7:{http.addHeader("X-ntfy-priority","5");httpRespo=http.POST("text msg1 but important");break;}
        //avoid adding any http request for default situation as the sensor senses every ir signal in range
        default:{break;} 

      }
      //condition for error in http requests
      if(httpRespo > 0){
        String response=http.getString();
        //put print here for active serial debug 
        Serial.println(httpRespo);
      } else{
        Serial.print("Error");
      }
      http.end(); //end the http request sequence
      
      //delay so to avoid repeated remote spam conditions and network overload
      delay(1500);
      irrecv.resume(); // resume after delay
    }
    

  }
  else{Serial.println("Wifi error");}
  
}
