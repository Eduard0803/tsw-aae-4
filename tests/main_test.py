from src.decode import Decode

# def test_decode_message_example_FAIL():
#     decode = Decode()

#     message = "peenjaaveep_xee_aaqiieen*234"

#     message_decoded = decode.decode(message=message)

#     assert message == message_decoded

# def test_decode_number_CORRECT():
#     decode = Decode()

#     message = "0123456789"

#     message_decoded = decode.decode(message=message)

#     assert message_decoded == "9012345678"

# def test_decode_simbol_CORRECT():
#     decode = Decode()

#     message = "*|$_"

#     message_decoded = decode.decode(message=message)

#     assert message_decoded == "@!? "

# def test_decode_consoante_CORRECT():
#     decode = Decode()

#     message = "bcdfghjklmnpqrstvwxyz"

#     message_decoded = decode.decode(message=message)

#     assert message_decoded == "yxwutsqponmkjihgedcba"

def test_decode_vogal_dupla_CORRECT():
    decode = Decode()

    message = "aaeeiioouu"

    message_decoded = decode.decode(message=message)

    print(message_decoded)

    assert message_decoded == "aeiou"
