import arrow

from .. import db
from .market import Market
from .currency import Currency
from .base_mt_view import BaseMTView


class COM(db.Model):
    __tablename__ = 'currency_on_market_update'

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    symbol = db.Column(db.String(20))
    alias = db.Column(db.String(50))
    mytoken_id = db.Column(db.String(20))
    pair = db.Column(db.String(50))
    price = db.Column(db.Float)
    price_cny = db.Column(db.Float)
    volume_24h_usd = db.Column(db.Float)
    enabled = db.Column(db.Boolean)
    review_status = db.Column(db.Integer)
    price_updated_at = db.Column(db.TIMESTAMP)
    created_at = db.Column(db.TIMESTAMP)
    updated_at = db.Column(db.TIMESTAMP)

    currency_id = db.Column(db.Integer, db.ForeignKey('currency.id'))
    currency = db.relationship('Currency', back_populates='coms')

    market_id = db.Column(db.Integer, db.ForeignKey('market.id'))
    market = db.relationship('Market', back_populates='coms')


class COMView(BaseMTView):
    can_create = False
    can_edit = True

    column_labels = dict(
        name='com货币',
        symbol='com简称',
        currency='货币',
        pair='交易对',
        price='价格',
        price_cny='RMB价格',
        volume_24h_usd='USD 24H交易量',
        market='交易所',
        enabled='有效',
        review_status='审核状态',
        price_updated_at='价格更新时间',
        created_at='创建时间',
        updated_at='修改时间'
    )

    column_list = (
        'name',
        'currency',
        'pair',
        'market',
        'price',
        'volume_24h_usd',
        'enabled',
        'price_updated_at',
        'created_at'
    )

    form_columns = (
        'name',
        'symbol',
        'currency',
        'market',
        'enabled',
        'review_status'
    )

    column_sortable_list = ('created_at',)
    column_filters = ('enabled', Market.name, 'symbol', 'price_updated_at', 'review_status')
    column_searchable_list = (Market.name, 'symbol', Currency.symbol, 'name', Currency.name)
    column_default_sort = ('id', True)

    column_editable_list = ('name', 'currency', 'enabled', 'review_status')

    column_formatters = dict(
        name=lambda v, c, m, p: BaseMTView._currency_display(v, c, m, p),
        price_updated_at=lambda v, c, m, p: arrow.get(m.price_updated_at)
                                                 .to('Asia/Shanghai')
                                                 .format('YYYY-MM-DD HH:mm:ss'),
        created_at=lambda v, c, m, p: arrow.get(m.created_at)
                                                 .to('Asia/Shanghai')
                                                 .format('YYYY-MM-DD HH:mm:ss')
    )
