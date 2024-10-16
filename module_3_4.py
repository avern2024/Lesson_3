def single_root_words(root_word, *other_words):
    # Создаем пустой список для хранения подходящих слов
    same_words = []
    # Приводим все слова к нижнему регистру
    root_word = root_word.lower()
    other_words = tuple(element.lower() for element in other_words)
    # Проверяем, содержится ли одно слово в другом
    for word in other_words:
        if root_word in word or word in root_word:
            # Если условие выполняется, добавляем слово в список
            same_words.append(word)
    # Возвращаем получившийся список
    return same_words


# Примеры вызова функции
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
print(result1)
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result2)