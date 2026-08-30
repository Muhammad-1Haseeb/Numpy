# adding 2 in temperature
import numpy as np

# temperature = np.array([20, 25, 30, 35, 40])

# new_temperature = temperature + 2
# print(new_temperature)

# Add 5 to every student's marks.

# marks = np.array([65, 72, 81, 90, 55])
# bonus_marks = marks + 5
# print(bonus_marks)

# Students getting different bonus marks
# marks = np.array([65, 72, 81, 90, 55])
# bonuses = np.array([5, 2, 10, 0, 7])
# new_marks = marks + bonuses
# print(new_marks)

# marks = np.array([65, 72, 81, 90, 55])
# bonuses = np.array([5, 2])
# new_marks = marks + bonuses
# print(new_marks)


# marks = np.array([65, 72, 81, 90, 55])

# bonus = np.array([5])
# result = marks + bonus
# print(result)

# marks = np.array([65, 72, 81, 90, 55])

# bonus = np.array([5, 10])
# result = marks + bonus
# print(result)

# bonus = np.array([5, 10])

# print(bonus)
# print(bonus.shape)

# bonus = bonus.reshape(2, 1)

# print(bonus)
# print(bonus.shape)

# marks = np.array([65, 72, 81, 90, 55])
# bonus = np.array([5, 10]).reshape(2, 1)

# result = marks + bonus

# print(result)
# print(result.shape)

# marks = np.array([65, 72, 81, 90, 55])
# bonus = np.array([5, 10]).reshape(2, 1)

# result = marks + bonus

# print(bonus)
# print(bonus.shape)

# print(result)
# print(result.shape)

# marks = np.array([
#     [70, 80, 90],
#     [60, 75, 85],
#     [88, 92, 79]
# ])

# bonus = np.array([5,2,10])

# final_marks = marks + bonus
# print(f"Final Marks: {final_marks}")
# print(f"Final marks Shape: {final_marks.shape}")


# sales = np.array([
#     [100, 120, 110],
#     [80,  95,  105],
#     [150, 140, 160],
#     [90,  100, 115]
# ])

# bonus_rate = np.array([0.10, 0.05, 0.20])
# bonus_amount = sales * bonus_rate

# print(bonus_amount)
# print(bonus_amount.shape)

# marks = np.array([
#     [70, 80, 90],
#     [60, 75, 85],
#     [88, 92, 79],
#     [95, 87, 91]
# ])

# student_averages = np.mean(marks, axis=0)
# print(student_averages)
# print(student_averages.shape)


marks = np.array([
    [70, 80, 90],
    [60, 75, 85],
    [88, 92, 79],
    [95, 87, 91]
])
student_averages = np.mean(marks, axis=1)

excellent = student_averages >= 80
excellent_students = student_averages[excellent]
print(excellent_students)