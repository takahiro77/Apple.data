from urllib.parse import SplitResultBytes
from altair.vegalite.v4.schema.channels import Column
from altair.vegalite.v4.schema.core import UnitSpecWithFrame
from attr import s
from numpy.lib.shape_base import _kron_dispatcher
from requests.api import options
import streamlit as st 
import numpy as np 
import matplotlib.pyplot as plt 
from PIL import Image
import pandas as pd 
import altair as alt 
import time
from streamlit.elements.legacy_altair import generate_chart 
from streamlit.proto.Button_pb2 import Button
import yfinance as yf 
from streamlit_folium import folium_static
import folium

st.sidebar.write("""
### Apple財務データ可視化アプリ
""")
img=Image.open('ap3.jpeg')
st.sidebar.image(img,use_column_width=True)

genre = st.sidebar.radio(
     "項目を選択してください",
     ('企業詳細', '財務分析','指標計算機能'))

st.sidebar.write('情報源（https://www.sec.gov/edgar/searchedgar/companysearch.html)')
img=Image.open('sec2.jpeg')

st.sidebar.image(img,use_column_width=True)
st.sidebar.write('My Github(https://github.com/takahiro77/Apple.stock)')

img=Image.open('git3.jpeg')
st.sidebar.image(img,use_column_width=True)

