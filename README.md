# GobangGame
一个五子棋机器人

# 作者
Simon-xuan(轩轩TAT)

# V 1.0.1
**发布时间** 2024.12.15
**语言** Python
**算法** Minimax+剪枝
**语言** 简体中文
## 库依赖
### numpy 
安装方法:pip install numpy(用于输出)
### os
安装方法:pip install os(用于清除终端)
### time
安装方法:pip install time(用于等待)
## 功能
玩家先下(执黑子),通过输入横竖坐标传入数据.
机器人后下(执白子),两方谁先连续WIN_CONDITION(默认值=5)连接(可以在横、竖、斜上连接),机器人会自动判定胜利.
## 变量作用
SEARCH_DEPTH 调节机器人搜索深度(数值越大,机器人越智能,但运行速度越慢) 默认值=1
BOARD_SIZE 棋盘大小(横纵大小,从0开始计算) 默认值=10
PLAYER_HUMAN 人类下棋人数 目前数值仅可为1 默认值=1
PLAYER_ROBOT 机器人下棋人数 目前数值仅可为2 默认值=2
WIN_CONDITION 获胜条件(即相连获胜数) 默认值=5
CLEAN 判定下棋后是否清屏(美观) 默认值=True
## 用户输入
是否开始游戏？(y/n) y为开始 除y以外的其他值为结束
x y 即横坐标和纵坐标 用空格隔开
## 电脑输出
思考提示词
机器人下棋位置
棋盘样式
提示下棋词
## 使用示例
<img width="255" alt="截屏2024-12-15 14 38 35" src="https://github.com/user-attachments/assets/107000f9-62b0-4704-8b54-c0efeb48619b" />
<img width="232" alt="截屏2024-12-15 14 38 52" src="https://github.com/user-attachments/assets/88b922aa-2c95-4dc4-b674-aa6016ba981c" />
**感谢使用v.1.0.1**
