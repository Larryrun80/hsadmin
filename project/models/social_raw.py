from .. import db
from .base_mt_view import BaseMTView


class SocialCurrency(db.Model):
    __tablename__ = 'social_currency'
    __bind_key__ = 'social'

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    currency_id = db.Column(db.Integer)
    social_source = db.Column(db.String(20))
    social_account = db.Column(db.String(50))
    need_review = db.Column(db.Boolean)
    remark = db.Column(db.String(20))
    avatar = db.Column(db.String(255))


class SocialCurrencyView(BaseMTView):
    column_labels = dict(
                         currency_id='货币id',
                         social_account='账号',
                         social_source='来源',
                         avatar='头像',
                         need_review='需审核',
                         remark='备注',)
    column_descriptions = dict(
        remark='注明了账号的身份',
    )
    column_list = (
        'currency_id',
        'social_source',
        'social_account',
        'remark',
        'avatar',
        'need_review',
    )
    # column_exclude_list = ['social_content_id', ]
    # column_sortable_list = ('posted_at',)
    column_filters = ('need_review', 'currency_id')
    column_searchable_list = ('social_account',)
    column_default_sort = ('id', True)
    column_formatters = dict(
        avatar=lambda v, c, m, p: BaseMTView._list_thumbnail(
            v, c, m, 'avatar'),
    )
    column_editable_list = ('need_review', 'remark')

    form_columns = (
        'currency_id',
        'social_source',
        'social_account',
        'remark',
        'avatar',
        'need_review',
    )

    form_choices = {
        'remark': [
            ('官方', '官方'),
            ('交易所', '交易所'),
            ('创始人', '创始人'),
            ('投资人', '投资人'),
            ('媒体', '媒体'),
            ('数据公司', '数据公司'),
            ('KOL', 'KOL'),
            ('', '其他')
        ]
    }
