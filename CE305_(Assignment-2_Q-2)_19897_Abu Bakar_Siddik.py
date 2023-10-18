def HamEncoding(msg):
    # Calculate the number of extra parity bits (k)
    m = len(msg)
    k = 1
    while 2**k < m + k + 1:
        k += 1

    # Create a list to store the encoded message
    encoded_msg = [0] * (m + k)
    
    # Initialize the position of parity bits
    j = 0

    # Fill in the positions of parity bits with zeros
    for i in range(1, m + k + 1):
        if i == 2**j:
            j += 1
        else:
            encoded_msg[i - 1] = int(msg[i - j - 1])

    # Calculate the values of the parity bits
    for j in range(k):
        mask = 2**j
        parity = 0
        for i in range(1, m + k + 1):
            if (i & mask) == 2**j:
                parity ^= encoded_msg[i - 1]
        encoded_msg[2**j - 1] = parity

    # Convert the list to a string and return the encoded message
    encoded_msg_str = ''.join(map(str, encoded_msg))
    return encoded_msg_str

def HamDecoding(rcv, k):
    received_msg = list(map(int, rcv))
    m = len(received_msg) - k

    # Calculate the values of the parity bits for error detection
    error_positions = [0] * k
    for j in range(k):
        mask = 2**j
        parity = 0
        for i in range(1, m + k + 1):
            if (i & mask) == 2**j:
                parity ^= received_msg[i - 1]
        error_positions[j] = parity

    # Check for errors and correct if possible
    error_location = sum([2**j for j, error in enumerate(error_positions) if error])
    if error_location == 0:
        return 'No error'

    # Correct the error
    received_msg[error_location - 1] ^= 1

    # Convert the list to a string and return the corrected message
    corrected_msg_str = ''.join(map(str, received_msg))
    return f'Error at Position {error_location}, and correct data: {corrected_msg_str}'

# Test cases
org_sig1 = '1101'  # original binary data
encoded_msg1 = HamEncoding(org_sig1)
print(encoded_msg1)  # Output: '1010101'

org_sig2 = '1001011'  # original binary data
encoded_msg2 = HamEncoding(org_sig2)
print(encoded_msg2)  # Output: '10110010011'

received_sig1 = '1010101'  # if receiving the data without error
k1 = 3
decoded_result1 = HamDecoding(received_sig1, k1)
print(decoded_result1)  # Output: 'No error'

received_sig2 = '1010001'  # if receiving the data with 1-bit error at Position 5
k2 = 3
decoded_result2 = HamDecoding(received_sig2, k2)
print(decoded_result2)  # Output: 'Error at Position 5, and correct data: 1010101'

received_sig3 = '10110010011'  # if receiving the data without error
k3 = 4
decoded_result3 = HamDecoding(received_sig3, k3)
print(decoded_result3)  # Output: 'No error'

received_sig4 = '10110000011'  # if receiving the data with 1-bit error at Position 7
k4 = 4
decoded_result4 = HamDecoding(received_sig4, k4)
print(decoded_result4)  # Output: 'Error at Position 7, and correct data: 10110010011'
