import os, sys, random, string, time
try:import requests
except:os.system('pip install requests')
import requests

# Line Function 
def linex():
    print('\033[0m================================================')

# Logo For script 
logo = f"""
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

# Generate Proxy Function
def generate_proxy():
    try:
        response = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=5000&country=all")
        proxies = response.text.strip().split("\n")
        if proxies:
            return random.choice(proxies)
        else:
            raise Exception("No proxies available.")
    except Exception as e:
        print(f'\033[31m⚠️ Proxy generation failed: {e} \033[0m')
        return None

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
        os.system('cls');print(logo)
    else:
        os.system('clear');print(logo)

# Get headers set / with `auth_token` or head only
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

# Registration account using proxy or not
def reg_account(email, password, username, ref_code, proxy_url=None, captcha_token=None):
    try:
        if proxy_url:
            print(f'\r\r\033[0m>>\033[1;32m Proxy : {proxy_url} \033[0m')
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
        print(f'\r\r\033[31m⚠️ Error: {str(e)} \033[0m'); linex(); time.sleep(1)

# Main function for processing full action
def main():
    clear_screen()
    try:
        ref_limit = int(input('\033[0m>>\033[1;32m Put Your Reff Amount: '))
    except:
        print('\033[1;32m⚠️ Input Wrong Default Reff Amount is 1k '); ref_limit = 1000; time.sleep(1)
    ref_code = input("\033[0m>>\033[1;32m Input referral code : ")
    clear_screen(); success_crt = 0
    for atm in range(ref_limit):
        try:
            print(f'\r\r\033[0m>>\033[1;32m Processing  {str(success_crt)}/{str(ref_limit)} complete : {((atm+1) / ref_limit) * 100:.2f}% ')
            domains = ["@gmail.com", "@outlook.com", "@yahoo.com", "@hotmail.com"]
            characters = string.ascii_letters + string.digits
            username = str(''.join(random.choice(characters) for _ in range(12))).lower()
            password = str(''.join(random.choice(string.ascii_letters) for _ in range(6)) + 'Rc3@' + ''.join(random.choice(string.digits) for _ in range(3)))
            email = f"{username}{str(random.choice(domains))}"
            proxy_url = generate_proxy()
            captcha_token = get_token()
            response_data = reg_account(email, password, username, ref_code, proxy_url, captcha_token)
            if response_data['msg'] == 'Success':
                print(f'\r\r\033[0m>>\033[1;32m Account Created Successfully \033[0m')
                success_crt += 1
                open('accounts.txt', 'a').write(f"{str(email)}|{str(password)}\n")
            else:
                print(f'\r\r\033[1;31m🌲 Account Creation Failed \033[0m {response_data["msg"]}')
            linex()
        except Exception as e:
            print(f'\r\r\033[31m⚠️ Error: {str(e)} \033[0m'); linex(); time.sleep(1)
    print('\r\r\033[0m>>\033[1;32m Your Referral Completed \033[0m')
    exit()

main()
