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
# 우선 단어들을 저장해 둔 csv 파일을 읽어오고 리스트로 변환해주는 함수 get_words_list 를 만들어야 한다.  
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


def start():
  os.system('clear')
  print("""HANGMAN GAME

  1.play

  2. tutorial

  """)
  ask = int(input("Enter number: "))
  return ask

#플래이 하는 함수 play()
def play():
  #get_words_list와 random_element 함수를 사용해서 한 단어와 그에 대한 정보를 담은 리스트를 무작위로 뽑고 randword라는 변수에 저장해둔다.
  ml = get_words_list('wordlist.csv')
  randword = random_element(ml)
  
  # randword에서 단어, 유사어, 의미를 각각 word,alais,meaning 변수에 저장해둔다.
  word = randword[0]
  alais = randword[1]
  meaning = randword[2]

  # 단어를 맞추기 전 단어의 글자 수 만큼 _로 된 빈칸이 생기고 이는 한 글자를 맞출 때 마다 채워진다. 
  # 이를 위해 letterlist 와 matchletter 두 리스트를 생성한다.
  # letterlist에는 word를 이터레이트 하면서 한 글자씩 추가한다.
  # matchletter에는 len(word)를 이용해서 단어 길이만큼 '_'를 추가한다.  
  letterlist = []
  matchletter = []
  for letter in word:
    letterlist.append(letter)
  for i in range(len(word)):
    matchletter.append('_')
  
  #벌써 시도해 본 글자들을 모아두는 guessed 리스트를 생성하고 틀린 갯수를 세는 wrong 변수를 0값으로 저장.
  guessed = []
  wrong = 0
  #게임에서 승리 유무를 따져주는 correct 변수를 False로 저장.
  correct = False
  #게임 화면 프린트 시작!
  # os.system('clear')로 화면을 비운다. "힌트를 얻고 싶으시다면 '힌트'라고 입력하세요" 라는 문장 프린트. drawing의 wrong 인덱스에 해당하는 그림 프린트. matchletter 리스트 속 엘리멘트들을 스페이스 바 로 연결해서 프린트.
  # 글자를 물어보고 guess라는 변수에 저장한다.
  os.system('clear')
  print("힌트를 얻고 싶으시다면 '힌트'라고 입력하세요.")
  print(drawing[wrong])
  print(' '.join(matchletter)+"\n")
  guess = input("글자를 입력하시오: ")
  
  # 참일 동안 글자를 계속 물어보고 입력값에 따라 다르게 반응한다.
  # wrong이 6보다 작을 때의 경우의 수를 if문으로 따진다.
  # 만약 guess가 한 글자 이고 guessed에 없으면 guessed에 guess를 추가하고, letterlist에 guess가 있는지 없는지에 따라 다르게 반응.
  # guess가 letterlist 안에 있으면 letterlist를 루핑하는 for문에서 guess와 단어 글자가 같으면 matchletter의 그 인덱스를 guess로 바꾼다. 
  # guess가 letterlist 안에 없으면 wrong에 1을 추가한다.
  # 만약 단어 전체를 입력해서 맞으면 correct를 True 로 바꿔준다.
  # 만약 입력한 단어를 벌써 시도해 본 적이 있었다면 "당신은 이미 그 글자를 입력한 적이 있습니다" 라고 프린트.
  # 만약 '힌트'라고 입력했으면 wrong에 1을 추가하고 유사어를 5초 동안 보여준다.
  # 만약 글자를 한 개 한 개 넣어서 단어를 맞췄으면 correct를 True로 바꿔준다. 
  # 화면을 비우고 행맨 그림을 저장하고 있는 리스트의 wrong인덱스에 해당하는 그림을 프린트해주고 matchletter를 join한 스트링을 프린트해준다.
  # 만약 correct = True여서 정답을 맞췄으면 단어를 맞춘 후 while문을 끝내고, 만약 6번 틀렸으면 "GAME OVER!"와 단어 의미를 프린트해주고 while문을 끝낸다.
  # 위 두 사항에 해당하지 않을 경우 글자를 다시 물어본다.
  while True:
    if wrong < 6:
      if guess not in guessed and len(guess)==1:
        if guess in letterlist:
          for letter in letterlist:
              if letter == guess:
                num = letterlist.index(letter)
                matchletter[num] = guess
        elif guess not in letterlist:
          wrong += 1
        guessed.append(guess)

      elif guess == word:
        correct = True

      elif guess in guessed:
        print("당신은 '"+guess+"'를 벌써 시도해봤습니다")
        time.sleep(10)

      elif guess == 'hint':
        wrong += 1
        print("5초동안 힌트공개!")
        time.sleep(0.5)
        print("유사어: "+alais)
        time.sleep(5)

      if ''.join(matchletter) == word:
        correct = True


      os.system('clear')
      print("힌트를 얻고 싶으시다면 '힌트'라고 입력하세요.")
      print(drawing[wrong])
      
      print(' '.join(matchletter)+"\n")
      if correct == True:
        print("정답! 단어는 '"+word+"' 였습니다")
        print("뜻: ",meaning)
        time.sleep(2)
        break
      if wrong == 6:      
        #os.system('clear')  
        #print(drawing[6])
        print("GAME OVER!")
        print("뜻: "+meaning)
        time.sleep(2)
        break
      guess = input("글자를 입력하시오: ")
        

def tutorial():
  os.system('clear')
  print("tutorial")
 

if __name__ == "__main__":
  a = play()
  while input("다음 게임으로 넘어가시겠습니까? (Y/N): ").upper() == "Y":
    a = play()