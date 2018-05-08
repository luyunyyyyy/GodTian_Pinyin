#coding=utf-8

import heapq


class Item(object):

    def __init__(self, score, path):
        self.__score = score
        self.__path = path

    @property
    def score(self):
        return self.__score

    @property
    def path(self):
        return self.__path

    def __lt__(self, other):
        return self.__score < other.score

    def __le__(self, other):
        return self.__score <= other.score

    def __eq__(self, other):
        return self.__score == other.score

    def __ne__(self, other):
        return self.__score != other.score

    def __gt__(self, other):
        return self.__score > other.score

    def __ge__(self, other):
        return self.__score >= other.score
# TODO 这个地方编码的问题，打印出来的是 	< score=617, path=[u'\u6f06', u'\u9ed1'] > 这种，中文有问题
    def __str__(self):
        return '< score={0}, path={1} >'.format(self.__score,self.__path)# [ item.decode('utf-8') for item in self.__path])

    def __repr__(self):
        return self.__str__()


class PrioritySet(object):

    def __init__(self, capacity):
        self.capacity = capacity # 在构造的时候设置一个最大值，若后续put数据进来的时候，总数超过最大容量，则只保留最大的一组值。
        self.data = []

    def put(self, score, path):
        assert(isinstance(path, list) == True)
        heapq.heappush(self.data, [score, Item(score, path)])
        while len(self.data) > self.capacity: # 可能是获取序列里分数最大的一组值， 多了就给去掉。
            heapq.heappop(self.data) # 弹出最小值

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        for item in self.data:
            yield item[1]

    def __str__(self):
        s = '[ \n'
        for item in self.data:
            s = s + '\t' + str(item[1]) + '\n'
        s += ']'
        return s

    def __getitem__(self, key):
        return self.data[key][1]


    def __repr__(self):
        return self.__str__()
