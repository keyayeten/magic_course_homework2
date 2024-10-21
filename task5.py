# В большой текстовой строке подсчитать
# количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.

text = input().lower().replace('.,:;!@#$%^&*(){["]}\|/><', '').split()

text_spk = {}
for i in text:
    if i not in text_spk:
        text_spk[i] = 1
    else:
        text_spk[i] += 1

sort_text_spk = sorted(text_spk.items())

for i in range(len(sort_text_spk)):
    for j in range(len(sort_text_spk) - 1):
        if sort_text_spk[j][1] < sort_text_spk[j + 1][1]:
            sort_text_spk[j], sort_text_spk[j + 1] = sort_text_spk[j + 1], sort_text_spk[j]

for i in range(10):
    print(f'Слово {sort_text_spk[i][0]} встречается {sort_text_spk[i][1]} раз')