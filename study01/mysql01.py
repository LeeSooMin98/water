import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='hanbitDB', charset='utf8')
cur = conn.cursor()
#cur.excute("CREATE TABLE IF NOT EXISTS userTable (id char(4) not null primary key, userName varchar(15), email varchar(20), birthYear int)")
try:
    cur.execute("insert into usertable values('Lee', 'LEESOOMIN', 'leesoomin@gmail.com', 1998)")#insert문은 외부를 쌍타옴표, 내부 정보는 외따옴표 사용해야함, 숫자는 따옴표 사용 안함
except:
    conn.rollback()#try except는 예외 처리 구문
else:
    conn.commit()


conn.close()