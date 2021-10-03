from selenium import webdriver
import requests
import bs4
from mongoengine import *

driver = webdriver.Chrome(executable_path='./chromedriver')

# constants
BASE_URL = 'https://www.work.ua/'
SEARCH_PARAMETER = 'junior python'
SEPARATOR = ', вакансія від '


class JobProposition(Document):
    name = StringField(required=True)
    href = StringField(required=True)
    publication_date = StringField(required=True)


class JobScraper:

    @staticmethod
    def generate_url_for_scraping() -> str:
        """
        Takes basic ulr and generates url for scraping.
        """
        driver.get(BASE_URL)
        element = driver.find_element_by_class_name('form-control.jobseeker-search')
        element.send_keys(SEARCH_PARAMETER)
        driver.find_element_by_id('sm-but').click()
        current_page = driver.current_url
        driver.quit()
        return current_page

    def find_data_on_page(self, current_page: str):
        list_of_hrefs = []
        list_of_full_names = []
        result = requests.get(current_page)
        soup = bs4.BeautifulSoup(result.text, 'lxml')

        for text in soup.find_all('h2'):
            if text.a:
                list_of_hrefs.append(f'{BASE_URL}{text.a["href"]}')
                list_of_full_names.append(text.a['title'])

        list_of_names, list_of_publication_date = self._get_name_and_date(list_of_full_names)
        result = list(zip(list_of_names, list_of_hrefs, list_of_publication_date))
        return result

    @staticmethod
    def _get_name_and_date(list_of_full_names: list):
        """
        Gets the full name of job position and splits it into name and publication date.
        Gets one list of full titles and returns two lists with names and publication dates.
        """
        list_of_names = []
        list_of_publication_date = []
        for title in list_of_full_names:
            list_of_names.append(title.split(SEPARATOR)[0])
            list_of_publication_date.append(title.split(SEPARATOR)[1])
        return list_of_names, list_of_publication_date

    @staticmethod
    def save_data_in_mongo(result: list):
        print(result)  # for checking
        connect('job')
        for obj in result:
            JobProposition(name=obj[0], href=obj[1], publication_date=obj[2]).save()
        disconnect_all()


scraper = JobScraper()
url_for_scraping = scraper.generate_url_for_scraping()
data_for_mongo = scraper.find_data_on_page(url_for_scraping)
scraper.save_data_in_mongo(data_for_mongo)

