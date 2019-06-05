def validate_data(**kwargs):
    cleaned_data = {}
    for key in kwargs:
        if kwargs[key] is None:
            assert False, key + ' key is missing'
        else:
            cleaned_data[key] = str(kwargs[key])
    for field in cleaned_data:
        value = cleaned_data.get(field)
        if isinstance(value, str):
            value = value.strip()
        if not type(value) is bool and not value:
            assert False, field + " is required field"
    
    return cleaned_data