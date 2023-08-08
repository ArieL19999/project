
from selenium import webdriver

import Utils
import os

def test_scores_service(app_url, element_id):
  # Open a web browser and navigate to a webpage
  driver = webdriver.Chrome()
  driver.get(app_url)

  # Find an element with the ID "element-id"
  element = driver.find_element_by_id(element_id)
  element_value = element.text()
  print(f"Got element value for score = {element_value}")
  

def main():
  app_url = Utils.HOME_URL
  element_id = Utils.ELEMENT_ID_SCORE
  test_result = test_scores_service(app_url, element_id)

if __name__ == "__main__":
  main()  
