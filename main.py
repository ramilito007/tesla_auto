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


def main():
    parser = ArgumentParser()
    parser.add_argument("-e", "--email", default="", help="Tesla Email Account")
    args = parser.parse_args()
    if(args.email == ''):
        args.email = input("Please enter your email address: ")
    with teslapy.Tesla(args.email, authenticator=custom_auth) as tesla:
        ret = tesla.fetch_token()
    print(f"The returned token is: {ret}")
    vehicles = tesla.vehicle_list()
    print(vehicles[0])
    tesla.close()


if __name__ == "__main__":
    main()



