from matplotlib import pyplot as plt
import sys
import math

nums = []
for line in sys.stdin:
    line = line.split()
    nums.append(int(line[1]))

x = [x for x in range(1,1001)]

plt.xscale('log')
plt.yscale('log')

plt.plot(x,nums)
# plt.show()
plt.savefig("h01_김현민_20171609_plot.png",dpi=300)

s = -1 *((math.log(nums[0]) - math.log(nums[-1])) / (math.log(x[0]) - math.log(x[-1])))
c = 2 ** (math.log(nums[-1]) + s * math.log(x[-1]))
print(f"s = {s} , c = {c}")

'''지프의 법칙의 양변에 log를 취하면 log n = log c - s log k 가된다.
   즉, log n 과 log k 로 그린 그래프의 기울기에 -1 을 곱한 값이 s이고 y절편이 log c 이므로
   s = -기울기 c = 10 ** (y절편) 이다.'''