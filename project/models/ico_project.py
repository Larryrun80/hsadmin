import arrow

from .. import db
from .base_mt_view import BaseMTView
from jinja2 import Markup
from .editor import CKTextAreaField


projects_tags_table = db.Table('project_tag', db.Model.metadata,
                               db.Column('project_id', db.Integer, db.ForeignKey('project.id')),
                               db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
                               )
projects_raters_table = db.Table('project_rate', db.Model.metadata,
                               db.Column('project_id', db.Integer, db.ForeignKey('project.id')),
                               db.Column('rater_id', db.Integer, db.ForeignKey('rater.id')),
                               )

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

    ico_accepts = db.Column(db.String(100))
    ico_hardcap = db.Column(db.String(50))
    ico_started_at = db.Column(db.DateTime)
    ico_ended_at = db.Column(db.DateTime)
    ico_price = db.Column(db.Text)
    ico_bounty = db.Column(db.Text)
    ico_bounty_cn = db.Column(db.Text)
    ico_distribution = db.Column(db.Text)
    ico_distribution_cn = db.Column(db.Text)
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
    # raters = db.relationship("ProjectRate", back_populates="project")
    # tags = db.relationship("ProjectTag", back_populates="project")
    raters = db.relationship('Rater', secondary=projects_raters_table)
    tags = db.relationship('Tag', secondary=projects_tags_table)

    def __repr__(self):
        return self.name


class Rater(db.Model):
    __tablename__ = 'rater'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    url = db.Column(db.String(255))
    weight = db.Column(db.Integer)
    created_at = db.Column(db.Integer)
    updated_at = db.Column(db.Integer)
    # projects = db.relationship("ProjectRate", back_populates="rater")

    def __repr__(self):
        return self.name


class Tag(db.Model):
    __tablename__ = 'tag'
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


# class ProjectRate(db.Model):
#     __tablename__ = 'project_rate'

#     grade = db.Column(db.String(100))
#     report_link = db.Column(db.String(255))
#     comment = db.Column(db.Text)
#     created_at = db.Column(db.Integer)
#     updated_at = db.Column(db.Integer)
#     project_id = db.Column(db.Integer, db.ForeignKey('project.id'), primary_key=True)
#     project = db.relationship('ICOProject', back_populates='raters')
#     rater_id = db.Column(db.Integer, db.ForeignKey('rater.id'))
#     rater = db.relationship('Rater', back_populates='projects')

#     def __repr__(self):
#         return self.rater.name


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
        ico_price='ICO价格',
        ico_started_at='ICO开始时间',
        ico_ended_at='ICO结束时间',
        # project_started_at='项目开始时间',
        features='项目特色/En',
        features_cn='项目特色/Cn',
        team='团队介绍/En',
        team_cn='团队介绍/Cn',
        ico_distribution='代币分配/En',
        ico_distribution_cn='代币分配/Cn',
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
        'ico_started_at',
        'ico_ended_at',
        'logo',
        'brief_intro_cn',
        'enabled',
        'created_at'
    )

    column_sortable_list = ('name', 'ico_started_at', 'ico_ended_at', 'created_at')
    column_searchable_list = ('name', 'currency_symbol')
    column_filters = ('ico_started_at', 'ico_ended_at', 'enabled')
    column_default_sort = ('id', False)

    column_editable_list = ('name', 'currency_symbol', 'brief_intro_cn',)

    column_formatters = dict(
        brief_intro_cn=lambda v, c, m, p: m.brief_intro if not m.brief_intro_cn else '{} | {}'.format(m.brief_intro_cn, m.brief_intro),
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
            v, c, m, 'logo'),
        info_source_url=lambda v, c, m, p: Markup('<a href="{}" target="_blank">source_url</a>'.format(m.info_source_url)),
    )

    form_columns = (
        'name',
        'currency_symbol',
        'logo',
        'country',
        'tags',
        'raters',
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
        'ico_accepts',
        'ico_hardcap',
        # 'ico_started_at',
        'ico_price',
        'ico_bounty',
        'ico_bounty_cn',
        'ico_distribution',
        'ico_distribution_cn',
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
        'ico_distribution': CKTextAreaField,
        'ico_distribution_cn': CKTextAreaField,
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

    form_ajax_refs = {
        'tags': {
            'fields': (Tag.name, Tag.name_cn)
        },
        'raters': {
            'fields': (Rater.name,)
        }
    }

class RaterView(BaseMTView):
    can_create = True

    column_labels = dict(
        name='评级者',
        weight='评级权重',
        created_at='创建时间',
        updated_at='修改时间'
    )

    column_descriptions = dict(
        weight='数字越大优先级越高',
    )

    column_sortable_list = ('name', 'weight', 'created_at', 'updated_at')
    column_searchable_list = ('name', )
    column_filters = ('weight', )
    column_default_sort = ('id', False)

    column_editable_list = ('name', 'weight', 'url')

class TagView(BaseMTView):
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

# class ProjectRateView(BaseMTView):
#     can_create = True

#     column_labels = dict(
#         project='项目',
#         rater='评分者',
#         grade='评分',
#         report_link='报告url',
#         comment='评论',
#         created_at='创建时间',
#         updated_at='修改时间'
#     )

#     column_list = (
#         'project',
#         'rater',
#         'grade',
#         'report_link',
#         'comment',
#         'created_at',
#         'updated_at',
#     )

#     # column_descriptions = dict(
#     #     weight='数字越大优先级越高',
#     # )

#     column_sortable_list = ('created_at', 'updated_at')
#     column_searchable_list = (ICOProject.name, Rater.name)
#     column_filters = (ICOProject.name, Rater.name, 'grade')
#     column_default_sort = ('created_at', False)

#     column_editable_list = ('grade', 'report_link', 'comment')
