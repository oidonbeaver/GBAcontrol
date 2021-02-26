#%%
import RPi.GPIO as GPIO
from time import sleep
#%%
import numpy as np
# %%
GPIO.setmode(GPIO.BCM)
# 4番ピン故障
# ７番ピンモニターと接触不良
# %%

for i in range(2,12):
    GPIO.setup(i,GPIO.OUT)
    GPIO.output(i,GPIO.LOW) 
    # print(i)

# %%
def A(time=0.2):
    GPIO.output(2,GPIO.HIGH)
    sleep(time)
    GPIO.output(2,GPIO.LOW)

def B(time=0.2):
    GPIO.output(3,GPIO.HIGH)
    sleep(time)
    GPIO.output(3,GPIO.LOW)
def R(time=0.2):
    GPIO.output(5,GPIO.HIGH)
    sleep(time)
    GPIO.output(5,GPIO.LOW)


def U(time=0.2):#緑
    GPIO.output(6,GPIO.HIGH)
    sleep(time)
    GPIO.output(6,GPIO.LOW)

def D(time=0.2):#オレンジ
    GPIO.output(8,GPIO.HIGH)
    sleep(time)
    GPIO.output(8,GPIO.LOW)

def L(time=0.2):#紫
    GPIO.output(9,GPIO.HIGH)
    sleep(time)
    GPIO.output(9,GPIO.LOW)


def Start(time=0.2):
    GPIO.output(10,GPIO.HIGH)
    sleep(time)
    GPIO.output(10,GPIO.LOW)

def Select(time=0.2):
    GPIO.output(11,GPIO.HIGH)
    sleep(time)
    GPIO.output(11,GPIO.LOW)
#%%
def B_push():
     GPIO.output(3,GPIO.HIGH)
    
def B_release():
    GPIO.output(3,GPIO.LOW)


def A_push():
    GPIO.output(2,GPIO.HIGH)
    
def A_release():
    GPIO.output(2,GPIO.LOW)

def R_push():
    GPIO.output(5,GPIO.HIGH)
    
def R_release():
    GPIO.output(5,GPIO.LOW)

def U_push():
    GPIO.output(6,GPIO.HIGH)
    
def U_release():
    GPIO.output(6,GPIO.LOW)

def D_push():
    GPIO.output(8,GPIO.HIGH)
    
def D_release():
    GPIO.output(8,GPIO.LOW)

def L_push():
    GPIO.output(9,GPIO.HIGH)
    
def L_release():
    GPIO.output(9,GPIO.LOW)

def Start_push():
    GPIO.output(10,GPIO.HIGH)
    
def Start_release():
    GPIO.output(10,GPIO.LOW)

def Select_push():
    GPIO.output(11,GPIO.HIGH)
    
def Select_release():
    GPIO.output(11,GPIO.LOW)
# %%

# %%
