# Что использую

## Данные из датасета для соревнования

| Поле  | Описание   | Тип признака | Колличество строк |
| ------- | -------- | ----| ----|
| id    | Id записи     | float64 | 8765|
| atm_group    | Код банка, к которому принадлежит банкомат    | float64| 8765|
| address_rus    | Адрес банкомата на русском языке    |object| 8765|
| lat     | Кордината банкомата по широте    |object| 8765|
| long    | Кордината банкомата по долготе |float64| 8765|
| target    | индекс популярности банкомата    |float64| 8765|

## Данные с mainfin.ru

Можно собрать информацию для любого города для обучения моделей данные использовать не буду, но сервис будет работать по всей стране

| Поле  | Описание   | Тип признака |
| ------- | -------- | ----|
| address    | Адрес банкомата на русском языке     | object |
| bank_name    | На    | object|
| schedule    | Адрес банкомата на русском языке    |object|

Дополнительно при помощи Proton API и DaData были получены координаты по широте и долготе, что позволяет сооединить с исходнымм датасетом

 ## Дополнительная информация не о банкоматах с OSM
  
Добавил информацию о большом количестве точек интереса в радиусе 100м от банкомата: 'hospital', 'nightclub', 'parking', 'post_office', 'pub;bar;restaurant', 
    'clock', 'bar', 'cafe', 'public_bath', 'photostudio', 'community_centre', 
    'post_box', 'restaurant', 'school', 'kindergarten', 'bus_station', 
    'marketplace', 'food_court', 'exhibition_centre', 'money_transfer', 
    'charging_station', 'car_wash', 'drinking_water', 'pub', 'ice_cream', 
    'bank', 'townhall', 'loto', 'vending_machine', 'bicycle_rental', 
    'loading_dock', 'fast_food', 'fuel', 'parking_entrance', 'atm', 'sport', 
    'sanatorium', 'pharmacy'.
    
Посчитал расстояние до ближайшего банкомата в метрах, выделил информацию информацию о названии населенного пункта, добавил население

### [Ссылка](https://drive.google.com/drive/folders/1G3g9_ce5O9vWhomKqKXkfQs43EoUgaS2?usp=sharing) на диск с данными

# Попытки были, но не использую

## Парсинг данных с сайта Open Street Map
Тестировал только для Москвы удалось получить 2053 записи 

## Данные с banki.ru

Сайт содержит большое количество информации о финсовых организациях в РФ, но спарсить не получилось
