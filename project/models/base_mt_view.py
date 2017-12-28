import arrow
import datetime
from jinja2 import Markup

from flask_admin.contrib.sqla import ModelView
from flask_admin.form import SecureForm


class BaseMTView(ModelView):
    form_base_class = SecureForm

    can_delete = False

    page_size = 20
    can_set_page_size = True
    can_export = True
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

    @staticmethod
    def _currency_display(view, context, model, name):
        if not model.alias:
            return '{} ( {} )'.format(model.name,
                                      model.symbol)
        else:
            return '{} ( {} ) / {}'.format(model.name,
                                           model.symbol,
                                           model.alias)

    @staticmethod
    def _list_html(view, context, model, name):
        return Markup(getattr(model, name))

    @staticmethod
    def _list_has_value(view, context, model, name):
        return 'Y' if getattr(model, name) else 'N'

    @staticmethod
    def _list_thumbnail(view, context, model, name):
        if not getattr(model, name):
            return ''

        return Markup(
            '<img src="{}" style="width: 100px; height: 75px;">'.format(
                getattr(model, name)))
