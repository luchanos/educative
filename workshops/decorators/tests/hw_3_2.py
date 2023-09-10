from random import randint

import pytest

from workshops.decorators.homeworks.block_3.hw_3_2 import retry, retry_parametrized


@pytest.mark.parametrize("success_func_execution_on_attempt", [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10
])
def test_retry_deco(success_func_execution_on_attempt):
    executed_cnt = 0
    decorated_func_result = randint(0, 10)

    @retry
    def func_to_be_decorated():
        nonlocal executed_cnt
        if executed_cnt != success_func_execution_on_attempt:
            executed_cnt += 1
            raise Exception
        return decorated_func_result

    assert func_to_be_decorated() == decorated_func_result


@pytest.mark.parametrize("success_func_execution_on_attempt", [
    11, 12, 135, 43, 12, 10000, 45
])
def test_retry_deco_out_of_attempts(success_func_execution_on_attempt):
    executed_cnt = 0
    decorated_func_result = randint(0, 10)

    @retry
    def func_to_be_decorated():
        nonlocal executed_cnt
        if executed_cnt != success_func_execution_on_attempt:
            executed_cnt += 1
            raise Exception
        return decorated_func_result

    with pytest.raises(Exception):
        func_to_be_decorated()


@pytest.mark.parametrize("success_func_execution_on_attempt, retry_parameter", [
    (1, 12),
    (2, 3),
    (3, 4),
    (4, 10),
])
def test_retry_deco(success_func_execution_on_attempt, retry_parameter):
    executed_cnt = 0
    decorated_func_result = randint(0, 10)

    @retry_parametrized(retry_parameter)
    def func_to_be_decorated():
        nonlocal executed_cnt
        if executed_cnt != success_func_execution_on_attempt:
            executed_cnt += 1
            raise Exception
        return decorated_func_result

    assert func_to_be_decorated() == decorated_func_result


@pytest.mark.parametrize("success_func_execution_on_attempt, retry_parameter", [
    (12, 1),
    (3, 2),
    (4, 3),
    (10, 4),
])
def test_retry_deco(success_func_execution_on_attempt, retry_parameter):
    executed_cnt = 0
    decorated_func_result = randint(0, 10)

    @retry_parametrized(retry_parameter)
    def func_to_be_decorated():
        nonlocal executed_cnt
        if executed_cnt != success_func_execution_on_attempt:
            executed_cnt += 1
            raise Exception
        executed_cnt += 1
        return decorated_func_result

    with pytest.raises(Exception):
        func_to_be_decorated()