if genre == '企業詳細':
    st.title('APPLE(AAPL) NASDAQ.GS')
    img=Image.open('Apple.png')
    st.image(img,use_column_width=True)
    
    st.write('### 企業情報')
    button34=st.button('CEO Tim cook')
    if button34:
        st.write("""
        ティム・クックはアップルのCEOであり、取締役会のメンバーです。
2011年8月にCEOに任命される前は、ティムはAppleの最高執行責任者であり、Appleのサプライチェーンのエンドツーエンド管理、営業活動、すべての市場でのサービスとサポートを含む、同社の世界的な販売と運営のすべてを担当していました。
ティムはまた、IBMに12年間勤務し、最近では北米フルフィルメントのディレクターとして、北米およびラテンアメリカにあるIBMのパーソナルコンピューターカンパニーの製造および流通部門を率いていました。
ティムはデューク大学でMBAを取得し、そこではFuqua Scholarであり、オーバーン大学で工業工学の理学士号を取得しています。""")
        st.write('参照：(https://investor.apple.com/leadership-and-governance/person-details/default.aspx?ItemId=cb4c5428-aaa5-4e54-b553-69f4778fa361)')
    
    button33=st.button('Apple park map')
    if button33:
        m = folium.Map(location=[37.33271, -122.00865], zoom_start=16)
        tooltip = "Apple park"
        folium.Marker(
            [37.33271, -122.00865], popup="Apple park", tooltip=tooltip
        ).add_to(m)
        folium_static(m)
    
    img=Image.open('applepark.jpeg')
    st.image(img,use_column_width=True)
    st.write('(公式サイト)https://investor.apple.com/investor-relations/default.aspx')
    
    img=Image.open('aap2.jpeg')
    st.image(img,use_column_width=True)
    st.write('(公式youtube)https://www.youtube.com/channel/UCE_M8A5yxnLfW0KghEeajjw')
    
    img=Image.open('aap.jpeg')
    st.image(img,use_column_width=True)
    st.write('詳細')
    st.write('アップル（Apple Inc）は、スマートフォン、パソコン、タブレット、ウェアラブル、アクセサリーの設計・製造・販売及び関連する多様なサービスの販売を行う。【事業内容】製品には、「アイフォーン」、「マック」、「アイパッド」、「ウェアラブル」、「ホーム」、「アクセサリー」が含まれる。「アイフォーン」は、アイフォーンオーエス（iOS）オペレーティングシステムをベースにしたスマートフォンラインである。「マック」は、マックオーエス（macOS）オペレーティングシステムをベースにしたパーソナルコンピュータである。「アイパッド」は、アイパッドオーエス（iPadOS）オペレーティングシステムをベースにした多目的タブレットである。「ウェアラブル」、「ホーム」、「アクセサリー」には、「エアーポッズ」、「アップルテレビ」、「アップルウォッチ」、ビーツ製品、「ホームポッド」、「アイポッドタッチ」、その他の「アップル」ブランドおよびサードパーティのアクセサリーが含まれる。「エアーポッズ」は、シリと相互作用するワイヤレスヘッドフォンである。「アイポッドウォッチ」は、スマートウォッチの製品ラインである。サービスには、広告、アップルケア、クラウドサービス、デジタルコンテンツ、支払いサービスが含まれる。顧客は、主に消費者、中小企業、教育、企業、政府の市場にいる。')
    st.write('引用先：(https://www.rakuten-sec.co.jp/ITS/rakuten_g/creditcard/?sclid=a_GO_brand_rakuten&gclid=EAIaIQobChMIlZKppMa88gIVDrqWCh2Pngz7EAAYASAAEgKlV_D_BwE)')
    
    aapl=yf.Ticker('AAPL')
    hist=aapl.history(period='max')
    hist1=hist['Close']
    hist2=hist['Volume']
    st.write('株価推移')
    st.area_chart(hist1)
    st.write('可視化したい項目を選択してくだい')
    col1,col2,col3=st.columns(3)
    hist3=aapl.dividends
    hist4=aapl.actions['Stock Splits']
    button=col1.button('出来高推移')
    button1=col2.button('配当金推移')
    button2=col3.button('株式分割推移')
    if button:
        st.area_chart(hist2)
    if button1:
        st.area_chart(hist3)
    if button2:
        st.area_chart(hist4)
    col4,col5,col6=st.columns(3)
    eps=pd.DataFrame([[2.09],[2.32],[3.08],[2.99],[3.31]],index=['2016','2017','2018','2019','2020'],columns=['EPS'])
    bps=pd.DataFrame([[6.01],[6.54],[5.63],[5.09],[3.85]],index=['2016','2017','2018','2019','2020'],columns=['BPS'])
    per=pd.DataFrame([[13.54],[16.63],[18.33],[18.72],[44.24]],index=['2016','2017','2018','2019','2020'],columns=['PER'])
    st.write('指標')
    col7,col8,col9=st.columns(3)
    col4,col5,col6=st.columns(3)
    col7.write('EPS')
    col4.area_chart(eps)
    col8.write('BPS')
    col5.area_chart(bps)
    col9.write('PER')
    col6.area_chart(per)

    st.write('商品別売上比率')
    ip=pd.DataFrame([[136000,20628,22831,24348,11132],[141319,19222,25850,29980,12863],[166699,18805,25484,37190,17417],[142381,21280,25740,46291,24482],[137781,23724,28622,53768,30620]],index=['2016','2017','2018','2019','2020'],columns=['iPhone','iPad','Mac','サービス','その他商品'])
    st.table(ip)
    fig = plt.figure(figsize=(30,10))

    ax1 = fig.add_subplot(2, 3, 1)
    ax2 = fig.add_subplot(2, 3, 2)
    ax3 = fig.add_subplot(2, 3, 3)
    ax4 = fig.add_subplot(2, 3, 4)
    ax5 =fig.add_subplot(2,3,5)

    x=np.array([136000,20628,22831,24348,11132])
    y=np.array([141319,19222,25850,29980,12863])
    t=np.array([166699,18805,25484,37190,17417])
    r=np.array([142381,21280,25740,46291,24482])
    e=np.array([137781,23724,28622,53768,30620])


    labels=['iPhne','iPad','Mac','service','otherproduct']

    ax1.pie(x,labels=labels,counterclock=False,startangle=90,autopct='%1.2f%%')
    ax2.pie(y,labels=labels,counterclock=False,startangle=90,autopct='%1.2f%%')
    ax3.pie(t,labels=labels,counterclock=False,startangle=90,autopct='%1.2f%%')
    ax4.pie(r,labels=labels,counterclock=False,startangle=90,autopct='%1.2f%%')
    ax5.pie(e,labels=labels,counterclock=False,startangle=90,autopct='%1.2f%%')
    fig.tight_layout() 
    st.pyplot(fig)
    st.write('*左上(2016)・左下(2017)・真ん中上(2018)・真ん中下(2019)・右上(2020)')

    st.write("""
    ### こちらは株価可視化ツールです。以下のオプションから日数を選択できます
    """)
    days=st.slider('日数選択',1,50,20)
    st.write(f"""
    過去{days}日間のGAFAMとの比較株価推移
    """)
    @st.cache
    def get_data(days,tickers):
        df=pd.DataFrame()
        for company in tickers.keys():
            tkr=yf.Ticker(tickers[company])
            hist=tkr.history(period=f'{days}d')
            hist.index.strftime('%d %B %Y')
            hist=hist[['Close']]
            hist.columns=[company]
            hist=hist.T
            hist.index.name='Name'
            df=pd.concat([df,hist])
        return df


    ymin,ymax=st.slider(
        '株価範囲指定をしてください',
        0.0,3500.0,(0.0,3500.0)
    )
    tickers={
        'Google':'GOOG',
        'Apple':'AAPL',
        'Facebook':'FB',
        'Amazon':'AMZN',
        'Microsoft':'MSFT'
    
    }

    df=get_data(days,tickers)
    companies=st.multiselect(
        '比較したい企業名を選択してください',
        list(df.index),
        ['Google','Apple','Facebook','Amazon','Microsoft']
    )

    if not companies:
        st.error('少なくとも一社は選んでください')
    else:
        data=df.loc[companies]
        st.write('### 株価(USD)',data.sort_index())
        data=data.T.reset_index()
        data=pd.melt(data, id_vars=['Date']).rename(
            columns={'value':'Stock Prices(USD)'}
        )

        chart = (
            alt.Chart(data)
            .mark_line(opacity=0.8)
            .encode(
                x="Date:T",
                y=alt.Y("Stock Prices(USD):Q", stack=None),
                color='Name:N'
            )
        )   
        st.altair_chart(chart,use_container_width=True)

        from pandas_datareader import data
        st.write('### S&P500指数との相関関係')
        start='2008-11-05'
        end='2021-8-21'
        spx=data.DataReader('^SPX','stooq',start,end)
        aapl=data.DataReader('AAPL','stooq',start,end)
        button77=st.button('S＆P500株価チャート')
        if button77:
            st.area_chart(spx['Close'])
        st.write('AppleとS＆P500指数の散布図')
        fig=plt.figure(figsize=(20,5))
        ax1=fig.add_subplot()
        x1=spx['Close']
        x2=aapl['Close']
        ax1.scatter(x1,x2,label='Close',s=5,color='orange')
        plt.legend(loc='best')
        st.pyplot(fig)
