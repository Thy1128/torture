import prettytable as pt   # 表格形式显示
import time

bank_log = []    # 初始化银行交易日志

class Bank:
    '''银行类'''
    def __init__(self):
        """初始化"""
        self.money = 0    # 封装和初始化金额
        self.bank_log = bank_log

    def deposit(self):
        """存款"""
        amount = float(input("请输入存款金额："))
        self.money += amount
        self.write_log(amount, '转入')

    def withdrawl(self):
        """取款"""
        amount = float(input("请输入取款金额："))
        if amount > self.money:
            print("余额不足")
        else:
            self.money -= amount
            self.write_log(amount, "消费")

    def transaction_log(self):
        """打印交易日志"""
        tb = pt.PrettyTable()
        tb.field_names = ['交易日期', '摘要', '金额', '币种', '余额']  # 设置表头
        for info in self.bank_log:
            # 判断转入还是消费，为金额前添加“+” 或“-”
            if info[1] == '转入':
                amout = "+{}".format(info[2])
            else:
                amout = "-{}".format(info[2])
            tb.add_row([info[0], info[1], amout, '人民币', info[3]])
        print(tb)

    def write_log(self, amount, handle):
        """写入日志"""
        # 按照指定形式获取时间
        creat_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        data = [creat_time, handle, amount, self.money]  # 组装列表
        self.bank_log.append(data)  # 写入日志信息


def display():
    """显示菜单栏"""
    menu = """
    ====================银行账户资金交易管理====================
            0：退出
            1：存款
            2：取款
            3：打印交易详情
    ==========================================================
    """
    print(menu)


if __name__ == '__main__':
    display()  # 显示菜单
    account = Bank()  # 创建对象
    while True:
        choice = int(input("请输入您的选择："))
        if choice == 0:
            exit(0)
            print("退出系统")
        elif choice == 1:
            flag = True
            while flag:
                # deposit_money = float(input('存款金额：'))
                account.deposit()
                flag = True if input("是否继续存款（yes/no）: ").lower() == "yes" else False
        elif choice == 2:
            flag = True
            while flag:
                # wd_money = float(input("取款金额："))
                account.withdrawl()
                flag = True if input("是否继续取款（yes/no）:").lower() == 'yes' else False
        elif choice == 3:
            account.transaction_log()
        else:
            print("请重新选择正确的序号")
import prettytable as pt   # 表格形式显示
import time

bank_log = []    # 初始化银行交易日志

class Bank:
    '''银行类'''
    def __init__(self):
        """初始化"""
        self.money = 0    # 封装和初始化金额
        self.bank_log = bank_log

    def deposit(self):
        """存款"""
        amount = float(input("请输入存款金额："))
        self.money += amount
        self.write_log(amount, '转入')

    def withdrawl(self):
        """取款"""
        amount = float(input("请输入取款金额："))
        if amount > self.money:
            print("余额不足")
        else:
            self.money -= amount
            self.write_log(amount, "消费")

    def transaction_log(self):
        """打印交易日志"""
        tb = pt.PrettyTable()
        tb.field_names = ['交易日期', '摘要', '金额', '币种', '余额']  # 设置表头
        for info in self.bank_log:
            # 判断转入还是消费，为金额前添加“+” 或“-”
            if info[1] == '转入':
                amout = "+{}".format(info[2])
            else:
                amout = "-{}".format(info[2])
            tb.add_row([info[0], info[1], amout, '人民币', info[3]])
        print(tb)

    def write_log(self, amount, handle):
        """写入日志"""
        # 按照指定形式获取时间
        creat_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        data = [creat_time, handle, amount, self.money]  # 组装列表
        self.bank_log.append(data)  # 写入日志信息


def display():
    """显示菜单栏"""
    menu = """
    ====================银行账户资金交易管理====================
            0：退出
            1：存款
            2：取款
            3：打印交易详情
    ==========================================================
    """
    print(menu)


if __name__ == '__main__':
    display()  # 显示菜单
    account = Bank()  # 创建对象
    while True:
        choice = int(input("请输入您的选择："))
        if choice == 0:
            exit(0)
            print("退出系统")
        elif choice == 1:
            flag = True
            while flag:
                # deposit_money = float(input('存款金额：'))
                account.deposit()
                flag = True if input("是否继续存款（yes/no）: ").lower() == "yes" else False
        elif choice == 2:
            flag = True
            while flag:
                # wd_money = float(input("取款金额："))
                account.withdrawl()
                flag = True if input("是否继续取款（yes/no）:").lower() == 'yes' else False
        elif choice == 3:
            account.transaction_log()
        else:
            print("请重新选择正确的序号")
import prettytable as pt   # 表格形式显示
import time

bank_log = []    # 初始化银行交易日志

class Bank:
    '''银行类'''
    def __init__(self):
        """初始化"""
        self.money = 0    # 封装和初始化金额
        self.bank_log = bank_log

    def deposit(self):
        """存款"""
        amount = float(input("请输入存款金额："))
        self.money += amount
        self.write_log(amount, '转入')

    def withdrawl(self):
        """取款"""
        amount = float(input("请输入取款金额："))
        if amount > self.money:
            print("余额不足")
        else:
            self.money -= amount
            self.write_log(amount, "消费")

    def transaction_log(self):
        """打印交易日志"""
        tb = pt.PrettyTable()
        tb.field_names = ['交易日期', '摘要', '金额', '币种', '余额']  # 设置表头
        for info in self.bank_log:
            # 判断转入还是消费，为金额前添加“+” 或“-”
            if info[1] == '转入':
                amout = "+{}".format(info[2])
            else:
                amout = "-{}".format(info[2])
            tb.add_row([info[0], info[1], amout, '人民币', info[3]])
        print(tb)

    def write_log(self, amount, handle):
        """写入日志"""
        # 按照指定形式获取时间
        creat_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        data = [creat_time, handle, amount, self.money]  # 组装列表
        self.bank_log.append(data)  # 写入日志信息


def display():
    """显示菜单栏"""
    menu = """
    ====================银行账户资金交易管理====================
            0：退出
            1：存款
            2：取款
            3：打印交易详情
    ==========================================================
    """
    print(menu)


if __name__ == '__main__':
    display()  # 显示菜单
    account = Bank()  # 创建对象
    while True:
        choice = int(input("请输入您的选择："))
        if choice == 0:
            exit(0)
            print("退出系统")
        elif choice == 1:
            flag = True
            while flag:
                # deposit_money = float(input('存款金额：'))
                account.deposit()
                flag = True if input("是否继续存款（yes/no）: ").lower() == "yes" else False
        elif choice == 2:
            flag = True
            while flag:
                # wd_money = float(input("取款金额："))
                account.withdrawl()
                flag = True if input("是否继续取款（yes/no）:").lower() == 'yes' else False
        elif choice == 3:
            account.transaction_log()
        else:
            print("请重新选择正确的序号")
