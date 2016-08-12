int LEDPIN = 8;
int BUTTON = 7;
void setup() {
pinMode(8,OUTPUT);
pinMode (7, INPUT);

Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  if (digitalRead(7) == HIGH) {
    digitalWrite(8, HIGH);
  }
  else{ 
    digitalWrite (8, LOW);
  }
}

