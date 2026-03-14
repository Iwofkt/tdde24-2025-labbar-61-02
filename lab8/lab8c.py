from cal_ui import *
from cal_ui import calendars
from cal_booking import *
from cal_abstraction import *


def remove(cal_name: str, d: int, m: str, t1: str) -> None:
    """Book a new appointment in the calendar with the given name."""
    day = new_day(d)
    mon = new_month(m)
    start = new_time_from_string(t1)

    cal_year = get_calendar(cal_name)
    cal_month = cy_get_month(mon, cal_year)
    cal_day = cm_get_day(cal_month, day)

    if is_booked_from(cal_day, start):
        new_year = minus_appointment(cal_name, d, m, t1)
        insert_calendar(cal_name, new_year)
        print("Appointment removed.")
    else:
        print("Appointment does not exist")


def minus_appointment(cal_name: str, d: int, m: str, t1: str):

    # Used to find the calendar day of the appointment
    day = new_day(d)
    mon = new_month(m)
    cal_year = get_calendar(cal_name)
    cal_month = cy_get_month(mon, cal_year)
    cal_day = cm_get_day(cal_month, day)

    # Start of the appointment to be removed
    start = new_time_from_string(t1)

    # All appointments except the one that should be deleted.
    rest_appointments = []

    # Find the appointment that should be deleted
    for app in cd_iter_appointments(cal_day):
        if ts_start(app_span(app)) == start and app_subject(app) == t1:
            rest_appointments.append(app)

    new_date(day, mon)

    old_cal_month = cy_get_month(mon, cal_year)

    # Create a new calendar
    new_cal_day = new_calendar_day(cd_day(cal_day), rest_appointments)
    new_cal_month = cm_plus_cd(old_cal_month, new_cal_day)
    new_cal_year = cy_plus_cm(cal_year, new_cal_month)

    return new_cal_year
