import configparser

config = configparser.ConfigParser() # configparser 모듈에서 객체 생성
config.sections() # 섹션 정보 읽어오기

config.read('example.cfg') # ['example.cfg']
config.sections() # ['Section One', 'Section Two', 'Section Three']

for key in config['Section One']: # 키 출력
    print(key)