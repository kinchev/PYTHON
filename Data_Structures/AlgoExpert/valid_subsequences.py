array_input = [int(x) for x in input().split(", ")]
sequence_input = [int(x) for x in input().split(", ")]


# def is_valid_sequence(array, sequence):
#     seq_index = 0
#     for number in array:
#         if len(sequence) == seq_index:
#             break
#
#         if sequence[seq_index] == number:
#             seq_index += 1
#
#     return seq_index == len(sequence)

def is_valid_sequence(array, sequence):
    seq_index = 0
    arr_index = 0

    while seq_index < len(sequence) and arr_index < len(array):
        if array[arr_index] == sequence[seq_index]:
            seq_index += 1
        arr_index += 1

    return seq_index == len(sequence)


print(is_valid_sequence(array_input, sequence_input))
