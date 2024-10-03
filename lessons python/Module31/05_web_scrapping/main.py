import re
import requests
from pprint import pprint

if __name__ == '__main__':
    def search_pattern(pattern, list_text):
        res = re.findall(pattern, list_text)
        result_tag = []
        for index, tag in enumerate(res):
            string = re.sub(r'</?h3>', '', tag)
            string1 = re.sub(r'<h3.*>', '', string)
            result_tag.append(string1)
        return result_tag


    # В данном случае запрос request.get заменен на загрзку сайта из файла html
    with open('examples.html', 'r') as f:
        text = f.read()
    # По итогу вы так же получаете код сайта в виде одной строки
    h3_parrern = r'<h3>.+'
    print(search_pattern(h3_parrern, text))

    site = 'https://www.columbia.edu/~fdc/sample.html'
    text = requests.get(site)
    site_text = text.text
    site_pattern = r'<h3.+>'
    pprint(search_pattern(site_pattern, site_text))
