import time


def get_time():
    while True:
        user_input = input("Insert time to count down (h:m:s) ")

        try:
            parts = user_input.split(":")

            if len(parts) != 3:
                print("Please use the format h:m:s, for example 0:5:32.")
                continue

            hours, minutes, seconds = [int(part) for part in parts]

            if hours < 0 or minutes < 0 or seconds < 0:
                print("Time cannot be negative.")
                continue

            if minutes >= 60 or seconds >= 60:
                print("Minutes and seconds must be between 0 and 59.")
                continue

            return hours, minutes, seconds

        except ValueError:
            print("Please enter numbers in the format h:m:s.")


def countdown(hours, minutes, seconds):
    total_seconds = hours * 3600 + minutes * 60 + seconds

    while total_seconds >= 0:
        current_hours = total_seconds // 3600
        current_minutes = (total_seconds % 3600) // 60
        current_seconds = total_seconds % 60

        print(f"{current_hours:02d}:{current_minutes:02d}:{current_seconds:02d}")

        if total_seconds == 0:
            break

        total_seconds -= 1
        time.sleep(1)

    print("Time is up!")


def main():
    hours, minutes, seconds = get_time()
    countdown(hours, minutes, seconds)


if __name__ == "__main__":
    main()
