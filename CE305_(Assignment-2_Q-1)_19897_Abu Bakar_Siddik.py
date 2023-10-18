def crc_encode(original_data, polynomial):
    data = original_data + '0' * (len(polynomial) - 1)
    remainder = data

    # Perform CRC encoding
    for i in range(len(original_data)):
        if remainder[0] == '1':
            xor_result = ''.join(['1' if a != b else '0' for a, b in zip(remainder, polynomial)])
            remainder = xor_result[1:] + data[i + 1:]
        else:
            remainder = remainder[1:]

    encoded_data = original_data + remainder[-(len(polynomial) - 1):]
    return encoded_data

def crc_decode(received_data, polynomial):
    remainder = received_data
    for i in range(len(received_data) - len(polynomial) + 1):
        if remainder[0] == '1':
            xor_result = ''.join(['1' if a != b else '0' for a, b in zip(remainder, polynomial)])
            remainder = xor_result[1:] + received_data[i + 1:]
        else:
            remainder = remainder[1:]

    if '1' in remainder:
        return 'Error'  # CRC detected an error
    else:
        return 'No Error'  # No error detected

# Test cases
original_data1 = '1101'  # 4-bit original binary data
crc_polynomial = '101001'  # 𝑥^5 + 𝑥^2 + 1 in binary form

encoded_data1 = crc_encode(original_data1, crc_polynomial)
print("Encoded Data 1:", encoded_data1)  # Output: '110101'

received_data1 = '110101'  # Received data (without errors)
decoded_result1 = crc_decode(received_data1, crc_polynomial)
print("Decoded Result 1:", decoded_result1)  # Output: 'No Error'

received_data2 = '111101'  # Received data (with 1-bit error)
decoded_result2 = crc_decode(received_data2, crc_polynomial)
print("Decoded Result 2:", decoded_result2)  # Output: 'Error'

