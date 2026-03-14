# Write your code for lab 8d here.

from test_driver import store_test_case, run_free_spans_tests

# Create additional test cases, and add to them to create_tests_for_free_span().


def create_tests_for_free_span() -> dict:
    """Create and return a number of test cases for the free_spans function"""
    test_cases = dict()

    store_test_case(
        test_cases,
        1,
        start_str="08:00",  # Search interval starts
        end_str="21:00",  # Search interval ends
        booking_data=["07:00-09:00", "13:00-18:00"],  # This day's appointments
        exp_result=["09:00-13:00", "18:00-21:00"],
    )  # Expected free time

    # -------- YOUR TEST CASES GO HERE -----------------------
    # For each case, add a brief description of what you want to test.

    # Start time after end time
    store_test_case(
        test_cases,
        2,
        start_str="12:00",  # Search interval starts
        end_str="11:00",  # Search interval ends
        booking_data=["07:00-09:00", "13:00-18:00"],  # This day's appointments
        exp_result=[],
    )  # Expected invalid input

    # Start time same time as end time
    store_test_case(
        test_cases,
        3,
        start_str="11:00",  # Search interval starts
        end_str="11:00",  # Search interval ends
        booking_data=["07:00-09:00", "13:00-18:00"],  # This day's appointments
        exp_result=[],
    )  # Expected no free time

    # Start and end time after all appointments
    store_test_case(
        test_cases,
        4,
        start_str="22:00",  # Search interval starts
        end_str="23:00",  # Search interval ends
        booking_data=["07:00-09:00", "13:00-18:00"],  # This day's appointments
        exp_result=["22:00-23:00"],
    )  # Expected no free time

    # Start and end time before all appointments
    store_test_case(
        test_cases,
        5,
        start_str="05:00",  # Search interval starts
        end_str="06:00",  # Search interval ends
        booking_data=["07:00-09:00", "13:00-18:00"],  # This day's appointments
        exp_result=["05:00-06:00"],
    )  # Expected free time

    # Calender day has no appointments
    store_test_case(
        test_cases,
        6,
        start_str="05:00",  # Search interval starts
        end_str="21:00",  # Search interval ends
        booking_data=[],  # This day's appointments
        exp_result=["05:00-21:00"],
    )  # Expected free time

    # Calander day with 3 appointments inside checkspan
    store_test_case(
        test_cases,
        7,
        start_str="05:00",
        end_str="21:00",
        booking_data=["06:00-08:00", "10:00-11:00", "14:00-15:00"],
        exp_result=["05:00-06:00", "08:00-10:00", "11:00-14:00", "15:00-21:00"],
    )

    # Calander day with 3 appointments with first appointment outside checkspan
    store_test_case(
        test_cases,
        8,
        start_str="09:00",
        end_str="21:00",
        booking_data=["06:00-08:00", "10:00-11:00", "14:00-15:00"],
        exp_result=["09:00-10:00", "11:00-14:00", "15:00-21:00"],
    )

    # Calander day with 3 appointments with last appointment outside checkspan
    store_test_case(
        test_cases,
        9,
        start_str="05:00",
        end_str="13:00",
        booking_data=["06:00-08:00", "10:00-11:00", "14:00-15:00"],
        exp_result=["05:00-06:00", "08:00-10:00", "11:00-13:00"],
    )

    # Calander day with 3 appointments with start time inside appointment
    store_test_case(
        test_cases,
        10,
        start_str="07:00",
        end_str="21:00",
        booking_data=["06:00-08:00", "10:00-11:00", "14:00-15:00"],
        exp_result=["08:00-10:00", "11:00-14:00", "15:00-21:00"],
    )

    # Calander day with 3 appointments with end time inside appointment
    store_test_case(
        test_cases,
        11,
        start_str="05:00",
        end_str="14:30",
        booking_data=["06:00-08:00", "10:00-11:00", "14:00-15:00"],
        exp_result=["05:00-06:00", "08:00-10:00", "11:00-14:00"],
    )

    # Calander day with 3 appointments with both start and end inside appointments
    store_test_case(
        test_cases,
        12,
        start_str="07:00",
        end_str="14:30",
        booking_data=["06:00-08:00", "10:00-11:00", "14:00-15:00"],
        exp_result=["08:00-10:00", "11:00-14:00"],
    )

    # Check for a timespan that is completely covered by a booking
    store_test_case(
        test_cases,
        13,
        start_str="07:00",
        end_str="08:00",
        booking_data=["07:00-08:00"],
        exp_result=[],
    )

    # Check for a timespan that is completely covered by multiple bookings
    store_test_case(
        test_cases,
        13,
        start_str="07:00",
        end_str="09:00",
        booking_data=["07:00-08:00", "08:00-09:00"],
        exp_result=[],
    )

    print("Test cases generated.")

    return test_cases


if __name__ == "__main__":
    # Actually run the tests, using the test driver functions
    tests = create_tests_for_free_span()
    run_free_spans_tests(tests)
