def replace(array, fake_len: int):
    real_len = len(array)
    diff_len = real_len - fake_len

    spaces_remaining = diff_len / 2
    write_position = real_len - 1
    index = fake_len - 1

    while spaces_remaining > 0:
        if array[index] != " ":
            array[write_position] = array[index]
            write_position -= 1
        else:
            for char in reversed(replacement):
                array[write_position] = char
                write_position -= 1

            spaces_remaining -= 1

        index -= 1

    return "".join(array)


def calculate_fake_len(input_len, replacement_len, quantity_to_replace):
    return int(input_len - (replacement_len - 1) * (quantity_to_replace / replacement_len))


replacement = "&32"
to_replace = " "

print("Digite o vetor de caracteres de entrada:")
input_array = list(input())

length = calculate_fake_len(len(input_array), len(replacement), input_array.count(to_replace))

print(replace(input_array, length))
