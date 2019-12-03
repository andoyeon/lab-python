"""
emp.csv 파일을 읽어서, DataFrame을 생성
- 급여(sal)가 2000 이상인 직원들의 모든 정보를 출력
- 부서 번호(deptno)가 10인 직원들의 모든 정보를 출력
- 급여가 전체 직원의 급여의 평균보다 많은 직원의 사번, 이름, 급여를 출력
- 30번 부서에서 일하는, 직책이 SALESMAN인 직원들의 사번, 이름, 급여, 부서번호를 출력
- 20번, 30번 부서에 근무하는 직원들 중 급여가 2000을 초과하는
  직원들의 사번, 이름, 급여, 부서번호를 출력
- 수당이 없는 직원들 중에서, 매니저가 있고, 직책이 'MANAGER' 또는 'CLERK'인
  직원들의 모든 정보를 검색
- 사원 이름에 'E'가 포함된 직원들의 이름만 출력(str.contains() 이용)
- DataFrame을 csv 형식으로 파일에 write하는 함수를 찾아서 데이터 프레임을 파일로 저장
"""
import pandas as pd
import numpy as np

mpg = pd.read_csv('emp.csv', encoding='utf-8', header=None)
mpg.columns = ['empno', 'ename', 'job', 'mgr', 'hiredate', 'sal', 'comm', 'deptno']
print(mpg)

# 급여(sal)가 2000 이상인 직원들의 모든 정보를 출력
print(mpg[mpg['sal'] >= 2000])

# 부서 번호(deptno)가 10인 직원들의 모든 정보를 출력
print(mpg[mpg['deptno'] == 10])

# 급여가 전체 직원의 급여의 평균보다 많은 직원의 사번, 이름, 급여를 출력
sal_mean = mpg['sal'].mean()
print(f'sal 평균: {sal_mean}')
print(mpg[mpg['sal'] > sal_mean][['empno', 'ename', 'sal']])

# 30번 부서에서 일하는, 직책이 SALESMAN인 직원들의 사번, 이름, 급여, 부서번호를 출력
cond1 = (mpg['deptno'] == 30)
cond2 = (mpg['job'] == 'SALESMAN')
print(mpg[cond1 & cond2][['empno', 'ename', 'sal', 'deptno']])

# 20번, 30번 부서에 근무하는 직원들 중 급여가 2000을 초과하는
#   직원들의 사번, 이름, 급여, 부서번호를 출력
cond1 = (mpg['deptno'] == 20) | (mpg['deptno'] == 30)
print(cond1)
cond2 = (mpg['sal'] > 2000)
print(mpg[cond1 & cond2][['empno', 'ename', 'sal', 'deptno']])

# 수당이 없는 직원들 중에서, 매니저가 있고, 직책이 'MANAGER' 또는 'CLERK'인
#   직원들의 모든 정보를 검색
cond1 = mpg['comm'].isnull()
cond2 = (mpg['job'] == 'MANAGER') | (mpg['job'] == 'CLERK')
print(mpg[cond1 & cond2])

# 사원 이름에 'E'가 포함된 직원들의 이름만 출력(str.contains() 이용)
print(mpg[mpg['ename'].str.contains('E')])

# DataFrame을 csv 형식으로 파일에 write하는 함수를 찾아서 데이터 프레임을 파일로 저장
mpg.to_csv('mpg.csv', mode='w', encoding='utf-8')
