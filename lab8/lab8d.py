# Write your code for lab 8d here.
from cal_abstraction import CalendarDay, Time
from settings import CHECK_AGAINST_FACIT

#Remove this later
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
    free_span_start = start
    tss = new_time_span_seq([])

    # -- BASE CASES --

    if time_precedes(end, start):
        return tss

    if time_equals(start, end):
        return tss

    if cd_is_empty(cal_day):
        tss_plus_span(tss, new_time_span(start, end))
        return tss

    for app in cd_iter_appointments(cal_day):
        astart: Time = ts_start(app_span(app))
        aend: Time = ts_end(app_span(app))
        check_span = new_time_span(free_span_start, end)

        if not ts_overlap(check_span, app_span(app)):
            continue

        overlap = ts_overlapping_part(check_span, app_span(app))

        if time_precedes(free_span_start, ts_start(overlap)):
            tss_plus_span(tss, new_time_span(free_span_start, ts_start(overlap)))
        
        free_span_start = ts_end(app_span(app))

    if time_precedes(free_span_start, end):
        tss_plus_span(tss, new_time_span(free_span_start, end))
    
    return tss
    '''
        if index == 0:
            if time_precedes_or_equals(end, astart):
                tss_plus_span(tss, new_time_span(start, end))

            elif (time_precedes(start, astart)
                  and time_precedes_or_equals(astart, end)):
                tss_plus_span(tss, new_time_span(start, astart))

        elif index == len(cd_iter_appointments(cal_day) - 1):
            if time_precedes_or_equals(aend, start):
                tss_plus_span(tss, new_time_span(start, end))

            elif (time_precedes(aend, end)
                  and time_precedes_or_equals(start, aend)):
                tss_plus_span(tss, new_time_span(aend, end))

        else:
            if time_precedes(preaend, astart):
                if (time_precedes_or_equals(preaend, start)
                   and time_precedes_or_equals(end, astart)):
                    tss_plus_span(tss, new_time_span(start, end))

                elif (time_precedes_or_equals(start, preaend)
                      and time_precedes_or_equals(end, astart)):
                    if time_precedes(preaend, end):
                        tss_plus_span(tss, new_time_span(preaend, end))

                elif (time_precedes_or_equals(preaend, start)
                      and time_precedes_or_equals(astart, end)):
                    if time_precedes(start, astart):
                        tss_plus_span(tss, new_time_span(start, astart))

                elif (time_precedes_or_equals(start, preaend)
                      and time_precedes_or_equals(astart, end)):
                    if time_precedes(preaend, astart):
                        tss_plus_span(tss, new_time_span(preaend, astart))

        preaend = aend

    return tss'''
