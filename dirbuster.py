import requests

def dirbust(url, wordlist, options = [200, 301, 302], cookies = None, headers = None, report = 1):
    try:
        with open(wordlist, 'r') as f:
            for line in f:
                dir = line.strip()
                full_url = url + '/' + dir
                res = requests.get(full_url, cookies=cookies, headers=headers)
                if res.status_code in options:
                    if report == 1:
                        with open('report.txt', 'a') as report_file:
                            report_file.write(f'{full_url}: {res.status_code})\n')
                    else:
                        print(f'{full_url}: {res.status_code})')
    except FileNotFoundError:
        print(f"File not found: {wordlist}")
        print("defaulting to directory-list-2.3-big.txt")
        dirbust(url, "wordlists/directory-list-2.3-big.txt", options, cookies, headers, report)
    except Exception as e:
        print(f"An error occurred: {e}")