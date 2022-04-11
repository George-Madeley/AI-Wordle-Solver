wordle_url = "https://www.nytimes.com/games/wordle/index.html"

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(wordle_url)
