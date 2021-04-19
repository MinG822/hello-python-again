'''
가변 객체의 값 공유 관련
https://docs.python.org/ko/3/faq/programming.html#id14
'''

def dont_get_mutable_arg(alpha, m_dict={}):
    m_dict[alpha] = alpha.upper()
    print(m_dict)
    return m_dict


def do_none_than_mutable(alpha, m_dict=None):
    if m_dict is None:
        m_dict = {}
        m_dict[alpha] = alpha.upper()
        print(m_dict)
        return m_dict
    raise ValueError()


def cache_expensive(arg1, arg2, _cache={}):
    if (arg1, arg2) in _cache:
        print('cached!')
        return _cache[(arg1, arg2)]

    result = ( arg1 ** arg2 ) - (arg1 ** 2) - (arg2 ** 2)
    _cache[(arg1, arg2)] = result
    return _cache


if __name__ == "__main__":
    a_dict = dont_get_mutable_arg('a')
    b_dict = dont_get_mutable_arg('b')
    print(a_dict == b_dict)

    new_a_dict = do_none_than_mutable('a')
    new_b_dict = do_none_than_mutable('b')
    print(new_a_dict == new_b_dict)

    result1 = cache_expensive(3, 4)
    result2 = cache_expensive(3, 4)



