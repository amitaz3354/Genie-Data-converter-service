class BytesDecoder:

    @staticmethod
    def decode_to_string(encoded_file: bytes):
        return encoded_file.decode("utf-8")
