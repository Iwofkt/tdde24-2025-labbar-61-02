import calc as c
import copy


def exec_program(const_calc_program, table: dict = {}):
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
    variable_table = exec_statements(statements, table)
    return variable_table


def exec_statements(statements, table):
    """
    STATEMENTS =
        STATEMENT
      | STATEMENT, COMMA, STATEMENTS

    Execute a list of Calc statements.

    param: statements: list, A list of Calc statements.
    return: The result of executing the statements.
    """
    print("Executing statements:", statements)
    if c.empty_statements(statements):
        return None  # No statements to execute (Base case)

    first_statement = c.first_statement(statements)
    print("First statement:", first_statement)
    rest_statements = c.rest_statements(statements)
    print("Rest statement:", rest_statements)

    # Execute the first statement
    variable_table = exec_statement(first_statement, table)

    # Recursively execute the rest of the statements
    variable_table = exec_statements(rest_statements, variable_table)

    return variable_table


def exec_statement(statement, table):
    """
    STATEMENT =
        ASSIGNMENT
      | REPETITION
      | SELECTION
      | INPUT
      | OUTPUT
    Execute a single Calc statement.

    param: statement: list, A single Calc statement.
    return: The result of executing the statement.
    """

    # Check the type of statement and delegate to the appropriate exec
    # function
    if c.is_assignment(statement):
        print("Assignment statement:", statement)
        return exec_assignment(statement, table)

    elif c.is_repetition(statement):
        print("Repetition statement:", statement)
        return exec_repetition(statement, table)

    elif c.is_selection(statement):
        print("Selection statement:", statement)
        return exec_selection(statement)

    elif c.is_input(statement):
        print("Input statement:", statement)
        return exec_input(statement, table)

    elif c.is_output(statement):
        print("Output statement:", statement)
        return exec_output(statement, table)

    else:
        raise Exception(f"Error: {statement} is not a valid Calc statement.")


def exec_assignment(statement, table):
    """
    ASSIGNMENT = '[', "'set'", COMMA, VARIABLE, COMMA, EXPRESSION, ']'

    Execute an assignment statement.

    param: statement: list, An assignment statement.
    return: The result of executing the assignment statement.
    """

    variable = c.assignment_variable(statement)
    expression = c.assignment_expression(statement)
    value = eval_expr(expression, table)
    variable_table = copy.deepcopy(table)

    print(f"Assigning {value} to variable '{variable}'")
    variable_table[variable] = value
    return variable_table


def exec_repetition(statement, table):
    """
    REPETITION = '[', "'while'", COMMA, CONDITION, COMMA, STATEMENTS, ']'

    Execute a repetition statement.

    param: statement: list, A repetition statement.
    return: The result of executing the repetition statement.
    """
    condition = c.repetition_condition(statement)
    print("Repetition condition:", condition)
    statements = c.repetition_statements(statement)
    print("Repetition statements:", statements)

    while eval_expr(condition, table):
        '''print(
            f"Repetition condition is true; executing statements: {statements}"
            )'''
        exec_statements(statements, table)


def exec_selection(statement, table):
    """
    SELECTION = '[', "'if'", COMMA, CONDITION, COMMA,
      STATEMENT, [COMMA, STATEMENT], ']'

    Execute a selection statement.

    param: statement: list, A selection statement.
    return: The result of executing the selection statement.
    """
    condition = c.selection_condition(statement)
    print("Selection condition:", condition)
    then_statement = c.selection_true_branch(statement)
    print("Then statement:", then_statement)

    if c.selection_has_false_branch(statement):
        print("Else statement exists.")
        else_statement = c.selection_false_branch(statement)
    else:
        else_statement = None

    if eval_expr(condition, table):
        print("Selection condition is true; executing then branch.")
        exec_statement(then_statement)
    elif else_statement is not None:
        print("Selection condition is false; executing else branch.")
        exec_statement(else_statement)


