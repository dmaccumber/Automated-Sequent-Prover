import re
import types

# dictionary holding all connectives and their associated symbols
connectives = {'neg':'¬',
                        'and':'∧',
                        'or':'∨',
                        'imp':'→',
                        'iff':'↔'}

# a class for constructing a sequent 
class Sequent:

    def __init__(self, left, right):
        '''
        Constructor

        Parameters:
        left(list): the left side of the sequent
        right(list): the right side of the sequent
        ''' 
        self.left = left
        self.right = right

    def rule_one_check(self):
        '''
        Checks if the sequent satisfies rule one, i.e. it is a theorem
        '''
        for formula in self.left:   
            if formula in self.right:
                return self._isAtomic()
        return False

    def _isAtomic(self):
        '''
        Helper to rule_one_check() that ensures each formula is also atomic
        '''
        for formula_l in self.left:
            if type(formula_l) is tuple:
                return False
        for formula_r in self.right:
            if type(formula_r) is tuple:
                return False
        return True 

    def _enter(self, formula):
        '''
        Calls _enter_helper() with empty string

        Parameters:
        formula(tuple): an individual formula of a sequent in prefix notation
        '''
        partial = ""
        return self._enter_helper(partial, formula)

    def _enter_helper(self, partial, formula):
        '''
        Recursive function that transforms sequent in prefix notation into more human-readable one
        
        Paramaters:
        partial(str): the human-readable sequent being constructed
        formula(tuple): an individual formula of a sequent because reformatted
        '''
        if len(formula) < 2:
            return " ".join(re.findall("[a-zA-Z]+", str(formula)))
        connective = formula[0]
        parameters = formula[1:]
        if connective == 'neg':
            partial += '¬'
            partial += self._enter_helper("", parameters[0])
        else:
            partial += "("
            partial += self._enter_helper("", parameters[0])
            partial += " "
            partial += connectives[connective]
            partial += " "
            partial += self._enter_helper("", parameters[1])
            partial += ")"
        return partial
    
    def _format(self, unformatted):
        '''
        Function for reformatting sequents in prefix notation
        
        Paramaters:
        unformatted(tuple): a formula in prefix notation not in human-readable form
        '''
        result = ""
            
        for i in range(len(unformatted)):
            if len(unformatted[i]) <= 1:
                result += unformatted[i]
            else:
                result += self._enter(unformatted[i])
            if i < len(unformatted)-1:
                result += ", "
        return result
    
    def __repr__(self):
        left = self._format(self.left)
        right = self._format(self.right)
        
        return "{left} ⊢ {right}".format(left=left,right=right)

# a class for creating tokens for parsing input sequents
class Token:
    '''
    - Ajax1234 
    - October 15, 2019
    - Stack Overflow Solution
    - Code version (N/A)
    - Source code
    - <https://stackoverflow.com/questions/58386078/how-can-i-parse-these-strings-into-tuples-of-prefix-notation-in-python>
    '''
    def __init__(self, _t, val):
        self._type, self.val = _t, val
    def __repr__(self):
        return f'{self.__class__.__name__}({self._type}, {self.val})'

# a class for tokenizing input sequents based on their connectives in order to transform them into prefix
# notation which is far easier to work with than infix notation
class Tokenize:
    '''
    - Ajax1234 
    - October 15, 2019
    - Stack Overflow Solution
    - Code version (N/A)
    - Source code
    - <https://stackoverflow.com/questions/58386078/how-can-i-parse-these-strings-into-tuples-of-prefix-notation-in-python>
    '''
    gram, _t = r'neg|or|imp|and|iff|\(|\)|\w+', [(r'neg|or|imp|and|iff', 'func'), (r'\(', 'oparen'), (r'\)', 'cparen'), (r'\w+', 'value')]

    @classmethod
    def tokenize(cls, _input):
        return [Token([b for a, b in cls._t if re.findall(a, i)][0], i) for i in re.findall(cls.gram, _input)]

