import re

grammar = re.compile(
    r'CARI\s+(BUKU|JURNAL|PROSIDING|SEMUA)\s+DENGAN\s+'
    r'((topik|penulis|penerbit)\s*(=|~=)\s*"([\w\s]+)")\s*'
    r'(DAN\s+(topik|penulis|penerbit)\s*(=|~=)\s*"([\w\s]+)"\s*)*',
    re.IGNORECASE
)

if '__main__' == __name__:
    import argparse
    parser = argparse.ArgumentParser(description="Mengecek query untuk mencari referensi")
    parser.add_argument('query', help='query untuk mencari referensi')
    args = parser.parse_args()

    matching = grammar.match(args.query)
    if matching:
        print 'Query yang Anda masukkan valid: %(query)s' % {'query': args.query}
        for i, g in enumerate(matching.groups()):
            print '%d: %s' % (i, g)
    else:
        print 'Query yang Anda masukkan tidak valid: %(query)s' % {'query': args.query}
