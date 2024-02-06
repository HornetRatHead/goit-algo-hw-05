# Tsygankov_HW5_3
import timeit
import os

def get_file_path():
    while True:
        file_path = input("Введіть шлях до файлу: ")
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as file:
                file_text = file.read()
            return file_text
        else:
            print("Файл не знайдено. Спробуйте ще раз.")

def search_naive(text, pattern):
    occurrences = []
    n = len(text)
    m = len(pattern)
    for i in range(n - m + 1):
        if text[i:i + m] == pattern:
            occurrences.append(i)
    return occurrences

def search_boyer_moore(text, pattern):
    occurrences = []
    return occurrences

def search_kmp(text, pattern):
    occurrences = []
    return occurrences

def search_rabin_karp(text, pattern):
    occurrences = []
    return occurrences

def compare_search_algorithms(article_text, pattern_exists, pattern_nonexistent):
    algorithms = ["search_naive", "search_boyer_moore", "search_kmp", "search_rabin_karp"]
    results_exists = {}
    results_nonexistent = {}

    print("Перевірка наявності текста, який точно міститься у файлі:")
    for algorithm in algorithms:
        time_taken = timeit.timeit(
            f"{algorithm}(article_text, pattern_exists)", 
            setup=f"from __main__ import {algorithm}, article_text, pattern_exists", 
            number=10
        )
        results_exists[algorithm] = time_taken
        print(f"{algorithm}: {time_taken} сек")

    print("\nПеревірка наявності текста, якого точно немає у файлі:")
    for algorithm in algorithms:
        time_taken = timeit.timeit(
            f"{algorithm}(article_text, pattern_nonexistent)", 
            setup=f"from __main__ import {algorithm}, article_text, pattern_nonexistent", 
            number=10
        )
        results_nonexistent[algorithm] = time_taken
        print(f"{algorithm}: {time_taken} сек")

    print("\nПорівняння швидкості виконання алгоритмів:")
    for algorithm in algorithms:
        exists_time = results_exists[algorithm]
        nonexistent_time = results_nonexistent[algorithm]
        print(f"{algorithm}: Наявний текст - {exists_time} сек, Відсутній текст - {nonexistent_time} сек")

if __name__ == "__main__":
    article_text = get_file_path()
    pattern_exists = input("Введіть текст, який точно міститься у файлі: ")
    pattern_nonexistent = input("Введіть текст, якого точно немає у файлі: ")

    compare_search_algorithms(article_text, pattern_exists, pattern_nonexistent)
