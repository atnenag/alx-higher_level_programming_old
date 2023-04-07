#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("out of range")
            dividend = my_list_1[i]
            divisor = my_list_2[i]
            if type(dividend) not in (int, float) or type(divisor) \
            not in (int, float):
                raise TypeError("wrong type")
            if divisor == 0:
                raise ZeroDivisionError("division by 0")
            result = dividend / divisor
        except IndexError:
            print("out of range")
            new_list.append(0)
        except TypeError:
            print("wrong type")
            new_list.append(0)
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        else:
            new_list.append(result)
        finally:
            pass
    return new_list
