import re

def validate_phone_number(number):
    #선언하고 아무것도 하지 않을때 pass 입력해준다.
    #pass

    if not re.match(r'^01[01678][1-9]\d{6,7}$',number):
        return False
    return True

    print(validate_phone_number('01012341234'))
    print(validate_phone_number('0101234123'))
    print(validate_phone_number('01812341234'))
