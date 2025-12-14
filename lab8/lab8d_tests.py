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
        exp_result="Invalid time interval"
    )  # Expected invalid input

    # Start time same time as end time
    store_test_case(
        test_cases,
        3,
        start_str="21:00",  # Search interval starts
        end_str="21:00",  # Search interval ends
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
        5,
        start_str="05:00",  # Search interval starts
        end_str="21:00",  # Search interval ends
        booking_data=[],  # This day's appointments
        exp_result=["05:00-21:00"],
    )  # Expected free time

    print("Test cases generated.")

    return test_cases


if __name__ == '__main__':
    # Actually run the tests, using the test driver functions
    tests = create_tests_for_free_span()
    run_free_spans_tests(tests)
