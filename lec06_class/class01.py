"""
클래스(class):
프로그램에서 만들려고 하는 대상(객체)이 가져야 할
속성(데이터)과 기능(함수)을 묶은 "데이터 타입"

메소드(method): 클래스가 가지고 있는 함수
필드(field): 클래스가 가지고 있는 데이터(변수)
"""

# TV 소프트웨어 작성
# TV 속성(데이터): 채널, 음량, 전원
# TV 기능: 채널 변경, 음량 변경, 전원 on/off
class BasicTv:
    """
    BasicTv 클래스
    """
    # 생성자가 호출됐을 때 실행되는 메소드(함수)
    def __init__(self, power, channel, volume):
        print('BasicTv 생성자 호출')
        self.power = power
        self.channel = channel
        self.volume = volume


    # 클래스 내부에서 정의하는 함수: 메소드
    def powerOnOff(self):
        if self.power:  # power가 True이면(TV가 켜져 있으면)
            self.power = False  # TV를 끔
            print('TV Off')
        else:   # TV가 꺼져 있으면
            self.power = True   # TV를 켬
            print('TV On')

    # 전원이 켜져있는 동안에만
    # 채널 순환(0 ~ 5)
    # 볼륨은 0 ~ 5 까지
    def channelUp(self):
        if self.power:
            self.channel += 1
            if self.channel == 6:
                self.channel = 0
            print('Channel:', self.channel)


    def channelDown(self):
        if self.power:
            self.channel -= 1
            if self.channel == -1:
                self.channel = 5
            print('Channel:', self.channel)


    def volumeUp(self):
        if self.power:
            if self.volume < 5:
                self.volume += 1
            print('Volume:', self.volume)


    def volumeDown(self):
        if self.power:
            if self.volume > 0:
                self.volume -= 1
            print('Volume:', self.volume)

# 클래스 설계(정의)

# 클래스의 객체(인스턴스)를 생성해서 변수에 저장
# 생성자(constructor) 호출 -> 객체(object) 생성
tv1 = BasicTv(power=False, channel=0, volume=0)
print(tv1)
print(tv1.power)
tv1.powerOnOff()  # TV 켬    # 메모리 주소값을 가지고 있는 변수 사용
tv1.channelUp()
tv1.channelUp()
tv1.channelUp()
tv1.channelDown()
tv1.powerOnOff()  # TV 끔
tv1.powerOnOff()  # TV 켬
print(tv1.channel)

tv2 = BasicTv(True, 100, 2)
tv2.volumeDown()
tv2.volumeDown()
tv2.volumeDown()
tv2.volumeDown()