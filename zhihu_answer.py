import requests
import json
import os


question_id=392257701
br=requests.Session()
br.headers['User-Agent']='Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36'
url='https://www.zhihu.com/mssp/zhihu/api/v1/landing'
data={"ac":True,"token":"https://www.zhihu.com/tardis/sogou/in/qus/%s"%question_id,"limit":200,"from":0}
if not os.path.exists('%s/'%question_id):
    os.mkdir('%s'%question_id)

info=br.post(url,json.dumps(data)).json()

#我们从镜像中勉强恢复了几个重要回答
#-1指未知
append_cards=[{
        "id": "1198561457",
        "content": "<blockquote><b>先说结论：支持</b></blockquote><hr><p>长期以来，我都是以沉默的，躲在阴暗角落的双眼，来看这个世界。</p><p>因为我害怕我一说话，他们就会看见我，然后夺走我最后一口口粮。</p><p><b>但是，我错了，就算我不说话，这一天最终也会到来。</b></p><p>而五五断更节，是为数不多的，大家一起站出来发声的机会。</p><p>这也是一次为数不多的，历史性的时刻。</p><hr><p><b>文以载道</b>，意思指文章是为了说明道理的。</p><p>我们所写的小说，传达了我们笔者的每一个模因，我们笔下每一个角色，似乎生来都是为了反对强权、艰险和霸道。</p><p>我们生来就有这样的基因。</p><p><b>知行合一</b>，是由王阳明老先生提出来的，即认识事物的道理与在现实中运用此道理，是密不可分的。</p><p>既然我们写手总是在自己的小说里写正确的事情，并在小说里将那些糟粕碾碎，扔进异世界历史的垃圾桶，那为何不敢在现实中发声呢？</p><p>究竟是什么，<b>阻止了我们的知行合一</b>？</p><p>仅仅是因为生活么？</p><p>长期习惯了那些无端的指责、恶意的谩骂，很多看似是我们的过错，最后都会体现在我们自己拿到手的面包上。</p><p>于是，我们学会了低头做人，不得不以沉默去默认他们。</p><p>但现在，就连理想都要让步。</p><p>阳明老先生在天之灵或许也会感到悲哀吧？</p><p><b>我也想活着，但我想活的更好一些，尤其是在这个还算不错的时代。</b></p><p><b>所以，在这个节日里，我选择发声。</b></p><hr><p><b>人间正道是沧桑。</b></p><p></p>",
        "upvoted_count": 23,
        "downvoted_count": -1,
        "author": {
            "name": "姬惊",
            "logo": "https://pic2.zhimg.com/v2-80097bb5c299544b3096ae97334a4e86_l.jpg",
            "info": "想赚钱不敢作死型胆大包天写手喵"
        },
        "created": 1588525184
    },{
        "id": "1198130640",
        "content": "<p>我就不说，有多少人邀请我来回应了，微博私信也不少。</p><p>讲个老笑话，第二次讲了。</p><p>谭嗣同说：各国变法，无不从流血而成，今中国未闻有流血而牺牲者，此国之所以不昌也。有之，请自嗣同始。</p><p>康有为说：各国变法，无不从流血而成，今中国未闻有流血而牺牲者，此国之所以不昌也。有之，请自嗣同始。</p><p>我一剑斩破九重天5月2号大结局，新书本月中旬发，这个事儿，我早一个月就跟主编安逸说好了，然后跑过来跟大家说，你们要五月五号断更啊。</p><p>我可以有个绰号——南海圣蛤！</p><p>或者南海生蚝？</p><p>ps：虽然自从到了知乎，在某个群体的眼里，我就变成了不是在装逼，就是在装逼的路上，但我真不想有南海圣蛤蟆的绰号。</p><p>ps：我劝大家更新是不是等于是找骂？</p><p>ps：我就不配有看法……</p>",
        "upvoted_count": 5151,
        "downvoted_count": -1,
        "author": {
            "name": "流浪的蛤蟆",
            "logo": "https://pic4.zhimg.com/1682d1960_is.jpg",
            "info": "《一剑斩破九重天》起点连载中，各位大爷常来玩啊！"
        },
        "created": 1588492029
    },{
        "id": "1197617455",
        "content": "<p>是读者，支持。</p><p>唯独一点，必须要提“著作权”，对外不要模糊或局限成合同等。</p><p>当然，作者方面完全可以模糊化处理，作者群体内部也可以合同问题来团结大多数，无论发声内容是坚决还是模糊，以此促成。</p><p>因为作者没有著作权才是最让外界同情你们的点，才是让其他文创行业从业者感到唇亡齿寒的点，才有破圈能力。</p><p>因为取法乎上，仅得乎中。</p><p>因为一鼓作气，三而竭。</p><p>这两个道理，各位应该很清楚，包括阅文。</p><p>注意：1、不需要改名。现在你们策划的这名字易懂易操作，才能握指成拳。至于断更后面的原创文化权利保护意义，水到渠成时，媒体一句话的事；</p><p>2、理性维权，不攻击、不PD任何人，甚至不攻击资本，只强调拿回属于自己的正当著作权利！否则，会被泼脏水，失去舆论同情。</p>",
        "upvoted_count": 633,
        "downvoted_count": -1,
        "author": {
            "name": "知乎用户",
            "logo": "https://pic4.zhimg.com/da8e974dc_is.jpg",
            "info": ""
        },
        "created": 1588476542
    }]
info['cards']=append_cards+info['cards']

while len(info['cards'])<info['total_cards']:
    data['from']+=200
    temp=br.post(url,json.dumps(data)).json()
    if 'cards' in temp.keys():
        info['cards']+=temp['cards']
        print('%.2f%%'%(len(info['cards'])/info['total_cards']*100))
    else:
        break
f=open('%s/answers.json'%question_id,'w',encoding='utf-8')
f.write(json.dumps(info,ensure_ascii=False))
f.close()