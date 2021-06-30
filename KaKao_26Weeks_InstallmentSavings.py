import datetime
m = datetime.datetime(2020, 12 ,12)
mWeek = m.isocalendar()[1]    # 적금 시작한 날의 주차

mlast = datetime.datetime(2020, 12, 31)   
mlastWeek = mlast.isocalendar()[1]       # 2020년 마지막 주차

n = datetime.datetime.now() #현재 날짜
nWeek = n.isocalendar()[1] #현재 주차

mDiff = mlastWeek - mWeek  # 2020년 마지막 주차 - 적금을 시작한 날의 주차

sum26 = 0
all26 = 0
sum = 0
all = 0

print("<카카오뱅크 26주 적금 with 마켓컬리>")
money = int(input("얼마씩 누적되나요? : "))
print(f"{money}원")
week = int(input("현재 몇 주차인가요? : "))
print(f"{week}주 적금")

for r in range(1, 26+1):
    sum26 = r * money # sum: 주차 별 적립되는 적금 액수
    all26 += sum26    # all: 26주차까지 모인 적금 액수

for r in range(1, week+1):
    sum = r * money # sum: 주차 별 적립되는 적금 액수
    all += sum      # all: 현재 주차까지 모인 적금 액수

print(f"26주차에 모이는 총 적금 액수는 {all26}원 입니다.")

allWeek = mDiff + nWeek  # 현재 몇 주차
print(f"현재 {week}주차까지 모은 적금액은 {all}원입니다.") # week주차까지 모인 money만큼 누적된 적금

input("\nPress enter to exit ;)")
