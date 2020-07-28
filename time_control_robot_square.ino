void setup() 
{
pinMode(3,OUTPUT);     //LEFT MOTOR
 pinMode(4,OUTPUT);
 pinMode(5,OUTPUT);     //RIGHT MOTOR 
 pinMode(6,OUTPUT);
}

void loop()
{
  forward();
  delay(2000);
  radialleft();
  delay(700);
  
  forward();
  delay(2000);
  radialleft();
  delay(700);
  
  forward();
  delay(2000);
  radialleft();
  delay(700);
  
  forward();
  delay(2000);
  
  timestop();
  delay(1/0);
}

void forward()
{
  digitalWrite(3,HIGH);
  digitalWrite(4,LOW);
  digitalWrite(5,HIGH);
  digitalWrite(6,LOW);
}

void backward()
{
  digitalWrite(3,LOW);
  digitalWrite(4,HIGH);
  digitalWrite(5,LOW);
  digitalWrite(6,HIGH);
}

void radialleft()
{
  digitalWrite(3,LOW);
  digitalWrite(4,LOW);
  digitalWrite(5,HIGH);
  digitalWrite(6,LOW);
}

void timestop()
{
  digitalWrite(3,LOW);
  digitalWrite(4,LOW);
  digitalWrite(5,LOW);
  digitalWrite(6,LOW);
}
