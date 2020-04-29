import utils
import sorts

bookshelf = utils.load_books('books_large.csv')

def by_title_ascending(book_a, book_b):
    return book_a['title_lower'] > book_b['title_lower']

def by_author_ascending(book_a, book_b) :
    return book_a['author_lower'] > book_b['author_lower']

def by_total_length(book_a, book_b) :
    return (len(book_a['title']) + len(book_a['author'])) > (len(book_b['title']) + len(book_b['author']))

#bookshelf_v1 = bookshelf.copy()
bookshelf_v2 = bookshelf.copy()
#sort_2 = sorts.bubble_sort(bookshelf_v1, by_author_ascending)
sorts.quicksort(bookshelf_v2, 0, len(bookshelf_v2) - 1, by_author_ascending)
#sorts.quicksort(bookshelf_v2, 0, len(bookshelf_v2) - 1, by_total_length)

for book in bookshelf_v2 :
    print(book['author'])