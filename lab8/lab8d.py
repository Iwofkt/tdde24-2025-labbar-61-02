# Write your code for lab 8d here.
from cal_abstraction import CalendarDay, Time
from settings import CHECK_AGAINST_FACIT
from cal_ui import get_calendar, create, book

from lab8b import *

if CHECK_AGAINST_FACIT:
    try:
        from facit_la8_uppg import TimeSpanSeq
    except:
        print("*" * 100)
        print("*" * 100)
        print("Kan inte hitta facit; ändra CHECK_AGAINST_FACIT i test_driver.py till False")
        print("*" * 100)
        print("*" * 100)
        raise
else:
    from lab8b import *


def free_spans(cal_day: CalendarDay, start: Time, end: Time) -> TimeSpanSeq:
    """
    Check for free times between start and end in a calendar day.
    """
    ensure_type(cal_day, CalendarDay)
    ensure_type(end, Time)
    ensure_type(start, Time)

    free_span_start = start
    tss = new_time_span_seq([])

    # Start and end is at same time so return the timespan sequence
    if time_precedes_or_equals(end, start):
        return tss

    # If the day is empty just return the timespan sequence
    if cd_is_empty(cal_day):
        tss = tss_plus_span(tss, new_time_span(start, end))
        return tss

    for app in cd_iter_appointments(cal_day):
        check_span = new_time_span(free_span_start, end)

        if not ts_overlap(check_span, app_span(app)):
            continue

        overlap = ts_overlapping_part(check_span, app_span(app))

        if time_precedes(free_span_start, ts_start(overlap)):
            tss = tss_plus_span(tss, new_time_span(free_span_start, ts_start(overlap)))

        free_span_start = ts_end(app_span(app))

    if time_precedes(free_span_start, end):
        tss = tss_plus_span(tss, new_time_span(free_span_start, end))

    return tss


def show_free(cal_name: str, d: int, m: str, t1: str, t2: str):
    """
    A ui function to show all free times within a given time during a day
    """

    ensure_type(cal_name, str)
    ensure_type(d, int)
    ensure_type(m, str)
    ensure_type(t1, str)
    ensure_type(t2, str)

    day = new_day(d)
    mon = new_month(m)
    start = new_time_from_string(t1)
    end = new_time_from_string(t2)
    cal_year = get_calendar(cal_name)
    cal_month = cy_get_month(mon, cal_year)
    cal_day = cm_get_day(cal_month, day)

    free_time = free_spans(cal_day, start, end)
    show_time_spans(free_time)
