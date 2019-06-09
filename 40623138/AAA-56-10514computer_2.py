import vrep
import keyboard
import time
import sys, math     
# child threaded script: 
# 內建使用 port 19997 若要加入其他 port, 在  serve 端程式納入
#simExtRemoteApiStart(19999)
  
vrep.simxFinish(-1)


clientID = vrep.simxStart('127.0.0.1', 19997, True, True, 5000, 5)
KickBallV = 360
R_KickBallVel = (math.pi/180)*KickBallV
B_KickBallVel = -(math.pi/180)*KickBallV
if clientID!= -1:
    print("Connected to remote server")
else:
    print('Connection not successful')
    sys.exit('Could not connect')
    
errorCode,Sphere_handle=vrep.simxGetObjectHandle(clientID,'Sphere',vrep.simx_opmode_oneshot_wait)
errorCode,P1_handle=vrep.simxGetObjectHandle(clientID,'P1',vrep.simx_opmode_oneshot_wait)
errorCode,P2_handle=vrep.simxGetObjectHandle(clientID,'P2',vrep.simx_opmode_oneshot_wait)
errorCode,R1_handle=vrep.simxGetObjectHandle(clientID,'R1',vrep.simx_opmode_oneshot_wait)
errorCode,R2_handle=vrep.simxGetObjectHandle(clientID,'R2',vrep.simx_opmode_oneshot_wait)
errorCode,B1_handle=vrep.simxGetObjectHandle(clientID,'B1',vrep.simx_opmode_oneshot_wait)


vrep.simxSetJointTargetVelocity(clientID,P1_handle,0,vrep.simx_opmode_oneshot_wait)
vrep.simxSetJointTargetVelocity(clientID,P2_handle,0,vrep.simx_opmode_oneshot_wait)
vrep.simxSetJointTargetVelocity(clientID,R1_handle,0,vrep.simx_opmode_oneshot_wait)
vrep.simxSetJointTargetVelocity(clientID,R2_handle,0,vrep.simx_opmode_oneshot_wait)

def speed(handle,speed):
    errorCode = vrep.simxSetJointTargetVelocity(clientID,handle,speed,vrep.simx_opmode_oneshot_wait)
def getballposition():
    while True:
        errorCode,position_BR=vrep.simxGetObjectPosition(clientID,R1_handle,-1,vrep.simx_opmode_oneshot)
        errorCode,position_S=vrep.simxGetObjectPosition(clientID,Sphere_handle,-1,vrep.simx_opmode_oneshot)
        errorCode,position_RR=vrep.simxGetObjectPosition(clientID,R1_handle,-1,vrep.simx_opmode_oneshot)
        BB =position_S[1] - position_BR[1]
        BBB =position_S[0] - position_BR[0]
        vrep.simxStartSimulation(clientID,vrep.simx_opmode_oneshot_wait)
        Mv = BB*-1.5
        vrep.simxSetJointTargetVelocity(clientID,P1_handle,Mv,vrep.simx_opmode_oneshot_wait)
getballposition()
