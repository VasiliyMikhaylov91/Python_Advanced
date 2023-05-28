def popular(inp_text: str) -> list[str]:
    result = []
    temp_dict = dict()

    text_list = inp_text.\
        replace('\n', ' '). \
        replace('.', ''). \
        replace(',', ''). \
        replace(':', ''). \
        replace(';', ''). \
        replace('"', ''). \
        replace('(', ''). \
        replace(')', ''). \
        replace('!', ''). \
        replace('?', ''). \
        replace('—', ''). \
        replace('«', '').\
        replace('»', ''). \
        lower().split()

    for item in text_list:
        if item not in temp_dict:
            temp_dict.update({item: 0})
        temp_dict[item] += 1

    for _ in range(10):
        popular_word = None
        count_popular = 0

        for key in temp_dict:
            if temp_dict[key] > count_popular:
                popular_word = key
                count_popular = temp_dict[key]
        result.append(popular_word)
        temp_dict[popular_word] = 0

    return result

if __name__ == '__main__':
    text = '''«В ночь большого прилива» — фантастическая трилогия Владислава Крапивина. 
Состоит из повести или рассказа «Далёкие горнисты», повестей «В ночь большого прилива» и «Вечный жемчуг», 
опубликованных в периодических изданиях в 1970, 1977 и 1978 годах соответственно. 
Первое книжное издание вышло в 1979 году. Содержит сказочные и фантастические мотивы.
Главный герой, Сергей Витальевич, чудесным образом оказывается в сказках, напоминающих сны,
где превращается в двенадцатилетнего и обретает друзей. 
Неожиданно он понимает, что испытывает ностальгию по детству, 
и на протяжении трилогии помогает товарищам обрести утраченный дом. 
Во время приключений Сергей побеждает чудовище — Железного Змея, сражается в поединке с диктатором — Канцлером; 
герои оказываются в далёком необитаемом мире, встречают разумного краба и находят волшебный «вечный жемчуг».
Трилогия посвящена борьбе добра со злом, затрагивает традиционные для Крапивина темы дружбы, преданности, мужества. 
Исследователи отмечали сновидческие и визионерские мотивы, переплетение реальности и снов, 
стирание границ между действительностью и вымыслом, обыденным и чудесным.'''
    print(popular(text))