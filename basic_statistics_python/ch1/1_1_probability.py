# 문제
# 공정한 동전을 던졌을 때, 앞(Head) 또는 뒤(Tail)가 나올 확률을 구하는 함수를 작성해보세요.

# 베이스라인의 code here 을 채우세요.


def pmf_coin(outcome):
    """
    본 함수는 동전을 던졌을 때 나오는 결과(Head 혹은 Tail)를 입력값으로 받는다.
    입력값 outcome이 Head와 Tail 둘 중 하나일 때는 0.5, 그 외에는 0이 확률이 된다.
    확률 변수의 형식으로, 주어진 outcome에 대한 확률을 출력한다.
    """
    if outcome in ["Head", "Tail"]:
        """
        code here
        """
        p = 0.5
    else:
        """
        code here
        """
        p = 0
    print(f"P(X = x) = {p:.2f}")


# Input
pmf_coin("Head")

pmf_coin("Tail")

pmf_coin("etc")
