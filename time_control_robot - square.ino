void setup() 
{
pinMode(3,OUTPUT);     //LEFT MOTOR
 pinMode(4,OUTPUT);
 pinMode(5,OUTPUT);     //RIGHT MOTOR 
 pinMode(6,OUTPUT);
 //FORWARD
  digitalWrite(3,HIGH);
  digitalWrite(4,LOW);
  digitalWrite(5,HIGH);
  digitalWrite(6,LOW);
  delay(2000);
  //BAcKWARD
  digitalWrite(3,LOW);
  digitalWrite(4,HIGH);
  digitalWrite(5,LOW);
  digitalWrite(6,HIGH);
  delay(2000);
  //AXIAL LEFT
  digitalWrite(3,LOW);
  digitalWrite(4,HIGH);
  digitalWrite(5,HIGH);
  digitalWrite(6,LOW);
  delay(2000);
  //AXIAL RIGHT
  digitalWrite(3,HIGH);
  digitalWrite(4,LOW);
  digitalWrite(5,LOW);
  digitalWrite(6,HIGH);
  delay(2000);
  //RADIAL LEFT
  digitalWrite(3,LOW);
  digitalWrite(4,LOW);
  digitalWrite(5,HIGH);
  digitalWrite(6,LOW);
  delay(2000);
  //RADIAL RIGHT
  digitalWrite(3,HIGH);
  digitalWrite(4,LOW);
  digitalWrite(5,HIGH);
  digitalWrite(6,HIGH);
  delay(2000);
  //STOP
  digitalWrite(3,LOW);
  digitalWrite(4,LOW);
  digitalWrite(5,LOW);
  digitalWrite(6,LOW);
  delay(5000);
}

void loop()
{
  
}
