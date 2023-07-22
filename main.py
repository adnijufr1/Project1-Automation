from modules.book import Book
from modules.magazine import Magazine
from modules.dvd import Dvd
from modules.cd import Cd
from modules.catalog import Catalog
import json

book1 = Book(
    'Title test',
    'ini subject test',
    None,
    '12323123-44',
    'Adni',
    '089897876'
)


book2 = Book(
    'title test 2',
    'ini subject test 2',
    None,
    '212323123-44',
    'Adni2',
    '208881111'
)


book3 = Book(
    'title test 3',
    'ini subject test 3',
    None,
    '312323123-44',
    'Adni3',
    '308881111'
)


Magazine1 = Magazine(
    'Test media CNN',
    'EDISI 14 JULI 2023',
    None,
    'VOLUME 1',
    '.'
)

Magazine2 = Magazine(
    'Test media DETIK',
    'EDISI 14 APRIL 2023',
    None,
    'VOLUME 6',
    '.'
)


Dvd1 = Dvd(
    'Test DVD1',
    'INI SUBJECT DVD 1',
    None,
    None,
    None,
    'COMEDY'
)


Cd1 = Cd(
    'Test CD 1',
    'Subject CD 1',
    None,
    'Artist CD 1'
)

Cd2 = cd1 = Cd(
    'Test CD 2',
    'Subject CD 2',
    None,
    'Artist CD 2'
)


book = [book1,book2,book3]
magazine = [Magazine1,Magazine2]
dvd = [Dvd1]
cd = [Cd1,Cd2]


# get data from json
f = open('filescatalogjson\catalog.json')
data_json = json.load(f)

# get object from data json
for item in data_json:
    if item['source'] == 'book':
        book.append(Book(
            title= item['title'],
            subject= item['subject'],
            upc = item['upc'],
            isbn=item['isbn'],
            authors= item['authors'],
            dds_number=item['dds_number']
            ))
    elif item['source'] == 'magazine':
        magazine.append(Magazine(
            title = item['title'],
            subject= item['subject'],
            upc= item['upc'],
            volume= item['volume'],
            issue = item['issue']
            ))
    elif item['source'] == 'Dvd':
        dvd.append(Dvd(
            title = item['title'],
            subject= item['subject'],
            upc= item['upc'],
            actors =item['actors'],
            director= item['director'],
            genre = item['genre']
            ))
    elif item['source'] == 'Cd':
        cd.append(Cd(
            title=item['title'],
            subject= item['subject'],
            upc= item['upc'],
            artist=item['artist']
        ))
        
    else:
        print("No Result / Error")



#collect all data
catalog_all = [book,magazine,dvd, cd]

#search and result
input_search = 'test'
results = Catalog(catalog_all).search(input_search)
if results:
    for index, result in enumerate(results):
        print(f'result ke - {index+1} | {result}')
else:
    print('No Result')



    
            

