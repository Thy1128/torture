#列表的基本操作
#定义列表
name_list=["张三","王五","李四"]

#获取对应序列或者下标的元素
name_list[2]

#获取对应元素的序列或者下标
name_list.index("王五")

#修改相应下标的元素
name_list[0]="1"

#添加列表
name_list.append("feiyue")  #在末尾添加
name_list.insert(1,"ok")  #在指定位置添加

age_list=["23","12","56"]
name_list.extend(age_list)  #将两个列表进行拼接

name_list.remove("feiyue")  #删除指定元素，如果有多个，则删除第一个。
name_list.pop()  #删除最后一个元素
name_list.pop(2)  #删除固定序号的元素
name_list.clear()  #删除全部的元素
del name_list[1]  #删除指定列表的元素
del name_list  #删除列表

len(name_list)  #测试列表的长度
name_list.count("王五")  #计算列表的某个元素出现的次数

name_list.sort()  #升序排序
name_list.sort(reverse=True)  #降序输出
name_list.reverse()  #反转，逆序







