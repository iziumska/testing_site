### Набор тестов для тестирование сайта


#### Цель тестов:
- тестирование 'Options' при выборе Chart type = 'Area stacked'
- тестирование 'Options' при выборе Chart type = 'Line'
- тестирование рандомно 5 слов и добавление в поле 'Search' 

##### Структура
                
+ items
   + locators
      - locators.py
   + pages
      - base_page.py
      - main_page.py
      - options_page.py
+ report
    - Test Results - Unittests_in_tests.html
    - Test Results - Unittests_in_tets_suit_options_page_line_py.html
+ resource
    * chromedriver.exe
    * geckodriver.exe
    * path_driver.py
    * url_site.py
+ tests
   + test_base.py
   + test_base_set_up_class.py
   + test_suit_options_page.py
   + test_suit_random_words.py
   + tets_suit_options_page_line.py	

### Запуск тестов
- клонировать репозиторий
- в PyCharm открыть проект 
-  с помощью Unittest запустить папку 'tests'

