import urllib.request
import re 

def url_open(url):
    response=urllib.request.urlopen(url)
    html=response.read().decode('utf-8')

    return html

if __name__=='__main__':
    url='http://www.tuling123.com/openapi/api?key=97e5e74b7bb74dc4a892c683d3ef5baa'+'&info='
    p=r'\:\".*'
    while True:
        question=urllib.parse.quote(input("我："))
        request=url+question
        response=url_open(request)
        answer=re.findall(p,response)
        print("二郎"+str(answer))
