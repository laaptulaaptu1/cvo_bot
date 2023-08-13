from bs4 import BeautifulSoup as bs4
import requests
import schedule
import time

cv_url='https://coursevania.com'

def getCVLinks():
    cv_links_data = []
    cv_divs = []
    cv_page = requests.get(cv_url)
    soup = bs4(cv_page.text, 'html.parser')
    # print(soup.prettify())
    courses = soup.find_all('div', class_='stm_lms_courses__single_animation')
    # print(courses)
    for course in courses:
        cv_div_soup = course.find('div', class_='stm_lms_courses__single--info_title')
        cv_divs.append(cv_div_soup)
    for cv_div in cv_divs:
        # cv_link = cv_div.find('a').text.strip() # gets all the text inside the a tag, acts like innerHtml
        cv_link = cv_div.find('a')['href']
        cv_links_data.append(cv_link)

    print(cv_links_data)
    return cv_links_data
    # print(cv_page.status_code)

def getUDLinks(cv_links):
    ud_links_data = []
    for link in cv_links:
        ud_page = requests.get(link)
        soup = bs4(ud_page.text, 'html.parser')
        ud_course_div = soup.find('div', class_ = 'stm-lms-buy-buttons')
        ud_course_link = ud_course_div.find('a')['href']
        ud_links_data.append(ud_course_link)
    #print(ud_links_data)
    for clink in ud_links_data:
        print(clink)

    return ud_links_data

def scrapper():
    cv_links = getCVLinks()
    ud_links = getUDLinks(cv_links)
    return ud_links

scrapper()
