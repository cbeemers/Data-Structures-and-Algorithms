import unittest

class TestHashTable(unittest.TestCase):

    def test_initialize(self):
        from hashtable import HashTable, HashNode, word_frequency

        table = HashTable(capacity=100)
        assert (table.capacity == 100)
        assert (table.size == 0)
        assert (table.table == [None for _ in range(100)])

    def test_hash(self):
        from hashtable import HashTable, HashNode, word_frequency

        table = HashTable(capacity=16)

        table.table = [None, None, None,
                       HashNode('class_ever', 1), HashNode(None, None, True),
                       HashNode(None, None, True), None, None, None,
                       None, HashNode(None, None, True), None,
                       None, None, HashNode('cse331', 100), None]

        # Should insert in the first available bin
        assert (4 == table.hash("is_the", inserting=True))

        # Should search until the first None/unused bin
        assert (15 == table.hash("is_the"))

        # Should insert in the first available bin
        assert (5 == table.hash("yash", inserting=True))

        # Should search until the first None/unused bin
        assert (7 == table.hash("yash"))

        assert (3 == table.hash("class_ever"))

    def test_insert(self):
        from hashtable import HashTable, HashNode, word_frequency

        table = HashTable()

        solution = [None, None, None, HashNode('class_ever', 1), HashNode('is_the', 3005), None, None, None, None,
                    None, HashNode('best', 42), None, None, None, HashNode('cse331', 100), None]

        table.insert("cse331", 100)
        table.insert("is_the", 3005)

        assert (table.size == 2)
        assert (table.capacity == 8)

        table['best'] = 42
        table['class_ever'] = 1

        assert (table.size == 4)
        assert (table.capacity == 16)
        print(table)
        assert (solution == table.table)

    def test_get(self):
        from hashtable import HashTable, HashNode, word_frequency

        table = HashTable()

        solution = [None, None, None, HashNode('class_ever', 1), HashNode('is_the', 3005), None, None, None, None,
                    None, HashNode('best', 42), None, None, None, HashNode('cse331', 100), None]

        table.insert("cse331", 100)
        table.insert("is_the", 3005)

        assert (table.size == 2)
        assert (table.capacity == 8)

        table['best'] = 42
        table['class_ever'] = 1

        assert (table.size == 4)
        assert (table.capacity == 16)
        print(table)
        assert (solution == table.table)

        for i in solution:
            if i:
                assert (table[i.key] == i)

    def test_delete(self):
        from hashtable import HashTable, HashNode, word_frequency

        table = HashTable()

        pre_solution = [None, None, None, HashNode('class_ever', 1), HashNode('is_the', 3005), None, None, None, None,
                        None, HashNode('best', 42), None, None, None, HashNode('cse331', 100), None]

        post_solution = [None, None, None, HashNode('class_ever', 1), HashNode(None, None), None, None, None, None, None,
                         HashNode(None, None), None, None, None, HashNode('cse331', 100), None]

        table.insert("cse331", 100)
        table.insert("is_the", 3005)

        assert (table.size == 2)
        assert (table.capacity == 8)

        table['best'] = 42
        table['class_ever'] = 1

        assert (table.size == 4)
        assert (table.capacity == 16)
        print(table)

        assert (pre_solution == table.table)

        delete = ['best', 'is_the']
        for k in delete:
            table.delete(k)

        assert (post_solution == table.table)
        print(table)

    def test_all(self):
        from hashtable import HashTable, HashNode, word_frequency

        table = HashTable()

        pre_solution = [None, None, None, HashNode('class_ever', 1), HashNode('is_the', 3005), None, None, None, None,
                        None, HashNode('best', 42), None, None, None, HashNode('cse331', 100), None]

        post_solution = [None, None, None, HashNode('class_ever', 1), HashNode(None, None), None, None, None, None,
                         None, HashNode(None, None), None, None, None, HashNode('cse331', 100), None]

        table.insert("cse331", 100)
        table.insert("is_the", 3005)

        assert (table.size == 2)
        assert (table.capacity == 8)

        table['best'] = 42
        table['class_ever'] = 1

        assert (table.size == 4)
        assert (table.capacity == 16)
        print(table)

        assert (pre_solution == table.table)

        delete = ['best', 'is_the']
        for k in delete:
            table.delete(k)

        assert (post_solution == table.table)
        print(table)

        assert(table['is_the'] == None)
        assert(table['best'] == None)


