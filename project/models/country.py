from .. import db
from .base_mt_view import BaseMTView


class Country(db.Model):
    __tablename__ = 'country'

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    short_name = db.Column(db.String(255))
    name_cn = db.Column(db.String(255))
    alpha2_code = db.Column(db.String(2))
    alpha3_code = db.Column(db.String(3))
    numeric_code = db.Column(db.Integer)
    flag = db.Column(db.String(255))

    currencies = db.relationship('Currency', back_populates='country')
    icoprojects = db.relationship('ICOProject', back_populates='country')
    exchanges = db.relationship('ExchangeExt', back_populates='country')

    def __repr__(self):
        return self.short_name


class CountryView(BaseMTView):
    can_create = False
    can_edit = False

    column_labels = dict(short_name='国家',
                         name_cn='中文名',
                         alpha2_code='2位国家代码',
                         alpha3_code='3位国家代码',
                         numeric_code='数字编码',
                         flag='国旗url'
                         )

    column_sortable_list = ('id', 'short_name', 'alpha2_code', 'alpha3_code')
    column_filters = ('short_name', 'name_cn', 'alpha2_code', 'alpha3_code', 'flag')
    column_searchable_list = ('short_name', 'name_cn', 'alpha2_code', 'alpha3_code')
    column_default_sort = ('short_name', False)

    column_editable_list = ('flag', 'name_cn')
