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
    {pattern: '"\\w.*?"', tag: PARAM_VALUE},
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
    this.QUERY_PATTERN = /CARI OBJECT DENGAN (.+)/i;
    this.CRITERIA_PATTERN = /(PARAM_NAME OPERATOR PARAM_VALUE)( DAN PARAM_NAME OPERATOR PARAM_VALUE)*/i;

    this.parse = function (tokens) {
        this.checkSentence(tokens);

        var criteria = [];
        var index = 3;

        do {
            criteria.push({
                'paramName': tokens[index].text,
                'operator': tokens[index+1].text,
                'paramValue': tokens[index+2].text,
            });
            index += 4;
        } while (index < tokens.length)

        return {
            "objectToSearch": tokens[1].text,
            "criteria": criteria
        }
    };

    /**
    * Check whether query matched the sentence pattern or not. Throw exception if it is not.
    */
    this.checkSentence = function(tokens) {
        var tokenTagString = this.createTokenTagString(tokens);
        var queryMatch = this.QUERY_PATTERN.exec(tokenTagString);

        if (queryMatch === null) {
            throw new Error('Parsing gagal dilakukan, struktur query salah!');
        }

        var criteriaTagString = queryMatch[1];
        if (!this.CRITERIA_PATTERN.test(criteriaTagString)) {
            throw new Error('Parsing gagal dilakukan, struktur klausa kriteria pencarian salah!');
        }
    };

    /**
    * Create token tag string i.e. string of token's tag, with RESERVED token as an exception,
    * their occurences will be represented by their text instead of their tag. Token tags will
    * be separated by single space character.
    */
    this.createTokenTagString = function(tokens) {
        var tokenTagString = tokens[0].tag == RESERVED ? tokens[0].text : tokens[0].tag;

        for (var i=1; i < tokens.length; i++) {
            var tokenTag = tokens[i].tag == RESERVED ? tokens[i].text : tokens[i].tag;
            tokenTagString += ' ' + tokenTag;
        }

        return tokenTagString;
    };
}
