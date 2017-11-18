import arrow

from .. import dbt
from .base_mt_view import BaseMTView
from jinja2 import Markup


class ICORaw(dbt.Model):
    __bind_key__ = 'social'
    __tablename__ = 'project'

    # Columns
    id = dbt.Column(dbt.Integer, primary_key=True)
    project_id = dbt.Column(dbt.String(100))
    country = dbt.Column(dbt.String(50))
    name = dbt.Column(dbt.String(100))
    symbol = dbt.Column(dbt.String(10))
    info_source = dbt.Column(dbt.String(255))
    info_source_url = dbt.Column(dbt.String(255))
    task_id = dbt.Column(dbt.String(64))
    logo = dbt.Column(dbt.String(1000))
    funded = dbt.Column(dbt.String(20))
    website = dbt.Column(dbt.String(255))
    twitter = dbt.Column(dbt.String(255))
    facebook = dbt.Column(dbt.String(255))
    bitcointalk = dbt.Column(dbt.String(255))
    email = dbt.Column(dbt.String(255))
    telegram = dbt.Column(dbt.String(255))
    reddit = dbt.Column(dbt.String(255))
    slack = dbt.Column(dbt.String(255))
    blog = dbt.Column(dbt.String(255))
    linkedin = dbt.Column(dbt.String(255))
    whitepaper = dbt.Column(dbt.String(255))
    github = dbt.Column(dbt.String(255))
    blockchain = dbt.Column(dbt.String(50))
    brief_intro = dbt.Column(dbt.String(1000))
    detail_intro = dbt.Column(dbt.Text)
    features = dbt.Column(dbt.Text)
    opening_date = dbt.Column(dbt.String(20))
    close_date = dbt.Column(dbt.String(20))
    opening_date_standard = dbt.Column(dbt.TIMESTAMP)
    close_date_standard = dbt.Column(dbt.TIMESTAMP)
    token_distribution = dbt.Column(dbt.Text)
    team = dbt.Column(dbt.Text)
    hardcap = dbt.Column(dbt.String(50))
    accepts = dbt.Column(dbt.String(100))
    ico_price = dbt.Column(dbt.Text)
    bounty = dbt.Column(dbt.Text)
    created_at = dbt.Column(dbt.TIMESTAMP)
    updated_at = dbt.Column(dbt.TIMESTAMP)


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
        opening_date_standard=lambda v, c, m, p: arrow.get(m.opening_date_standard)
                                                      .to('Asia/Shanghai')
                                                      .format('YYYY-MM-DD HH:mm:ss'),
        close_date_standard=lambda v, c, m, p: arrow.get(m.close_date_standard)
                                                    .to('Asia/Shanghai')
                                                    .format('YYYY-MM-DD HH:mm:ss'),
        logo=lambda v, c, m, p: BaseMTView._list_thumbnail(
            v, c, m, p, 'logo'),
        info_source_url=lambda v, c, m, p: Markup('<a href="{}" target="_blank">source_url</a>'.format(m.info_source_url)),
    )
