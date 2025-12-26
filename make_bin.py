import base64

b64data = """
AAAAAP//AAAAgD8AAAAAAIA/AAAAAAAAgD8AAABAAIA/AAAAgD8AAAAAAIA/AAAAAP//AAAA
AAAAgD8AAAAAAIA/AAAAAP//AAAAgD8AAABAAIA/AAAAAP//AAAAgD8AAAAAAIA/AAAAAAA=
"""

with open("scene.bin", "wb") as f:
    f.write(base64.b64decode(b64data))

print("scene.bin created!")
