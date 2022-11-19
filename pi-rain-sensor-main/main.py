import argparse
from time import sleep
from gpiozero import Buzzer, InputDevice


def main():
    print("pi-rain-sensor launched.")
    tune = load_tune(args.tune)
    buzzer = Buzzer(args.pin_buzzer)
    rain_sensor = InputDevice(args.pin_sensor)

    while True:
        if rain_detected(rain_sensor):
            play_tune(buzzer, tune)
            sleep(args.buzzer_suspension_time)
            continue
        sleep(args.poll_time)


def sound_buzzer(buzzer, seconds):
    buzzer.on()
    sleep(seconds)
    buzzer.off()


def rain_detected(rain_sensor):
    return False if rain_sensor.is_active else True     # Active input device indicates dry sensor


def play_tune(buzzer, tune):
    sound = True
    for timing in tune:
        if sound:
            sound_buzzer(buzzer, timing)
        else:
            sleep(timing)
        sound = not sound


def load_tune(tune_file_path):
    with open(tune_file_path) as tune_file:
        return [float(line.strip()) for line in tune_file.readlines() if line.strip() is not False]


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tune", help="Path to tune file.", type=str, default="tunes/default.tune")
    parser.add_argument("--pin_buzzer", help="Pin of buzzer.", type=int, default=13)
    parser.add_argument("--pin_sensor", help="Pin of sensor.", type=int, default=18)
    parser.add_argument("--poll_time", help="Seconds between subsequent polls of sensor state.", type=float, default=1)
    parser.add_argument("--buzzer_suspension_time", help="Seconds after sounding buzzer to suspend further activity.", type=float, default=10)
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()
    main()
