from lxml import etree
import logging
import typing

_Element = etree._Element

class ArxmlBase:

    def __init__(self, fileName):
        self._file_name = fileName
        self._name_space = {'test_ns':'http://autosar.org/schema/r4.0'}
        self._root = self.get_arxml_root()

    @property
    def arxml_root(self):
        return self._root

    def get_arxml_root(self):
        parser = etree.XMLParser(remove_blank_text=True)
        etree.register_namespace('test_ns', self._name_space['test_ns'])
        tree = etree.parse(self._file_name, parser=parser)

        root = tree.getroot()

        return root

    def get_first_child_by_xpath(self, parent: _Element, format_str: str) -> _Element:
        child = parent.xpath(format_str, namespaces=self._name_space)
        if len(child) >= 1:
            child = child[0]
        else:
            logging.debug('XPATH GET None, and format is {}'.format(format_str))

        return child

    def get_all_childs_by_xpath(self, parent: _Element, format_str: str) -> _Element:
        childs = parent.xpath(format_str, namespaces=self._name_space)
        return childs

    def xml_write_to_file(self, output_fileName):
        tree = etree.ElementTree(self._root)
        tree.write(output_fileName, pretty_print=True, xml_declaration=True, encoding='utf-8')
        logging.debug('Generate arxml file {}'.format(output_fileName))

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)