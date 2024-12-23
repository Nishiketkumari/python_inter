import matplotlib.pyplot as plt

languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

plt.figure(figsize=(6, 6))
plt.pie(popularity, labels=languages, autopct='%5.1f%%', startangle=140)
plt.title('popularity of programming languages')
plt.show()
