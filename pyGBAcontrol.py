#%%
from timeout_decorator.timeout_decorator import timeout
from GBAmodule import *
import sys
import termios
import timeout_decorator
# %%
# A()
# %%
# p=A_push()
# l=B_push()
# s=R_push()
# w=U_push()
# a=L_push()
# z=D_push()
# k=Start_push()
# m=Select_push()

# pr=A_release()
# lr=B_release()
# sr=R_release()
# wr=U_release()
# ar=L_release()
# zr=D_release()
# kr=Start_release()
# mr=Select_release()

#%%
#timeout_s*(time_count+1)が0.2ぐらいになるように
timeout_s=0.04
time_count=6

#%%
def pushkey(ch):
    if (ch=="p"):
        A_push()
        # sleep(0.1)
    elif(ch=="l"):
        B_push()
        # sleep(0.1)
    elif(ch=="s"):
        R_push()
        # sleep(0.01)
    elif(ch=="w"):
        U_push()
        # sleep(0.01)
    elif(ch=="a"):
        L_push()
        # sleep(0.01)
    elif(ch=="z"):
        D_push()
        # sleep(0.01)
    elif(ch=="k"):
        Start_push()
        # sleep(0.1)
    elif(ch=="m"):
        Select_push()
        # sleep(0.1)
    elif(ch=="pr"):
        A_release()
    elif(ch=="lr"):
        B_release()
    elif(ch=="sr"):
        R_release()
    elif(ch=="wr"):
        U_release()
    elif(ch=="ar"):
        L_release()
    elif(ch=="zr"):
        D_release()
    elif(ch=="kr"):
        Start_release()
    elif(ch=="mr"):
        Select_release()







#%%
#標準入力のファイルディスクリプタを取得
fd = sys.stdin.fileno()
#%%
#fdの端末属性をゲットする
#oldとnewには同じものが入る。
#newに変更を加えて、適応する
#oldは、後で元に戻すため
old = termios.tcgetattr(fd)
new = termios.tcgetattr(fd)

#new[3]はlflags
#ICANON(カノニカルモードのフラグ)を外す
new[3] &= ~termios.ICANON
#ECHO(入力された文字を表示するか否かのフラグ)を外す
new[3] &= ~termios.ECHO

@timeout_decorator.timeout(timeout_s)
def test():
    termios.tcsetattr(fd, termios.TCSANOW, new)
    # キーボードから入力を受ける。
    # lfalgsが書き換えられているので、エンターを押さなくても次に進む。echoもしない
    ch = sys.stdin.read(1)
    return ch



#%%
ch=""
A_time_count=0
B_time_count=0
Start_time_count=0
Select_time_count=0
tmp_b=False
while (True):
    try:
        # # 書き換えたnewをfdに適応する
        # termios.tcsetattr(fd, termios.TCSANOW, new)
        # # キーボードから入力を受ける。
        # # lfalgsが書き換えられているので、エンターを押さなくても次に進む。echoもしない
        # ch = sys.stdin.read(1)
        # if ch
        ch_old = ch
        ch=test()
        
        # 矢印キーが押される場合
        arrow = (ch=="s")|(ch=="w")|(ch=="a")|(ch=="z")
        arrow_old = (ch_old=="s")|(ch_old=="w")|(ch_old=="a")|(ch_old=="z")


        if (ch=="o"):
            if(tmp_b):
                B_push()
                tmp_b=False
            else:
                B_release()
                tmp_b=True


            

        if(ch=="p"):
            A_time_count+=1
        elif(ch=="l"):
            B_time_count+=1
        elif(ch=="k"):
            Start_time_count+=1
        elif(ch=="m"):
            Select_time_count+=1
        
        if(A_time_count>0):
                pushkey("p")
                A_time_count+=1
                if(A_time_count>time_count):
                    A_time_count=0
                    pushkey("pr")
        if(B_time_count>0):
            pushkey("l")
            B_time_count+=1
            if(B_time_count>time_count):
                B_time_count=0
                pushkey("lr")
        if(Start_time_count>0):
            pushkey("k")
            Start_time_count+=1
            if(Start_time_count>time_count+3):
                Start_time_count=0
                pushkey("kr")
        if(Select_time_count>0):
            pushkey("m")
            Select_time_count+=1
            if(Select_time_count>time_count):
                Select_time_count=0
                pushkey("mr")
            
        if (ch_old==ch):
            pushkey(ch)
        # 矢印キーの向きが変わった場合
        elif(arrow&arrow_old):
            pushkey(ch_old+"r")#リリース
            pushkey(ch)
            


    except:
        pushkey(ch_old)
        ch=""
        print("timed out") 
        # A_release()
        # B_release()
        R_release()
        U_release()
        D_release()
        L_release()
        # Start_release()
        # Select_release()

    finally:
        # fdの属性を元に戻す
        # 具体的にはICANONとECHOが元に戻る
        termios.tcsetattr(fd, termios.TCSANOW, old)

    print(ch)
    
    # print(type(ch))