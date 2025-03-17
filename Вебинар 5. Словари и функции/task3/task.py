def everything_for_your_cat(cats_data):
    owner_dict = {}
    for cat_name, age, first_name, last_name in cats_data:
        owner_key = (first_name, last_name)
        if owner_key not in owner_dict:
            owner_dict[owner_key] = []
        owner_dict[owner_key].append(f"{cat_name}, {age}")
    result = []
    for (first_name, last_name), cats in owner_dict.items():
        cats_info = "; ".join(cats)
        result.append(f"{first_name} {last_name}: {cats_info}")
    if result:
        end_result = "\n".join(result) + "\n"
    else:
        end_result = ""
    return end_result

