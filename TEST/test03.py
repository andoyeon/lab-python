from lec06_class.class07 import Account

print('Banking Application')
accounts = {}

while True:
    print('[0] 종료')
    print('[1] 계좌 개설')
    print('[2] 입금')
    print('[3] 출금')
    print('[4] 계좌 이체')
    print('[5] 계좌 정보 출력')
    print('--------')
    print('선택>>')
    menu = input()
    if menu == '0':
        break
    elif menu == '1':
        print('--- 신규 개좌 개설 ---')
        account_no = int(input('계좌번호 입력>> '))
        money = int(input('잔액 입력>> '))
        accounts[account_no] = Account(account_no, money)
        print(accounts)



