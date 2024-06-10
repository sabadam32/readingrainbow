from pyramid.view import view_config
from pyramid.response import Response
from sqlalchemy.exc import SQLAlchemyError

from .. import models


@view_config(route_name='home', renderer='app:templates/mds.jinja2')
def my_view(request):
    data = {}
    try:
        query = request.dbsession.query(models.Category)
        data['hundreds'] = query.filter(models.Category.mds_number.like('_')).all()
        data['tens'] = query.filter(models.Category.mds_number.like('2_')).all()
        data['ones'] = query.filter(models.Category.mds_number.like('25_')).all()
        data['tenths'] = query.filter(models.Category.mds_number.like('258._')).all()
        data['hundredths'] = query.filter(models.Category.mds_number.like('258.1_')).all()
        data['active'] = ["2", "25", "258", "258.1", "258.14"]
    except SQLAlchemyError:
        return Response(db_err_msg, content_type='text/plain', status='500')
    return data


db_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to initialize your database tables with `alembic`.
    Check your README.txt for descriptions and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""
