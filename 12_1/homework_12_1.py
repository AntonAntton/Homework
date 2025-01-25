import re
import codecs
import html


def delete_html_tags(html_file: str, result_file: str = 'cleaned.txt') -> None:
    """
    Видаляє HTML теги, скрипти, стилі та HTML-утворення з HTML-файлу.
    Очищає вміст, декодуючи HTML-утворення та видаляючи непотрібні пробіли,
    після чого зберігає результат у текстовий файл.
    """

    # Читання вхідного файлу
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html_content = file.read()

    # Видалення вмісту скриптів та стилів
    html_content = re.sub(r'<script.*?>.*?</script>', '', html_content, flags=re.DOTALL)
    html_content = re.sub(r'<style.*?>.*?</style>', '', html_content, flags=re.DOTALL)

    # Видалення всіх HTML тегів
    clean_text = re.sub(r'<[^>]+>', '', html_content, flags=re.DOTALL)

    # Декодування HTML утворень (наприклад, &nbsp;, &lt;, &gt;)
    clean_text = html.unescape(clean_text)

    # Видалення зайвих пробілів та порожніх рядків
    clean_lines = [line.strip() for line in clean_text.split('\n') if line.strip()]
    clean_text = '\n'.join(clean_lines)

    # Запис очищеного тексту у вихідний файл
    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write(clean_text)

# Приклад використання
delete_html_tags('draft.html', 'output.txt')
