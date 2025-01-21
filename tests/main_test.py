from src.decode import Decode

def test_decode_numero():
    decode = Decode()

    message = "peenjaaveep_xee_aaqiieen*234"

    message_decoded = decode.decode(message=message)

    print(message_decoded)

    assert message_decoded == 'mensagem de alien@123!'
