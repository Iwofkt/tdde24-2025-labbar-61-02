import calc as c
variable_table = {}

def exec_program(const_calc_program):
    """
    Execute a Calc program represented as a constant list structure.

    param: const_calc_program: list, A Calc program in the form of a
      list structure.
    return: The result of executing the Calc program.
    """
    variable_table.clear()
    p = const_calc_program

    if not c.is_program(p):
        raise Exception(f"Error: {p} is not a valid Calc program.")

    # Extract statements from the program because all programs are of
    # the form ['calc', ...statements...]
    statements = c.program_statements(p)

    # Execute the statements
    result = exec_statements(statements)

    return result


def exec_statements(statements):
    """
    Execute a list of Calc statements.

    param: statements: list, A list of Calc statements.
        return: The result of executing the statements.
    """
    if c.empty_statements(statements):
        return None  # No statements to execute (Base case)

    first_statement = c.first_statement(statements)
    print("First statement:", first_statement)
    rest_statements = c.rest_statements(statements)
    print("Rest statement:", rest_statements)

    # Execute the first statement
    result = exec_statement(first_statement)

    # Recursively execute the rest of the statements
    exec_statements(rest_statements)

    return result


def exec_statement(statement):
    """
    Execute a single Calc statement.

    param: statement: list, A single Calc statement.
    return: The result of executing the statement.
    """

    # Check the type of statement and delegate to the appropriate exec
    # function
    if c.is_assignment(statement):
        print("Assignment statement:", statement)
        return exec_assignment(statement)

    elif c.is_repetition(statement):
        print("Repetition statement:", statement)
        return exec_repetition(statement)

    elif c.is_selection(statement):
        print("Selection statement:", statement)
        return exec_selection(statement)

    elif c.is_output(statement):
        print("Output statement:", statement)
        return exec_output(statement)

    elif c.is_binaryexpr(statement):
        print("binary statement", statement)
        return eval_binaryexpr(statement)
    else:
        raise Exception(f"Error: {statement} is not a valid Calc statement.")


def exec_assignment(statement):
    """
    Execute an assignment statement.

    param: statement: list, An assignment statement.
    return: The result of executing the assignment statement.
    """
    variable = c.assignment_variable(statement)
    expression = c.assignment_expression(statement)
    value = eval_expr(expression)
    print(f"Assigning {value} to variable '{variable}'")
    variable_table[variable] = value

    # Now we just need to store the value in the variable


def exec_repetition(statement):
    """
    Execute a repetition statement.

    param: statement: list, A repetition statement.
    return: The result of executing the repetition statement.
    """


def exec_selection(statement):
    """
    Execute a selection statement.

    param: statement: list, A selection statement.
    return: The result of executing the selection statement.
    """


def exec_input(statement):
    """
    Execute an input statement.

    param: statement: list, An input statement.
    return: The result of executing the input statement.
    """


def exec_output(statement):
    """
    Execute an output statement.

    param: statement: list, An output statement.
    return: The result of executing the output statement.
    """
    print_expr = c.output_expression(statement)
    print_expr = variable_table.get(print_expr, print_expr)
    print(print_expr)


def eval_expr(expression):
    """
    Evaluate a Calc expression.

    param: expression: list/int/float, A Calc expression.
    return: The result of evaluating the expression.
    """

    # Check the type of expression and delegate to the appropriate eval
    # function
    if c.is_constant(expression):
        print("Constant expression:", expression)
        return expression
    elif c.is_binaryexpr(expression):
        print("Binary expression:", expression)
        return eval_binaryexpr(expression)
    elif c.is_variable(expression):
        print("Variable expression:", expression)
        return eval_variable(expression)
    else:
        raise Exception(f"Error: {expression} is not a valid Calc expression.")


def eval_binaryexpr(expression):
    """
    Evaluate a binary expression.

    param: expression: list, A binary expression.
    return: The result of evaluating the binary expression.
    """
    binop = c.binaryexpr_operator(expression)
    left_expr = c.binaryexpr_left(expression)
    right_expr = c.binaryexpr_right(expression)

    left_expr = eval_expr(left_expr)
    right_expr = eval_expr(right_expr)
    if binop == '+':
        print(left_expr + right_expr)
        return left_expr + right_expr
    elif binop == '-':
        print(left_expr - right_expr)
        return left_expr - right_expr
    elif binop == '*':
        print(left_expr * right_expr)
        return left_expr * right_expr
    elif binop == '/':
        print(left_expr / right_expr)
        return left_expr / right_expr
    else:
        raise Exception(f"Error: {binop} is not a valid binary operator")

    # Evaluate left and right expressions


def eval_variable(expression):
    """
    Evaluate a variable expression.

    param: expression: list, A variable expression.
    return: The result of evaluating the variable expression.
    """
    return variable_table.get(expression, expression)


if __name__ == "__main__":
    program_set = ["calc", ["set", "a", 7]]
    program_print_set = ["calc",
                         ["print", "a"],
                         ["set", "a", 0],
                         ["print", "a"]]
    program_add = ["calc", [7, "+", 7]]

    exec_program(program_set)
    print("-----")
    exec_program(program_print_set)
    print("-----")
    exec_program(program_add)