class TestApplication(unittest.TestCase):

    def test_1(self):
        from hashtable import HashTable, HashNode, word_frequency

        string = "chefallfall"
        dictionary = ['chef', 'all', 'fall', 'a']

        table = HashTable()
        table = word_frequency(string, dictionary, table)
        solution = [None, HashNode('all', 1), None, None, None, None, None, None, HashNode('a', 0), None, None, None,
                    None, None, HashNode('chef', 1), HashNode('fall', 1)]

        print(solution)
        assert (solution == table.table)
        print(table)



    def test_2(self):
        from hashtable import HashTable, HashNode, word_frequency

        # Frank Ocean - Thinking bout you
        string = """atornadoflewaroundmyroombeforeyoucame"""
        dictionary = {'a': 1, 'tornado': 1, 'flew': 1, 'around': 1, 'my': 1, 'room': 1, 'before': 1, 'you': 1,
                      'came': 1}
        table = HashTable()
        table = word_frequency(string, dictionary.keys(), table)

        for word, count in dictionary.items():
            assert (table[word].value == count)
        print(table)

    def test_3(self):
        from hashtable import HashTable, HashNode, word_frequency

        # Isaac Asimov - The last question
        # https://www.multivax.com/last_question.html
        string = """thelastquestionwasaskedforthefirsttimehalfinjestonmay212061atatimewhenhumanityfirststeppedintothelightthequestioncameaboutasaresultofafivedollarbetoverhighballsandithappenedthiswayalexanderadellandbertramlupovweretwoofthefaithfulattendantsofmultivacaswellasanyhumanbeingscouldtheyknewwhatlaybehindthecoldclickingflashingfacemilesandmilesoffaceofthatgiantcomputertheyhadatleastavaguenotionofthegeneralplanofrelaysandcircuitsthathadlongsincegrownpastthepointwhereanysinglehumancouldpossiblyhaveafirmgraspofthewholemultivacwasselfadjustingandselfcorrecting"""
        dictionary = {'the': 9, 'last': 1, 'question': 2, 'was': 2, 'asked': 1, 'for': 1, 'first': 2, 'time': 2, 'half': 1, 'in': 1, 'jest': 1, 'on': 1, 'may': 1, '21': 1, '2061': 1, 'at': 2, 'a': 5, 'when': 1, 'humanity': 1, 'stepped': 1, 'into': 1, 'light': 1, 'came': 1, 'about': 1, 'as': 3, 'result': 1, 'of': 8, 'five': 1, 'dollar': 1, 'bet': 1, 'over': 1, 'highballs': 1, 'and': 5, 'it': 1, 'happened': 1, 'this': 1, 'wayalexander': 1, 'adell': 1, 'bertram': 1, 'lupov': 1, 'were': 1, 'two': 1, 'faithful': 1, 'attendants': 1, 'multivac': 1, 'well': 1, 'any': 2, 'human': 2, 'beings': 1, 'could': 2, 'they': 2, 'knew': 1, 'what': 1, 'lay': 1, 'behind': 1, 'cold': 1, 'clicking': 1, 'flashing': 1, 'face': 2, 'miles': 2, 'that': 2, 'giant': 1, 'computer': 1, 'had': 2, 'least': 1, 'vague': 1, 'notion': 1, 'general': 1, 'plan': 1, 'relays': 1, 'circuits': 1, 'long': 1, 'since': 1, 'grown': 1, 'past': 1, 'point': 1, 'where': 1, 'single': 1, 'possibly': 1, 'have': 1, 'firm': 1, 'grasp': 1, 'wholemultivac': 1, 'selfadjusting': 1, 'selfcorrecting': 1}

        table = HashTable()
        table = word_frequency(string, dictionary.keys(), table)

        for word, count in dictionary.items():
            assert (table[word].value == count)
        print(table)

if __name__ == "__main__":
    unittest.main()