from .. import db
from .base_mt_view import BaseMTView


class Currency(db.Model):
    __tablename__ = 'currency'

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    symbol = db.Column(db.String(20))
    alias = db.Column(db.String(50))
    mytoken_id = db.Column(db.String(20))
    website = db.Column(db.String(255))
    rank = db.Column(db.Integer)
    market_cap_usd = db.Column(db.Float)
    available_supply = db.Column(db.BigInteger)
    total_supply = db.Column(db.BigInteger)
    max_supply = db.Column(db.BigInteger)
    search_field = db.Column(db.String(255))
    wallet = db.Column(db.String(200))
    # review_status = db.Column(db.Boolean)
    # enabled = db.Column(db.Boolean)
    created_at = db.Column(db.TIMESTAMP)
    updated_at = db.Column(db.TIMESTAMP)

    socials = db.relationship('Social', back_populates='currency')
    ico = db.relationship('Ico', uselist=False, back_populates='currency')

    def __repr__(self):
        return '{} ({})'.format(self.name, self.symbol)


class CurrencyView(BaseMTView):
    can_create = False
    can_edit = True

    column_labels = dict(alias='别名',
                         website='官网',
                         rank='排名',
                         market_cap_usd='市值',
                         available_supply='流通量',
                         total_supply='当前总量',
                         max_supply='总量上限',
                         search_field='搜索词',
                         wallet='钱包',
                         # review_status='审核状态',
                         # enabled='有效',
                         created_at='创建时间',
                         updated_at='修改时间')
    column_descriptions = dict(
        alias='如果填写将被展示，可不填',
        available_supply='当前可以交易的货币数量',
        total_supply='当前已经生成的货币数量',
        max_supply='理论上货币数量的最大值',
        search_field='用于用户搜索的关键词，用空格分隔',
        wallet='支持的钱包'
    )
    column_exclude_list = [
        'website',
        'market_cap_usd',
        'available_supply',
        'total_supply',
        'max_supply',
        'search_field',
        'wallet'
    ]
    column_sortable_list = ('id', 'symbol', 'rank', 'created_at', 'updated_at')
    column_filters = ('name', 'symbol')
    column_searchable_list = ('name', 'symbol')
    column_default_sort = ('id', True)

    # column_editable_list = ('content_translation', 'review_status')

    form_columns = ('alias', 'website', 'wallet')
