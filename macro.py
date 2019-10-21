import pyautogui #마우스 키보드 제어
import pyperclip # 클립보드 제어
import random    # 랜덤

#마우스 포인터를 s초 만큼 움직이고 클릭하는 함수 생성
def moveclick(x,y,s):
    pyautogui.moveTo(x,y,s)
    pyautogui.click()
    return

pyperclip.copy('https://www.thecamp.or.kr/pcws/main/viewList.do') # 더캠프 주소 복사
pyautogui.click(213,32)                                           # 첫 번째 탭 클릭
pyautogui.click(420,69)                                           # 주소창 클릭
pyautogui.hotkey('ctrl', 'v')                                     # 붙여넣기
pyautogui.press('enter')                                          # 엔터키 presss 
moveclick(1799,121,3)                                             # 로그인 버튼 클릭
pyautogui.moveTo(1799,121,3)                                      # 스크롤를 위해 3초 delay
pyautogui.scroll(-1000)                                           # 아래로 1000만큼 스크롤
moveclick(513,204,3)                                              #'가입카페 목록' 버튼 클릭
moveclick(513,250,1)                                              # 바로 밑 부대 클릭
moveclick(564,578,3)                                              #'위문편지' 클릭
moveclick(874,661,5)                                              #'제목을 입력하세요' 클릭
f = open("title.txt", 'r',encoding='UTF8')                        # 타이틀 불러오기
title = f.read()
finaltitle = title.split('\n')[random.randrange(3)]               # 랜덤으로 불러오기
pyperclip.copy(finaltitle)                                        # 랜덤값 복사
f.close()
pyautogui.hotkey('ctrl', 'v')                                     #붙여넣기 
moveclick(1079,766,2)                                             #본문 부분 클릭
f = open("detail.txt", 'r',encoding='UTF8')                        #본문 부분 불러오기
detali = f.read()
pyperclip.copy(detali)
f.close()
pyautogui.hotkey('ctrl', 'v') 
pyautogui.scroll(-500)                                            #아래로 500만큼 스크롤
moveclick(1454,568,3)                                             #'보내기' 클릭
moveclick(876,629,3)                                              #'알림' 클릭
moveclick(937,628,3)                                              #'확인' 클릭