elif genre == '財務分析':
    st.title('財務分析')
    img=Image.open('ap7.jpeg')
    st.image(img,use_column_width=True)
    page = st.selectbox("財務諸表を選択してください", ["損益計算書", "貸借対照表", "キャッシュフロー計算書"]) 
    if page == "損益計算書":
        PL=pd.DataFrame([[215639,131376,84263,10045,14194,24239,60024,61372,15685,45687,8.35],[229234,141048,88186,11581,15261,26842,61344,64089,15738,48351,9.27],[265595,163756,101839,14236,16705,30941,70898,72903,13372,59531,12.01],[260174,161782,98392,16217,18245,34462,63930,65737,10481,55256,2.99],[274515,169559,104956,18752,19916,38668,66288,67091,9680,57411,3.31]],index=['2016','2017','2018','2019','2020'],columns=['純売上高','売上原価','売上総利益','研究開発費','販管費','総営業費用','営業利益','税引前当期純利益','法人税引等金','当期純利益','一株あたり利益'])
        S=pd.DataFrame([[215639,84263,60024,45687],[229234,88186,61344,48351],[265595,101839,70898,59531],[260174,98392,63930,55256],[274515,104956,66288,57411]],index=['2016','2017','2018','2019','2020'],columns=['純売上高','売上総利益','営業利益','当期純利益'])
        st.write(PL.T)
        st.write('ボタン選択で業績推移をグラフで可視化できます')
        pl1,pl2,pl3,pl4=st.columns(4)
        button3=pl1.button('純売上高')
        button4=pl2.button('売上総利益')
        button5=pl3.button('営業利益')
        button6=pl4.button('当期純利益')

        if button3:
            st.bar_chart(PL['純売上高'])
        elif button4:
            st.bar_chart(PL['売上総利益'])
        elif button5:
            st.bar_chart(PL['営業利益'])
        elif button6:
            st.bar_chart(PL['当期純利益'])
        st.write('収益性分析')
        
        a=pd.DataFrame([[39.07,27.83,21.18,6.58,14.20,35.62],[38.46,26.76,21.09,6.65,12.88,36.07],[38.34,26.69,22.41,6.28,16.27,55.56],[37.81,24.57,21.23,7.01,16.32,55.56],[38.23,24.14,20.91,7.25,17.72,87.86]],index=['2016','2017','2018','2019','2020'],columns=['売上総利益率','営業利益率','当期純利益率','SGA比率','ROA(総資産回転率)','ROE(自己資本利益率)'])
        st.table(a.T)
        st.line_chart(a)
        
        st.write('四半期決算(最終四半期を除く)')
        pl1=pd.DataFrame([[75872,30423,2404,3848,24171,6212,18361,3.30],[50557,19921,2511,3423,13987,3626,10516,1.91],[42358,16106,2560,3441,10105,2573,7796,1.43],[78351,30176,2871,3946,23359,6289,17891,3.38],[52896,20591,2776,3718,14097,3655,11029,2.11],[45408,17488,2937,3783,10768,2691,8717,1.68],[88293,33912,3407,4231,26274,6965,20065,3.92],[61137,23422,3378,4150,15894,2346,13822,2.75],[53265,20421,3701,4108,12612,1765,11519,2.36],[84310,32031,3902,4783,23346,3941,19965,4.22],[58015,21821,3948,4458,13415,2232,11561,2.47],[53809,20227,4257,4426,11544,1867,10044,2.20],[91819,35217,4451,5197,25569,3682,22236,5.04],[58313,22370,4565,4952,12853,1866,11249,2.58],[59685,22680,4758,4831,13091,1884,11253,2.61]],index=['2016(Q1)','2016(Q2)','2016(Q3)','2017(Q1)','2017(Q2)','2017(Q3)','2018(Q1)','2018(Q2)','2018(Q3)','2019(Q1)','2019(Q2)','2019(Q3)','2020(Q1)','2020(Q2)','2020(Q3)'],columns=['純売上高','売上総利益','研究開発費','販管費','営業利益','法人税等引等金','当期純利益','一株あたりの利益'])
        st.write(pl1.T)
        left_colum,right_column=st.columns(2)
        img=Image.open('ap1.jpeg')
        genre2=left_colum.radio('可視化したい項目を選択してください',('純売上高','売上総利益','研究開発費','販管費','営業利益','法人税等引等金','当期純利益','一株あたりの利益'))
        right_column.image(img,use_column_width=True)
        
        if genre2 == '純売上高':
            st.bar_chart(pl1['純売上高'])
        elif genre2 == '売上総利益':
            st.bar_chart(pl1['売上総利益'])
        elif genre2=='研究開発費':
            st.area_chart(pl1['研究開発費'])
        elif genre2=='販管費':
            st.bar_chart(pl1['販管費'])
        elif genre2=='営業利益':
            st.bar_chart(pl1['営業利益'])
        elif genre2 == '法人税等引等金':
            st.bar_chart(pl1['法人税等引等金'])
        elif genre2=='当期純利益':
            st.bar_chart(pl1['当期純利益'])
        elif genre2=='一株あたりの利益':
            st.bar_chart(pl1['一株あたりの利益'])
    
    elif page == "貸借対照表":
        BS=pd.DataFrame([[20484,15754,2132,8283,106869,214817,321686,75427,36074,78927,193437,31251,96364,634,128249,321686],[20289,17874,4855,13936,128645,246674,375319,100814,40415,103703,241272,35867,98330,-150,134047,375319],[25913,23186,3956,12087,131339,234366,365725,116866,45180,102519,258578,40241,70400,-3454,107147,365725],[48844,22926,4106,12352,162819,175697,338516,105718,50503,102067,248028,45174,45898,-584,90488,338516],[38016,16120,4061,11264,143713,180175,323888,105392,54490,107440,258549,50779,14966,-406,65339,323888]],index=['2016','2017','2018','2019','2020'],columns=['現金同等物','売掛金','在庫','その他流動資産','流動資産合計','固定資産','総資産','流動負債','その他固定負債','有利子負債','負債合計','株主資本','利益剰余金','その他包括利益累計額','総株主資本','負債と株主資本の合計'])
        PL=pd.DataFrame([[215639,131376,84263,10045,14194,24239,60024,61372,15685,45687,8.35],[229234,141048,88186,11581,15261,26842,61344,64089,15738,48351,9.27],[265595,163756,101839,14236,16705,30941,70898,72903,13372,59531,12.01],[260174,161782,98392,16217,18245,34462,63930,65737,10481,55256,2.99],[274515,169559,104956,18752,19916,38668,66288,67091,9680,57411,3.31]],index=['2016','2017','2018','2019','2020'],columns=['純売上高','売上原価','売上総利益','研究開発費','販管費','総営業費用','営業利益','税引前当期純利益','法人税引等金','当期純利益','一株あたり利益'])
        B=pd.DataFrame([[321686,193437,96364,128249],[375319,241272,98330,134047],[365725,258578,70400,107147],[338516,248028,45898,90488],[323888,258549,14966,65339]],index=['2016','2017','2018','2019','2020'],columns=['総資産','負債合計','利益剰余金','総株主資本'])
        st.write(BS.T)
        st.write('ボタン選択で業績推移をグラフで可視化できます')
        
        bs1,bs2,bs3,bs4=st.columns(4)
        button7=bs1.button('現金同等物')
        button8=bs2.button('在庫')
        button9=bs3.button('流動資産')
        button10=bs4.button('総資産')
        
        if button7:
            st.bar_chart(BS['現金同等物'])
        elif button8:
            st.bar_chart(BS['在庫'])
        elif button9:
            st.bar_chart(BS['流動資産'])
        elif button10:
            st.bar_chart(BS['総資産'])
        
        bs5,bs6,bs7,bs8=st.columns(4)
        button11=bs5.button('流動負債')
        button12=bs6.button('負債合計')
        button13=bs7.button('株主資本')
        button14=bs8.button('利益剰余金')
        
        if button11:
            st.bar_chart(BS['流動負債'])
        elif button12:
            st.bar_chart(BS['負債合計'])
        elif button13:
            st.bar_chart(BS['株主資本'])
        elif button14:
            st.bar_chart(BS['利益剰余金'])
        
        bs9,bs10=st.columns(2)
        button15=bs9.button('総株主資本')
        button16=bs10.button('負債と株主資本の合計')
        
        if button15:
            st.bar_chart(BS['総株主資本'])
        elif button16:
            st.bar_chart(BS['負債と株主資本の合計'])
        st.write('安全性分析')
        g=pd.DataFrame([[67.03,150.82,39.86,141.68,9.71,61.54,167.49],[61.07,179.99,35.71,127.60,9.55,77.36,184.02],[72.62,241.33,29.29,112.38,11.00,95.68,218.73],[76.85,274.10,26.73,154.01,13.34,112.79,194.16],[84.75,395.70,20.17,136.36,15.67,164.43,275.75]],index=['2016','2017','2018','2019','2020'],columns=['総資産回転率','負債比率','自己資本比率','流動比率','株主資本比率','ネットD/Eレシオ','固定比率'])
        st.table(g.T)
        st.line_chart(g)

        st.write('四半期決算(最終四半期を除く)')
        bs1=pd.DataFrame([[16689,12953,2451,76219,217065,293284,33312,76092,88925,165017,28253,101494,-1480,128267,293384],[21514,12229,2281,87592,217685,305277,25098,68265,106555,174820,29484,102021,-1048,130457,305277],[18237,11714,1831,93761,211841,305602,26318,71486,107575,179061,30106,96542,-107,126541,305602],[16371,14057,2712,103332,227809,331141,38510,84130,114621,198751,32144,100001,245,132390,331141],[15157,11579,2910,101990,232542,334532,28573,73342,127108,200450,33579,100925,-422,134082,334532],[18571,12399,3146,112875,232298,345173,31915,81302,131446,212748,34445,98525,-545,132425,345173],[27491,23440,4421,143810,262984,406794,62985,115788,150807,266595,36447,104593,-841,140199,406794],[45059,14324,7662,130053,237449,367502,34311,89230,151304,240624,38044,91898,-3064,126878,367502],[31971,14104,5936,115761,233436,349197,38489,88548,145700,234248,38624,79436,-311,114949,349197],[44771,18077,4988,140828,232891,373719,44293,108283,147544,255827,40970,80510,-3588,117892,373719],[37988,150851,4884,123346,218652,341998,30443,93772,142366,236138,42801,64558,-1499,105860,341998],[50530,14148,3355,134973,187266,322239,29115,89704,136079,225783,43371,53724,-639,96456,322239],[39771,20970,4097,163231,177387,340618,45111,102161,148926,251087,45972,43997,-418,89531,340618],[40174,15722,3334,143753,176647,320400,32421,96094,145881,241975,48032,33182,-2789,78425,320400],[33383,17882,3978,140065,177279,317344,35325,95318,149744,245062,48696,24136,-550,72282,317344]],index=['2016(Q1)','2016(Q2)','2016(Q3)','2017(Q1)','2017(Q2)','2017(Q3)','2018(Q1)','2018(Q2)','2018(Q3)','2019(Q1)','2019(Q2)','2019(Q3)','2020(Q1)','2020(Q2)','2020(Q3)'],columns=['現金同等物','売掛金','在庫','流動資産','固定資産','総資産','買掛金','流動負債','固定負債','負債','株主資本','利益上余剰金','その他包括利益累計額','総株主資本','負債と株主資本の合計'])
        st.write(bs1)
        left_colum,right_column=st.columns(2)
        img=Image.open('ap4.jpeg')
        genre3=left_colum.radio('可視化したい項目を選択してください',('現金同等物','売掛金','在庫','流動資産','固定資産','総資産','買掛金','流動負債','固定負債','負債','株主資本','利益上余剰金','その他包括利益累計額','総株主資本','負債と株主資本の合計'))
        right_column.image(img,use_column_width=True)
        
        if genre3 == '現金同等物':
            st.bar_chart(bs1['現金同等物'])
        elif genre3 == '売掛金':
            st.bar_chart(bs1['売掛金'])
        elif genre3=='在庫':
            st.bar_chart(bs1['在庫'])
        elif genre3=='流動資産':
            st.bar_chart(bs1['流動資産'])
        elif genre3=='固定資産':
            st.bar_chart(bs1['固定資産'])
        elif genre3 == '総資産':
            st.bar_chart(bs1['総資産'])
        elif genre3=='買掛金':
            st.bar_chart(bs1['買掛金'])
        elif genre3=='流動負債':
            st.bar_chart(bs1['流動負債'])
        elif genre3=='固定負債':
            st.bar_chart(bs1['固定負債'])
        elif genre3=='負債':
            st.bar_chart(bs1['負債'])
        elif genre3 == '株主資本':
            st.bar_chart(bs1['株主資本'])
        elif genre3=='利益上余剰金':
            st.bar_chart(bs1['利益上余剰金'])
        elif genre3=='その他包括利益累計額':
            st.bar_chart(bs1['その他包括利益累計額'])
        elif genre3=='総株主資本':
            st.bar_chart(bs1['総株主資本'])
        elif genre3=='負債と株主資本の合計':
            st.bar_chart(bs1['負債と株主資本の合計'])
    
    elif page == "キャッシュフロー計算書":
        CF=pd.DataFrame([[65824,-45977,20484],[64225,-46446,20289],[77434,16066,87876],[69391,45896,90976],[80674,-4289,-86820]],index=['2016','2017','2018','2019','2020'],columns=['営業活動によるキャッシュフロー','投資活動によるキャッシュフロー','財務活動によるキャッシュフロー'])
        st.write(CF.T)
        st.write('ボタン選択で業績推移をグラフで可視化できます')
        cf1,cf2,cf3=st.columns(3)
        button17=cf1.button('営業活動によるキャッシュフロー')
        button18=cf2.button('投資活動によるキャッシュフロー')
        button19=cf3.button('財務活動によるキャッシュフロー')
        
        if button17:
            st.bar_chart(CF['営業活動によるキャッシュフロー'])
        elif button18:
            st.bar_chart(CF['投資活動によるキャッシュフロー'])
        elif button19:
            st.bar_chart(CF['財務活動によるキャッシュフロー'])
        st.write('安全性分析')
        
        i=pd.DataFrame([[30.52,19847],[28.01,17779],[29.15,93500],[26.67,115287],[29.38,76385]],index=['2016','2017','2018','2019','2020'],columns=['営業キャッシュフローマージン','フリーキャッシュフロー'])
        st.table(i.T)
        st.line_chart(i['営業キャッシュフローマージン'])
        st.bar_chart(i['フリーキャッシュフロー'])
        st.write('判断基準')
        
        CF1=pd.DataFrame([['+','-','-'],['+','-','+'],['+','+','-'],['+','+','+'],['-','-','-'],['-','-','+'],['-','+','-'],['-','+','+']],index=['優良','積極投資','財務改善','転換','再検討','大勝負','融資途絶','要注意'],columns=['営業キャッシュフロー','投資キャッシュフロー','財務キャッシュフロー'])
        st.table(CF1)
        st.write('四半期決算(最終四半期を除く)')
        
        cf1=pd.DataFrame([[27463,-20450,-11444],[39064,-34110,-4560],[49698,-38580,-14001],[27056,-19122,-12047],[36579,-33324,-11582],[47942,-36504,-13351],[28293,-13590,-7501],[43423,15120,-33773],[57911,19067,-65296],[26690,5844,-13676],[37845,19192,-43133],[49481,46694,-69937],[30516,-13668,-25407],[43827,-4655,-46347],[60098,-9820,-65463]],index=['2016(Q1)','2016(Q2)','2016(Q3)','2017(Q1)','2017(Q2)','2017(Q3)','2018(Q1)','2018(Q2)','2018(Q3)','2019(Q1)','2019(Q2)','2019(Q3)','2020(Q1)','2020(Q2)','2020(Q3)'],columns=['営業活動によるCF','投資活動によるCF','財務活動によるCF'])
        st.write(cf1)
        left_colum,right_column=st.columns(2)
        img=Image.open('ap2.jpeg')
        genre4=left_colum.radio('可視化したい項目を選択してください',('営業活動によるキャッシュフロー','投資活動によるキャッシュフロー','財務活動によるキャッシュフロー'))
        right_column.image(img,use_column_width=True)
        
        if genre4 == '営業活動によるキャッシュフロー':
            st.bar_chart(cf1['営業活動によるCF'])
        elif genre4 == '投資活動によるキャッシュフロー':
            st.bar_chart(cf1['投資活動によるCF'])
        elif genre4=='財務活動によるキャッシュフロー':
            st.bar_chart(cf1['財務活動によるCF'])
