import tkinter as tk
from tkinter import messagebox

def calculate_health_plan():
    weight = int(weight_entry.get())
    height = int(height_entry.get())
    age = int(age_entry.get())
    intensity = intensity_var.get()
    sex = sex_var.get()

    BMI = (weight / (height * height)) * 10000

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


    gain = calories + (200 if sex == '女' else 400)
    loss = calories - 800

    proteingain = (gain * (0.2 if sex == '女' else 0.15)) // 4
    fatgain = (gain * (0.4 if sex == '女' else 0.35)) // 9
    carbsgain = (gain * (0.4 if sex == '女' else 0.5)) // 4

    proteinloss = (loss * 0.2) // 4
    fatloss = (loss * 0.35) // 9
    carbsloss = (loss * 0.45) // 4
    messagebox.showinfo("Health Plan", f"你的BMI为{round(BMI)}，\n正常卡路里摄入量为{calories}\n\n如果为了增肌，\n你应该摄入 {gain} 卡路里，\n这包含{proteingain}g蛋白质，{fatgain}g脂肪和{carbsgain}g碳水化合物\n\n如果为了减重，\n你应该摄入 {loss} 卡路里，\n这包含{proteinloss}g蛋白质，{fatloss}g脂肪和{carbsloss}g碳水化合物")

root = tk.Tk()
root.title("Auto-HealthPlan")

# Create input fields and labels
weight_label = tk.Label(root, text="体重 (kg):")
weight_label.grid(row=0, column=0)
weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1)

height_label = tk.Label(root, text="身高 (cm):")
height_label.grid(row=1, column=0)
height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1)

age_label = tk.Label(root, text="年龄（阿拉伯数字）:")
age_label.grid(row=2, column=0)
age_entry = tk.Entry(root)
age_entry.grid(row=2, column=1)

intensity_label = tk.Label(root, text="运动强度:")
intensity_label.grid(row=3, column=0)
intensity_var = tk.StringVar(root)
intensity_var.set("无")
intensity_options = ["无", "久坐", "低", "中", "高"]
intensity_menu = tk.OptionMenu(root, intensity_var, *intensity_options)
intensity_menu.grid(row=3, column=1)

sex_label = tk.Label(root, text="性别:")
sex_label.grid(row=4, column=0)
sex_var = tk.StringVar(root)
sex_var.set("男")
sex_options = ["男", "女"]
sex_menu = tk.OptionMenu(root, sex_var, *sex_options)
sex_menu.grid(row=4, column=1)

# Add a button to calculate the health plan
calculate_button = tk.Button(root, text="计算健康计划", command=calculate_health_plan)
calculate_button.grid(row=5, column=0, columnspan=2)

root.mainloop()