def exec_input(statement, table):
    """
    INPUT = '[', "'read'", COMMA, VARIABLE, ']' ;

    Execute an input statement.

    param: statement: list, An input statement.
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

    variable_table = copy.deepcopy(table)
    variable_table[variable] = value
    return variable_table


def exec_output(statement, table):
    """
    Execute an output statement.

    param: statement: list, An output statement.
    return: The result of executing the output statement.
    """
    print_expr = c.output_expression(statement)
    print_expr_value = table.get(print_expr, print_expr)
    print(print_expr, "=", print_expr_value)


def eval_expr(expression, table):
    """
    Evaluate a Calc expression.

    param: expression: list/int/float, A Calc expression.
    return: The result of evaluating the expression.
    """

    # Check the type of expression and delegate to the appropriate eval
    # function
    print("Evaluating expression:", expression)
    if c.is_constant(expression):
        print("Constant expression:", expression)
        return expression

    elif c.is_variable(expression):
        print("Variable expression:", expression)
        return eval_variable(expression, table)

    elif c.is_binaryexpr(expression):
        print("Binary expression:", expression)
        return eval_binaryexpr(expression, table)
    elif c.is_condition(expression):
        print("Condition expression:", expression)
        return eval_condition(expression, table)

    else:
        raise Exception(f"Error: {expression} is not a valid Calc expression.")


def eval_binaryexpr(expression, table):
    """
    Evaluate a binary expression.

    param: expression: list, A binary expression.
    return: The result of evaluating the binary expression.
    """
    binop = c.binaryexpr_operator(expression)
    left_expr = c.binaryexpr_left(expression)
    right_expr = c.binaryexpr_right(expression)

    left_expr = eval_expr(left_expr, table)
    right_expr = eval_expr(right_expr, table)
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


def eval_variable(expression, table):
    """
    Evaluate a variable expression.

    param: expression: list, A variable expression.
    return: The result of evaluating the variable expression.
    """
    return table.get(expression, expression)


def eval_condition(expression, table):
    """
    Evaluate a condition expression.

    param: expression: list, A condition expression.
    return: The result of evaluating the condition expression.
    """
    condop = c.condition_operator(expression)
    left_expr = c.condition_left(expression)
    right_expr = c.condition_right(expression)

    left_expr = eval_expr(left_expr, table)
    right_expr = eval_expr(right_expr, table)

    if condop == '=':
        print(left_expr == right_expr)
        return left_expr == right_expr
    elif condop == '<':
        print(left_expr < right_expr)
        return left_expr < right_expr
    elif condop == '>':
        print(left_expr > right_expr)
        return left_expr > right_expr
    else:
        raise Exception(f"Error: {condop} is not a valid condition operator")


if __name__ == "__main__":
    _set_a_prog = ["calc", ["set", "a", 7]]
    _print_and_set_a_prog = ["calc", ["print", "a"], ["set", "a", 0]]
    _input_a_prog = ["calc", ["read", "a"]]
    _print_a_prog = ["calc", ["print", "a"]]
    _print_if_prog = ["calc", ["if", ["a", ">", "b"], ["print", "a"],
                                     ["print", "a"]]]
    _read_and_print_a_prog = ["calc", ["read", "a"], ["print", "a"]]
    _if_prog = [
        "calc",
        ["read", "x"],
        ["set", "zero", 0],
        ["set", "pos", 1],
        ["set", "nonpos", -1],
        ["if", ["x", "=", 0], ["print", "zero"]],
        ["if", ["x", ">", 0], ["print", "pos"]],
        ["if", ["x", "<", 0], ["print", "nonpos"]],
    ]
    _if_set_prog = [
        "calc",
        ["read", "x"],
        ["if", ["x", ">", 0], ["set", "a", 1], ["set", "a", -1]],
        ["if", ["x", "=", 0], ["set", "a", 0]],
    ]
    _loop_prog = [
        "calc",
        ["read", "n"],
        ["set", "sum", 0],
        [
            "while",
            ["n", ">", 0],
            ["set", "sum", ["sum", "+", "n"]],
            ["set", "n", ["n", "-", 1]],
        ],
        ["print", "sum"],
    ]
    _loop_with_binexpr_prog = [
        "calc",
        ["read", "n"],
        ["set", "sum", 0],
        [
            "while",
            [["n", "-", 1], ">", 0],
            ["set", "sum", ["sum", "+", "n"]],
            ["set", "n", ["n", "-", 1]],
        ],
        ["print", "sum"],
    ]
    exec_program(_set_a_prog)
    print("-----")
    exec_program(_loop_with_binexpr_prog)
    print("-----")
    exec_program(_if_set_prog)
    print("-----")
    exec_program(_loop_prog)
    print("-----")
    exec_program(_if_prog)
    print("-----")
    exec_program(_read_and_print_a_prog)
    print("-----")
    exec_program(_print_if_prog)
    print("-----")
    exec_program(_print_a_prog)
    print("-----")
    exec_program(_input_a_prog)
    print("-----")
    exec_program(_print_and_set_a_prog)