elif genre == '指標計算機能':
    st.title('指標計算機能')
    img=Image.open('ap6.jpeg')
    st.image(img,use_column_width=True)
    st.write('『売上総利益率』')
    left_colum,right_column=st.columns(2)
    cd=left_colum.number_input('売上総利益を入力してください',1)
    ce=right_column.number_input('売上高を入力してください',1)
    st.write('売上総利益率:',cd/ce*100,'%')
    st.write('----------------------------------')
    st.write('『営業利益率』')
    left_colum,right_column=st.columns(2)
    ca=left_colum.number_input('営業利益を入力してください',1)
    cb=right_column.write('上記の売上高と同じ')
    st.write('営業利益率:',ca/ce*100,'%')
    st.write('----------------------------------')
    st.write('『当期純利益率』')
    left_colum,right_column=st.columns(2)
    cf=left_colum.number_input('当期純利益を入力してください',1)
    cg=right_column.write('＊上記の売上高と同じ')
    st.write('当期純利益率:',cf/ce*100,'%')
    st.write('----------------------------------')
    st.write('『SGA比率』')
    left_colum,right_column=st.columns(2) 
    cp=left_colum.number_input('販管費を入力してください',1)
    cq=right_column.write('＊上記の売上高と同じ')
    st.write('SGA比率:',cp/ce*100,'%')
    st.write('----------------------------------')
    st.write('『ROA(総資産利益率)』')
    left_colum,right_column=st.columns(2)
    ch=left_colum.number_input('総資産を入力してください',1)
    ci=right_column.write('＊上記の当期純利益と同じ')
    st.write('ROA(総資産利益率):',cf/ch*100,'%')
    st.write('----------------------------------')
    st.write('『総資産回転率』')
    left_colum,right_column=st.columns(2)
    cj=left_colum.write('＊上記の総資産と同じ')
    ck=right_column.write('＊上記の売上高と同じ')
    st.write('総資産回転率：',ce/ch*100,'%')
    st.write('----------------------------------')
    st.write('『ROE(自己資本利益率)』')
    left_colum,right_column=st.columns(2)
    cm=right_column.write('＊上記の当期純利益と同じ')
    cn=left_colum.number_input('自己資本を入力してください',1)
    st.write('ROE(自己資本利益率):',cf/cn*100,'%')
    st.write('----------------------------------')
    st.write('『EPS(一株あたりの利益)』')
    left_colum,right_column=st.columns(2)
    pg=left_colum.write('＊上記の当期純利益と同じ')
    ph=right_column.number_input('発行済み株式数を入力してください',1)
    st.write('EPS(一株あたりの利益):',cf/ph*100,'%')
    st.write('----------------------------------')
    st.write('『BPS(一株あたりの純資産)』')
    left_colum,right_column=st.columns(2)
    pi=right_column.number_input('純資産を入力してください',1)
    pj=left_colum.write('＊上記の発行済み株式数と同じ')
    st.write('BPS(一株あたりの純資産):',pi/ph*100,'%')
    st.write('----------------------------------')
    st.write('『ネットD/Eレシオ』')
    left_colum,right_column=st.columns(2)
    co=left_colum.number_input('有利子負債を入力してください',1)
    cr=right_column.write('＊上記の純資産と同じ')
    st.write('ネットD/Eレシオ:',co/pi*100,'%')
    st.write('----------------------------------')
    st.write('『負債比率』')
    left_colum,right_column=st.columns(2)
    cs=left_colum.number_input('負債を入力してください',1)
    ct=right_column.write('＊上記の自己資本と同じ')
    st.write('負債比率:',cs/cn*100,'%')
    st.write('----------------------------------')
    st.write('『自己資本比率』')
    left_colum,right_column=st.columns(2)
    cu=right_column.write('＊上記の自己資本と同じ')
    cv=left_colum.number_input('総資本を入力してください',1)
    st.write('自己資本比率:',cn/cv*100,'%')
    st.write('----------------------------------')
    st.write('『流動比率』')
    left_colum,right_column=st.columns(2)
    cw=left_colum.number_input('流動資産を入力してください',1)
    cx=right_column.number_input('流動負債を入力してください',1)
    st.write('流動比率:',cw/cx*100,'%')
    st.write('----------------------------------')
    st.write('『株主資本比率』')
    left_colum,right_column=st.columns(2)
    cy=left_colum.number_input('株主資本を入力してください',1)
    cz=right_column.write('＊上記の総資産と同じ')
    st.write('株主資本比率:',cy/ch*100,'%')
    st.write('----------------------------------')
    st.write('『固定比率』')
    left_colum,right_column=st.columns(2)
    pa=left_colum.number_input('固定資産を入力してください',1)
    pb=right_column.number_input('総株主資本を入力してください',1)
    st.write('固定比率:',pa/pb*100,'%')
    st.write('----------------------------------')
    st.write('『営業キャッシュフローマージン』')
    left_colum,right_column=st.columns(2)
    pc=left_colum.number_input('営業キャッシュフローを入力してください',1)
    pf=right_column.write('＊上記の売上高と同じ')
    st.write('営業キャッシュフローマージン:',pc/ce*100,'%')

