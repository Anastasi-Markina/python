def print_operation_table(operation, num_rows=6, num_columns=6):
    print('\n'.join(list(map(lambda x: ' '.join(list(map(lambda y: str(operation(x, y)), range(1, num_columns  +1)))), range(1, num_rows + 1)))))


print_operation_table(lambda x, y: x * y)


# def print_operation_table(operation, num_rows=6, num_columns=6):
#     for x in range(1, num_rows + 1):
#         print(*list(map(lambda y: operation(x, y), range(1, num_columns + 1))))


# print_operation_table(lambda x, y: x * y)




