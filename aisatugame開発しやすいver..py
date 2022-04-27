English0=["Good morning","Good aternoon","Good evening","Sleeping...zzz"]
Japanese1=["おはよう","こんにちは！","こんばんは","睡眠中zzz"]
Arabic2=["صباح الخير","مرحبا","مساء الخير","نائم"]

input_language = input('英語表記の場合は0日本語表記の場合は1アラビア語の場合は2と入れよう!! : ')
input_time = input('時間を二桁入力しよう!! : ')
time = int(input_time)

for asa in range(5,12):
    if int(asa) == time:
        if str(input_language) == '0':
            print(English0[0])
        if str (input_language) == '1':
            print(Japanese1[0])
        if str(input_language) == '2':
            print(Arabic2[0])

for hiru in range(12,19):
    if int(hiru) == time:
        if str(input_language) == '0':
            print(English0[1])
        if str (input_language) == '1':
            print(Japanese1[1])
        if str(input_language) == '2':
            print(Arabic2[1])

for yoru in range(19,25):
    if int(yoru) == time:
        if str(input_language) == '0':
            print(English0[2])
        if str (input_language) == '1':
            print(Japanese1[2])
        if str(input_language) == '2':
            print(Arabic2[2])

for sleep in range(0,5):
    if int(sleep) ==time:
        if str(input_language) == '0':
            print(English0[3])
        if str (input_language) == '1':
            print(Japanese1[3])
        if str(input_language) == '2':
            print(Arabic2[3])

if 2 < int(input_language):
    print("言語の開発が必要です(・_・;)")
if 24 < int(input_time):
    print("存在しない時間です。")

# ベース
# 言語.数字=[挨拶３つ(順番通りにしよう)と、睡眠中と入れる]

# 例
# Japanese1=["おはよう","こんにちは！","こんばんは","睡眠中zzz"]
#　　　　　　　これ↑は0   　これは↑1　　　これは↑2　　これは↑3　　　　←上の挨拶たちを数字に直すとこうなる
#　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　↑こいつらを(言語の)数字とします

# これらを文字起こしします
# そのためのプログラムたち[ここの部分イラン↓][こ↓こ重要]
#         if str (input_language) =='(言語.)数字':
#             print(言語.数字[(言語の)数字])
#             (プログラミングでは0スタートである)

# 例
#         if str (input_language) == '1':
#             print(Japanese1[0])
#　　　　　　　　　　　おはよう
#         if str (input_language) == '1':
#             print(Japanese1[1])
# 　　　　　　　　　　こんにちは
#         if str (input_language) == '1':
#             print(Japanese1[2])
# 　　　　　　　　　　こんばんは
#         if str (input_language) == '1':
#             print(Japanese1[3])
# 　　　　　　　　　　睡眠中zzz

# これで言語の追加が完了します。