import random
import wikipedia
import os

def prefecture_quiz():
    pref_city_dict = {}
    pref_url_dict = {}
    with open(os.path.dirname(os.path.abspath(__file__))+'/static/pref_office_loc.txt', encoding='utf-8') as f:
        for i in f:
            txt_lines = i.strip().split(',')
            pref = txt_lines[0]
            city = txt_lines[1]
            url = txt_lines[2]

            if pref not in pref_city_dict:
                pref_city_dict[pref] = city
            
            if pref not in pref_url_dict:
                pref_url_dict[pref] = url
        
    pref_name = []

    for i in pref_city_dict.keys():
        pref_name.append(i)
    random_pref = random.choice(pref_name)
    city_name = pref_city_dict[random_pref]
    pref_url = pref_url_dict[random_pref]

    return random_pref, city_name, pref_url

def quiz():
    qa = []

    with open(os.path.dirname(os.path.abspath(__file__))+'/static/quiz.txt', encoding='utf-8') as f:
        for i in f:
            data = i.strip().split(',')
            qa.append(data)

    selected_qa = random.sample(qa, 5)

    return selected_qa

def wikipy(word):
    wikipedia.set_lang('ja')
    candidate_list = wikipedia.search(word)
    if not candidate_list:
        result = '該当する結果がありませんでした'
    else:
        search_page = wikipedia.page(candidate_list[0])
        result = search_page.summary
    return result

if __name__ == '__main__':
    p, c, u = prefecture_quiz()
    print(p, c, u)

    selected_qa = quiz()
    for i in selected_qa:
        print(i[0], i[1])
    
    print(wikipy('中山未知'))