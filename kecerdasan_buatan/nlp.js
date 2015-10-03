RESERVED = 'RESERVED';
OBJECT = 'OBJECT';
PARAM_NAME = 'PARAM_NAME';
OPERATOR = 'OPERATOR';
PARAM_VALUE = 'PARAM_VALUE';

TOKEN_EXPRS = [
    {pattern: '\\s+', tag: false},
    {pattern: 'CARI', tag: RESERVED},
    {pattern: 'BUKU', tag: OBJECT},
    {pattern: 'JURNAL', tag: OBJECT},
    {pattern: 'PROSIDING', tag: OBJECT},
    {pattern: 'SEMUA', tag: OBJECT},
    {pattern: 'DENGAN', tag: RESERVED},
    {pattern: 'TOPIK', tag: PARAM_NAME},
    {pattern: 'JUDUL', tag: PARAM_NAME},
    {pattern: 'PENULIS', tag: PARAM_NAME},
    {pattern: 'PENERBIT', tag: PARAM_NAME},
    {pattern: '=', tag: OPERATOR},
    {pattern: 'MENGANDUNG', tag: OPERATOR},
    {pattern: 'DAN', tag: RESERVED},
    {pattern: '"\\w[\\w\\s]*"', tag: PARAM_VALUE},
]

function scan(characters, tokenExprs) {
    var pos = 0;
    var tokens = [];

    while (pos < characters.length) {
        var matched = false;

        for (var i in tokenExprs) {
            var tokenExpr = tokenExprs[i];
            var regex = new RegExp('^' + tokenExpr.pattern, "i");
            var stringToCompare = characters.slice(pos);
            var match = regex.exec(stringToCompare);

            if (match) {
                matchedToken = match[0];

                if (tokenExpr.tag) {
                    var token = {text: matchedToken, tag: tokenExpr.tag};
                    tokens.push(token);
                }

                pos = pos + matchedToken.length;
                matched = true;
                break;
            }
        }

        if (!matched) {
            throw new Error(
                "Scanning gagal untuk karakter: '" + characters[pos] + "'' pada indeks: " + pos
            );
        }
    }

    return tokens;
}

function QueryParser() {
    this.MIN_TOKENS = 6;

    this.parseTokens = function (tokens) {
        if (tokens.length < this.MIN_TOKENS) {
            throw new Error('Panjang token tidak valid!');
        }

        if (tokens[0].tag != RESERVED || tokens[0].text != 'CARI') {
            throw new Error('token pertama tidak valid!');
        }

        if (tokens[1].tag != OBJECT) {
            throw new Error('Objek yang dicari tidak valid: ' + tokens[1].text + ' !');
        }
        var objectToSearch = tokens[1].text;

        if (tokens[2].tag != RESERVED || tokens[2].text != 'DENGAN') {
            throw new Error('token ketiga tidak valid!');
        }

        var index = 3;
        var criteria = [];
        do {
            if (index > this.MIN_TOKENS && tokens[index-1] != RESERVED && tokens[index-1] != 'DAN') {
                throw new Error('Parser gagal memparsing kriteria pencarian!');
            }

            if (tokens[index].tag != PARAM_NAME) {
                throw new Error('Parser gagal memparsing nama parameter pencarian!');
            }

            if (tokens[index+1].tag != OPERATOR) {
                throw new Error('Parser gagal memparsing operator!');
            }

            if (tokens[index+2].tag != PARAM_VALUE) {
                throw new Error('Parser gagal memparsing nilai parameter pencarian! ' + tokens[index+2].tag);
            }

            criteria.push({
                paramName: tokens[index].text, operator: tokens[index+1].text, paramValue: tokens[index+2].text
            });
            index += 5;
        } while (index < tokens.length)

        return {
            "objectToSearch": objectToSearch,
            "criteria": criteria
        }
    }
}
