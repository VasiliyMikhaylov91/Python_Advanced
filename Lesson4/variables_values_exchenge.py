def exchange(*, some, non_some, clear) -> dict:
    temp = locals()
    result = dict()
    for item in temp:
        key = None
        try:
            hash(temp[item])
            key = temp[item]
        except:
            key = str(temp[item])

        result.update({key: item})

    return result


print(exchange(some=[1, 2, 3], non_some='adad', clear=(5,6,8)))
