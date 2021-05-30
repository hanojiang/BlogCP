from lxml import etree

def parseData(in_dict, root_et):
    for key_, value_ in in_dict.items():
        et_list = []

        if isinstance(value_, dict) and '-DEST' in value_ and '#text' in value_:
            et = etree.Element(key_, DEST=value_['-DEST'])
            et.text = value_['#text']
        elif isinstance(value_, str):
            et = etree.Element(key_)
            et.text = value_
            # return et
        elif isinstance(value_, dict):
            et = etree.Element(key_)
            parseData(value_, et)
        elif isinstance(value_, list):

            for v_i in value_:
                et = etree.Element(key_)
                parseData(v_i, et)
                et_list.append(et)
        else:
            et = etree.Element('NULL')

        if len(et_list) != 0:
            for et_tmp in et_list:
                root_et.append(et_tmp)
        else:
            root_et.append(et)