import arrow

from .. import db
from .base_mt_view import BaseMTView
from jinja2 import Markup
from .editor import CKTextAreaField


class ICOProject(db.Model):
    __tablename__ = 'project'

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    # currency_id = db.Column(db.Integer)
    currency_symbol = db.Column(db.String(20))
    # currency_name = db.Column(db.String(50))
    currency_alias = db.Column(db.String(20))
    logo = db.Column(db.String(1000))
    project_started_at = db.Column(db.TIMESTAMP)
    max_supply = db.Column(db.String(50))
    blockchain = db.Column(db.String(50))

    website = db.Column(db.String(255))
    twitter = db.Column(db.String(255))
    facebook = db.Column(db.String(255))
    bitcointalk = db.Column(db.String(255))
    email = db.Column(db.String(255))
    telegram = db.Column(db.String(255))
    reddit = db.Column(db.String(255))
    slack = db.Column(db.String(255))
    blog = db.Column(db.String(255))
    linkedin = db.Column(db.String(255))
    github = db.Column(db.String(255))
    whitepaper = db.Column(db.String(255))

    brief_intro = db.Column(db.String(1000))
    brief_intro_cn = db.Column(db.String(1000))
    description = db.Column(db.Text)
    description_cn = db.Column(db.Text)
    features = db.Column(db.Text)
    features_cn = db.Column(db.Text)
    roadmap = db.Column(db.Text)
    roadmap_cn = db.Column(db.Text)

    ico_started_at = db.Column(db.TIMESTAMP)
    ico_ended_at = db.Column(db.TIMESTAMP)
    ico_bounty = db.Column(db.Text)
    ico_bounty_cn = db.Column(db.Text)
    plan = db.Column(db.Text)
    plan_cn = db.Column(db.Text)

    team = db.Column(db.Text)
    team_cn = db.Column(db.Text)
    advisor = db.Column(db.Text)
    advisor_cn = db.Column(db.Text)
    partnership = db.Column(db.Text)
    partnership_cn = db.Column(db.Text)

    remark = db.Column(db.String(255))
    enabled = db.Column(db.Boolean)
    is_deleted = db.Column(db.Boolean)
    created_at = db.Column(db.TIMESTAMP)
    updated_at = db.Column(db.TIMESTAMP)

    currency_id = db.Column(db.Integer, db.ForeignKey('currency.id'),
                            autoincrement=True)
    currency = db.relationship('Currency', back_populates='icoproject')
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'))
    country = db.relationship('Country', back_populates='icoprojects')


class ICOProjectView(BaseMTView):
    can_create = True
    can_edit = True

    column_labels = dict(
        currency_symbol='缩写',
        currency_name='货币名',
        currency_alias='别名',
        name='项目名',
        brief_intro='项目简介/En',
        brief_intro_cn='项目简介/Cn',
        description='详细介绍/En',
        description_cn='详细介绍/Cn',
        max_supply='最大供给',
        blockchain='基础网络',
        website='官网',
        twitter='推特',
        whitepaper='白皮书',
        ico_started_at='ICO开始时间',
        ico_ended_at='ICO结束时间',
        # project_started_at='项目开始时间',
        features='项目特色/En',
        features_cn='项目特色/Cn',
        team='团队介绍/En',
        team_cn='团队介绍/Cn',
        plan='募资规划/En',
        plan_cn='募资规划/Cn',
        roadmap='路线图/En',
        roadmap_cn='路线图/Cn',
        advisor='顾问/En',
        advisor_cn='顾问/Cn',
        partnership='外部合作/En',
        partnership_cn='外部合作/Cn',
        remark='备注',
        enabled='是否有效',
        created_at='创建时间',
        updated_at='修改时间'
    )

    column_descriptions = dict(
        blockchain='项目运行于哪个基础链',
        max_supply='项目发行的最大代币数量，格式： 2100万 BTC',
        opening_date='最终使用的不是这个时间，是“标准”时间',
        close_date='最终使用的不是这个时间，是“标准”时间'
    )

    column_list = (
        'name',
        'currency_symbol',
        'logo',
        'brief_intro',
        'ico_started_at',
        'ico_ended_at',
        'enabled',
        'created_at'
    )

    column_sortable_list = ('name', 'ico_started_at', 'ico_ended_at', 'created_at')
    column_searchable_list = ('name', 'currency_symbol')
    column_filters = ('ico_started_at', 'ico_ended_at', 'enabled')
    column_default_sort = ('id', False)

    column_editable_list = ('name', 'currency_symbol', 'brief_intro', 'ico_started_at', 'ico_ended_at')

    column_formatters = dict(
        ico_started_at=lambda v, c, m, p: arrow.get(m.ico_started_at)
                                               .to('Asia/Shanghai')
                                               .format('YYYY-MM-DD HH:mm:ss'),
        ico_ended_at=lambda v, c, m, p: arrow.get(m.ico_ended_at)
                                             .to('Asia/Shanghai')
                                             .format('YYYY-MM-DD HH:mm:ss'),
        created_at=lambda v, c, m, p: arrow.get(m.created_at)
                                           .to('Asia/Shanghai')
                                           .format('YYYY-MM-DD HH:mm:ss'),
        logo=lambda v, c, m, p: BaseMTView._list_thumbnail(
            v, c, m, p, 'logo'),
        info_source_url=lambda v, c, m, p: Markup('<a href="{}" target="_blank">source_url</a>'.format(m.info_source_url)),
    )

    form_columns = (
        'name',
        'currency_symbol',
        'logo',
        'country',
        'max_supply',
        'blockchain',
        'website',
        'twitter',
        'facebook',
        'bitcointalk',
        'email',
        'telegram',
        'reddit',
        'slack',
        'blog',
        'linkedin',
        'github',
        'whitepaper',
        'brief_intro',
        'brief_intro_cn',
        'description',
        'description_cn',
        'features',
        'features_cn',
        'roadmap',
        'roadmap_cn',
        'ico_bounty',
        'ico_bounty_cn',
        'plan',
        'plan_cn',
        'team',
        'team_cn',
        'advisor',
        'advisor_cn',
        'partnership',
        'partnership_cn',
        'remark',
        'enabled',
    )

    form_overrides = {
        'description': CKTextAreaField,
        'description_cn': CKTextAreaField,
        'features': CKTextAreaField,
        'features_cn': CKTextAreaField,
        'roadmap': CKTextAreaField,
        'roadmap_cn': CKTextAreaField,
        'ico_bounty': CKTextAreaField,
        'ico_bounty_cn': CKTextAreaField,
        'plan': CKTextAreaField,
        'plan_cn': CKTextAreaField,
        'team': CKTextAreaField,
        'team_cn': CKTextAreaField,
        'advisor': CKTextAreaField,
        'advisor_cn': CKTextAreaField,
        'partnership': CKTextAreaField,
        'partnership_cn': CKTextAreaField,
    }
    create_template = 'ckeditor.html'
    edit_template = 'ckeditor.html'
