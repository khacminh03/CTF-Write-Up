import base64

hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

bytes_input = bytes.fromhex(hex_string)

encoded_base64 = base64.b64encode(bytes_input)

print(encoded_base64)
