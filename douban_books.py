from bs4 import BeautifulSoup
import requests
import pymysql


db = pymysql.connect('127.0.0.1','debian-sys-maint','flZ0fXaL0vn6KA3h','books_db',charset='utf8')

cur = db.cursor()





path='./douban/105.html'
with open(path) as f:
    html=f.read()


soup = BeautifulSoup(html,"lxml")




for book_html in soup.find_all('li',class_='works-item'):

    try:
        #书本链接
        book_url=book_html.find('a',class_='pic').attrs['href']
        #书名
        book_name=book_html.find('img').attrs['alt']
        print(book_name)
        #作者
        book_auth=book_html.find_all('span',class_='')[3].text
        #内容
        book_context=book_html.find_all('span',class_='')[5].text
        #书的简介
        book_introduction = book_context.split()[0]
        #作者的介绍
        # auth_introduction = book_context.split()[2]
        #星数
        book_starts=book_html.find('span',class_='score').text
        #评分
        book_score=book_html.find('a',class_='amount').text
        #字数
        book_words=book_html.find_all('span',class_='')[6].text
        #书的价格
        book_price=float(book_html.find('span',class_='price-tag').text[1:5])

        #书的详细信息
        book_data=requests.get(book_url).content.decode('utf-8')

        s = BeautifulSoup(book_data,"lxml")
        #书的出版社
        # book_press=s.find_all('span',class_="labeled-text")[2].find('a').text
        #tag1
        book_tag1=s.find_all('span',itemprop="title")[0].text
        #tag2
        book_tag2=s.find_all('span',itemprop="title")[1].text
        #tag3
        book_tag3=s.find_all('span',itemprop="title")[2].text


        # book图像
        book_image_url = s.find('img',itemprop="image").get('src')

        book_image = requests.get(book_image_url).content
        image_name = "./book_image/" + book_name

        with open(image_name,"wb") as f:
            f.write(book_image)



        # print(p)




        select_sql = "select book_name from books where book_name = %s"
        res=cur.execute(select_sql,[book_name])

        if not res:
            #插入books表数据
            insert_sql = "insert into books (book_name,book_author,book_price,book_introduction, \
            book_words,book_starts) VALUES (%s,%s,%s,%s,%s,%s);"
            try:
                insert_books_data=[book_name,book_auth,book_price,book_introduction, \
            book_words,book_starts]
                cur.execute(insert_sql,insert_books_data)
                db.commit()
            except Exception as e:
                print(e)
                db.rollback()

            #插入Labels表
            select_book_id_sql = "select book_id from books where book_name = %s"
            cur.execute(select_book_id_sql,[book_name])
            book_id = int(cur.fetchone()[0])
            insert_labels_sql="insert into labels (label_book_id,label_L1,label_L2,label_L3) values (%s,%s,%s,%s);"
            insert_labels_data = [book_id,book_tag1,book_tag2,book_tag3]
            try:
                cur.execute(insert_labels_sql,insert_labels_data)
                db.commit()
            except Exception as e:
                print(e)
                db.rollback()
    except Exception as e:
        print(e)




cur.close()

db.close()
