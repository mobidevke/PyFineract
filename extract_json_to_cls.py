import json
import re

SPACING = ' ' * 4
D_SPACING = ' ' * 8


def camel_to_snake(string):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', string)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def get_line_and_class(obj_name, key, val):
    suffix = key[0].upper() + key[1:]
    sub_obj_name = f'{obj_name}{suffix}'
    parent = 'Type' if ''.endswith('Type') else 'FineractObject'
    line = (SPACING * 2) + f'self.{camel_to_snake(key)} = self._make_fineract_object({sub_obj_name}, attributes.get(\'{key}\', None))'
    clz = f'class {sub_obj_name}({parent}):\n\n'
    clz += (SPACING + 'def _init_attributes(self):\n')
    for key2 in val.keys():
        clz += (D_SPACING + f'self.{camel_to_snake(key2)} = None\n')

    clz += '\n'

    clz += (SPACING + 'def _use_attributes(self, attributes):\n')

    for key2 in val.keys():
        if isinstance(val[key2], list):
            clz += (D_SPACING + f'self.{camel_to_snake(key2)} = self._make_date_object(attributes.get(\'{key2}\', None))\n')
        else:
            if key2 == 'currency':
                clz += (D_SPACING + f'self.{camel_to_snake(key2)} = self._make_fineract_object(Currency, attributes.get(\'{key2}\', None))\n')
            else:
                clz += (D_SPACING + f'self.{camel_to_snake(key2)} = attributes.get(\'{key2}\', None)\n')

    clz += '\n\n'

    return line, clz


if __name__ == '__main__':
    obj_name = input('Enter object name: ')
    lines = ['from fineract.objects.currency import Currency',
             'from fineract.objects.fineract_object import FineractObject', 'from fineract.objects.types import Type',
             ]
    classes = []
    with open('extract.json', 'r') as fp:
        data = json.load(fp)

    lines.append('\n')

    lines.append(f'class {obj_name}(FineractObject):\n')
    lines.append(SPACING + 'def _init_attributes(self):')
    for key in data.keys():
        lines.append((SPACING * 2) + f'self.{camel_to_snake(key)} = None')

    lines.append('')

    lines.append(SPACING + 'def _use_attributes(self, attributes):')

    for key in data.keys():
        if isinstance(data[key], dict):
            if key == 'currency':
                lines.append((SPACING * 2) + f'self.{camel_to_snake(key)} = self._make_fineract_object(Currency, attributes.get(\'{key}\', None))')
            elif len(data[key]) == 3 and key.endswith('Type'):
                lines.append((SPACING * 2) + f'self.{camel_to_snake(key)} = self._make_fineract_object(Type, attributes.get(\'{key}\', None))')
            else:
                l, clz = get_line_and_class(obj_name, key, data[key])
                lines.append(l)
                classes.append(clz)
        elif isinstance(data[key], list):
            lines.append(
                (SPACING * 2) + f'self.{camel_to_snake(key)} = self._make_date_object(attributes.get(\'{key}\', None))')
        else:
            lines.append((SPACING * 2) + f'self.{camel_to_snake(key)} = attributes.get(\'{key}\', None)')

    with open('extract.py', 'w') as out_file:
        for line in lines:
            out_file.write(line + '\n')

        if classes:
            out_file.write('\n\n')
            for clz in classes:
                out_file.write(clz)

    print('Done')
