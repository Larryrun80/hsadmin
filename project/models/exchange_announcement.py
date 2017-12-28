from .. import db
from .base_mt_view import BaseMTView


class ExchangeAnnouncement(db.Model):
    __tablename__ = 'exchange_announcement'

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    content = db.Column(db.Text)
    abstract = db.Column(db.String(500))
    link = db.Column(db.String(255))
    is_deleted = db.Column(db.Boolean)
    created_at = db.Column(db.TIMESTAMP)
    updated_at = db.Column(db.TIMESTAMP)

    exchange_id = db.Column(db.Integer, db.ForeignKey('market.id'))
    exchange = db.relationship('Market', back_populates='announcements')


class ExchangeAnnouncementView(BaseMTView):
    can_create = True
    can_edit = True

    column_labels = dict(
        title='标题',
        link='链接',
        is_deleted='隐藏',
        abstract='摘要',
        content='内容',
        created_at='创建时间',
        updated_at='修改时间'
    )

    column_descriptions = dict(
        link='点击公告后跳转的地址，无需跳转则留空',
    )

    column_list = (
        'title',
        'is_deleted',
        'created_at',
        'updated_at'
    )

    column_sortable_list = ('created_at',)
    column_searchable_list = ('content',)
    column_default_sort = ('id', True)

    column_editable_list = ('content', 'is_deleted')

    form_columns = (
        'exchange',
        'title',
        'abstract',
        'content',
        'link',
        'is_deleted'
    )
