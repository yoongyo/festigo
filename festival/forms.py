from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Festival, Comment
from .widgets import PreviewClearableFileInput, KakaoMap
from bootstrap_datepicker_plus import DatePickerInput


class FestivalForm(forms.ModelForm):

     class Meta:
           model = Festival
           fields = '__all__'
           widgets = {
                'content': SummernoteWidget(
                    attrs={
                        'style': 'width:100%'
                    }
                ),

                'image': PreviewClearableFileInput(),

                'start': DatePickerInput(
                    format='%Y-%m-%d',
                    attrs={
                        'autocomplete': 'off'
                    }
                ).start_of('event days'),

                'end': DatePickerInput(
                    format='%Y-%m-%d',
                    attrs={
                        'autocomplete': 'off'
                    }
                ).end_of('event days'),

                'map': KakaoMap(),

                'file': forms.FileField(
                    widget=forms.ClearableFileInput(
                        attrs={'multiple': True}
                    )
                ),
           }


class CommentForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'comment-form',
        'size': '70px',
        'placeholder': '댓글 달기...',
        'maxlength': '40', }))

    class Meta:
        model = Comment
        fields = ['content']


class FileFieldForm(forms.Form):
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

