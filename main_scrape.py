from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from string import ascii_lowercase
import time
from datetime import datetime
import io


def log_print(log_text):
    print(datetime.now().strftime("[%H:%M:%S] > ") + log_text)


def write_person(output_filename, name, division, email, url):
    output = io.open(output_filename,"a+",encoding="utf-8") # This APPENDS to output file.
    output.write(str(name)+","+str(division)+","+str(email)+","+str(url))
    output.write("\n")
    output.close()


def main():
    log_print("Beginning operation...")

    # Setup for scraper
    log_print("Opening browser.")

    # PUT PATH FOR WEBDRIVER HERE
    browser = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")

    log_print("Fetching login page.")
    browser.get("https://acadinfo.wustl.edu/WSHome/Default.aspx")
    time.sleep(2)

    button = browser.find_element_by_css_selector("input[value='Login to WebSTAC']")
    button.click()
    time.sleep(2)

    login_field = browser.find_element_by_id("ucWUSTLKeyLogin_txtUsername")
    pw_field = browser.find_element_by_id("ucWUSTLKeyLogin_txtPassword")
    login_button = browser.find_element_by_css_selector("input[value='Login']")
    
    # PUT YOUR WUSTL KEY AND LOGIN HERE
    login = "mdizon"
    pw = "Porkflossbun!2"

    log_print("Logging in...")
    login_field.send_keys(login)
    pw_field.send_keys(pw)
    login_button.click()

    log_print("Waiting for DUO authentication.")
    time.sleep(12)

    browser.get("https://acadinfo.wustl.edu/apps/Faces/")

    for a in ascii_lowercase:
        for b in ascii_lowercase:

            query = str(a+b)

            log_print("Searching with query: "+query)

            search_text = browser.find_element_by_id("Body_txtNameSearch")
            search_text.send_keys(query)  # SEARCH QUERY
            search_text = browser.find_element_by_id("Body_txtNameSearch")
            search_text.send_keys(Keys.RETURN)
            time.sleep(5)
            soup = BeautifulSoup(browser.page_source, 'html.parser')

            amount = len(soup.find_all(style="font-size: 12pt;"))

            log_print("Amount for query " + query + ": " + str(amount))
            if amount == 0:
                log_print("WARN: Zero entries found for "+query+".")

            for n in range(0, amount):
                email = soup.find(id="Body_repResults_aEmail_" + str(n))
                if (email is not None):
                    email_string = (email.get_text().strip())  # Email
                    name_string = (email.previous_sibling.get_text().strip())  # Name
                pic = soup.find(id="Body_repResults_picPhoto_" + str(n))

                pic_url = pic.img.attrs.get("src")  # Picture

                if (email is not None):
                    division = email.parent.parent.table.tbody.find(style="width: 85%;")
                    division_string = (division.get_text().strip())

                # CHANGE THE OUTPUT PATH HERE
                write_person("out/names_3052021.csv",name_string,division_string,email_string,pic_url)
                # log_print("Wrote "+name_string+" to file.") # For logging purposes

            log_print("Wrote "+str(amount)+" names for "+query+".")

    time.sleep(5)
    browser.close()

    log_print("End of operation.")


if __name__ == "__main__":
    main()
