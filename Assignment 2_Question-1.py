def xor_calculation(input1, input2):
    output = []
    for i in range(len(input2)):
        if input1[i] == input2[i]:
            output.append('0')
        else:
            output.append('1')
    return ''.join(output)

def message_encoding(binary_message, generator_poly):
    temp_var = binary_message + '00000'
    remainder = temp_var
    for i in range(len(binary_message)):
        if remainder[i] == '1':
            xor_result = xor_calculation(remainder[i:i + len(generator_poly)], generator_poly)
            remainder = remainder[:i] + xor_result + remainder[i + len(xor_result):]
    crc_value = remainder[len(binary_message):len(binary_message) + len(generator_poly) - 1]
    encoded_output = binary_message + crc_value
    print("The encoded output of the given number is :", encoded_output)

def message_decoding(received_message, generator_poly):
    remainder = received_message
    for i in range(len(received_message) - len(generator_poly) + 1):
        if remainder[i] == '1':
            xor_result = xor_calculation(remainder[i:i + len(generator_poly)], generator_poly)
            remainder = remainder[:i] + xor_result + remainder[i + len(xor_result):]
    if remainder[-(len(generator_poly) - 1):] == '0' * (len(generator_poly) - 1):
        print("No Error")
    else:
        print('Error!!!!!!!!!!!!!!')

# Test cases
binary_message = "110011111"
generator_poly = "100101"

message_encoding(binary_message, generator_poly)

received_message = "1100111110010"
message_decoding(received_message, generator_poly)