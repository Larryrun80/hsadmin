import arrow

from .. import db
from .currency import Currency
from .base_mt_view import BaseMTView


class Social(db.Model):
    __tablename__ = 'social_timeline'

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    social_account = db.Column(db.String(50))
    social_content_id = db.Column(db.String(20))
    social_account_remark = db.Column(db.String(20))
    content = db.Column(db.String(1000))
    content_translation = db.Column(db.String(1000))
    source = db.Column(db.String(20))
    is_deleted = db.Column(db.Boolean)
    review_status = db.Column(db.Boolean)
    posted_at = db.Column(db.TIMESTAMP)

    currency_id = db.Column(db.Integer, db.ForeignKey('currency.id'))
    currency = db.relationship('Currency', back_populates='socials')


class SocialView(BaseMTView):
    can_create = False

    column_labels = dict(social_account='账号',
                         social_account_remark='备注',
                         content='原文',
                         content_translation='译文',
                         source='来源',
                         is_deleted='隐藏',
                         review_status='审核状态',
                         posted_at='发布时间')
    column_descriptions = dict(
        social_account_remark='注明了账号的身份',
    )
    column_list = (
        # Social.currency,
        'currency',
        'source',
        'posted_at',
        'social_account',
        'social_account_remark',
        'content',
        'content_translation',
        'review_status',
    )
    # column_exclude_list = ['social_content_id', ]
    column_sortable_list = ('posted_at',)
    column_filters = ('social_account', 'social_account_remark')
    column_searchable_list = ('social_account',)
    column_default_sort = ('posted_at', True)
    column_formatters = dict(
        content=lambda v, c, m, p: BaseMTView._list_html(v, c, m, p, 'content'),
        content_translation=lambda v, c, m, p: BaseMTView._list_html(
            v, c, m, p, 'content_translation'),
        posted_at=lambda v, c, m, p: arrow.get(m.posted_at)
                                          .to('Asia/Shanghai')
                                          .format('YYYY-MM-DD HH:mm:ss')
    )
    column_editable_list = ('review_status',)

    form_columns = (
        'currency',
        'social_account',
        'content_translation',
        'review_status'
    )

    form_ajax_refs = {
        'currency': {
            'fields': (Currency.name, Currency.symbol)
        },
    }
