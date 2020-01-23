# Create function dollarize() that takes Float and returns dollarized format:
# dollarize(123456.78901) -> "$123,456.80"
# dollarize(-123456.7801) -> "-$123,456.78"
# dollarize(1000000) -> "$1,000,000"
# Convert this function into useful class MoneyFmt. MoneyFmt contains single data value(the
# amount) and 4 methods.
# "init" //constructor initializes the data value
# "update" //method replaces data value with new one
# "repr" //methods returns Float value
# "str" //method, that implements logic of dollarize() method
# //The output will look like this:
# import moneyfmt
# cash = moneyfmt.MoneyFmt(12345678.021)
# print(cash) -- returns "$12,345,678.02"
# cash.update(100000.4567)
# print(cash) -- returns "$100,000.46"
# cash.update(-0.3)
# print(cash) -- returns "-$0.30"
# repr(cash) -- returns -0.3
#
#
# Создайте функцию dollarize (), которая принимает Float и возвращает долларизованный формат:
# долларизация (123456,78901) -> "$123 456,80"
# долларизация (-123456,7801) -> "-$123 456,78"
# долларизация (1000000) -> «1 000 000»
# Преобразуйте эту функцию в полезный класс MoneyFmt. MoneyFmt содержит одно значение данных (
# количество) и 4 метода.
# "init" // конструктор инициализирует значение данных
# "update" // метод заменяет значение данных новым
# "repr" // методы возвращают значение типа Float
# "str" ​​// метод, который реализует логику метода dollarize ()
# // Вывод будет выглядеть так:
# импорт денег
# cash = moneyfmt.MoneyFmt (12345678.021)
# распечатать (наличными) - возвращает «$ 12 345 678,02»
# cash.update (100000.4567)
# распечатать (наличными) - возвращает "100 000,46 долларов"
# cash.update (-0,3)
# распечатать (наличными) - возвращает "- $ 0,30"
# repr (cash) - возвращает -0,3

import locale
locale.setlocale( locale.LC_ALL, '' )
'English_United States.1252'

class MoneyFmt:

    def __init__(self, value):
        self.value = value
        self.update(value)

    def update(self, value1):
        self.up_value = round(value1, 2)
        print("\n", value1)
        self.__str__()

    def __repr__(self):
        pass

    def __str__(self):
        self.str_value = str(self.up_value)
        # print(self.str_value)
        self.li = [i for i in self.str_value.split(".")]
        self.nu = self.li[0]
        self.li_nu = list(self.nu)
        # print(self.li_nu)
        self.rev_li_nu = self.li_nu[-1::-1]
        # print(self.rev_li_nu)
        three = 1
        for i in self.rev_li_nu:
            three += 1
            if three % 4 == 0:
                self.rev_li_nu.insert(three - 1, ",")
        # print(f"{self.rev_li_nu}")
        self.ori = self.rev_li_nu[-1::-1]
        # print(self.ori)
        if self.ori[0] == ",":
            self.ori.remove(",")
        # print(self.ori)
        self.lis = ""
        for i in self.ori:
            self.lis += i
        # print(self.lis)
        # print(self.li[-1])
        self.to4ka = "."
        self.to4ka += self.li[-1]
        self.message = self.lis
        # print((self.message))
        self.dollarize()

    def dollarize(self):
        self.dol = "$"
        if type(self.up_value) == float:
            self.message1 = self.dol + self.message + self.to4ka
        else:
            self.message1 = self.dol + self.message
        print(self.message1)

many = MoneyFmt(123456789.123456789)

many.update(987654321.546)
many.update(8.349)