from django import forms


class PreviewClearableFileInput(forms.ClearableFileInput):
    template_name = 'widgets/preview_clearable_file_input.html'

    class Media:
        js = [
            '//code.jquery.com/jquery-2.2.4.min.js',
        ]


class DatePickerWidget(forms.DateInput):
    template_name = 'widgets/picker_date.html'

    class Media:
        css = {
            'all': [
                '//code.jquery.com/ui/1.12.1/themes/smoothness/jquery-ui.css',
            ],
        }
        js = [
            '//code.jquery.com/jquery-2.2.4.min.js',
        ]


class KakaoMap(forms.TextInput):
    template_name = 'widgets/kakao_map.html'

