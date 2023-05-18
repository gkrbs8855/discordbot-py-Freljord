from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import os
import random
load_dotenv()

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

client = discord.Client()


update_txt = ('13.10 패치\n\n'
                '상향\n'
'나르: 입히는 피해량 100% ⇒ 입히는 피해량 105%\n'
'그라가스: 입히는 피해량 100% ⇒ 입히는 피해량 105%\n'
'클레드: 입히는 피해량 100% ⇒ 입히는 피해량 105%\n\n'
'하향\n'
'이블린: 입히는 피해량 115% ⇒ 입히는 피해량 110%\n'
'밀리오: 보호막 흡수량 100% ⇒ 보호막 흡수량 95%, 체력 회복량 100% ⇒ 체력 회복량 95%\n'
'쉔: 받는 피해량 100% ⇒ 받는 피해량 105%\n')

ban_list = ['아우렐리온 솔']

champs = ['가렌',
'갈리오',
'갱플랭크',
'그라가스',
'그레이브즈',
'그웬',
'나르',
'나미',
'나서스',
'노틸러스',
'녹턴',
'누누와 윌럼프',
'니달리',
'니코',
'닐라',
'다리우스',
'다이애나',
'드레이븐',
'라이즈',
'라칸',
'람머스',
'럭스',
'럼블',
'레나타 글라스크',
'레넥톤',
'레오나',
'렉사이',
'렐',
'렝가',
'루시안',
'룰루',
'르블랑',
'리 신',
'리븐',
'리산드라',
'릴리아',
'마스터 이',
'마오카이',
'말자하',
'말파이트',
'모데카이저',
'모르가나',
'문도 박사',
'미스 포츈',
'밀리오',
'바드',
'바루스',
'바이',
'베이가',
'베인',
'벡스',
'벨베스',
'벨코즈',
'볼리베어',
'브라움',
'브랜드',
'블라디미르',
'블리츠크랭크',
'비에고',
'빅토르',
'뽀삐',
'사미라',
'사이온',
'사일러스',
'샤코',
'세나',
'세라핀',
'세주아니',
'세트',
'소나',
'소라카',
'쉔',
'쉬바나',
'스웨인',
'스카너',
'시비르',
'신 짜오',
'신드라',
'신지드',
'쓰레쉬',
'아리',
'아무무',
'아우렐리온 솔',
'아이번',
'아지르',
'아칼리',
'아크샨',
'아트록스',
'아펠리오스',
'알리스타',
'애니',
'애니비아',
'애쉬',
'야스오',
'에코',
'엘리스',
'오공',
'오른',
'오리아나',
'올라프',
'요네',
'요릭',
'우디르',
'우르곳',
'워윅',
'유미',
'이렐리아',
'이블린',
'이즈리얼',
'일라오이',
'자르반 4세',
'자야',
'자이라',
'자크',
'잔나',
'잭스',
'제드',
'제라스',
'제리',
'제이스',
'조이',
'직스',
'진',
'질리언',
'징크스',
'초가스',
'카르마',
'카밀',
'카사딘',
'카서스',
'카시오페아',
'카이사',
'카직스',
'카타리나',
'칼리스타',
'케넨',
'케이틀린',
'케인',
'케일',
'코그모',
'코르키',
'퀸',
'크산테',
'클레드',
'키아나',
'킨드레드',
'타릭',
'탈론',
'탈리야',
'탐 켄치',
'트런들',
'트리스타나',
'트린다미어',
'트위스티드 페이트',
'트위치',
'티모',
'파이크',
'판테온',
'피들스틱',
'피오라',
'피즈',
'하이머딩거',
'헤카림'
]



@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content == f'{PREFIX}help':
        help_txt = '!랜덤픽, !업데이트, !밴리스트, !밴추가 [챔피언풀네임], !밴삭제 [챔피언풀네임], !밴초기화'
        await message.channel.send(help_txt)

    if message.content == f'{PREFIX}랜덤픽':
        team1 = []
        team2 = []
        i=0
        while i<20:
            ran_num = random.randint(0,len(champs)-1)
            if champs[ran_num] in ban_list:
                i=i
            elif ran_num not in team1 and ran_num not in team2:
                i+=1
                if len(team1)<10:
                    team1.append(ran_num)
                else:
                    team2.append(ran_num)

        print(list(map(lambda x:champs[x],team1)))
        print(list(map(lambda x:champs[x],team2)))
        result = "1팀 : "+', '.join(list(map(lambda x:champs[x],team1)))+"\n2팀 : "+', '.join(list(map(lambda x:champs[x],team2)))

        await message.channel.send(result)
    
    if message.content == f'{PREFIX}업데이트':
        await message.channel.send(update_txt)
    
    if message.content.startswith(f'{PREFIX}밴추가'):
        champ_name = message.content[5:len(message.content)]
        if champ_name in champs:
            ban_list.append(champ_name)
            result = champ_name + '밴 추가 성공'
            await message.channel.send(result)
        else:
            result = champ_name + '밴 추가 실패'
            await message.channel.send(result)
          
    if message.content.startswith(f'{PREFIX}밴삭제'):
        champ_name = message.content[5:len(message.content)]
        if champ_name in ban_list:
            ban_list.remove(champ_name)
            result = champ_name + '밴 삭제 성공'
            await message.channel.send(result)   
        else:
            result = champ_name + '밴 삭제 실패'
            await message.channel.send(result)
            
    if message.content == f'{PREFIX}밴초기화':
        ban_list.clear()
        await message.channel.send('밴초기화 성공')
        
    if message.content == f'{PREFIX}밴리스트':
        result = ', '.join(list(map(lambda x:x,ban_list)))
        await message.channel.send(result)
        
    if message.content.startswith(f'{PREFIX}hello'):
        await message.channel.send('Hello!')


try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
