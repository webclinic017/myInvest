
code = '삼성전자'
# code = '005930'
# code = '현대건설'
codes = {'000020' : '동화약품', '005930' : '삼성전자'}
codes_keys = list(codes.keys())
codes_values = list(codes.values())

if code in codes_keys:
    print(f"Company Code ({code}), Name({codes[code]})")
    pass
elif code in codes_values:
    idx = codes_values.index(code)
    myCode = codes_keys[idx]
    print(f"Company Name ({code}), Code({myCode})")
else:
    print(f"ValueError: Code({code}) doesn't exist.")
