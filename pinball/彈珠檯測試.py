import vrep
import sys, math
import keyboard
# child threaded script: 
# 內建使用 port 19997 若要加入其他 port, 在  serve 端程式納入
#simExtRemoteApiStart(19999)
  
vrep.simxFinish(-1)
  
clientID = vrep.simxStart('127.0.0.1', 19997, True, True, 5000, 5)
KickBallV = 360  
Move_Minus =-0.1        
Move_Plus =0.1
n=1
R_KickBallVel = (math.pi/180)*KickBallV
B_KickBallVel = -(math.pi/180)*KickBallV
if clientID!= -1:
    print("Connected to remote server")
else:
    print('Connection not successful')
    sys.exit('Could not connect')

errorCode,Sphere_handle=vrep.simxGetObjectHandle(clientID,'Sphere',vrep.simx_opmode_oneshot_wait)
errorCode,LR_handle=vrep.simxGetObjectHandle(clientID,'LR',vrep.simx_opmode_oneshot_wait)
errorCode,RR_handle=vrep.simxGetObjectHandle(clientID,'RR',vrep.simx_opmode_oneshot_wait)
errorCode,P1_handle=vrep.simxGetObjectHandle(clientID,'P1',vrep.simx_opmode_oneshot_wait)
vrep.simxSetJointTargetVelocity(clientID,LR_handle,0,vrep.simx_opmode_oneshot_wait)
vrep.simxSetJointTargetVelocity(clientID,RR_handle,0,vrep.simx_opmode_oneshot_wait)
vrep.simxSetJointTargetVelocity(clientID,P1_handle,0,vrep.simx_opmode_oneshot_wait)

if errorCode == -1:
    print('Can not find left or right motor')
    sys.exit()
def R():
    errorCode=vrep.simxSetJointTargetVelocity(clientID,LR_handle,B_KickBallVel,vrep.simx_opmode_oneshot_wait)
def L():    
     errorCode=vrep.simxSetJointTargetVelocity(clientID,RR_handle,B_KickBallVel,vrep.simx_opmode_oneshot_wait)
def U():
     errorCode=vrep.simxSetJointTargetVelocity(clientID,P1_handle,1,vrep.simx_opmode_oneshot_wait)
#定義平移軸及旋轉軸的速度


vrep.simxStartSimulation(clientID,vrep.simx_opmode_oneshot_wait)
#開始

while True:
    try:
            if keyboard.is_pressed('l'):
                L()
            elif keyboard.is_pressed('a'):
                R()
            elif keyboard.is_pressed('8'):
                U()
            else:
                errorCode=vrep.simxSetJointTargetVelocity(clientID,LR_handle,R_KickBallVel,vrep.simx_opmode_oneshot_wait)
                errorCode=vrep.simxSetJointTargetVelocity(clientID,RR_handle,R_KickBallVel,vrep.simx_opmode_oneshot_wait)
                errorCode=vrep.simxSetJointTargetVelocity(clientID,P1_handle,-1,vrep.simx_opmode_oneshot_wait)            
            
    except:
            break