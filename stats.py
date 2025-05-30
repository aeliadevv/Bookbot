def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def wordcount(filepath):
    text = get_book_text(filepath)
    return len(text.split())

def charactercount(filepath):
    text = get_book_text(filepath).lower()
    charac_count_dict = dict(a = text.count("a"), b = text.count("b"), c = text.count("c"), d = text.count("d"), e = text.count("e"), f = text.count("f"), g = text.count("g"), h = text.count("h"), i = text.count("i"), j = text.count("j"), k = text.count("k"), l = text.count("l"), m = text.count("m"), n = text.count("n"), o = text.count("o"), p = text.count("p"), q = text.count("q"), r = text.count("r"), s = text.count("s"), t = text.count("t"), u = text.count("u"), v = text.count("v"), w = text.count("w"), x = text.count("x"), y = text.count("y"), z = text.count("z"), æ = text.count("æ"), â = text.count("â"), ê = text.count("ê"), ë = text.count("ë"), ô = text.count("ô"))
    return charac_count_dict

def sort_on(dict):
    return dict["num"]    

def sort_dict(filepath):
    charac_count_dict = charactercount(filepath)
    dict_key = charac_count_dict.keys()
    dict_value = charac_count_dict.values()
    keys = list(dict_key)
    values = list(dict_value)
    
    list_of_dict = []
    for i in range(len(keys)):
        item_dict = {}
        item_dict["char"] = keys[i]
        item_dict["num"] = values[i]
        list_of_dict.append(item_dict)
    
    list_of_dict.sort(reverse=True, key = sort_on)

    report_list = []
    for item in list_of_dict:
        x = f"{item["char"]}: {item["num"]}"
        report_list.append(x)
    return "\n".join(report_list)





    
