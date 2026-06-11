from time import sleep

from gpiozero import LED


def blink_led(pin: int = 17, interval: float = 1) -> None:
    led = LED(pin)

    try:
        while True:
            led.on()
            sleep(interval)
            led.off()
            sleep(interval)
    except KeyboardInterrupt:
        led.off()
    finally:
        led.close()


if __name__ == "__main__":
    blink_led()
