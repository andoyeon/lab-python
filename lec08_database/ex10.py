"""
ex10.py

emp, dept 테이블에서 부서번호를 입력받아서
해당 부서 사원의 사번, 이름, 급여, 부서 번호, 부서 이름을 출력(join)
"""
import cx_Oracle
import lec08_database.oracle_config as cfg

with cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn) as connection:
    with connection.cursor() as cursor:
        sql_select = '''select e.empno, e.ename, e.sal, d.deptno, d.dname
        from emp e join dept d
        on e.deptno = d.deptno
        where e.deptno = :deptno
        '''
        dept_no = int(input('부서 번호 입력>> '))
        cursor.execute(sql_select, deptno = dept_no)
        for row in cursor:
            print(row)