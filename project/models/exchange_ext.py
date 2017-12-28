from .. import db
from .base_mt_view import BaseMTView
from .market import Market
from .editor import CKTextAreaField

exchanges_tags_table = db.Table('exchanges_tags', db.Model.metadata,
                               db.Column('market_id', db.Integer, db.ForeignKey('exchange_ext.market_id')),
                               db.Column('exchange_tag_id', db.Integer, db.ForeignKey('exchange_tag.id'))
                               )

class ExchangeExt(db.Model):
    __tablename__ = 'exchange_ext'

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.TEXT)
    description_cn = db.Column(db.TEXT)
    twitter = db.Column(db.String(255))
    twitter_account = db.Column(db.String(255))
    facebook = db.Column(db.String(255))
    email = db.Column(db.String(255))
    blog = db.Column(db.String(255))
    linkedin = db.Column(db.String(255))
    telegram = db.Column(db.String(255))
    weibo = db.Column(db.String(255))
    wechat = db.Column(db.String(255))
    contact = db.Column(db.TEXT)
    app_download = db.Column(db.TEXT)
    fee = db.Column(db.TEXT)
    enabled = db.Column(db.Boolean)
    is_deleted = db.Column(db.Boolean)
    created_at = db.Column(db.TIMESTAMP)
    updated_at = db.Column(db.TIMESTAMP)

    market_id = db.Column(db.Integer, db.ForeignKey('market.id'),
                            autoincrement=True)
    market = db.relationship('Market', back_populates='exchange_ext')

    # country_id = db.Column(db.Integer, db.ForeignKey('country.id'))
    # country = db.relationship('Country', back_populates='markets')

    tags = db.relationship('ExchangeTag', secondary=exchanges_tags_table)


class ExchangeTag(db.Model):
    __tablename__ = 'exchange_tag'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    name_cn = db.Column(db.String(50))
    weight = db.Column(db.Integer)
    is_deleted = db.Column(db.Boolean)
    created_at = db.Column(db.Integer)
    updated_at = db.Column(db.Integer)

    def __repr__(self):
        if self.name_cn:
            return '{} / {}'.format(self.name, self.name_cn)
        else:
            return self.name


class ExchangeExtView(BaseMTView):
    can_create = True
    can_edit = True

    column_labels = dict(description='项目介绍（英文）',
                         description_cn="项目介绍（中文）",
                         app_download='APP 下载信息',
                         fee='交易/提现费率',
                         enabled='是否有效',
                         is_deleted='删除',
                         created_at='创建时间',
                         updated_at='修改时间')

    column_list = (
        'market',
        'enabled',
        'created_at',
        'updated_at'
    )
    column_searchable_list = (Market.name,)
    column_sortable_list = ('created_at', 'updated_at')

    column_default_sort = ('id', True)

    form_columns = (
        'market',
        'tags',
        'description',
        'description_cn',
        'twitter',
        'twitter_account',
        'facebook',
        'email',
        'blog',
        'linkedin',
        'telegram',
        'weibo',
        'wechat',
        'contact',
        'app_download',
        'fee',
        'enabled',
        'is_deleted',
    )

    form_overrides = {
        'description': CKTextAreaField,
        'description_cn': CKTextAreaField,
        'contact': CKTextAreaField,
        'app_download': CKTextAreaField,
        'fee': CKTextAreaField,
    }

    create_template = 'ckeditor.html'
    edit_template = 'ckeditor.html'

    form_ajax_refs = {
        'market': {
            'fields': (Market.name, )
        },
        'tags': {
            'fields': (ExchangeTag.name, ExchangeTag.name_cn)
        }
    }

class ExchangeTagView(BaseMTView):
    can_create = True

    column_labels = dict(
        name='标签/En',
        name_cn='标签/Cn',
        weight='权重',
        is_deleted='删除',
        created_at='创建时间',
        updated_at='修改时间'
    )

    column_descriptions = dict(
        weight='数字越大优先级越高',
    )

    column_sortable_list = ('name', 'weight', 'created_at', 'updated_at')
    column_searchable_list = ('name', )
    column_filters = ('weight', 'is_deleted')
    column_default_sort = ('id', False)

    column_editable_list = ('name', 'name_cn', 'weight', 'is_deleted', )
