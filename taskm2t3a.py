import matplotlib.pyplot as plt

languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

plt.figure(figsize=(10, 6))
plt.bar(languages, popularity, color=['yellow', 'purple', 'red', 'blue', 'orange', 'grey'])
plt.title('Popularity of Programming Languages', fontsize=16)
plt.xlabel('Programming Languages', fontsize=14)
plt.ylabel('Popularity (%)', fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
