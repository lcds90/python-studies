from typing import Literal


class ColorGenerator:
    RED = "\033[31m"
    GREEN = "\033[32m"
    BLUE = "\033[34m"
    YELLOW = "\033[33m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    END = "\033[0m"

    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_BLUE = "\033[44m"
    BG_YELLOW = "\033[43m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"

    @staticmethod
    def set_background_color(
        text: str,
        color: Literal[
            "red", "green", "blue", "yellow", "cyan", "magenta"
        ] = "",
    ):
        texts = f"{text}{ColorGenerator.END}"
        return {
            "red": f"{ColorGenerator.BG_RED}{texts}",
            "green": f"{ColorGenerator.BG_GREEN}{texts}",
            "yellow": f"{ColorGenerator.BG_YELLOW}{texts}",
            "blue": f"{ColorGenerator.BG_BLUE}{texts}",
            "magenta": f"{ColorGenerator.BG_MAGENTA}{texts}",
            "cyan": f"{ColorGenerator.BG_CYAN}{texts}",
        }.get(color, text)

    @staticmethod
    def set_color(
        text: str,
        color: Literal[
            "red", "green", "blue", "yellow", "cyan", "magenta"
        ] = "",
    ):
        texts = f"{text}{ColorGenerator.END}"
        return {
            "red": f"\033[31m{texts}",
            "green": f"\033[32m{texts}",
            "blue": f"\033[34m{texts}",
            "yellow": f"\033[33m{texts}",
            "magenta": f"\033[35m{texts}",
            "cyan": f"\033[36m{texts}",
        }.get(color, text)
