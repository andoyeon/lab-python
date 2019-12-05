"""
ex03.py
"""
import pandas as pd

if __name__ == '__main__':
    # csv 파일에서 데이터 프레임을 생성
    emp_df = pd.read_csv('emp_df.csv')
    print(emp_df.iloc[0:5])

    # 부서(deptno)별, 직책(job)별 직원 수를 출력
    grouped = emp_df.groupby(['DEPTNO', 'JOB'])
    emp_by_dept = grouped['EMPNO']
    result_df = emp_by_dept.count()
    print(result_df)