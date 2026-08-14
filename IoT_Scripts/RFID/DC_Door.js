var door = 1;
var reader = A0;

function setup() {
	pinMode(door, OUTPUT);
    pinMode(reader, INPUT);
}

function loop() {

    if(analogRead(reader) == 0){
        customWrite(door,1);
    }
    else{
        customWrite(door,0);
    }

	digitalWrite(1, HIGH);
	delay(1000);
	digitalWrite(1, LOW);
	delay(500);
}
