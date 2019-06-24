import vrep
import sys, math
import keyboard 
#導入鍵盤
# child threaded script: 
# 內建使用 port 19997 若要加入其他 port, 在  serve 端程式納入
#simExtRemoteApiStart(19999)
  
vrep.simxFinish(-1)
  
clientID = vrep.simxStart('127.0.0.1', 19997, True, True, 5000, 5)
if clientID!= -1:
    print("Connected to remote server")
else:
    print('Connection not successful')
    sys.exit('Could not connect')

KickBallV = 360  
R_KickBallVel = (math.pi/180)*KickBallV
B_KickBallVel = -(math.pi/180)*KickBallV

errorCode,LR_handle=vrep.simxGetObjectHandle(clientID,'LR',vrep.simx_opmode_oneshot_wait)
errorCode,RR_handle=vrep.simxGetObjectHandle(clientID,'RR',vrep.simx_opmode_oneshot_wait)
errorCode,PL_handle=vrep.simxGetObjectHandle(clientID,'PL',vrep.simx_opmode_oneshot_wait)
vrep.simxSetJointTargetVelocity(clientID,LR_handle,0,vrep.simx_opmode_oneshot_wait)
vrep.simxSetJointTargetVelocity(clientID,RR_handle,0,vrep.simx_opmode_oneshot_wait)
vrep.simxSetJointTargetVelocity(clientID,PL_handle,0,vrep.simx_opmode_oneshot_wait)
#定義平移軸旋轉軸

def speed(handle,speed):
    errorCode=vrep.simxSetJointTargetVelocity(clientID,handle,speed,vrep.simx_opmode_oneshot_wait)



vrep.simxStartSimulation(clientID,vrep.simx_opmode_oneshot_wait)
#開始

while True:
    try:
        if keyboard.is_pressed('a'):
            speed(LR_handle,B_KickBallVel)
        elif keyboard.is_pressed('l'):
            speed(RR_handle,B_KickBallVel)
        else:
            speed(LR_handle,R_KickBallVel)
            speed(RR_handle,R_KickBallVel)
        if  keyboard.is_pressed('8'):
            errorCode=vrep.simxSetJointTargetVelocity(clientID,PL_handle,1,vrep.simx_opmode_oneshot_wait)
        else:
            errorCode=vrep.simxSetJointTargetVelocity(clientID,PL_handle,-1,vrep.simx_opmode_oneshot_wait)
    except:
            break