# -- TESTING CODE -- #

def upg6_tests(exec_program):

    print("Testing Calc interpreter with working sample programs:")

    print("------------------------")

    print("Testing selection functionality")
    equal = ['calc',
             ['if', [5, '=', 5], ['print', 10]]
             ]
    exec_program(equal)

    print("------------------------")

    print("Testing print functionality with conditions")
    equal_print = ['calc', ['print', [5, '=', 5]]]
    exec_program(equal_print)

    factorial = ['calc',
                 ['read', 'n'],
                 ['set', 'result', 1],
                 ['while', ['n', '>', 1],
                  ['set', 'result', ['result', '*', 'n']],
                  ['set', 'n', ['n', '-', 1]]
                  ], ['print', 'result']
                 ]
    exec_program(factorial)

    print("------------------------")

    print("Given example to test fibonacci sequence.")
    # Fibonacci-sekvens: F(n) = F(n-1) + F(n-2)
    fibonacci = ['calc',
                 ['read', 'n'],
                 ['set', 'a', 0],
                 ['set', 'b', 1],
                 ['set', 'i', 1],
                 ['while', ['i', '<', 'n'],
                  ['set', 'temp', 'b'],
                  ['set', 'b', ['a', '+', 'b']],
                  ['set', 'a', 'temp'],
                  ['set', 'i', ['i', '+', 1]]
                  ], ['print', 'b']
                 ]
    exec_program(fibonacci)

    print("------------------------")

    print("Given example to find minimum value")
    # Read n digits and find the smallest one
    find_min = ['calc',
                ['set', 'min', float('inf')],
                ['read', 'n'],
                ['set', 'count', 0],
                ['while', ['count', '<', 'n'],
                 ['read', 'num'],
                 ['if', ['num', '<', 'min'],
                  ['set', 'min', 'num']
                  ], ['set', 'count', ['count', '+', 1]]
                 ], ['print', 'min']
                ]
    exec_program(find_min)

    print("------------------------")

    print("Testing Calc interpreter with defect sample programs:")

    print("Catching that variables can't be asigned strings")
    # Test asigning variable a string value
    print_text = ['calc',
                  ['set', 'text', "'Hello'"],
                  ['print', 'text']
                  ]
    try:
        exec_program(print_text)

    except Exception as e:
        print("Got given error", e, "which is good!")

    print("------------------------")

    print("Catching that calc programs not starting with calc is being caught")

    # Test a program without calc in the beginning
    no_clac = [
                  ['set', 'text', 5],
                  ['print', 'text']
                  ]
    try:
        exec_program(no_clac)

    except Exception as e:
        print("Got given error", e, "which is good!")

    print("------------------------")

    print("Program with invalid binary operand")

    # Test a program with invalid binary operand
    modulo = ['calc',
              ['set', 'variable', [5, '<=', 2]],
              ['print', 'variable']
              ]
    try:
        exec_program(modulo)

    except Exception as e:
        print("Got given error", e, "which is good!")

    print("------------------------")

    print("Program with invalid condition operand")

    # Test a program with invalid condition operand
    big_or_equal = ['calc',
                    ['if', [5, '>=', 2]],
                    ['print', 10]
                    ]
    try:
        exec_program(big_or_equal)

    except Exception as e:
        print("Got given error", e, "which is good!")

    print("------------------------")

    print("Passed all tests.")
