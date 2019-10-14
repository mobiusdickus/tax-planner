import base64


def decode_base64(data, filename):
    with open(filename, "wb") as fh:
        fh.write(base64.b64decode(data))
