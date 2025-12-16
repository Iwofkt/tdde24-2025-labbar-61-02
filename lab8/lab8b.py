from cal_abstraction import *
from typing import NamedTuple

# =========================================================================
# Type definition
# =========================================================================

# Define the type somehow...  The initial "" is simply here as a placeholder.
TimeSpanSeq = NamedTuple("TimeSpanSeq", [("time_span_list", list[TimeSpan])])

# =========================================================================
#  Function implementations
# =========================================================================

# Implement these functions!  Also determine if you need *additional* functions.


def new_time_span_seq(span_list=None) -> TimeSpanSeq:
    """
    Create and return a new times span sequence
    """
    if span_list is None:
        return TimeSpanSeq(time_span_list=[])
    return TimeSpanSeq(time_span_list=span_list)


def tss_is_empty(tss: TimeSpanSeq):
    """
    Check if time span sequence is empty
    """
    return not tss.time_span_list


def tss_plus_span(tss: TimeSpanSeq, ts: TimeSpan):
    """
    Add a time span to a time span sequence
    """
    ensure_type(tss, TimeSpanSeq)
    ensure_type(ts, TimeSpan)

    def add_timespan(add_ts: TimeSpan, timespan_list: List[TimeSpan]):
        if not timespan_list or time_precedes(
                ts_start(add_ts), ts_start(timespan_list[0])
        ):
            return [add_ts] + timespan_list
        else:
            return [timespan_list[0]] + add_timespan(add_ts, timespan_list[1:])

    return new_time_span_seq(
        add_timespan(ts, tss.time_span_list)
    )


def tss_iter_spans(tss):
    """
    Return the time span list in a sequence
    """
    ensure_type(tss, TimeSpanSeq)
    for time_span in tss.time_span_list:
        yield time_span


def show_time_spans(tss):
    """
    print a time span sequence
    """
    for time_span in tss_iter_spans(tss):
        print(time_span)


# Keep only time spans that satisfy pred.
# You do not need to modify this function.
def tss_keep_spans(tss, pred):
    result = new_time_span_seq()
    for span in tss_iter_spans(tss):
        if pred(span):
            result = tss_plus_span(result, span)

    return result
