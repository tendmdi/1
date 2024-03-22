#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Запятая не должна выводиться.  Переопределять my_favorite_movies нельзя
# Использовать .split() или .find()или другие методы строки нельзя - пользуйтесь только срезами,
# как указано в задании!
first_movie = my_favorite_movies[:my_favorite_movies.index(',')]
last_movie = my_favorite_movies[my_favorite_movies.rindex(',') + 2:]
second_movie = my_favorite_movies[my_favorite_movies.index(',') + 2:my_favorite_movies.index(',', my_favorite_movies.index(',') + 1)]
second_last_movie = my_favorite_movies[my_favorite_movies.rindex(',', 0, my_favorite_movies.rindex(',')) + 2:my_favorite_movies.rindex(',')]

# Вывод на консоль
print(first_movie)
print(last_movie)
print(second_movie)
print(second_last_movie)
