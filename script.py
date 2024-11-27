import os, sys, random, string, time
import requests

# Line Function 
def linex():
    print('\033[0m================================================')

# Logo For script 
logo = """
\x1b[38;5;46m     ▗▖  ▗▖ ▗▄▖ ▗▄▄▄  ▗▄▄▄▖▗▄▄▖  ▗▄▖▗▖  ▗▖
\x1b[38;5;47m     ▐▛▚▖▐▌▐▌ ▐▌▐▌  █ ▐▌   ▐▌ ▐▌▐▌ ▐▌▝▚▞▘
\x1b[38;5;48m     ▐▌ ▝▜▌▐▌ ▐▌▐▌  █ ▐▛▀▀▘▐▛▀▘ ▐▛▀▜▌ ▐▌
\x1b[38;5;49m     ▐▌  ▐▌▝▚▄▞▘▐▙▄▄▀ ▐▙▄▄▖▐▌   ▐▌ ▐▌ ▐▌\x1b[38;5;46m V/0.1
\033[0m================================================
 \033[1;35m        Developer : Saifur Rahman Siam
         YouTube   : Noob Programmer
         GitHub    : github.com/nbprg
         Telegram  : @TataCuto
\033[0m================================================"""

# Get proxies automatically by scraping a proxy list website
def get_proxies():
    try:
        proxies = requests.get('https://www.proxy-list.download/api/v1/get?type=https').text
        return proxies.splitlines()
    except Exception as e:
        print(f"⚠️ Error scraping proxies: {str(e)}")
        return []

# Get Captcha token 
def get_token():
    while True:
        res = requests.get(f'http://localhost:5000/get').text
        if not 'None' in res:
            print(f'\r\r\033[0m>>\033[1;32m Captcha token get successful \033[0m')
            return res
        else:
            time.sleep(0.5)

# Clear terminal session & print logo
def clear_screen():
    if sys.platform.startswith('win'):
        os.system('cls'); print(logo)
    else:
        os.system('clear'); print(logo)

# Validate proxy by checking connection to a known endpoint
def validate_proxy(proxy_url):
    try:
        proxy = {'http': proxy_url, 'https': proxy_url}
        response = requests.get('http://ip-api.com/json', proxies=proxy, timeout=5)
        return response.json()['query']  # Return IP address if proxy works
    except:
        return None  # Return None if proxy is invalid

# Get headers set with `auth_token` or head only
def get_headers(auth_token=None):
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'origin': 'https://app.nodepay.ai',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
    }
    if auth_token:
        headers['Authorization'] = f'Bearer {auth_token}'
        headers['origin'] = 'chrome-extension://lgmpfmgeabnnlemejacfljbmonaomfmm'
    return headers

# Registration account
def reg_account(email, password, username, ref_code, proxy_url=None, captcha_token=None):
    try:
        if proxy_url:
            print(f'\r\r\033[0m>>\033[1;32m Proxy: {proxy_url} \033[0m')
            proxy_url = {'http': proxy_url, 'https': proxy_url}
        register_data = {
            'email': email,
            'password': password,
            'username': username,
            'referral_code': ref_code,
            'recaptcha_token': captcha_token
        }
        headers = get_headers()
        url = "https://api.nodepay.ai/api/auth/register"
        response = requests.post(url, headers=headers, json=register_data, proxies=proxy_url, timeout=5)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f'\r\r\033[31m⚠️ Error: {str(e)} \033[0m')
        linex()
        time.sleep(1)

# Login account and get authorization token
def login_account(email, password, captcha_token, proxy_url):
    try:
        json_data = {
            'user': email,
            'password': password,
            'remember_me': True,
            'recaptcha_token': captcha_token
        }
        proxy_url = {'http': proxy_url, 'https': proxy_url}
        headers = get_headers()
        url = "https://api.nodepay.ai/api/auth/login"
        response = requests.post(url, headers=headers, json=json_data, proxies=proxy_url, timeout=5)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f'\r\r\033[31m⚠️ Error: {str(e)} \033[0m')
        linex()
        time.sleep(1)

# Main function for processing actions
def main():
    clear_screen()
    try:
        reff_limit = int(input('\033[0m>>\033[1;32m Put Your Reff Amount: '))
    except:
        print('\033[1;32m⚠️ Input Wrong Default Reff Amount is 1k ')
        reff_limit = 1000
        time.sleep(1)
    ref_code = input("\033[0m>>\033[1;32m Input referral code : ")
    clear_screen()
    success_crt = 0
    proxy_list = get_proxies()  # Get proxies from the scraper
    if not proxy_list:
        print("⚠️ No proxies found. Exiting.")
        return
    for atm in range(reff_limit):
        try:
            print(f'\r\r\033[0m>>\033[1;32m Possessing {str(success_crt)}/{str(reff_limit)} complete : {((atm+1) / reff_limit) * 100:.2f}% ')
            domains = ["@gmail.com", "@outlook.com", "@yahoo.com", "@hotmail.com"]
            characters = string.ascii_letters + string.digits
            username = str(''.join(random.choice(characters) for _ in range(12))).lower()
            password = str(''.join(random.choice(string.ascii_letters) for _ in range(6)) + 'R@' + ''.join(random.choice(string.digits) for _ in range(3)))
            email = f"{username}{str(random.choice(domains))}"
            proxy_url = random.choice(proxy_list)  # Randomly pick a proxy from the scraped list
            if validate_proxy(proxy_url):  # Validate the proxy before using it
                captcha_token = get_token()
                response_data = reg_account(email, password, username, ref_code, proxy_url, captcha_token)
                if response_data and 'msg' in response_data and response_data['msg'] == 'Success':
                    print(f'\r\r\033[0m>>\033[1;32m Account Created Successfully \033[0m')
                    captcha_token = get_token()
                    response_data = login_account(email, password, captcha_token, proxy_url)
                    if response_data and 'msg' in response_data and response_data['msg'] == 'Success':
                        print(f'\r\r\033[0m>>\033[1;32m Account Login Successful \033[0m')
                        auth_token = response_data['data']['token']
                        # Active account logic
                        success_crt += 1
                        open('accounts.txt', 'a').write(f"{str(email)}|{str(password)}|{str(auth_token)}\n")
                        time.sleep(1)
                    else:
                        print(f'\r\r\033[1;31m🌲 Account Login Failed \033[0m {response_data.get("msg", "Unknown error")}')
            else:
                print(f"⚠️ Invalid Proxy: {proxy_url}")
        except Exception as e:
            print(f'\r\r\033[31m⚠️ Error: {str(e)} \033[0m')
            linex()
            time.sleep(1)
    print(f"Completed {success_crt}/{reff_limit} successful accounts created.")
