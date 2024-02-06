# Tsygankov_HW5_2

import timeit

# Ось ваші реалізації алгоритмів Боєра-Мура, Кнута-Морріса-Пратта та Рабіна-Карпа
def boyer_moore(text, pattern):
    m, n = len(pattern), len(text)
    last_occurrence = {pattern[i]: i for i in range(m)}
    i = m - 1  # index in text
    j = m - 1  # index in pattern
    while i < n:
        if text[i] == pattern[j]:
            if j == 0:
                return i  # match found
            else:
                i -= 1
                j -= 1
        else:
            bad_char_skip = j - last_occurrence.get(text[i], -1)
            i += max(1, bad_char_skip)
            j = m - 1

    return -1

def knuth_morris_pratt(text, pattern):
    m, n = len(pattern), len(text)
    lps = compute_lps(pattern)
    i, j = 0, 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
            if j == m:
                return i - j  # match found
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1

def rabin_karp(text, pattern):
    d = 256  # number of characters in the alphabet
    q = 101  # prime number
    m, n = len(pattern), len(text)
    h_pattern, h_text = 0, 0
    h = pow(d, m - 1, q)  # d^(m-1) % q
    for i in range(m):
        h_pattern = (d * h_pattern + ord(pattern[i])) % q
        h_text = (d * h_text + ord(text[i])) % q
    for i in range(n - m + 1):
        if h_pattern == h_text and text[i:i + m] == pattern:
            return i  # match found
        if i < n - m:
            h_text = (d * (h_text - ord(text[i]) * h) + ord(text[i + m])) % q
    return -1

if __name__ == '__main__':
    # Задаємо дані для тестування
    file_1_path = input("Введіть шлях до файлу, який потрібно перевірити: ")
    pattern_1_exists = input("Введіть текст, який має присутній бути в файлі: ")
    pattern_1_nonexistent = input("Введіть текст, якого має бути відсутнім в файлі: ")


    file_2_path = input("Введіть шлях до файлу, який потрібно перевірити: ")
    pattern_2_exists = input("Введіть текст, який має присутній бути в файлі: ")
    pattern_2_nonexistent = input("Введіть текст, якого має бути відсутнім в файлі: ")

    # Вимірюємо час виконання для алгоритмів
    time_boyer_moore_1_exists = timeit.timeit(lambda: boyer_moore(text_1, pattern_1_exists), number=1000)
    time_knuth_morris_pratt_1_exists = timeit.timeit(lambda: knuth_morris_pratt(text_1, pattern_1_exists), number=1000)
    time_rabin_karp_1_exists = timeit.timeit(lambda: rabin_karp(text_1, pattern_1_exists), number=1000)

    time_boyer_moore_2_exists = timeit.timeit(lambda: boyer_moore(text_2, pattern_2_exists), number=1000)
    time_knuth_morris_pratt_2_exists = timeit.timeit(lambda: knuth_morris_pratt(text_2, pattern_2_exists), number=1000)
    time_rabin_karp_2_exists = timeit.timeit(lambda: rabin_karp(text_2, pattern_2_exists), number=1000)

    # Виводимо результати
    print("Час виконання для алгоритму Боєра-Мура (підрядок, який існує у тексті):", time_boyer_moore_1_exists)
    print("Час виконання для алгоритму Кнута-Морріса-Пратта (підрядок, який існує у тексті):", time_knuth_morris_pratt_1_exists)
    print("Час виконання для алгоритму Рабіна-Карпа (підрядок, який існує у тексті):", time_rabin_karp_1_exists)

    # Повторюємо для інших випадків