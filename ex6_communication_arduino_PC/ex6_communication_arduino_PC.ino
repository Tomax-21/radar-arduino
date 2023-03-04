#include <Servo.h>

Servo monServo;
int trigger = 25; // trigger sur pin 8
int echo = 23; // echo sur pin 7
// Définition des variables nécessaires
int maximumRange = 300;
int minimumRange = 2;
long distance;
long duree;
int distResult;


void setup()
{ 
  monServo.attach(10);
  monServo.write(0);
  pinMode( trigger , OUTPUT);
  pinMode( echo , INPUT);
  Serial.begin (9600);
  digitalWrite(trigger, LOW);
}

void loop() {
  while (Serial.available()>0)
      {
       char commande = char(Serial.read());
       if (commande == '1')
         { Serial.println("Lancement radar");
           radar();
           delay(1000); // Pause entre les mesures
         }
       else if (commande == '0')
         { Serial.println("Fin des mesures");
         }
      }         
}

void radar(){
  for(int i = 0; i<181; i+=10){
    monServo.write(i);
    distResult = mesure();
    Serial.println(distResult);
    delay(100);
  }
}

int mesure() {
 int mesures[5];
 for(int j = 0; j<5; j++){
    digitalWrite(trigger, HIGH); 
    delayMicroseconds(10);
    digitalWrite(trigger, LOW);
    duree = pulseIn(echo, HIGH);
    distance = duree * 0.034 / 2;
    mesures[j] = distance;
    delay(5);   
 }
 int total = 0; 
 for(int l = 0; l<5; l++){
    total += mesures[l];
 }
 int moyenne = total / 5 ;
 return distance;  
}
