from .. import db
from .country import Country
from .base_mt_view import BaseMTView


class Market(db.Model):
    __tablename__ = 'market'

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    alias = db.Column(db.String(50))
    website = db.Column(db.String(255))
    synchronized = db.Column(db.Boolean)
    weight = db.Column(db.Integer)
    enabled = db.Column(db.Boolean)
    created_at = db.Column(db.TIMESTAMP)
    updated_at = db.Column(db.TIMESTAMP)

    country_id = db.Column(db.Integer, db.ForeignKey('country.id'))
    country = db.relationship('Country', back_populates='markets')
    coms = db.relationship('COM', back_populates='market')
    announcements = db.relationship('ExchangeAnnouncement', back_populates='exchange')
    exchange_ext = db.relationship('ExchangeExt', uselist=False, back_populates='market')


    top_market = db.relationship(
        'TopMarket',
        uselist=False,
        back_populates='market'
    )

    def __repr__(self):
        return self.name


class MarketView(BaseMTView):
    can_create = False
    can_edit = False

    column_labels = dict(
        name='市场名',
        alias='别名',
        country='国家',
        website='官网',
        synchronized='可搜索',
        weight='权重',
        enabled='有效',
        created_at='创建时间',
        updated_at='修改时间'
    )
    column_descriptions = dict(
        alias='如果填写将被展示，可不填',
        synchronized='是否已经接入API信息'
    )

    column_list = (
        'name',
        'country',
        'alias',
        'top_market',
        'synchronized',
        'weight',
        'enabled',
        'created_at',
        'updated_at',
    )

    column_sortable_list = ('id', 'created_at', 'updated_at')
    column_filters = ('enabled',)
    column_searchable_list = ('name',)
    column_default_sort = ('id', True)

    column_editable_list = ('alias', 'weight', 'enabled', 'top_market')

    form_ajax_refs = {
        'country': {
            'fields': (Country.short_name, Country.alpha2_code, Country.alpha3_code, Country.numeric_code)
        },
    }
