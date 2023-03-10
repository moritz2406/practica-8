led.enable(false)
pins.digitalWritePin(DigitalPin.P0, 0)
let Brillo = 0
basic.forever(function () {
    while (pins.digitalReadPin(DigitalPin.P0) == 0) {
        pins.digitalWritePin(DigitalPin.P0, 0)
    }
    while (Brillo == 500) {
        Brillo += 100
        pins.analogWritePin(AnalogPin.P0, 1023)
    }
    Brillo = 0
})
