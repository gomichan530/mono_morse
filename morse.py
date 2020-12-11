#####################################
# International Morse Code
#
# 2020.12.11 Only Letters      RG
#####################################

# Define lists for International Morse Code
alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

string = "SOS"

#送信文字列は何文字かを判断
letters = len(string)

#文字数だけのループを組む
for count in range(letters):
    letter = alphabet.index(string[count])     #一文字づつ数値を割り当てる
    morseletter = morse[letter]                #文字の場所によって、対応コードを判断する
    morselength = len(morseletter)
    
    print (string[count]," : ",morseletter," : ",morselength)
    
    for eachmorse in range(morselength):       #モールスコードの点か線で行動する
        if morseletter[eachmorse] == ".":
            print ("DOT")
            #短いLED点滅かビープ音をここから
        else:
            print ("DASH")
            #長いLED点滅かビープ音をここから
    
    print ("PAUSE")