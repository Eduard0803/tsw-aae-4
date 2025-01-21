from src.decode import Decode

if __name__ == "__main__":
    decode = Decode()

    message = "peenjaaveep_xee_aaqiieen*234"

    message_decoded = decode.decode(message=message)

    print(message_decoded)
