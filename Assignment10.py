import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

# 1. Line Plot
plt.figure()
plt.plot(x, y, marker='o')
plt.title("Line Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()

# 2. Scatter Plot
plt.figure()
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()

# 3. Box Plot
marks = [45, 50, 55, 60, 65, 70, 75, 80]
plt.figure()
plt.boxplot(marks)
plt.title("Box Plot")
plt.ylabel("Marks")
plt.show()

# 4. Bar Chart
subjects = ["Python", "DBMS", "DSA", "Maths"]
scores = [85, 75, 90, 80]

plt.figure()
plt.bar(subjects, scores)
plt.title("Bar Chart")
plt.xlabel("Subjects")
plt.ylabel("Scores")
plt.show()

# 5. Pie Chart
labels = ["Python", "DBMS", "DSA", "Maths"]
plt.figure()
plt.pie(scores, labels=labels, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()
