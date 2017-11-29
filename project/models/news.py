import arrow
from jinja2 import Markup

from .. import db
from .base_mt_view import BaseMTView


class News(db.Model):
    __tablename__ = 'news'

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    abstract = db.Column(db.String(500))
    content = db.Column(db.Text)
    source = db.Column(db.String(200))
    author = db.Column(db.String(50))
    photo_abstract = db.Column(db.String(255))
    link = db.Column(db.String(255))
    tag = db.Column(db.String(20))
    posted_at = db.Column(db.TIMESTAMP)
    is_deleted = db.Column(db.Boolean)
    review_status = db.Column(db.Boolean)
    created_at = db.Column(db.TIMESTAMP)
    updated_at = db.Column(db.TIMESTAMP)


class NewsView(BaseMTView):
    can_create = True
    can_edit = True

    column_labels = dict(
        title='标题',
        abstract='简介',
        content='内容',
        source='来源',
        author='作者',
        tag='标签',
        photo_abstract='缩略图地址',
        link='文章链接',
        posted_at='发布时间',
        is_deleted='隐藏',
        review_status='审核状态',
        created_at='创建时间',
        updated_at='修改时间'
    )
    column_descriptions = dict(
        abstract='显示在列表页的文字',
        photo_abstract='显示在列表页的图片，填写url'
    )
    column_list = (
        'photo_abstract',
        'title',
        'tag',
        # 'abstract',
        'source',
        'author',
        'posted_at',
        # 'link',
        'is_deleted',
        'review_status',
        'created_at',
        'updated_at'
    )

    column_sortable_list = ('posted_at',)
    column_searchable_list = ('title',)
    column_filters = ('author',)
    column_default_sort = ('id', True)

    column_editable_list = ('title', 'source', 'link',
                            'author', 'posted_at', 'tag')

    form_choices = {
        'tag': [
            ('news', '教程'),
            ('new_currency', '每日上新'),
            ('token_talk', '币聊')
        ]
    }

    def _get_tag(view, context, model, name):
        tags = view.form_choices['tag']
        for (val, display) in tags:
            if val == model.tag:
                return display

        return ''

    column_formatters = dict(
        photo_abstract=lambda v, c, m, p: BaseMTView._list_thumbnail(
            v, c, m, 'photo_abstract'),
        tag=_get_tag,
        posted_at=lambda v, c, m, p: arrow.get(m.created_at)
                                          .to('Asia/Shanghai')
                                          .format('YYYY-MM-DD HH:mm:ss'),
        created_at=lambda v, c, m, p: arrow.get(m.created_at)
                                           .to('Asia/Shanghai')
                                           .format('YYYY-MM-DD HH:mm:ss'),
        updated_at=lambda v, c, m, p: arrow.get(m.updated_at)
                                           .to('Asia/Shanghai')
                                           .format('YYYY-MM-DD HH:mm:ss'),
    )

    form_columns = (
        'title',
        'abstract',
        'tag',
        'content',
        'source',
        'author',
        'photo_abstract',
        'link',
        'is_deleted',
        'review_status',
    )

    def on_model_change(self, form, model, is_created):
        model.updated_at = arrow.now().timestamp
        if is_created:
            model.created_at = arrow.now().timestamp
            model.posted_at = arrow.now().timestamp
