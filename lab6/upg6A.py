import calc as c
import copy


# -- EXECUTION FUNCTIONS -- #


def exec_program(const_calc_program: list, table: dict = {}):
    """
    PROGRAM = '[', "'calc'", COMMA, STATEMENTS, ']
    Execute a Calc program represented as a constant list structure.

    param: const_calc_program: list, A Calc program in the form of a
      list structure.
    return: The result of executing the Calc program.
    """
    p = const_calc_program

    if not c.is_program(p):
        raise Exception(f"Error: {p} is not a valid Calc program.")

    # Extract statements from the program
    statements = c.program_statements(p)

    # Execute the statements
    variable_table = copy.deepcopy(table)
    variable_table = exec_statements(statements, variable_table)
    return variable_table


def exec_statements(statements, table: dict):
    """
    STATEMENTS =
        STATEMENT
      | STATEMENT, COMMA, STATEMENTS

    Execute a list of Calc statements.

    param: statements: list, A list of Calc statements.
    param: table: dict, The current variable table.
    return: The result variable tables of executing the list of statements.
    """
    if c.empty_statements(statements):
        return table  # Return current table (Base case)

    first_statement = c.first_statement(statements)
    rest_statements = c.rest_statements(statements)

    # Execute the first statement
    variable_table = exec_statement(first_statement, table)

    # Recursively execute the rest of the statements
    variable_table = exec_statements(rest_statements, variable_table)

    return variable_table


def exec_statement(statement, table: dict):
    """
    STATEMENT =
        ASSIGNMENT
      | REPETITION
      | SELECTION
      | INPUT
      | OUTPUT
    Execute a single Calc statement.

    param: statement: list, A single Calc statement.
    param: table: dict, The current variable table.
    return: The result variable table of executing the statement.
    """
    # Check the type of statement and delegate to the appropriate exec function
    if c.is_assignment(statement):
        return exec_assignment(statement, table)
    elif c.is_repetition(statement):
        return exec_repetition(statement, table)
    elif c.is_selection(statement):
        return exec_selection(statement, table)
    elif c.is_input(statement):
        return exec_input(statement, table)
    elif c.is_output(statement):
        return exec_output(statement, table)
    else:
        raise Exception(f"Error: {statement} is not a valid Calc statement.")


def exec_assignment(statement, table: dict):
    """
    ASSIGNMENT = '[', "'set'", COMMA, VARIABLE, COMMA, EXPRESSION, ']'

    Execute an assignment statement.

    param: statement: list, An assignment statement.
    param: table: dict, The current variable table.
    return: The updated variable table after executing the assignment.
    """
    variable = c.assignment_variable(statement)
    expression = c.assignment_expression(statement)
    value = eval_expr(expression, table)

    # o we need this deepcopy?
    variable_table = copy.deepcopy(table)
    variable_table[variable] = value
    return variable_table


def exec_repetition(statement, table: dict):
    """
    REPETITION = '[', "'while'", COMMA, CONDITION, COMMA, STATEMENTS, ']'

    Execute a repetition statement.

    param: statement: list, A repetition statement.
    param: table: dict, The current variable table.
    return: The result of executing the repetition statement.
    """
    condition = c.repetition_condition(statement)
    statements = c.repetition_statements(statement)

    # Do we need this deepcopy?
    current_table = copy.deepcopy(table)

    while eval_expr(condition, current_table):
        current_table = exec_statements(statements, current_table)

    return current_table


def exec_selection(statement, table: dict):
    """
    SELECTION = '[', "'if'", COMMA, CONDITION, COMMA,
      STATEMENT, [COMMA, STATEMENT], ']'

    Execute a selection statement.

    param: statement: list, A selection statement.
    param: table: dict, The current variable table.
    return: The result of executing the selection statement.
    """
    condition = c.selection_condition(statement)
    then_statement = c.selection_true_branch(statement)

    if c.selection_has_false_branch(statement):
        else_statement = c.selection_false_branch(statement)
    else:
        else_statement = None

    if eval_expr(condition, table):
        return exec_statement(then_statement, table)
    elif else_statement is not None:
        return exec_statement(else_statement, table)
    else:
        return table


def exec_input(statement, table: dict):
    """
    INPUT = '[', "'read'", COMMA, VARIABLE, ']' ;

    Execute an input statement.

    param: statement: list, An input statement.
    param: table: dict, The current variable table.
    return: The result of executing the input statement.
    """
    variable = c.input_variable(statement)
    user_input = input(f"Enter value for {variable}: ")
    try:
        value = int(user_input)
    except ValueError:
        try:
            value = float(user_input)
        except ValueError:
            raise Exception(
                f"Error: Invalid input '{user_input}'"
                f"for variable '{variable}'." "Expected a number."
            )

    # Do we need this deepcopy?
    variable_table = copy.deepcopy(table)
    variable_table[variable] = value
    return variable_table


def exec_output(statement, table: dict):
    """
    Execute an output statement.

    param: statement: list, An output statement.
    param: table: dict, The current variable table.
    return: The result of executing the output statement.
    """
    print_expr = c.output_expression(statement)
    print_expr_value = eval_expr(print_expr, table)
    print(f"{print_expr} = {print_expr_value}")

    return table


# -- EVALUATION FUNCTIONS -- #


def eval_expr(expression, table):
    """
    Evaluate a Calc expression.

    param: expression: list/int/float, A Calc expression.
    return: The result of evaluating the expression.
    """
    if c.is_constant(expression):
        return expression
    elif c.is_variable(expression):
        return eval_variable(expression, table)
    elif c.is_binaryexpr(expression):
        return eval_binaryexpr(expression, table)
    elif c.is_condition(expression):
        return eval_condition(expression, table)


def eval_binaryexpr(expression, table: dict):
    """
    Evaluate a binary expression.

    param: expression: list, A binary expression.
    return: The result of evaluating the binary expression.
    """
    binop = c.binaryexpr_operator(expression)
    left_expr = c.binaryexpr_left(expression)
    right_expr = c.binaryexpr_right(expression)

    left_val = eval_expr(left_expr, table)
    right_val = eval_expr(right_expr, table)

    if binop == '+':
        return left_val + right_val
    elif binop == '-':
        return left_val - right_val
    elif binop == '*':
        return left_val * right_val
    elif binop == '/':
        return left_val / right_val


def eval_variable(expression, table):
    """
    Evaluate a variable expression.

    param: expression: list, A variable expression.
    return: The result of evaluating the variable expression.
    """
    # If variable exists in table, return its value, otherwise raise error
    if expression in table:
        return table[expression]
    else:
        raise Exception(f"Error: Variable '{expression}' is not defined.")


def eval_condition(expression, table: dict):
    """
    Evaluate a condition expression.

    param: expression: list, A condition expression.
    return: The result of evaluating the condition expression.
    """
    condop = c.condition_operator(expression)
    left_expr = c.condition_left(expression)
    right_expr = c.condition_right(expression)

    left_val = eval_expr(left_expr, table)
    right_val = eval_expr(right_expr, table)

    if condop == '=':
        return left_val == right_val
    elif condop == '<':
        return left_val < right_val
    elif condop == '>':
        return left_val > right_val
