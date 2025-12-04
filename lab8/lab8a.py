# This code violates abstraction layers, and should be reimplemented in lab 8A.
from cal_abstraction import *


def ts_equals(ts1: TimeSpan, ts2: TimeSpan):
    """Return true iff the two given TimeSpans are equal."""
    ensure_type(ts1, TimeSpan)
    ensure_type(ts2, TimeSpan)
    return (time_equals(ts1.start, ts2.start) and
            time_equals(ts1.end, ts2.end))


def ts_overlap(ts1: TimeSpan, ts2: TimeSpan) -> bool:
    """Return true if the two given TimeSpans overlap."""
    ensure_type(ts1, TimeSpan)
    ensure_type(ts2, TimeSpan)

    return (
            # TS1 isn't strictly after TS2
            time_precedes(ts1.start, ts2.end) and
            # TS2 isn't strictly after ts1
            time_precedes(ts2.start, ts1.end)
    )


def ts_overlapping_part(ts1: TimeSpan, ts2: TimeSpan) -> TimeSpan:
    """Return the overlapping part of two overlapping time spans,
    under the assumption that they really *are* overlapping."""
    ensure_type(ts1, TimeSpan)
    ensure_type(ts2, TimeSpan)
    ensure((ts1, ts2), lambda tup: ts_overlap(tup[0], tup[1]))

    # Tips: Det finns både snyggare och *enklare* sätt
    # att göra detta...
    min1 = max(
        ts1.start.hour.number * 60 + ts1.start.minute.number,  #
        ts2.start.hour.number * 60 + ts2.start.minute.number,
    )
    min2 = min(
        ts1.end.hour.number * 60 + ts1.end.minute.number,  #
        ts2.end.hour.number * 60 + ts2.end.minute.number,
    )
    return TimeSpan(Time(Hour(min1 // 60), Minute(min1 % 60)),
                    Time(Hour(min2 // 60), Minute(min2 % 60)))


def ts_duration(ts: TimeSpan) -> "Duration":
    """Return the duration (length) of a TimeSpan"""
    ensure_type(ts, TimeSpan)

    mins = (
            ts.end.hour.number * 60 + ts.end.minute.number -
            ts.start.hour.number * 60 - ts.start.minute.number
    )
    return Duration(Hour(mins // 60), Minute(mins % 60))


def duration_is_longer_or_equal(d1: Duration, d2: Duration):
    """
    Return true iff the first duration is longer than, or equally as long as,
    the second duration.
    """
    ensure_type(d1, Duration)
    ensure_type(d2, Duration)

    hours1 = d1.hour.number
    hours2 = d2.hour.number
    mins1 = d1.minute.number
    mins2 = d2.minute.number

    return (hours1, mins1) >= (hours2, mins2)


def duration_equals(d1: Duration, d2: Duration):
    """
    Return true iff the first duration is equally as long as,
    the second duration.
    """
    ensure_type(d1, Duration)
    ensure_type(d2, Duration)

    hours1 = d1.hour.number
    hours2 = d2.hour.number
    mins1 = d1.minute.number
    mins2 = d2.minute.number

    return (hours1, mins1) == (hours2, mins2)


if __name__ == "__main__":
    test_timespan_duration()
