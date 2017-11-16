import arrow

from .. import db
from .base_mt_view import BaseMTView
from jinja2 import Markup


class ICORaw(db.Model):
    __tablename__ = 'project'
    __bind_key__ = 'social'

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.String(100))
    country = db.Column(db.String(50))
    name = db.Column(db.String(100))
    symbol = db.Column(db.String(10))
    info_source = db.Column(db.String(255))
    info_source_url = db.Column(db.String(255))
    task_id = db.Column(db.String(64))
    logo = db.Column(db.String(1000))
    funded = db.Column(db.String(20))
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
    whitepaper = db.Column(db.String(255))
    github = db.Column(db.String(255))
    blockchain = db.Column(db.String(50))
    brief_intro = db.Column(db.String(1000))
    detail_intro = db.Column(db.Text)
    features = db.Column(db.Text)
    opening_date = db.Column(db.String(20))
    close_date = db.Column(db.String(20))
    opening_date_standard = db.Column(db.TIMESTAMP)
    close_date_standard = db.Column(db.TIMESTAMP)
    token_distribution = db.Column(db.Text)
    team = db.Column(db.Text)
    hardcap = db.Column(db.String(50))
    accepts = db.Column(db.String(100))
    ico_price = db.Column(db.Text)
    bounty = db.Column(db.Text)
    created_at = db.Column(db.TIMESTAMP)
    updated_at = db.Column(db.TIMESTAMP)


class ICORawView(BaseMTView):
    can_create = False
    can_edit = False

    column_labels = dict(
        project_id='项目id',
        country='国家',
        name='项目名',
        info_source='数据源',
        info_source_url='源url',
        funded='成立时间',
        blockchain='基础链',
        breif_intro='简介',
        detail_intro='详细介绍',
        features='特色',
        opening_date='ico开始时间',
        close_date='ico结束时间',
        opening_date_standard='ico开始时间/标准/',
        close_date_standard='ico结束时间/标准/',
        token_distribution='代币分发模式',
        team='团队',
        hardcap='硬顶',
        accepts='接受币种',
        ico_price='ICO价格',
        bounty='活动',
        created_at='创建时间',
        updated_at='修改时间'
    )
    column_descriptions = dict(
        project_id='同一个项目一定使用同一项目名',
        country='注意和country表国家名一致',
        opening_date='最终使用的不是这个时间，是“标准”时间',
        close_date='最终使用的不是这个时间，是“标准”时间'
    )
    column_list = (
        'project_id',
        'logo',
        'country',
        'name',
        'website',
        'info_source_url',
        'opening_date_standard',
        'close_date_standard'
    )

    column_sortable_list = ('name', 'opening_date_standard', 'close_date_standard')
    column_searchable_list = ('name', 'symbol')
    column_filters = ('project_id', 'info_source', 'opening_date', 'close_date_standard')
    column_default_sort = ('name', False)

    column_editable_list = ('project_id', 'country')

    column_formatters = dict(
        opening_date_standard=lambda v, c, m, p: arrow.get(m.created_at)
                                                      .to('Asia/Shanghai')
                                                      .format('YYYY-MM-DD HH:mm:ss'),
        close_date_standard=lambda v, c, m, p: arrow.get(m.updated_at)
                                                    .to('Asia/Shanghai')
                                                    .format('YYYY-MM-DD HH:mm:ss'),
        logo=lambda v, c, m, p: BaseMTView._list_thumbnail(
            v, c, m, p, 'logo'),
        info_source_url=lambda v, c, m, p: Markup('<a href="{}" target="_blank">source_url</a>'.format(m.info_source_url)),
    )
