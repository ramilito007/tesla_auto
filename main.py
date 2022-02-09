import teslapy
import teslapy
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from argparse import ArgumentParser

chromedriver = 'C:\\chromedriver\\chromedriver.exe'


def custom_auth(url):
    driver = webdriver.Chrome(chromedriver)
    driver.get(url)
    WebDriverWait(driver, 300).until(EC.url_contains('void/callback'))
    return driver.current_url
    # driver.quit()


def main():
    parser = ArgumentParser()
    parser.add_argument("-e", "--email", default="ramig23@gmail.com", help="Tesla Email Account")
    args = parser.parse_args()

    # tesla = teslapy.Tesla(args.email)
    with teslapy.Tesla(args.email, authenticator=custom_auth) as tesla:
        ret = tesla.fetch_token()
    print(f"The returned token is:{ret}")


if __name__ == "__main__":
    main()



