import requests
import json
import math
import bs4
import os

def dump_comments(answers_id):
    if not os.path.exists('%s/%s/'%(question_id,answers_id)):
        os.mkdir('%s/%s'%(question_id,answers_id))
    comment_url='https://www.zhihu.com/api/v4/answers/%s/root_comments?order=time&limit=20&offset=0'%answers_id
    info=br.get(comment_url).json()
    if 'error' in info.keys():
        print(answers_id,info['error']['message'])
        return
    while not info['paging']['is_end']:
        temp=br.get(info['paging']['next']).json()
        info['paging']['is_end']=temp['paging']['is_end']
        info['paging']['next']=temp['paging']['next']
        info['data']+=temp['data']
    with open('%s/%s/comments.json'%(question_id,answers_id),'w',encoding='utf-8') as f:
        f.write(json.dumps(info,ensure_ascii=False))
    for comment in info['data']:
        if 'comment_sticker' in comment['content']:
            soup=bs4.BeautifulSoup(comment['content'],'html.parser')
            for sticker in soup.find_all(class_='comment_sticker'):
                href=sticker['href']
                f=open(href.split('/')[-1],'wb')
                f.write(requests.get(href).content)
                f.close()

question_id=392257701
br=requests.Session()
br.headers['User-Agent']='Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36'
if not os.path.exists('%s/'%question_id):
    os.mkdir('%s'%question_id)

dump_comments(answers_id=1196639992)
dump_comments(answers_id=1198850183)
dump_comments(answers_id=1199700379)
dump_comments(answers_id=1197440417)
dump_comments(answers_id=1198561457)
dump_comments(answers_id=1198130640)
dump_comments(answers_id=1197617455)


"""如何看待网文作者将5月5日定义为五五断更节？ - 浪饿肥粥的回答 - 知乎
https://www.zhihu.com/question/392257701/answer/1196639992
如何看待网文作者将5月5日定义为五五断更节？ - 杨建东的回答 - 知乎
https://www.zhihu.com/question/392257701/answer/1198850183
如何看待网文作者将5月5日定义为五五断更节？ - JoJo王颀的回答 - 知乎
https://www.zhihu.com/question/392257701/answer/1199700379"""