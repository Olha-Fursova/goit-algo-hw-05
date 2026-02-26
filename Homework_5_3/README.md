# Substring search algorithms

Comparison of substring search algorithms

Three algorithms were implemented and tested:
- **Knuth-Morris-Pratt (KMP)**
- **Boyer-Moore**
- **Rabin-Karp**

### Testing was performed on two texts:
- `text1.txt` (copied text from the article provided in the homework) — 12,655 characters
- `text2.txt` (similar) — 17,590 characters

Substrings:
- Real fragments: `"search algorithm"`, `"economy form"`
- Fictional fragment: `"abracatabra"`

### Results
I ran this code several times and from time to time I got different results, but they were not much different from the previous ones. Basically, the difference was 0.000001 seconds. But even with this difference, I could see the differences.
- In most cases, **Boyer-Moore** showed the best speed on real text. After numerous attempts, the algorithm searched for 0.000000, compared to others that could have results of 0.000001. This algorithm gave a similar result only once, namely when searching for the original text.
- **KMP** was consistently fast and accurate on a par with the Boyer-Moore algorithm. But I must note that the aglorithm had problems with fast search in article #1. Almost every time the calculation stopped at 0.000001, when others did not have a similar problem.
- **Rabin-Karp** was the least stable — almost every time it gave a longer result of 0.000001 when checking a non-existent fragment in the text, and also several times when checking the original fragment.

## Conclusion

Comparison of three types of search algorithms took me a long time. But despite the complexity of constructing each of them and formulating calculations with the output of results, I really enjoyed analyzing the text and trying other substrings for searching. All three types work quickly and accurately, none of them made a mistake in the index position. But based on the results, I personally conclude that for large texts (namely in this example) it is best to use the Boyer-Moore algorithm.



# Алгоритми пошуку підрядка

Порівняння алгоритмів пошуку підрядка

Реалізовано та протестовано три алгоритми:
- **Кнута-Морріса-Пратта (KMP)**
- **Боєра-Мура**
- **Рабіна-Карпа**

### Тестування проводилось на двох текстах:
- `text1.txt` (скопійований текст з наданої статті у домашньому завданні) — 12 655 символів
- `text2.txt` (аналогічно) — 17 590 символів

Підрядки:
- Реальні фрагменти: `"алгоритм пошуку"`, `"економна форма"`
- Вигаданий фрагмент: `"абракатабра"`

### Результати
Я декілька разів запускала даний код і час від часу отримувала різні результати, але вони не сильно відрізнялися від попередніх. В основному, різниця була в 0.000001 секунди. Але навіть за даною різницею, я могла побачити відмінності.
- У більшості випадків **алгоритм Боєра-Мура** показав найкращу швидкість на реальному тексті. Після численних спроб, алгоритм виконував пошук за 0.000000, в порівнянні з іншими, які могли мати результати 0.000001. Даний алгоритм видав подібний результат лише один раз, а саме при пошуку оригінального тексту.
- **KMP** був стабільно швидким і точним на рівні з алгоритмом Боєра-Мура. Але мушу зауважити, що аглоритм мав проблеми зі швидким пошуком у статті №1. Майже щоразу обрахунок зупинявся на 0.000001, коли інші не мали подібної проблеми. 
- **Рабін-Карп** був найменш стабільним — майже щоразу видавав довший результат у 0.000001 при перевірці неіснуючого фрагменту в тексті, а також декілька разів при перевірці оригінального фрагменту.

## Висновок


Порівняння трьох різновидів алгоритмів пошуку зайняв особлисто у мене довгий час. Але не зважаючи на складність побудови кожного з них та формулювання обрахунків з виводом результатів, мені дуже сподобалося аналізувати текст та пробувати інші підрядки для пошуку. Усі три різновиди прцюють швидко та точно, жоден з них не помилився у позиції індексу. Але за результатами особисто для себе роблю висновок, що для великих текстів (а саме у даному прикладі) найкраще використовувати алгоритм Боєра-Мура.
