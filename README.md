### Набор тестов для тестирование сайта

- сайт : http://nhub.news/top-words-timeline/?apiUrl=http%3A%2F%2Fnewshub.tagsreaper.com%3A8080%2Fgraph_api.php%3Fparams%5Bmethod%5D%3Ddata%26params%5Btype%5D%3D2%26params%5BchartType%5D%3Dtype1%26params%5Bcolors%5D%3DcolorPatternFill%26params%5BgroupWords%5D%3DnotGroup%26params%5Bcount%5D%3D50¤tPageUrl=%2F:

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

