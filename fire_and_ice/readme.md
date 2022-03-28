# 关卡数据的形状

### 一个关卡有哪些东西呢？
* 墙
* 岩浆
* 冰水
* 毒水
* 机关， 由两部分组成一套：
  * 一个脚踩的按钮
  * 一个可以开关的门
* 通关地点

### 这些东西， 要记录哪些数据呢？
* 位置

----
# 结论是
数据的样子：
A set of actors, each actor have a pos.

```lang=python3
[
    {type pos}

    {id: btn1,
    type: button,
    pos: (300, 500)}

    {type: door,
    controlled_by: btn1,
    pos: (400, 600)}
]
```

### type表
| 物品类型   | type   |
| ---------- | ------ |
| 墙         | wall   |
| 岩浆       | lava   |
| 冰水       | water  |
| 毒水       | poison |
| 脚踩的按钮 | button |
| 门         | door   |
| 通关地点   | goal    |
