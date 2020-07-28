void setup() 
{
pinMode(3,OUTPUT); 
pinMode(4,OUTPUT);
pinMode(5,OUTPUT);
pinMode(6,OUTPUT);
Serial.begin(9600);
Serial.println("ROBOT IS READY");
}

void loop() 
{
  if(Serial.available())
  {
    char z = Serial.read();

    if(z=='w' || z=='W')
    {
     Serial.println("FORWARD");
     digitalWrite(3,HIGH);
     digitalWrite(4,LOW);
     digitalWrite(5,HIGH);
     digitalWrite(6,LOW);
    }
    if(z=='x' || z=='X')
    {
     Serial.println("BACKWARD");
     digitalWrite(3,LOW);
     digitalWrite(4,HIGH);
     digitalWrite(5,LOW);
     digitalWrite(6,HIGH);
    }
    if(z=='a' || z=='A')
    {
     Serial.println("RADIAL LEFT");
     digitalWrite(3,LOW);
     digitalWrite(4,LOW);
     digitalWrite(5,HIGH);
     digitalWrite(6,LOW);
    }
    if(z=='d' || z=='D')
    {
     Serial.println("RADIAL RIGHT");
     digitalWrite(3,HIGH);
     digitalWrite(4,LOW);
     digitalWrite(5,LOW);
     digitalWrite(6,LOW);
    }
    if(z=='s' || z=='S')
    {
     Serial.println("STOP");
     digitalWrite(3,LOW);
     digitalWrite(4,LOW);
     digitalWrite(5,LOW);
     digitalWrite(6,LOW);
    }
  }
}
