weight = int(input('体重 (kg): '))
height = int(input('身高 (cm): '))
age = int(input('年龄: '))
intensity = input('强度: ')
sex = input('性别: ')

BMI = (weight / (height * height)) * 10000
print(f"BMI = {round(BMI)}")

if sex == '女' and intensity == '久坐':
    calories = (10 * weight + 6.25 * height - 5 * age - 161) * 1.1
elif sex == '女' and intensity == '低':
    calories = (10 * weight + 6.25 * height - 5 * age - 161) * 1.3
elif sex == '女' and intensity == '中':
    calories = (10 * weight + 6.25 * height - 5 * age - 161) * 1.5
elif sex == '女' and intensity == '高':
    calories = (10 * weight + 6.25 * height - 5 * age - 161) * 1.7
elif sex == '女' and intensity == '无':
    calories = 10 * weight + 6.25 * height - 5 * age - 161
elif sex == '男' and intensity == '无':
    calories = 10 * weight + 6.25 * height - 5 * age + 5
elif sex == '男' and intensity == '久坐':
    calories = (10 * weight + 6.25 * height - 5 * age + 5) * 1.1
elif sex == '男' and intensity == '低':
    calories = (10 * weight + 6.25 * height - 5 * age + 5) * 1.3
elif sex == '男' and intensity == '中':
    calories = (10 * weight + 6.25 * height - 5 * age + 5) * 1.5
elif sex == '男' and intensity == '高':
    calories = (10 * weight + 6.25 * height - 5 * age + 5) * 1.7

print(f"卡路里消耗 = {calories}")

gain = calories + (200 if sex == '女' else 400)
loss = calories - 800

proteingain = (gain * (0.2 if sex == '女' else 0.15)) // 4
fatgain = (gain * (0.4 if sex == '女' else 0.35)) // 9
carbsgain = (gain * (0.4 if sex == '女' else 0.5)) // 4

proteinloss = (loss * 0.2) // 4
fatloss = (loss * 0.35) // 9
carbsloss = (loss * 0.45) // 4

print(f"你应该吃 {gain} 卡路里来增重，你需要{proteingain}g蛋白质，{fatgain}g脂肪和{carbsgain}g碳水化合物")
print(f"你应该吃 {loss} 卡路里来减重，你需要{proteinloss}g蛋白质，{fatloss}g脂肪和{carbsloss}g碳水化合物")

