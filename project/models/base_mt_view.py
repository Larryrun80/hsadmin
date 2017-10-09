import arrow

from flask_admin.contrib.sqla import ModelView
from flask_admin.form import SecureForm


class BaseMTView(ModelView):
    form_base_class = SecureForm

    can_delete = False

    page_size = 20
    can_set_page_size = True
    # can_export = True
    can_view_details = True
    column_display_pk = True

    column_formatters = dict(
        created_at=lambda v, c, m, p: arrow.get(m.created_at)
                                           .to('Asia/Shanghai')
                                           .format('YYYY-MM-DD HH:mm:ss'),
        updated_at=lambda v, c, m, p: arrow.get(m.updated_at)
                                           .to('Asia/Shanghai')
                                           .format('YYYY-MM-DD HH:mm:ss'),
    )

    def on_model_change(self, form, model, is_created):
        model.updated_at = arrow.now().timestamp
        if is_created:
            model.created_at = arrow.now().timestamp
