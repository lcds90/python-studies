def calculate_values_from_seconds(sec: int) -> list:
    years = sec // 31536000
    days = sec // 86400 % 365
    hours = sec // 3600 % 24
    minutes = sec // 60 % 60
    seconds = sec % 60

    def str_format(value: int, name: str) -> str:
        if value == 1:
            return f"{value} {name}"
        else:
            return f"{value} {name}s"

    values = [
        [str_format(years, 'year'), years],
        [str_format(days, 'day'), days],
        [str_format(hours, 'hour'), hours],
        [str_format(minutes, 'minute'), minutes],
        [str_format(seconds, 'second'), seconds]
    ]

    result = [
        i[0] for i in values if i[1] > 0
    ]

    return result


def generate_print(list: list) -> str:
    result = ''
    if len(list) == 1:
        return list[0]
    elif len(list) == 2:
        return f"{list[0]} and {list[1]}"
    else:
        for i in range(len(list)): 

            result += (
                f"{list[i]}, "
                if list[i] != list[-2]
                else f"{list[i]} and "
            )   

        result = result[:-2]
        return result


def format_duration(seconds: int) -> str:
    if seconds <= 0:
        return 'now'
    else:
        return generate_print(
            calculate_values_from_seconds(seconds)
        )



p = format_duration(1)

def test_duration_1():
    assert format_duration(1) == '1 second'


def test_duration_62():
    assert format_duration(
        62) == '1 minute and 2 seconds'


def test_duration_120():
    assert format_duration(120) == '2 minutes'


def test_duration_3600():
    assert format_duration(3600) == '1 hour'


def test_duration_3662():
    assert format_duration(
        3662) == '1 hour, 1 minute and 2 seconds'
