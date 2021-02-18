class JsonStr:
    def __init__(self, l):
        self.l = l
        self.arr = []
        for i in self.l:
            self.arr.append(dict(id=int(i.split(':')[0]), username=i.split(':')[
                            1], comment=i.split(':')[2], date=i.split(':')[3]))

    def __repr__(self):
        return str(self.arr)

    def repr(self):
        for i in self.arr:
            if '<=>' in i['comment']:
                i['comment'] = i['comment'].replace('<=>',':') 
        return self.arr

    def remove_comment(self, id):
        for i in self.arr:
            if i['id'] == id:
                self.arr.remove(i)
        return self.arr

    def add_comment(self, id, username, comment, date):
        comment = comment
        if ':' in comment:
            comment = comment.replace(':', "<=>")
        self.arr.append(dict(id=id, username=username,
                             comment=comment, date=date))
        return self.arr

    def to_string(self):
        self.strarr = []
        for i in self.arr:
            self.strarr.append(
                f"{i['id']}:{i['username']}:{i['comment']}:{i['date']}")
        return self.strarr