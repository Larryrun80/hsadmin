from .. import db
from .base_mt_view import BaseMTView
from .currency import Currency


class Ico(db.Model):
    __tablename__ = 'ico'

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    ico_cost = db.Column(db.String(100))
    ico_datetime = db.Column(db.String(50))
    ico_amount = db.Column(db.String(50))
    ico_distribution = db.Column(db.String(500))
    description = db.Column(db.String(500))
    team = db.Column(db.String(1000))
    advisor = db.Column(db.String(500))
    partership = db.Column(db.String(500))
    website = db.Column(db.String(255))
    whitepaper = db.Column(db.String(255))
    remark = db.Column(db.String(255))
    is_deleted = db.Column(db.Boolean)
    created_at = db.Column(db.TIMESTAMP)
    updated_at = db.Column(db.TIMESTAMP)

    currency_id = db.Column(db.Integer, db.ForeignKey('currency.id'),
                            autoincrement=True)
    currency = db.relationship('Currency', back_populates='ico')


class IcoView(BaseMTView):
    can_create = True
    can_edit = True

    column_labels = dict(ico_cost='ICO成本',
                         ico_datetime='ICO时间',
                         ico_amount='ICO总量',
                         ico_distribution='分发模式',
                         description='项目介绍',
                         team='团队',
                         advisor='顾问',
                         partership='合作关系',
                         remark='备注',
                         website='官网',
                         whitepaper='白皮书',
                         is_deleted='删除',
                         created_at='创建时间',
                         updated_at='修改时间')
    column_descriptions = dict(
        ico_cost='写明官方兑换比例，后面可以注明约多少RMB, 例：1 ETH = 1000 XXX，约¥2.1',
        ico_datetime='格式： 2017.6.13 - 7.14',
        ico_amount='格式： xxxx ETH，约$1000／¥6000',
        remark='写明确认渠道：官方确认／官网／官推／官博／媒体／bitcointalk／参与者确认（注明群，用户名）',
    )
    column_list = (
        'currency',
        'ico_cost',
        'ico_amount',
        'ico_datetime',
        'created_at',
        'updated_at'
    )
    column_searchable_list = (Currency.symbol, Currency.name)
    column_sortable_list = ('created_at', 'updated_at')

    column_default_sort = ('id', True)
    column_editable_list = ('ico_cost', 'ico_datetime', 'ico_amount')

    form_columns = ('currency', 'ico_cost', 'ico_datetime', 'website', 'whitepaper',
                    'ico_amount', 'ico_distribution', 'team', 'advisor',
                    'remark', 'partership', 'is_deleted')

    form_ajax_refs = {
        'currency': {
            'fields': (Currency.name, Currency.symbol)
        },
    }
