from lab6 import calc as c


def exec_program(const_calc_program):
    """
    Execute a Calc program represented as a constant list structure.

    param: const_calc_program: list, A Calc program in the form of a
      list structure.
    return: The result of executing the Calc program.
    """
    p = const_calc_program

    if not c.is_program(p):
        raise Exception(f"Error: {p} is not a valid Calc program.")

    # Extract statements from the program because all programs are of the form
    # ['calc', ...statements...]
    statements = c.program_statements(p)

    # Execute the statements
    result = execute_statements(statements)

    return result


def execute_statements(statements):
    """
    Execute a list of Calc statements.

    param: statements: list, A list of Calc statements.
        return: The result of executing the statements.
    """
    if c.empty_statements(statements):
        return None  # No statements to execute
    first_statement = c.first_statement(statements)
    print(first_statement)
    rest_statements = c.rest_statements(statements)
    print(rest_statements)

    # Execute the first statement
    result = execute_statement(first_statement)

    # Recursively execute the rest of the statements
    execute_statements(rest_statements)

    return result


def execute_statement(statement):
    """
    Execute a single Calc statement.

    param: statement: list, A single Calc statement.
    return: The result of executing the statement.
    """
    if c.is_assignment(statement):

    elif c.is_repetition(statement):
    
    elif c.is_selection(statement):

