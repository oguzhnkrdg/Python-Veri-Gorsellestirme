import matplotlib.pyplot as plt
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.style.use('ggplot') #Matplotlib kütüphanesi içinde hazır bulunan stillerden biridir.
#Bilgisayarınızda mevcut olan stilleri görmek için Python terminal oturumunda şu kodları çalıştırın:
#import matplotlib.pyplot as plt
#plt.style.available
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=5)

ax.set_title("Sayıların Karesi", fontsize=28)
ax.set_xlabel("Değer", fontsize=12)
ax.set_ylabel("Değerin Karesi", fontsize=12)

ax.tick_params(axis='both', labelsize=14)

plt.show()