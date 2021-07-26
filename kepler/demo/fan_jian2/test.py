from openccpy.opencc import *


class TestOpencc(object):
    """
    核心转换测试类
    """

    def test_to_simple(self, param):
        """
        测试转换为简体
        """
        # assert "丝" == Opencc.to_simple("絲")
        # assert "一目了然" == Opencc.to_simple("一目瞭然")
        if len(param) == 1:
            return Opencc.to_simple(param)
        if len(param) > 1:
            data = ''
            for i in param:
                k = Opencc.to_simple(i)
                data += data.join(k)
            return data

    def test_to_traditional(self, param):
        """
        测试转化为繁体
        """
        # assert "絲" == Opencc.to_traditional("丝")
        # assert "一目瞭然" == Opencc.to_traditional("一目了然")
        # return Opencc.to_traditional(param)

        if len(param) == 1:
            return Opencc.to_traditional(param)
        if len(param) > 1:
            data = ''
            for i in param:
                k = Opencc.to_traditional(i)
                data += data.join(k)
            return data


if __name__ == '__main__':
    test = TestOpencc()
    simple = "黑云科技张乐琪"
    traditional = "黑雲科技張樂琪"
    change_simple = test.test_to_simple(traditional)
    change_traditional = test.test_to_traditional(simple)
    print(change_simple)
    print(change_traditional)