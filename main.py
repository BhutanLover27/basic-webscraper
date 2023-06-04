from selenium import webdriver
from selenium.webdriver.common.by import By

featured_xpath = "/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/div/div[2]/div/div[2]/div[1]/p/b/a"
featured_title_xpath = "/html/body/div[2]/div/div[3]/main/header/h1/span[1]"
featured_languages_xpath = '//*[@id="p-lang-btn-label"]/span[2]'
url = "https://pl.wikipedia.org/wiki/Wikipedia:Strona_g%C5%82%C3%B3wna"
browser = webdriver.Chrome()

browser.get(url)
featured_link = browser.find_element(By.XPATH, featured_xpath)
featured_link.click()
featured_title = browser.find_element(By.XPATH, featured_title_xpath).text
featured_languages = browser.find_element(By.XPATH, featured_languages_xpath).text
if featured_languages != "Dodaj języki":
    featured_languages = str(featured_languages.split(" ")[0]).replace(" ", "")
else:
    featured_languages = "1"
print("Today's featured article on wikipedia is", featured_title, "and it's availible in", featured_languages, "languages.")

with open('examples.txt', 'r') as examples:
    text = examples.readlines()
    average = float(text[0].split(" ")[1])
    number_tested = int(text[1].split(" ")[1])
    last_featured = str(text[3])
    if featured_title != last_featured:
        new_number_tested = number_tested + 1
        new_average = str((float(featured_languages) + average*number_tested)/new_number_tested)
    else:
        new_number_tested = number_tested
        new_average = average
    examples.close()

with open('examples.txt', 'w') as examples:
    examples.write("average " + str(new_average))
    examples.write('\n')
    examples.write("tested " + str(new_number_tested))
    examples.write('\n')
    examples.write("last featured:")
    examples.write('\n')
    examples.write(featured_title)
    examples.close()
print("The average amount of languages is:", new_average)
