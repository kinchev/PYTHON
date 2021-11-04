searched_name = input()
book_count = 0
is_book_found = False
next_book = input()
while next_book != 'No More Books':
    if next_book == searched_name:
        next_book = input()
        is_book_found = True
        break
    book_count += 1
    next_book = input()
if is_book_found:
    print(f'You checked {book_count} books and found it.')
else:
    print(f'The book you search is not here!')
    print(f'You checked {book_count} books.')
