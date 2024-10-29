"""EX06 - Dictionary Utils - Working on dictionaries."""

__author__ = "730755654"


def invert(get_dict: dict[str, str]) -> dict[str, str]:
    inverted_dict = {}
    # changes the positionf of key and value in get_dict
    for key in get_dict:
        value = get_dict[key]
        # Raise KeyError if the value already exists as a key
        if value in inverted_dict:
            raise KeyError(f"Duplicate value '{value}' found in dictionary.")
        inverted_dict[value] = key
    return inverted_dict


def favorite_color(get_dict: dict[str, str]) -> str:
    # checks if dictionary is empty
    if len(get_dict) == 0:
        return ""
    value_list = []
    count = 0
    max_count = 0
    # creates a list of colors
    for key in get_dict:
        value = get_dict[key]
        value_list.append(value)
    max_color = value_list[0]
    # checks how many times a color occurs, changes max_count to max color occurance
    for i in value_list:
        for j in value_list:
            if i == j:
                count += 1
        if count > max_count:
            max_color = i
            max_count = count
        count = 0
    return max_color


def count(get_list: list[str]) -> dict[str, int]:
    get_dict: dict[str, int] = {}
    # if element is key in dict, value goes up 1, if not, element is added with value 1
    for i in get_list:
        if i in get_dict:
            get_dict[i] += 1
        else:
            get_dict[i] = 1
    return get_dict


def alphabetizer(get_list: list[str]) -> dict[str, list[str]]:
    get_dict: dict[str, list[str]] = {}
    # if letter is key in dict, string is added to its list, if not new letter list made
    for i in get_list:
        if i[0].lower() in get_dict:
            get_dict[i[0]].append(i)
        else:
            get_dict[i[0].lower()] = [i]
    return get_dict


def update_attendance(get_dict: dict[str, list[str]], day: str, stu: str) -> None:
    count = 0
    # if day exists, check if student repeats and add to list, else make new day list
    if day in get_dict:
        for i in get_dict[day]:
            if i == stu:
                count += 1
        if count == 0:
            get_dict[day].append(stu)
        count = 0
    else:
        get_dict[day] = [stu]
    print(get_dict)
