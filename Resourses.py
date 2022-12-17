import requests

def create_word_list_ru(every_x_th):
    """list_all length = 1532601, so recommended every_x_th - more than 1000"""
    response = requests.get('https://raw.githubusercontent.com/danakt/russian-words/master/russian.txt')
    text = response.content.decode('cp1251')
    list_all = text[200:].splitlines()
    word_list_ru = []
    counter = 0
    while not counter >= len(list_all) - 1:
        word_list_ru.append(list_all[counter].lower())
        counter += every_x_th
    print(len(list_all))
    return word_list_ru


def create_word_list_en(every_x_th):
    """list_all length = 370077, so recommended every_x_th - more than 500"""
    response = requests.get('https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt')
    text = response.content.decode()
    list_all = text[211:].splitlines()
    word_list_en = []
    counter = 0
    while not counter >= len(list_all) - 1:
        word_list_en.append(list_all[counter].lower())
        counter += every_x_th
    print(len(list_all))
    return word_list_en

def create_word_list_en_easy(every_x_th):
    """
    returns a list only of words that have length 5
    list_all length = 10173, so recommended every_x_th - more than 100
    """
    response = requests.get('https://raw.githubusercontent.com/digitalronin/wordle/main/data/valid-words.txt')
    text = response.content.decode()
    list_all = text.splitlines()
    word_list_en = []
    counter = 0
    while not counter >= len(list_all) - 1:
        word_list_en.append(list_all[counter].lower())
        counter += 50
    print(len(list_all))
    return word_list_en

create_word_list_ru(10000)
create_word_list_en(10000)
create_word_list_en_easy(1000)

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

