URL сайта. Укажите URL сайта, который вы выбрали для анализа.
https://books.toscrape.com/
одно из предыдущих домашних заданий делалось с применением этого сайта, поэтому легче было вспоминать

Описание. Предоставьте краткое описание информации, которую вы хотели извлечь из сайта.
извлекалась информация о книгах (название, цена, рейтинг, наличие)

Подход. Объясните подход, который вы использовали для навигации по сайту, определения соответствующих элементов и извлечения нужных данных.
сочетание selenium + beatifulsoup

Трудности. Опишите все проблемы и препятствия, с которыми вы столкнулись в ходе реализации проекта, и как вы их преодолели.
после установки библиотеки selenium сначала никак не получалось импортировать webdriver, вылечилось командой pip3 install selenium
возможно причина была не в этом, но помогло

Результаты. Включите образец извлеченных данных в выбранном вами структурированном формате (например, CSV или JSON)
результаты приложены в файле books.csv - не стала скрейпить все 50 страниц, ограничилась 2мя.