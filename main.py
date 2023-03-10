led.enable(False)
pins.digital_write_pin(DigitalPin.P0, 0)
Brillo = 0

def on_forever():
    global Brillo
    while pins.digital_read_pin(DigitalPin.P0) == 0:
        pins.digital_write_pin(DigitalPin.P0, 0)
    while Brillo == 500:
        Brillo += 100
        pins.analog_write_pin(AnalogPin.P0, 1023)
    Brillo = 0
basic.forever(on_forever)
