# -*- coding: utf-8 -*-
# @Author   : Slowly
# @FileName : test.py
# @Software : PyCharm
# @version  ：1.0
# @LastEdit : 2020/12/15 11:30


def compare(old, new, key=None):
    if isinstance(old, dict) and isinstance(new, dict):
        for key in new:
            if key in old:
                compare(old[key], new[key], key)

        # 差集
        new_to_old = set(list(new.keys())).difference(set(list(old.keys())))
        old_to_new = set(list(old.keys())).difference(set(list(new.keys())))
        if old_to_new or new_to_old:
            print(f'字典中的整个key所对应的values缺失:key=【old:{list(old_to_new)} ==> new:{list(new_to_old)}】')

    elif isinstance(old, list) and isinstance(new, list):
        if len(old) == len(new):
            try:
                if [len(list(list1.keys())) for list1 in old][0] == 1:
                    dif_old = set([list(x.values())[0] for x in old]).difference(
                        set([list(x.values())[0] for x in new]))
                    dif_new = set([list(x.values())[0] for x in new]).difference(
                        set([list(x.values())[0] for x in old]))
                    if dif_old or dif_new:
                        print(f"【{key}】所对应的差别为:【old:{list(dif_old)} ==> new:{list(dif_new)}】")
                else:
                    for list1, list2 in zip(old, new):
                        compare(list1, list2, key)
            except:
                pass
        else:
            # TODO: 比较列表的不同
            print(f'【{key}】所对应的列表长度不相等【len(old)={len(old)} ==> len(new)={len(new)}】')
    else:
        try:
            old_, new_ = old.strip(), new.strip()
        except:
            old_, new_ = old, new
        if old_ != new_:
            print(f'【{key}】所对应的values的差别为:【old:{[old]} ==> new:{[new]}】')


if __name__ == '__main__':
    pass
