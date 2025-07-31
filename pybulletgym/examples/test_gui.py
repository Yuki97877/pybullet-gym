import pybullet as p
import pybullet_data
import time

# GUIモードで接続
p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# 平面とロボット表示
p.loadURDF("plane.urdf")
p.loadURDF("r2d2.urdf", [0, 0, 1])

# 数秒表示
for _ in range(240):
    p.stepSimulation()
    time.sleep(1.0 / 60.0)

p.disconnect()
