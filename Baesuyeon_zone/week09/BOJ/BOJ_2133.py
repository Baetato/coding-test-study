# - N을 입력받아서 3xN 크기의 2차원 배열을 만들고
# - 그 안에 2x1 혹은 1x2 사이즈의 네모가 얼만큼 들어가는지 출력하기
#     - 네모를 코드 상에서 어떻게 다루면 좋지…?
#     - 이런 식으로 구현하면 굉장히 비효율적, 직접 배열을 만들고 타일을 넣어보는 방식은 매우 복잡하고 N=30까지 가면 시간초과 발생
    
#       ⇒ **따라서, 점화식을 도출해서 DP 방식으로 해결하는 것이 맞다.**
    
# - **3xN 벽을 2x1 or 1x2 사이즈 네모로 채우는 과정을 어떻게 점화식으로 구현할 것인가 ⭐️**
#     - 모르겟음..

import sys
input = sys.stdin.readline

N = int(input())
