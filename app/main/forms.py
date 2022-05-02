from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SelectField,SubmitField
from wtforms.validators import Required
from ..models import Pitch

class PitchForm(FlaskForm):
    title = StringField('Pitch Title', validators=[Required()])
    content = TextAreaField('Pitch', validators=[Required()])
    category = SelectField('Pitch Category',validators=[Required()],choices=[('pickup', 'Pick-UP Lines'),('interview', 'Interview Pitches'), ('product', 'Product Pitches'), ('business', 'Business Pitches')] )
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    title = StringField('Comment Title', validators=[Required()])
    comment_content = StringField('Comment', validators=[Required()])
    submit = SubmitField('Submit')