field_1 = list(map(int, input().split())) # 첫번째 간판
field_2 = list(map(int, input().split())) # 두번째 간판
truck = list(map(int, input().split())) # 트럭

# 넓이 구하는 함수
def width(x1, y1, x2, y2):
    return (x2-x1) * (y2-y1)

# 가리는 부분에 대해서
def block_field(x1, y1, x2, y2, x3, y3, x4, y4):
    bx1 = max(x1, x3)
    by1 = max(y1, y3)
    bx2 = min(x2, x4)
    by2 = min(y2, y4)

    # 트럭이 간판을 가리는 경우라면
    # 가리는 부분들에 대해서 좌표를 구한 후, 그 부분에 대해 넓이를 구한다
    if bx1 < bx2 and by1 < by2:
        return width(bx1, by1, bx2, by2)
    # 가리지 않는 경우, 가리는 영역에 대한 값은 0이다
    else:
        return 0

width_1 = width(*field_1)
width_2 = width(*field_2)
block_1 = block_field(*field_1, *truck)
block_2 = block_field(*field_2, *truck)

ans = (width_1 - block_1) + (width_2 - block_2)
print(ans)