from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pandas as pd


movie_dict = {
    'name': [],
    'year': [],
    'duration': [],
    'stars': [],
    'votes': [],
    'metascore': [],
    'description': []
}

if __name__ == '__main__':

    def decline_cookies(the_driver):
        try:
            decline_button = driver.find_element(By.XPATH, '//button[text()="Decline"]')
            decline_button.click()
        except:
            pass


    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_experimental_option('detach', True)

    driver = webdriver.Chrome(options=options)
    actions = ActionChains(driver)
    driver.implicitly_wait(1)
    wait = WebDriverWait(driver, 10)

    driver.get('https://www.imdb.com/')

    sleep(1)

    decline_cookies(driver)

    sleep(1)

    search_button = driver.find_element(By.ID, 'suggestion-search-button')
    search_button.click()

    sleep(1)

    movies_tv = driver.find_element(By.CSS_SELECTOR, 'a[data-testid="advanced-search-chip-tt"]')
    movies_tv.click()

    sleep(1)


    movie = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="test-chip-id-movie"]')

    if movie.is_displayed():
        actions.move_to_element(movie).perform()
        movie.click()
    else:
        title_type = driver.find_element(By.XPATH, '//div[text()="Title type"]')
        actions.move_to_element(title_type).perform()
        title_type.click()
        sleep(0.5)
        actions.move_to_element(movie).perform()
        movie.click()

    sleep(1)

    comedy = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="test-chip-id-Comedy"]')

    if comedy.is_displayed():
        actions.move_to_element(comedy).perform()
        comedy.click()
    else:
        genre = driver.find_element(By.XPATH, '//div[text()="Genre"]')
        actions.move_to_element(genre).perform()
        genre.click()
        sleep(0.5)
        actions.move_to_element(comedy).perform()
        comedy.click()
        
    sleep(1)
    # Awards & recognition
    awards = driver.find_element(By.XPATH, '//div[text()="Awards & recognition"]')
    actions.move_to_element(awards).perform()
    awards.click()

    sleep(1)

    oscar_nom = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="test-chip-id-oscar-nominated"]')
    actions.move_to_element(oscar_nom).perform()
    oscar_nom.click()

    sleep(1)

    results_button = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="See results"]')
    driver.execute_script('arguments[0].click()', results_button)
    sleep(2)

    while True:
        more_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.ipc-see-more__text')))

        if more_button:
            actions.move_to_element(more_button).perform()
            more_button.click()

            try:
                wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span.ipc-see-more__text')))
            except:
                break
        else:
            break


    movie_list = driver.find_elements(By.CLASS_NAME, 'ipc-metadata-list-summary-item')

    for movie in movie_list:
        # name = movie.find_element(By.CSS_SELECTOR, 'h3.ipc-title__text').text.split('. ')[1]
        raw_name = movie.find_element(By.CSS_SELECTOR, 'h3.ipc-title__text').text
        name = ' '.join(raw_name.split(' ')[1:])
        print(f"Name: {name}")
        movie_dict['name'].append(name)

        year = movie.find_elements(By.CSS_SELECTOR, 'span.dli-title-metadata-item')[0].text
        print(f"Year: {year}")
        movie_dict['year'].append(year)

        duration = movie.find_elements(By.CSS_SELECTOR, 'span.dli-title-metadata-item')[1].text
        print(f"Duration: {duration}")
        movie_dict['duration'].append(duration)

        stars = movie.find_element(By.CSS_SELECTOR, 'span.ipc-rating-star--rating').text
        print(f"Stars: {stars}")
        movie_dict['stars'].append(stars)

        votes = movie.find_element(By.CSS_SELECTOR, 'span.ipc-rating-star--voteCount').text.strip()[1:-1]
        print(f"Votes: {votes}")
        movie_dict['votes'].append(votes)

        try:
            metascore = movie.find_element(By.CSS_SELECTOR, 'span.metacritic-score-box').text
        except:
            metascore = 'Bilgi yok'

        print(f"Metascore: {metascore}")
        movie_dict['metascore'].append(metascore)

        description = movie.find_element(By.CSS_SELECTOR, 'div[role="presentation"]').text
        print(f"Description: {description}")
        movie_dict['description'].append(description)
        print("\n")

        df = pd.DataFrame(movie_dict)
        df.to_excel('filmler.xlsx')


