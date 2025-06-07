from pathlib import Path
import timeit


# ----------------------------------------------
# Алгоритм Кнута-Морріса_Пратта

def compute_lps(pattern):
  lps = [0] * len(pattern)
  length = 0
  i = 1

  while i < len(pattern):
    if pattern[i] == pattern[length]:
      length += 1
      lps[i] = length
      i += 1
    else: 
      if length != 0:
        length = lps[length - 1]
      else:
        lps[i] = 0
        i += 1
  
  return lps

def kmp_search(main_string, pattern):
  M = len(pattern)
  N = len(main_string)

  lps = compute_lps(pattern)

  i = j = 0

  while i < N:
    if pattern[j] == main_string[i]:
      i += 1
      j += 1
      if j == M:
        return i - j
    else:
      if j != 0:
        j = lps[j - 1]

      else:
        i += 1
    
  return -1




#------------------------------------------------------
# Алгоритм Боєра-Мура

def build_shift_table(pattern):
  """Створити таблицю зсувів для алгоритму Боєра-Мура."""
  table = {}
  length = len(pattern)
  # Для кожного символу в підрядку встановлюємо зсув рівний довжині підрядка
  for index, char in enumerate(pattern[:-1]):
    table[char] = length - index - 1
  # Якщо символу немає в таблиці, зсув буде дорівнювати довжині підрядка
  table.setdefault(pattern[-1], length)
  return table

def boyer_moore_search(text, pattern):
  # Створюємо таблицю зсувів для патерну (підрядка)
  shift_table = build_shift_table(pattern)
  i = 0 # Ініціалізуємо початковий індекс для основного тексту

  # Проходимо по основному тексту, порівнюючи з підрядком
  while i <= len(text) - len(pattern):
    j = len(pattern) - 1 # Починаємо з кінця підрядка

    # Порівнюємо символи від кінця підрядка до його початку
    while j >= 0 and text[i + j] == pattern[j]:
      j -= 1 # Зсуваємось до початку підрядка

    # Якщо весь підрядок збігається, повертаємо його позицію в тексті
    if j < 0:
      return i # Підрядок знайдено

    # Зсуваємо індекс i на основі таблиці зсувів
    # Це дозволяє "перестрибувати" над неспівпадаючими частинами тексту
    i += shift_table.get(text[i + len(pattern) - 1], len(pattern))

  # Якщо підрядок не знайдено, повертаємо -1
  return -1
  



#--------------------------------------------------------------
# Алгоритм Рабіна-Карпа

def polynomial_hash(s, base=256, modulus=101):
  """
  Повертає поліноміальний хеш рядка s.
  """
  n = len(s)
  hash_value = 0
  for i, char in enumerate(s):
    power_of_base = pow(base, n - i - 1) % modulus
    hash_value = (hash_value + ord(char) * power_of_base) % modulus
  return hash_value

def rabin_karp_search(main_string, substring):
  # Довжини основного рядка та підрядка пошуку
  substring_length = len(substring)
  main_string_length = len(main_string)

  # Базове число для хешування та модуль
  base = 256
  modulus = 101
  
  # Хеш-значення для підрядка пошуку та поточного відрізка в основному рядку
  substring_hash = polynomial_hash(substring, base, modulus)
  current_slice_hash = polynomial_hash(main_string[:substring_length], base, modulus)

  # Попереднє значення для перерахунку хешу
  h_multiplier = pow(base, substring_length - 1) % modulus

  # Проходимо крізь основний рядок
  for i in range(main_string_length - substring_length + 1):
    if substring_hash == current_slice_hash:
      if main_string[i:i+substring_length] == substring:
        return i
  
    if i < main_string_length - substring_length:
      current_slice_hash = (current_slice_hash - ord(main_string[i]) * h_multiplier) % modulus
      current_slice_hash = (current_slice_hash * base + ord(main_string[i + substring_length])) % modulus
      if current_slice_hash < 0:
        current_slice_hash += modulus
  return -1



def read_file(filename):
    try:
        with open(filename, encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"Помилка читання файлу {filename}: {e}")
        return ""
  


def benchmark_algorithms(text, pattern, label):
    print(f"\n=== {label} ===")
    print(f"Підрядок: '{pattern}'\n")

    for name, func in {
        "KMP": kmp_search,
        "Boyer-Moore": boyer_moore_search,
        "Rabin-Karp": rabin_karp_search,
    }.items():
        position = func(text, pattern)
        time_taken = timeit.timeit(lambda: position, number=1)

        found_msg = f"Знайдено на позиції {position}" if position != -1 else "Підрядок не знайдено"
        print(f"[{name:<12}] {found_msg:<30} Час: {time_taken:.6f} сек")

def main():
  base_path = Path(__file__).parent
  text1 = read_file(base_path / "text1.txt")
  text2 = read_file(base_path / "text2.txt")

  print(f"Текст 1 має {len(text1)} символів.")
  print(f"Текст 2 має {len(text2)} символів.")

  real_substring = "алгоритм пошуку"
  real_substring_2 = "економна форма"
  fake_substring = "абракатабра"

  benchmark_algorithms(text1, real_substring, "Текст 1 - реальний фрагмент")
  benchmark_algorithms(text1, fake_substring, "Текст 1 - вигаданий фрагмент")
  
  benchmark_algorithms(text2, real_substring_2, "Текст 2 - реальний фрагмент")
  benchmark_algorithms(text2, fake_substring, "Текст 2 - вигаданий фрагмент")

if __name__ == "__main__":
  main()

