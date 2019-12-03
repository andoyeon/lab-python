"""
ex08.py
lec08_database 패키지의 내용들을 참고해서,
오라클 데이터베이스에서 emp 테이블의 모든 레코드를 검색(select) -> 2차원 리스트
csv 모듈을 사용해서, csv 파일(emp.csv)로 저장
"""
import cx_Oracle
import lec08_database.oracle_config as cfg
import csv

emp = []
with cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn) as conn:
    with conn.cursor() as cursor:
        cursor.execute('select * from emp')
        for row in cursor:
            emp.append(list(row))

print(emp)




with open('emp.csv', mode='w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f, delimiter=',')
    for row in emp:
        writer.writerow(row)






