import base64

# Text to base64
def b64(text: str) -> str:
    text = text.encode('ascii')
    return base64.b64encode(text).decode('ascii')
