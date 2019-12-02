import requests

def get_html(url):
    r = requests.get(url)  # Получим метод Response
    r.encoding = 'utf8'
    return r.text  # Вернем данные объекта text

# 1 процедура разбора ударения с сайта https://accentonline.ru/ ------------------------------------------------
def check_accentonline(word_check):
    data = get_html(
        'https://accentonline.ru/' + word_check[0] + "/" + word_check)
    if data.find("404 Not Found") >= 0 or data.find(
            "Запрашиваемая страница на accentonline.ru не найдена.") >= 0:
        return 'Запрашиваемое слово отсутсвует в базе или не существует'
    else:
        site_symbol = "&#x301;"  # как обозначено ударение на сайте
        str_start = data.find('<span class="word-accent">') + len(
            '<span class="word-accent">')
        str_start_txt = data.find('<meta name="description" content="') + len(  
            '<meta name="description" content="' )                              

        return data[
               str_start:(str_start + len(word) + len(site_symbol))].replace(
            site_symbol, chr(769))


# конец процедуры разбора ударения с сайта https://accentonline.ru/


# 2 процедура разбора ударения с сайта https://udaren.ru/ --------------------------------------------------------
def check_udaren(word_check):
    data = get_html('https://udaren.ru/' + word_check)
    if data.find(
            'Мы не нашли такого слова в своей базе ударений. Попробуйте еще раз.') >= 0:
        return 'Запрашиваемое слово отсутсвует в базе или не существует'
    else:
        str_start = data.find('<span style="font-size: 40px;">') + len(
            '<span style="font-size: 40px;">')

        return data[str_start:(str_start + len(
            word_check) + 1)]  # !!почему-то выдает на 1 меньше!!


# конец процедуры разбора ударения с сайта https://udaren.ru/

# 3------------------ начало программы -----------------------------------------------------------------------------
word = input("Введите слово - ")
check_result = check_accentonline(word)

if check_result == 'Запрашиваемое слово отсутсвует в базе или не существует':
    check_result = check_udaren(word)
    print(check_result)
else:
    print(check_result)
