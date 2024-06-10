from pyramid.view import view_config
from pyramid.response import Response
from sqlalchemy.exc import SQLAlchemyError

from .. import models

@view_config(route_name='mds', renderer='app:templates/mds.jinja2')
def my_view(request):
    number = request.matchdict['number']
    data = get_rows(number)
    levels = ('hundreds', 'tens', 'ones', '', 'tenths', 'hundredths')
    query = request.dbsession.query(models.Category)
    for level in data['active']:
        index = len(level)-1
        try:
            data[levels[index]] = query.filter(models.Category.mds_number.like(f'{level[:-1]}_')).all()
        except SQLAlchemyError:
            return Response('Nogood', content_type='text/plain', status='500')
    else:
        res = max(data['active'], key=len)
        if len(res) < 6:
            if len(res) == 3:
                data['tenths'] = query.filter(models.Category.mds_number.like(f'{res}._')).all()
            else:
                data[levels[len(res)]] = query.filter(models.Category.mds_number.like(f'{res}_')).all()
    return data


def get_rows(number):
    levels = ['hundreds', 'tens', 'ones', '', 'tenths', 'hundredths']
    data = {}
    data['active'] = []
    for i in range(len(number)):
        if i == 3:
            continue

        tmp_num = number[:i+1]
        data[levels[i]] = []
        data['active'].append(tmp_num)

    return data