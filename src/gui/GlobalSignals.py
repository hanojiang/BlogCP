from PySide2.QtCore import Signal,QObject
from PySide2.QtWidgets import QTextBrowser, QPushButton

class GlobalSigals(QObject):
    # 定义一种信号，两个参数 类型分别是： QTextBrowser 和 字符串
    # 调用 emit方法 发信号时，传入参数 必须是这里指定的 参数类型
    text_print = Signal(QTextBrowser, str)

    # 还可以定义其他种类的信号
    #update_table = Signal(str)

    changeConnectionButtor = Signal(QPushButton, str)