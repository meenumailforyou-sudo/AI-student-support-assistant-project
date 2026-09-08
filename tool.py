from datetime import datetime


def get_current_date():
    return datetime.now().strftime("%d-%m-%Y")


def available_tools():
    return {
        "current_date": get_current_date()
    }