def parse(d, stop=None):
    '''
    Method for parsing string sequent inputs
    
    - Ajax1234 
    - October 15, 2019
    - Stack Overflow Solution
    - Code version (N/A)
    - Source code
    - <https://stackoverflow.com/questions/58386078/how-can-i-parse-these-strings-into-tuples-of-prefix-notation-in-python>
    '''
    s = next(d, None)
    if s is None or s._type == stop:
        return ''
    if s._type == 'func':
        return f'{s.val}({parse(d, stop=stop)})'
    if s._type == 'oparen':
        s = parse(d, stop='cparen')
    _n = next(d, None)
    if _n and _n._type == stop:
        return getattr(s, 'val', s)
    return getattr(s, 'val', s) if _n is None else f'{_n.val}({getattr(s, "val", s)}, {parse(d, stop=stop)})'

def tuplify(text):
    '''
    Method for taking parsed sequent input and turning it into a tuple in prefix notation

    Parameters:
    text(str): a sequent in prefix notation

    E.x.
    'neg(or(p,q))'  -->  ('neg', ('or', 'p', 'q'))
    
    - Charif DZ
    - October 16, 2019
    - Stack Overflow Solution
    - Code version (N/A)
    - Source code
    - <https://stackoverflow.com/questions/58393386/whats-the-best-way-to-turn-these-nested-strings-in-prefix-notation-into-tuples>
    '''
    # used to extract not nested expression
    pattern = re.compile('(\w+)\(([^\(]*?)\)')
    # extract the index of the expression
    index_pattern = re.compile('#(\d+)#')
    # contains all expression extracted from the text
    expressions = []
    # you only need to extract most global expression only
    global_expressions = []

    def fix_expression(expression):
        """  a recursive solution to rebuild nested expression. """
        if isinstance(expression, str):
            # if the expression is like #index# return the correct expression else return this str expression
            m = index_pattern.search(expression)
            if m:
                return tuple(fix_expression(expressions[int(m.group(1))]))
            return expression
        # if the expression is a tuple extract all fixed nested expression in a tuple
        return tuple(fix_expression(subexp) for subexp in expression)


    def extract_expression(code):
        """ keep extracting nested expressions list,  """

        def add_exp(match):
            """ handle the match return by sub to save the expression and return its index."""
            expressions.append(None)
            index = len(expressions) - 1
            name, args = match.groups()

            if ',' in args:
                # if what is between parentheses contains ',' split is
                args = tuple(args.split(','))
            else:
                # args should always be a tuple to support unpacking operation
                args = (args,)

            # expression transformed to a tuple
            expressions[index] = (name, *args)
            return '#{}#'.format(index)

        while pattern.search(code):
            code = re.sub(pattern, add_exp, code)

        # for debuging string after removing all expression
        # print(code)


    # this extract all nested expression in the  text
    extract_expression(text)

    # Global expression there index is not used in any other expression
    # the last expression is for sure a global one because.
    global_expressions.append(expressions[-1])
    for i, exp in enumerate(expressions[:-1]):
        for other_exp in expressions[i + 1:]:
            if any('#{}#'.format(i) in sub_exp for sub_exp in other_exp):
                break
        else:
            # this expression is not used in any expression it's a global one
            global_expressions.append(exp)

    # for debugging
    # print(expressions)
    # print(global_expressions)

    return fix_expression(global_expressions[0])

def fully_parsed(partial):
    '''
    Applies parsing to every formuala on one side of sequent. Turning a string input in infix 
    notation into a tuple of prefix notation which is much easier to work with in automated theorem
    proving
    
    Parameters:
    partial(str): unformatted side of sequent input
    '''
    if partial == '[]':
        return []
    if re.search(r"\[(\w+)\]", partial): 
        if len(re.search(r"\[(\w+)\]", partial).group(1)) <= 1:  
            return [re.search(r"\[(\w+)\]", partial).group(1)]
    result = []
    parsed = [parse(iter(Tokenize.tokenize(i))) for i in partial[1:-1].split(',')]
    for p in parsed:
        if len(p) > 1:
            result.append(tuplify(p.replace(" ","")))
        else:
            result.append(p)
    return result
