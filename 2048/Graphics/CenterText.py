def center_text(message, free_spaces):
    """
    Center the message using as reference the current free spaces
    then add the half of free spaces in each side of text
    """

    if free_spaces % 2 == 0:
        left_spaces = int(free_spaces / 2) * ' '
        right_spaces = int(free_spaces / 2) * ' '

    else:
        left_spaces = int(free_spaces / 2 + 0.5) * ' '
        right_spaces = int(free_spaces / 2) * ' '

    return left_spaces + message + right_spaces 
