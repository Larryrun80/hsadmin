from .. import db
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
        website='官网',
        synchronized='脚本同步',
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
