#####################################
# morse.py
# International Morse Code
#
# 文字列の入力を受け付け、モールス信号を出力する
#
# 2020.12.11 RG 初回リリース
#####################################

import time          # sleep関数を必要とするので
import winsound      # 音を鳴らしたいので

# モールス信号の定義をする
alphabet = [" ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
morse = [" ",".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

# モールス信号の定義をする
basetime = 0.070                #基本長は70msecのつもり
dottime = basetime * 1          #点の長さ
dashtime = basetime * 3         #線の長さ
gaptime = basetime * 1          #点とか線の間の待ち時間
lettergaptime = basetime * 3    #一文字の間の待ち時間
wordgaptime = basetime * 7      #単語間の待ち時間

frequency = 330                 #ビープ音の周波数

string = input("Please enter a string : ")
string = string.upper()                        #入力した文字列を大文字化する
letters = len(string)                          #全部で何文字？

for count in range(letters):                   #文字数だけのループを組む
    letter = alphabet.index(string[count])     #一文字づつに数値を割り当てる
    morseletter = morse[letter]                #文字の場所によって、対応モールスコードを判断する
    morselength = len(morseletter)
    
    print (string[count]," : ",morseletter," : ",morselength)
    
    for eachmorse in range(morselength):       #モールスコードの点か線か空白で行動を起こす
        if morseletter[eachmorse] == ".":
            print ("DOT")
            winsound.Beep (frequency, int(dottime*1000))
            time.sleep (gaptime)
            #短いLED点滅かビープ音をここから
        elif morseletter[eachmorse] == "-":
            print ("DASH")
            winsound.Beep (frequency, int(dashtime*1000))
            time.sleep (gaptime)
            #長いLED点滅かビープ音をここから
        else:
            print ("End of Word")
            time.sleep (wordgaptime)
            #単語の終わりなので待ちを入れる必要あり
            
    time.sleep (lettergaptime)