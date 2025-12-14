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
    return TimeSpanSeq(time_span_list=span_list)


def tss_is_empty(tss: TimeSpanSeq):
    """
    Check if time span sequence is empty
    """
    if tss_iter_spans(tss):
        return False
    return True


def tss_plus_span(tss: TimeSpanSeq, ts: TimeSpan):
    """
    Add a time span to a time span sequence
    """
    for index, time_span in enumerate(tss_iter_spans(tss)):
        if time_precedes_or_equals(ts_start(time_span), ts_start(ts)):
            tss_iter_spans(tss).insert(index + 1, ts)


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
