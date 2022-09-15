from flask import Flask
from table import TestItem, TestTable
import random, datetime

app = Flask(__name__)


@app.route('/')
def index():
    def bubble_sort_from_down_to_up(elements):
        for n in range(len(elements) - 1, 0, -1):
            for i in range(n):
                if elements[i] > elements[i + 1]:
                    elements[i], elements[i + 1] = elements[i + 1], elements[i]

    def bubble_sort_from_up_to_down(elements):

        for n in range(len(elements) - 1, 0, -1):
            for i in range(n):
                if elements[i] < elements[i + 1]:
                    elements[i], elements[i + 1] = elements[i + 1], elements[i]

    array_small = [random.randint(0, 10) for _ in range(10)]

    array_big = [random.randint(0, 10) for _ in range(100)]

    t1 = datetime.datetime.now()
    array_sort_from_down_to_up_small = array_small.copy()
    bubble_sort_from_down_to_up(array_sort_from_down_to_up_small)
    t2 = datetime.datetime.now() - t1

    t3 = datetime.datetime.now()
    array_sort_from_up_to_down_small = array_small.copy()
    bubble_sort_from_up_to_down(array_sort_from_up_to_down_small)
    t4 = datetime.datetime.now() - t3

    t5 = datetime.datetime.now()
    array_sort_from_down_to_up_big = array_big.copy()
    bubble_sort_from_down_to_up(array_big.copy())
    t6 = datetime.datetime.now() - t5

    t7 = datetime.datetime.now()
    array_sort_from_up_to_down_big = array_big.copy()
    bubble_sort_from_up_to_down(array_sort_from_up_to_down_big)
    t8 = datetime.datetime.now() - t7

    items = [TestItem(array_small, 0),
             TestItem(array_sort_from_up_to_down_small, t2),
             TestItem(array_sort_from_down_to_up_small, t4),
             TestItem(array_sort_from_up_to_down_big, t6),
             TestItem(array_sort_from_down_to_up_big, t8)]

    table = TestTable(items)

    print(table.__html__())

    return table.__html__()


if __name__ == '__main__':
    app.run(debug=True)
