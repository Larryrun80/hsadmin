from .. import db
from .market import Market
from .base_mt_view import BaseMTView


class TopMarket(db.Model):
    __tablename__ = 'top_market'

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    weight = db.Column(db.Integer)
    is_deleted = db.Column(db.Boolean)
    created_at = db.Column(db.TIMESTAMP)
    updated_at = db.Column(db.TIMESTAMP)

    market_id = db.Column(db.Integer, db.ForeignKey('market.id'),
                          autoincrement=True)
    market = db.relationship('Market', back_populates='top_market')


class TopMarketView(BaseMTView):
    can_create = True
    can_edit = False

    column_labels = dict(
        market='市场名',
        weight='权重',
        is_deleted='删除',
        created_at='创建时间',
        updated_at='修改时间'
    )

    column_list = (
        'market',
        'weight',
        'is_deleted',
        'created_at',
        'updated_at',
    )

    column_sortable_list = ('weight', 'created_at',)
    column_filters = ('is_deleted',)
    # column_searchable_list = ('market',)
    column_default_sort = ('weight', True)

    column_editable_list = ('weight', 'is_deleted',)

    form_ajax_refs = {
        'market': {
            'fields': (Market.name,)
        },
    }
