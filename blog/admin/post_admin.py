from flask_admin.contrib.sqla import ModelView
from flask_ckeditor import CKEditorField
from blog.forms.forms import PostAdminForm
from flask_login import current_user
from flask import redirect, url_for, request



class PostAdmin(ModelView):
    form = PostAdminForm
    form_overrides = dict(content=CKEditorField)
    create_template = 'admin/create.html'
    edit_template = 'admin/edit.html'

    def is_accessible(self):
        return current_user.is_authenticated
    
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login', next=request.url))
