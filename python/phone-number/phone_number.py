import re


class PhoneNumber:

    def validate_number(self, number):
        if len(number) < 10 or len(number) > 11:
            raise ValueError('Invalid number')

        if len(number) == 11:
            if number[0] != '1':
                raise ValueError('Invalid country code')
            number = number[1:]

        if int(number[0]) < 2:
            raise ValueError('Invalid area code')
        elif int(number[3]) < 2:
            raise ValueError('Invalid exchange code')

        return number

    def clean_number(self, number):
        # Strip everything but digits from an input number.
        return ''.join(re.findall('[\d]{1}', number))

    def pretty(self):
        return '({})-{}-{}'.format(self.area_code, self.exch_code, self.subscriber_no)

    def __init__(self, number):
        number = self.clean_number(number)
        self.number = self.validate_number(number)
        self.area_code = self.number[0:3]
        self.exch_code = self.number[3:6]
        self.subscriber_no = self.number[6:]
