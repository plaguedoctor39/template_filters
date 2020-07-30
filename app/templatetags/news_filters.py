import datetime

from django import template


register = template.Library()


@register.filter
def format_date(value):
    # Ваш код
    time_value = datetime.datetime(1970, 1, 1) + datetime.timedelta(seconds=value)
    time_difer = datetime.datetime.now() - time_value
    time_dif = str(time_difer).split(':')
    if len(time_dif[0]) > 3:
        result = time_value
    elif int(time_dif[0]) < 1 and int(time_dif[1]) < 10:
        result = 'только что'
    elif 1 < int(time_dif[0]) < 24:
        result = f'{time_dif[0]} часов назад'
    return result


# необходимо добавить фильтр для поля `score`
@register.filter
def format_score(value):
    if value < -5:
        result = 'все плохо'
    if -5 <= value <= 5:
        result = 'нейтрально'
    if value > 5:
        result = 'хорошо'
    return result


@register.filter
def format_num_comments(value):
    # Ваш код
    if value == 0:
        result = 'Оставьте комментарий'
    if 0 < value < 50:
        result = value
    if value > 50:
        result = '50+'
    return result

@register.filter
def format_selftext(value, count):
    text = str(value).split()
    if len(text) > 10:
        new_text = text[0] + ' ' + text[1] + ' ' + text[2] + ' ' + text[3] + ' ' + text[4] + ' ' + " ... " + text[-5] + ' ' + text[-4] + ' ' + text[-3] + ' ' + text[-2] + ' ' + text[-1] + ' '
    else:
        new_text = value
    return new_text


