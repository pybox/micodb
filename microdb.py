import json
class microdb(object):
    def __init__(self , location , key1='n' , key2='uc'):
        self.location = location
        self.key1 = key1
        self.key2 = key2
    def load(self):
        try :
            self.db = json.loads(open(self.location , 'r').read())
            return True
        except Exception as e :
            print(e)
            return False
    def dump(self):
        try :
            file = open(self.location , "w+")
            file.write(json.dumps(self.db))
            file.close()
            return True
        except Exception as e :
            print(e)
            return False
    def add(self ,value):
        try :
            self.db.append(value)
            self.dump()
            return True
        except Exception as e :
            print(str(e))
            return False
    def delete(self, value) :
        try :
            j = 0
            for i in self.db :
                if i[self.key1] == value :
                    del self.db[j]
                    self.dump()
                    return True
                j+=1
            return None
        except Exception as e :
            print(e)
            return False
    def length(self ):
        return len(self.db)

    def add_in_value(self, value , nvalue):
        try :
            for i in self.db :
                if i[self.key1] == value :
                    i[self.key2].append(nvalue)
                    self.dump()
                    return True
            return None
        except Exception as e :
            print(e)
            return False

    def value_count(self):
        c = 0
        for i in self.db :
            c += len(i[self.key2])
        return c

    def delete_in_value(self , value):
        result = self.search(value , True)
        if result == None :
            return None
        elif result != False :
            del self.db[result[1]]['unicode'][result[-1]]
            self.dump()
            return True
        return False

    def search(self , s , search_in_value=False):
        if search_in_value :
            idb = 0
            try :
                for i in self.db :
                    iv = 0
                    for j in i[self.key2] :
                        if j == s :
                            return (i, idb , iv)
                        iv+=1
                    idb+=1
                return None
            except Exception as e :
                print(e)
                return False
        else :
            try :
                n = 0
                for i in self.db :
                    if i[self.key1] == s :
                        return (i, n)
                    n+=1
                return None
            except Exception as e :
                print(e)
                return False
