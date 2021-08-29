import os

data_list = os.listdir("my_experiments/data/list/pictures/original")

train_datas = []
test_datas = []
for i, data in enumerate(data_list):
    if i%4 == 3:
        test_datas.append("pictures/original/" + data + "	pictures/mask/" + data)
    else:
        train_datas.append("pictures/original/" + data + "	pictures/mask/" + data)

test_lst = "\n".join(test_datas)
train_lst = "\n".join(train_datas)

with open("my_experiments/data/list/val.lst", "w") as f1:
    print(test_lst, file=f1)

with open("my_experiments/data/list/train.lst", "w") as f2:
    print(train_lst, file=f2)