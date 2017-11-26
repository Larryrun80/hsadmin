import arrow

from .. import db
from .country import Country
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
    twitter = db.Column(db.String(255))
    facebook = db.Column(db.String(255))
    weibo = db.Column(db.String(255))
    slack = db.Column(db.String(255))
    github = db.Column(db.String(255))
    whitepaper = db.Column(db.String(255))
    explorer = db.Column(db.String(255))
    announcement = db.Column(db.String(255))
    message_board = db.Column(db.String(255))
    email = db.Column(db.String(255))
    telegram = db.Column(db.String(255))
    reddit = db.Column(db.String(255))
    description = db.Column(db.String(500))
    description_en = db.Column(db.String(500))
    rank = db.Column(db.Integer)
    market_cap_usd = db.Column(db.Float)
    available_supply = db.Column(db.BigInteger)
    total_supply = db.Column(db.BigInteger)
    max_supply = db.Column(db.BigInteger)
    search_field = db.Column(db.String(255))
    wallet = db.Column(db.String(200))
    # review_status = db.Column(db.Boolean)
    enabled = db.Column(db.Boolean)
    created_at = db.Column(db.TIMESTAMP)
    updated_at = db.Column(db.TIMESTAMP)

    socials = db.relationship('Social', back_populates='currency')
    ico = db.relationship('Ico', uselist=False, back_populates='currency')
    icoproject = db.relationship('ICOProject', uselist=False, back_populates='currency')
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'))
    country = db.relationship('Country', back_populates='currencies')
    coms = db.relationship('COM', back_populates='currency')

    def __repr__(self):
        return '{} ({})'.format(self.name, self.symbol)


class CurrencyView(BaseMTView):
    can_create = False
    can_edit = True

    column_labels = dict(name='name ( symbol ) / alias',
                         alias='别名',
                         website='官网',
                         rank='排名',
                         market_cap_usd='市值',
                         ico='ICO信息',
                         available_supply='流通量',
                         total_supply='当前总量',
                         max_supply='总量上限',
                         search_field='搜索词',
                         wallet='钱包',
                         info='基本信息',
                         description='简介',
                         # review_status='审核状态',
                         enabled='有效',
                         created_at='创建时间',
                         updated_at='修改时间')
    column_descriptions = dict(
        alias='如果填写将被展示，可不填',
        available_supply='当前可以交易的货币数量',
        total_supply='当前已经生成的货币数量',
        max_supply='理论上货币数量的最大值',
        search_field='用于用户搜索的关键词，用空格分隔',
        wallet='支持的钱包',
    )
    column_list = [
        'id',
        'name',
        'mytoken_id',
        'rank',
        'info',
        'wallet',
        'description',
        'ico',
        'enabled',
        'created_at',
        'updated_at',
    ]
    column_sortable_list = ('id', 'symbol', 'rank', 'created_at', 'updated_at')
    column_filters = ('name', 'symbol', 'enabled')
    column_searchable_list = ('name', 'symbol')
    column_default_sort = ('id', True)

    def _list_infoed(view, context, model, name):
        return 'Y' if (model.twitter or model.facebook or model.slack or model.github) else 'N'

    column_formatters = dict(
        name=lambda v, c, m, p: BaseMTView._currency_display(v, c, m ,p),
        website=lambda v, c, m, p: BaseMTView._list_has_value(v, c, m, 'website'),
        ico=lambda v, c, m, p: BaseMTView._list_has_value(v, c, m, 'ico'),
        info=_list_infoed,
        wallet=lambda v, c, m, p: BaseMTView._list_has_value(v, c, m, 'wallet'),
        description=lambda v, c, m, p: BaseMTView._list_has_value(v, c, m, 'description'),
        created_at=lambda v, c, m, p: arrow.get(m.created_at)
                                           .to('Asia/Shanghai')
                                           .format('YYYY-MM-DD HH:mm:ss'),
        updated_at=lambda v, c, m, p: arrow.get(m.updated_at)
                                           .to('Asia/Shanghai')
                                           .format('YYYY-MM-DD HH:mm:ss'),
    )

    column_export_list = ('id', 'name', 'symbol', 'rank', 'description')

    # column_editable_list = ('content_translation', 'review_status')

    form_columns = (
        'alias',
        'country',
        'website',
        'twitter',
        'wallet',
        'facebook',
        'weibo',
        'slack',
        'github',
        'telegram',
        'email',
        'reddit',
        'whitepaper',
        'explorer',
        'announcement',
        'message_board',
        'description',
        'description_en',
    )

    form_ajax_refs = {
        'country': {
            'fields': (
                Country.short_name,
                Country.alpha2_code,
                Country.alpha3_code
            )
        },
    }
