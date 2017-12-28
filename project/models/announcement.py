import arrow

from .. import db
from .base_mt_view import BaseMTView


class Announcement(db.Model):
    __tablename__ = 'announcement'

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500))
    link = db.Column(db.String(255))
    is_deleted = db.Column(db.Boolean)
    review_status = db.Column(db.Boolean)
    end_time = db.Column(db.TIMESTAMP)
    created_at = db.Column(db.TIMESTAMP)
    updated_at = db.Column(db.TIMESTAMP)


class AnnouncementView(BaseMTView):
    can_create = True
    can_edit = True

    def on_model_change(self, form, model, is_created):
        model.end_time = arrow.get(model.end_time).timestamp
        # model.ico_ended_at = arrow.get(model.ico_ended_at).timestamp
        model.updated_at = arrow.now().timestamp

        if is_created:
            model.created_at = arrow.now().timestamp

    column_labels = dict(
        content='内容',
        link='链接',
        is_deleted='隐藏',
        review_status='审核状态',
        end_time='结束时间',
        created_at='创建时间',
        updated_at='修改时间'
    )
    column_descriptions = dict(
        link='点击公告后跳转的地址，无需跳转则留空',
    )
    column_list = (
        'content',
        'link',
        'is_deleted',
        'review_status',
        'end_time',
        'created_at',
        'updated_at'
    )

    column_sortable_list = ('created_at', 'end_time')
    column_searchable_list = ('content',)
    column_default_sort = ('id', True)

    column_editable_list = ('content', 'is_deleted')

    form_columns = (
        'content',
        'link',
        'is_deleted',
        'review_status',
        'end_time',
    )

    column_formatters = dict(
        end_time=lambda v, c, m, p: arrow.get(m.end_time)
                                           .to('Asia/Shanghai')
                                           .format('YYYY-MM-DD HH:mm:ss'),
        created_at=lambda v, c, m, p: arrow.get(m.created_at)
                                           .to('Asia/Shanghai')
                                           .format('YYYY-MM-DD HH:mm:ss'),
        updated_at=lambda v, c, m, p: arrow.get(m.updated_at)
                                           .to('Asia/Shanghai')
                                           .format('YYYY-MM-DD HH:mm:ss'),
    )
