 #!/usr/bin/env python3
# os,time,csv,random 모듈을 import한다.
import os
import time
import csv
import random

# 행맨게임에서 사용할 그림을 단계별로 그려서 drawing 이라는 리스트에 저장해둠
drawing = [
'''
+======+
|      |
|
|
|
|
|
+==+
''',
'''
+======+
|      |
|      O
|
|
|
|
+==+
''',
'''
+======+
|      |
|      O
|      |
|
|
|
+==+
''',
'''
+======+
|      |
|      O/
|      |
|
|
|
+==+
''',
'''
+======+
|      |
|     \O/
|      |
|
|
|
+==+
''',
'''
+======+
|      |
|     \O/
|      |
|     /
|
|
+==+
''',
'''
+======+
|      |
|     \O/
|      |
|     / \\
|
|
+==+
'''
]

# 우리가 사용할 csv 파일의 column들은 단어명,유사어,뜻 이 세가지가 있다.
# 단어들을 저장해 둔 csv 파일을 읽어오고 리스트로 변환해주는 함수 get_words_list 를 만들어야 한다.  
# csv 파일을 with open으로 읽어온 후 csv.reader()함수를 이용해서 매 줄마다 이터레이트 하면서 각 줄이 하나의 리스트가 되고 이 리스트들이 큰 리스트에 저장되도록 한다. 
# 단어 리스트들이 들어 있는 큰 리스트를 리턴해준다.
def get_words_list(f):
  with open(f) as file:
    csv_f = csv.reader(file)
    wordlist = []
    for row in csv_f:
      name,alais,meaning = row
      wordlist.append([name,alais,meaning])
  return wordlist

# 단어에 대한 정보가 들어있는 리스트들을 담고 있는 큰 리스트를 매개변수로 입력하면, 그 중 한 단어를 랜덤으로 뽑아주는 함수 random_element 를 만든다. 
def random_element(list):
  randEle = list[random.randint(0,len(list)-1)]
  return randEle



#플래이 하는 함수 play()
def play():
  #get_words_list와 random_element 함수를 사용해서 한 단어와 그에 대한 정보를 담은 리스트를 무작위로 뽑고 randword라는 변수에 저장해둔다.
  ml = get_words_list('wordlist.csv')
  randword = random_element(ml)
  
  # 단어,유사어,뜻 변수에 저장
  word = randword[0]
  alais = randword[1]
  meaning = randword[2]

  # 단어를 맞추기 전 단어의 글자 수 만큼 '_'로 된 빈칸이 생기고 이는 한 글자를 맞출 때 마다 채워진다. 
  # 이를 위해 letterlist 와 matchletter 두 리스트를 생성한다.
  # letterlist에는 word를 이터레이트 하면서 한 글자씩 추가한다.
  # matchletter에는 len(word)를 이용해서 단어 길이만큼 '_'를 추가한다.  
  letterlist = []
  matchletter = []
  for letter in word:
    letterlist.append(letter)
  for i in range(len(word)):
    matchletter.append('_')
  
  guessed = []  # 이미 시도해 본 글자들 모아둔 리스트
  wrong = 0   # 틀린 개수 세는 변수
  end = False  # 게임이 끝났는지의 알려주는 변수
  
  
  os.system('clear')
  print("힌트를 얻고 싶으시다면 '힌트'라고 입력하세요.")
  print(drawing[wrong])
  print(' '.join(matchletter)+"\n")
  guess = input("글자를 입력하시오: ")
  while True: # break될때까지 글자 물어보기
    if guess not in guessed and len(guess)==1:   # 처음 입력해보는 글자이고 한 글자라면:
      if guess in letterlist:   # 입력한 글자가 단어에 포함되면 해당 자리에 '_' 대신 글자 보여주기
        for letter in letterlist:
            if letter == guess:
              num = letterlist.index(letter)
              matchletter[num] = guess
      else:  #입력한 글자가 단어에 포함되지 않으면 틀린 갯수 하나 더하기
        wrong += 1
      guessed.append(guess)  # 처음 입력해보는 글자이니 guessed에 추가

    elif guess in guessed:  # 이미 입력해본 글자이면 안내 메시지 프린트하기
      print("당신은 '"+guess+"'를 벌써 시도해봤습니다")
      time.sleep(1)

    elif guess == '힌트':  # '힌트'라고 치면 유사어 5초동안 보여주기 
      wrong += 1
      print("5초동안 힌트공개!")
      time.sleep(0.5)
      print("유사어: "+alais)
      time.sleep(5)
    
    # 기본적으로 행맨 그림과 맞춘 글자들을 보여주고, 게임이 끝났는지 안끝났는지에 따라 다른 것을 프린트한다.
    os.system('clear')
    print("힌트를 얻고 싶으시다면 '힌트'라고 입력하세요.")
    print(drawing[wrong])
    print(' '.join(matchletter)+"\n")
    
    if matchletter == letterlist or guess == word: # 단어를 맞추면 '정답' 프린트, end를 True로 변경해서 게임 끝났다고 알리기
      print("정답!")
      end = True
    elif wrong == 6:     # 6번 틀리면 '게임오버' 프린트, end를 True로 변경해서 게임 끝났다고 알리기
      print("게임오버!")
      end = True

    if end == False:  # 단어를 맞추거나 게임에서 지지 않아서 게임이 끝나지 않았으면 글자 물어보기
      guess = input("글자를 입력하시오: ")
    
    else:  # 게임이 끝나서 end가 True 이면 정답과 단어 뜻을 알려주고 while문 끝내기
      print("단어는 '"+word+"' 였습니다")
      print("뜻: "+meaning)
      time.sleep(2)
      break    
    

if __name__ == "__main__":
  a = play()
  while input("다음 게임으로 넘어가시겠습니까? (Y/N): ").upper() == "Y":
    a = play()
