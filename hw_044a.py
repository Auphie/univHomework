def pretty(value, htchar='\t', lfchar='\n', indent=0):
    nlch = lfchar + htchar * (indent + 1)
    if type(value) is dict:
        items = [
            nlch + repr(key) + ': ' + pretty(value[key], htchar, lfchar, indent + 1)
            for key in value
        ]
        return '{%s}' % (','.join(items) + lfchar + htchar * indent)
    elif type(value) is list:
        items = [
            nlch + pretty(item, htchar, lfchar, indent + 1)
            for item in value
        ]
        return '[%s]' % (','.join(items) + lfchar + htchar * indent)
    elif type(value) is tuple:
        items = [
            nlch + pretty(item, htchar, lfchar, indent + 1)
            for item in value
        ]
        return '(%s)' % (','.join(items) + lfchar + htchar * indent)
    else:
        return repr(value)

data = {'breakfast': {'hours': '7-11', 'items': {'breakfast burritos': '$60', 'pancakes': '$40'}}, 'lunch': {'hours': '11-3', 'items': {'hamburger': '$50'}}, 'dinner': {'hours': '3-10', 'items': {'spaghetti': '$80'}}}

d_str = 'manu = ' + str(data)
#tmp = d_str.replace('{','{\n  ').replace('},','},\n').replace('}','}\n')

tmp = pretty(data)
print(tmp)